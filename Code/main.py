from mic_Contracts import microTech_contracts as mc
from hur_Contracts import hurston_contracts as hu
from myLocations import *


def print_Contract(con):
    lines = []
    lines.append(
        f"- #### {con.contract_Rank} Rank - {con.contract_Type} {con.contract_Size} Cargo")
    lines.append(f"  - Type: {con.contract_Size}")
    lines.append("")
    lines.append("  - From:")
    from_loc_text = (
        ", ".join(loc.name for loc in con.from_Location)
        if isinstance(con.from_Location, list)
        else con.from_Location.name
    )
    lines.append(f"    - {from_loc_text}")
    lines.append("")
    lines.append("  - To:")
    for amount, item, location in con.deliveries:
        lines.append(
            f"    - {amount} SCU {item} -> {location.name} on {location.planet}")
    lines.append("")
    lines.append(f"  - Max Container Size: {con.max_Container} SCU")
    lines.append("")
    lines.append(f"  - Pay: {'{:,}'.format(con.contract_Pay)} aUEC\n")

    print("\n".join(lines))


ship_Max_Cargo = 224
max_Delivery_Locations = 5

contracts = mc  # or hu, or combined list
chosen_location = port_Tressler


def order_contracts_by_route(selected_contracts, start_loc):
    ordered = []
    visited_locs = set()
    loc_queue = [start_loc]

    loc_to_contracts = {}
    for c in selected_contracts:
        from_locs = (
            [c.from_Location]
            if not isinstance(c.from_Location, list)
            else c.from_Location
        )
        for loc in from_locs:
            loc_to_contracts.setdefault(loc, []).append(c)

    while loc_queue:
        loc = loc_queue.pop(0)
        if loc in visited_locs:
            continue
        visited_locs.add(loc)
        contracts_at_loc = loc_to_contracts.get(loc, [])
        for c in contracts_at_loc:
            if c not in ordered:
                ordered.append(c)
            for _, _, delivery_loc in c.deliveries:
                if delivery_loc not in visited_locs and delivery_loc not in loc_queue:
                    loc_queue.append(delivery_loc)
    return ordered


def find_backhaul_contracts(selected_contracts, all_contracts, start_loc, max_cargo, max_stops):
    delivery_locs = set()
    used_amount = sum(sum(a for a, _, _ in c.deliveries)
                      for c in selected_contracts)
    used_locations = set()
    for c in selected_contracts:
        from_locs = c.from_Location if isinstance(
            c.from_Location, list) else [c.from_Location]
        for fl in from_locs:
            used_locations.add(fl)
        for _, _, loc in c.deliveries:
            delivery_locs.add(loc)
            used_locations.add(loc)

    backhaul_candidates = []

    for c in all_contracts:
        from_locs = c.from_Location if isinstance(
            c.from_Location, list) else [c.from_Location]
        delivers_to_start = any(loc == start_loc for _, _, loc in c.deliveries)
        if not delivers_to_start:
            continue

        # Require all pickup locations to be in delivery locations of forward route
        if not all(loc in delivery_locs for loc in from_locs):
            continue

        backhaul_candidates.append(c)

    extended_contracts = list(selected_contracts)
    extended_amount = used_amount
    extended_locations = set(used_locations)

    for c in backhaul_candidates:
        amount = sum(a for a, _, _ in c.deliveries)
        if amount > c.max_Container:
            continue

        new_locs = set(extended_locations)
        from_locs = c.from_Location if isinstance(
            c.from_Location, list) else [c.from_Location]
        for fl in from_locs:
            new_locs.add(fl)
        for _, _, dl in c.deliveries:
            new_locs.add(dl)

        if extended_amount + amount <= max_cargo and len(new_locs) <= max_stops:
            extended_contracts.append(c)
            extended_amount += amount
            extended_locations = new_locs

    return extended_contracts, extended_locations, extended_amount


def save_routes_to_markdown(routes, filename="route_Options.md", top_n=10):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# Top {top_n} Route Options\n\n")
        for i, (selected_contracts, used_locations, total_pay, start_loc) in enumerate(routes[:top_n], 1):
            ordered_contracts = order_contracts_by_route(
                selected_contracts, start_loc)

            locations_order = [start_loc]
            for con in ordered_contracts:
                for _, _, loc in con.deliveries:
                    if loc not in locations_order:
                        locations_order.append(loc)

            contract_cargo = {}
            for con in ordered_contracts:
                cargo_list = []
                for amount, item, delivery_loc in con.deliveries:
                    cargo_list.append({
                        "amount": amount,
                        "item": item,
                        "from_loc": con.from_Location if not isinstance(con.from_Location, list) else con.from_Location,
                        "to_loc": delivery_loc,
                        "contract": con
                    })
                contract_cargo[con] = cargo_list

            f.write(f"## Route Option {i}\n\n")
            f.write(f"  - **Total Profit:** {total_pay:,} aUEC  \n")
            f.write(
                f"  - **Number of Contracts:** {len(selected_contracts)}  \n")
            f.write(
                f"  - **Total stops (unique locations):** {len(used_locations)}\n\n")
            f.write("### Locations:\n")
            for loc in used_locations:
                f.write(f"  - {loc.name} on {loc.planet}\n")

            f.write("\n### Route Plan:\n")
            f.write(f"  - Start: {start_loc.name}\n\n")

            onboard_cargo = []

            for loc in locations_order:
                dropoff = [
                    cargo for cargo in onboard_cargo if cargo["to_loc"] == loc]
                onboard_cargo = [
                    cargo for cargo in onboard_cargo if cargo["to_loc"] != loc]

                pickups = []
                for con in ordered_contracts:
                    from_locs = (
                        [con.from_Location]
                        if not isinstance(con.from_Location, list)
                        else con.from_Location
                    )
                    if loc in from_locs:
                        pickups.extend(contract_cargo[con])

                onboard_cargo.extend(pickups)

                f.write(f"**{loc.name}:**\n\n")

                if dropoff:
                    f.write("  Dropoff:\n")
                    dropoff_summary = {}
                    for cargo in dropoff:
                        key = cargo['item']
                        dropoff_summary[key] = dropoff_summary.get(
                            key, 0) + cargo['amount']
                    for item, amt in dropoff_summary.items():
                        f.write(f"  - {amt} SCU {item}\n")
                else:
                    f.write("  Dropoff:\n    - None\n")

                if pickups:
                    f.write("\n  Pickup:\n")
                    pickup_summary = {}
                    total_pickup = 0
                    for cargo in pickups:
                        key = (cargo['item'], cargo['to_loc'].name)
                        pickup_summary[key] = pickup_summary.get(
                            key, 0) + cargo['amount']
                        total_pickup += cargo['amount']
                    for (item, dest), amt in pickup_summary.items():
                        f.write(f"    - {amt} SCU {item} -> {dest}\n")
                    f.write(
                        f"\n    - **Total Pickup: {total_pickup} SCU**\n\n")
                else:
                    f.write("\n  Pickup:\n    - None\n\n")

            f.write("\n### Contracts (in recommended pickup/delivery order):\n\n")
            for con in ordered_contracts:
                from_loc_text = (
                    ", ".join(loc.name for loc in con.from_Location)
                    if isinstance(con.from_Location, list)
                    else con.from_Location.name
                )

                lines = []
                lines.append(
                    f"- #### {con.contract_Rank} Rank - {
                        con.contract_Type} {con.contract_Size} Cargo"
                )
                lines.append(f"  - Type: {con.contract_Size}")
                lines.append("")
                lines.append("  - From:")
                lines.append(f"    - {from_loc_text}")
                lines.append("")
                lines.append("  - To:")
                for amount, item, location in con.deliveries:
                    lines.append(
                        f"    - {amount} SCU {item} -> {location.name} on {location.planet}"
                    )
                lines.append("")
                lines.append(
                    f"  - Max Container Size: {con.max_Container} SCU")
                lines.append("")
                lines.append(
                    f"  - Pay: {'{:,}'.format(con.contract_Pay)} aUEC\n")
                f.write("\n".join(lines) + "\n\n")
            f.write("---\n\n")

    print(f"Top {top_n} route options saved to route_Options.md")


def main():
    filtered_contracts = [
        c for c in contracts if (
            (c.from_Location == chosen_location)
            or (isinstance(c.from_Location, list) and chosen_location in c.from_Location)
        )
    ]

    print("Number of filtered contracts")
    print(len(filtered_contracts))

    contract_info = []
    for c in filtered_contracts:
        total_amount = sum(amount for amount, _, _ in c.deliveries)
        locations = set(loc for _, _, loc in c.deliveries)
        profitability = c.contract_Pay / total_amount if total_amount else 0
        contract_info.append((c, total_amount, locations, profitability))

    contract_info.sort(key=lambda x: x[3], reverse=True)

    selected_contracts = []
    used_locations = set()
    used_amount = 0

    print(f"Starting selection for contracts from {chosen_location}")
    print(f"Total contracts to consider: {len(contract_info)}\n")

    for idx, (c, amount, locs, profit) in enumerate(contract_info, 1):
        new_locations = used_locations.union(locs)
        can_add = (used_amount + amount <=
                   ship_Max_Cargo) and (len(new_locations) <= max_Delivery_Locations)
        print(f"Checking contract {idx}: Pay={c.contract_Pay}, Amount={
              amount}, Locations={len(locs)}, Profitability={profit:.2f}")
        print(f"  Current used amount: {
              used_amount}, used locations: {len(used_locations)}")
        print(f"  New total amount if added: {
              used_amount + amount}, new locations if added: {len(new_locations)}")

        if can_add:
            selected_contracts.append(c)
            used_amount += amount
            used_locations = new_locations
            print("  --> Added contract")
        else:
            print("  --> Skipped contract due to constraints")

    # Now look for backhaul contracts that fit after forward haul
    extended_contracts, extended_locations, extended_amount = find_backhaul_contracts(
        selected_contracts, filtered_contracts, chosen_location, ship_Max_Cargo, max_Delivery_Locations
    )

    total_pay = sum(c.contract_Pay for c in extended_contracts)

    print("\nSelection complete.")
    print(f"Selected {len(extended_contracts)
                      } contracts (including backhauls)")
    print(f"Total delivery amount: {extended_amount} SCU")
    print("Delivery locations:")
    for loc in extended_locations:
        print(f"- {loc.name} on {loc.planet}")

    formatted_Total_Profit = '{:,}'.format(total_pay)

    print("\nContracts:")
    for con in extended_contracts:
        print_Contract(con)

    print(" - Total Profit:", formatted_Total_Profit, "aUEC")

    routes = [(extended_contracts, extended_locations,
               total_pay, chosen_location)]
    save_routes_to_markdown(routes, top_n=1)


if __name__ == "__main__":
    main()
