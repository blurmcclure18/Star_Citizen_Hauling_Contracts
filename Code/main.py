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

# Use all contracts combined; you can combine mc and hu as needed
contracts = mc  # For now microTech contracts only


def order_contracts_by_route(selected_contracts, start_loc):
    """
    Orders contracts starting at start_loc, then visits delivery locations in
    order they appear in the selected contracts. Used for route planning.
    """
    ordered = []
    visited_locs = set()
    loc_queue = [start_loc]

    # Map contracts by their from_Location (support list or single)
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
        # Append contracts at this location in original order
        for c in contracts_at_loc:
            if c not in ordered:
                ordered.append(c)
            # Add delivery locations to queue if not visited
            for _, _, delivery_loc in c.deliveries:
                if delivery_loc not in visited_locs and delivery_loc not in loc_queue:
                    loc_queue.append(delivery_loc)
    return ordered


def save_routes_to_markdown(routes, filename="route_Options.md", top_n=10):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# Top {top_n} Route Options\n\n")
        for i, (selected_contracts, used_locations, total_pay, start_loc) in enumerate(routes[:top_n], 1):
            ordered_contracts = order_contracts_by_route(
                selected_contracts, start_loc)

            # Build ordered unique locations based on route
            locations_order = [start_loc]
            for con in ordered_contracts:
                for _, _, loc in con.deliveries:
                    if loc not in locations_order:
                        locations_order.append(loc)

            # Prepare contract cargo info
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

            # --- Route Plan Summary ---
            f.write("\n### Route Plan:\n")
            f.write(f"  - Start: {start_loc.name}\n\n")

            onboard_cargo = []

            for loc in locations_order:
                # Drop off cargo at this location
                dropoff = [
                    cargo for cargo in onboard_cargo if cargo["to_loc"] == loc]

                # Remove dropped off cargo from onboard
                onboard_cargo = [
                    cargo for cargo in onboard_cargo if cargo["to_loc"] != loc]

                # Pick up cargo at this location
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

    print(f"Top {top_n} route options saved to {filename}")


def select_contracts(filtered_contracts, start_loc):
    """
    Selects the best contracts from filtered_contracts starting at start_loc.
    This is where your cargo capacity, delivery location limits, and profitability logic applies.
    Returns:
        selected_contracts (list)
        used_locations (set)
        total_pay (int)
    """
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

    for idx, (c, amount, locs, profit) in enumerate(contract_info, 1):
        new_locations = used_locations.union(locs)
        can_add = (used_amount + amount <=
                   ship_Max_Cargo) and (len(new_locations) <= max_Delivery_Locations)

        if can_add:
            selected_contracts.append(c)
            used_amount += amount
            used_locations = new_locations

    total_pay = sum(c.contract_Pay for c in selected_contracts)
    return selected_contracts, used_locations, total_pay


def get_unique_start_locations(contracts):
    locations = set()
    for c in contracts:
        if isinstance(c.from_Location, list):
            locations.update(c.from_Location)
        else:
            locations.add(c.from_Location)
    return locations


def find_best_start_location(contracts):
    unique_starts = get_unique_start_locations(contracts)
    best_route = None
    best_profit = 0
    best_location = None

    print(f"Found {len(unique_starts)
                   } unique starting locations to evaluate...")

    for start_loc in unique_starts:
        filtered_contracts = [
            c for c in contracts if
            (c.from_Location == start_loc) or
            (isinstance(c.from_Location, list) and start_loc in c.from_Location)
        ]

        selected_contracts, used_locations, total_pay = select_contracts(
            filtered_contracts, start_loc)

        print(f"Start location: {start_loc.name} -> Total Profit: {
              total_pay:,} aUEC, Contracts: {len(selected_contracts)}")

        if total_pay > best_profit:
            best_profit = total_pay
            best_route = (selected_contracts, used_locations,
                          total_pay, start_loc)
            best_location = start_loc

    return best_route, best_location


def main():
    best_route, best_location = find_best_start_location(contracts)
    selected_contracts, used_locations, total_pay, start_loc = best_route

    print(f"\nBest start location is {
          best_location.name} with total profit {total_pay:,} aUEC")
    print(f"Selected {len(selected_contracts)} contracts with {
          len(used_locations)} unique delivery locations.")

    # Optionally print contracts to console
    # for con in selected_contracts:
    #     print_Contract(con)

    save_routes_to_markdown([best_route], top_n=1)


if __name__ == "__main__":
    main()
