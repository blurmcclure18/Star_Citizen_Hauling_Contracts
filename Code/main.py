from mic_Contracts import microTech_contracts as mc
from hur_Contracts import hurston_contracts as hu
from myLocations import *
# Assuming you want these ships available
from myShips import *


def print_Contract(con):
    lines = []
    lines.append(
        f"- #### {con.contract_Rank} Rank - {con.contract_Type} {con.contract_Size} Cargo")
    lines.append(f"  - Type: {con.contract_Size}")
    lines.append("")
    lines.append("  - From:")
    from_locs = con.from_Location if isinstance(
        con.from_Location, list) else [con.from_Location]
    from_loc_text = ", ".join(loc.name for loc in from_locs)
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


def contract_type_matches_ship(contract_type, ship_capabilities):
    contract_type_parts = contract_type.split()
    for part in contract_type_parts:
        if part in ship_capabilities:
            return True
    return False


def filter_contracts_by_ship(contracts, ship):
    filtered = []
    for c in contracts:
        if contract_type_matches_ship(c.contract_Type, ship.ship_Capabilities):
            filtered.append(c)
    return filtered


selected_ship = hull_C  # or starlancer


ship_Max_Cargo = selected_ship.ship_Max_Cargo
ship_Max_Container = selected_ship.ship_Max_Container
ship_Capabilities = selected_ship.ship_Capabilities

max_Delivery_Locations = 5

contracts = mc + hu


def can_add_contract_with_dynamic_cargo(selected_contracts, candidate_contract, ship_Max_Cargo, max_Delivery_Locations, start_loc=None):
    all_contracts = selected_contracts + [candidate_contract]
    loc_order = []

    def add_loc(loc):
        if loc not in loc_order:
            loc_order.append(loc)

    for con in all_contracts:
        from_locs = con.from_Location if isinstance(
            con.from_Location, list) else [con.from_Location]
        for loc in from_locs:
            add_loc(loc)

    for con in all_contracts:
        for _, _, dloc in con.deliveries:
            add_loc(dloc)

    unique_delivery_locations = set()
    for con in all_contracts:
        for _, _, dloc in con.deliveries:
            if start_loc is not None and dloc == start_loc:
                continue
            unique_delivery_locations.add(dloc)

    if len(unique_delivery_locations) > max_Delivery_Locations:
        return (False, f"Exceeded max delivery locations (excluding start): {len(unique_delivery_locations)} > {max_Delivery_Locations}")

    onboard = []

    for loc in loc_order:
        onboard = [cargo for cargo in onboard if cargo['to_loc'] != loc]

        for con in all_contracts:
            from_locs = con.from_Location if isinstance(
                con.from_Location, list) else [con.from_Location]
            if loc in from_locs:
                for amount, item, dloc in con.deliveries:
                    onboard.append({
                        'amount': amount,
                        'item': item,
                        'to_loc': dloc,
                    })

        total_cargo = sum(cargo['amount'] for cargo in onboard)
        if total_cargo > ship_Max_Cargo:
            return (False, f"Exceeded max cargo capacity at {loc.name}: {total_cargo} SCU > {ship_Max_Cargo} SCU")

    return (True, "")


def select_contracts(filtered_contracts, ship_Max_Cargo, max_Delivery_Locations, start_loc=None):
    contract_info = []
    for c in filtered_contracts:
        total_amount = sum(amount for amount, _, _ in c.deliveries)
        locations = set(loc for _, _, loc in c.deliveries)
        profitability = c.contract_Pay / total_amount if total_amount else 0
        contract_info.append((c, total_amount, locations, profitability))

    contract_info.sort(key=lambda x: x[3], reverse=True)

    selected_contracts = []
    for c, _, _, _ in contract_info:
        can_add, _ = can_add_contract_with_dynamic_cargo(
            selected_contracts, c, ship_Max_Cargo, max_Delivery_Locations, start_loc)
        if can_add:
            selected_contracts.append(c)

    used_locations = set()
    for con in selected_contracts:
        from_locs = con.from_Location if isinstance(
            con.from_Location, list) else [con.from_Location]
        used_locations.update(from_locs)
        for _, _, dloc in con.deliveries:
            used_locations.add(dloc)

    total_pay = sum(c.contract_Pay for c in selected_contracts)
    return selected_contracts, used_locations, total_pay


def find_top_routes(contracts, ship_Max_Cargo, max_Delivery_Locations, top_n=5):
    unique_from_locations = set()
    for c in contracts:
        from_locs = c.from_Location if isinstance(
            c.from_Location, list) else [c.from_Location]
        for loc in from_locs:
            unique_from_locations.add(loc)

    routes = []

    for start_loc in unique_from_locations:
        filtered_contracts = [
            c for c in contracts if (
                (c.from_Location == start_loc)
                or (isinstance(c.from_Location, list) and start_loc in c.from_Location)
            )
        ]

        filtered_contracts = filter_contracts_by_ship(
            filtered_contracts, selected_ship)

        selected_contracts, used_locations, total_pay = select_contracts(
            filtered_contracts, ship_Max_Cargo, max_Delivery_Locations, start_loc=start_loc)

        if selected_contracts:
            routes.append(
                (selected_contracts, used_locations, total_pay, start_loc))

    routes.sort(key=lambda r: r[2], reverse=True)
    return routes[:top_n]


def find_backhaul_contracts(selected_contracts, all_contracts, ship_Max_Cargo, max_Delivery_Locations, start_loc):
    delivery_locations = set()
    for con in selected_contracts:
        for _, _, dloc in con.deliveries:
            delivery_locations.add(dloc)

    preferred_backhauls = []
    other_backhauls = []

    for con in all_contracts:
        if con in selected_contracts:
            continue

        from_locs = con.from_Location if isinstance(
            con.from_Location, list) else [con.from_Location]
        from_locs_set = set(from_locs)
        overlap = from_locs_set.intersection(delivery_locations)

        if not overlap:
            continue

        delivers_only_to_start = all(
            dloc == start_loc for _, _, dloc in con.deliveries)

        can_add, reason = can_add_contract_with_dynamic_cargo(
            selected_contracts, con, ship_Max_Cargo, max_Delivery_Locations, start_loc=start_loc)
        if can_add:
            if delivers_only_to_start:
                preferred_backhauls.append(con)
            else:
                other_backhauls.append(con)
        else:
            print(f"# DEBUG - rejected backhaul contract: from {
                  ', '.join(loc.name for loc in from_locs)} - Reason: {reason}")

    return preferred_backhauls + other_backhauls


def order_contracts_by_route(selected_contracts, start_loc):
    ordered = []
    visited_locs = set()
    loc_queue = [start_loc]

    loc_to_contracts = {}
    for c in selected_contracts:
        from_locs = c.from_Location if isinstance(
            c.from_Location, list) else [c.from_Location]
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


def save_routes_to_markdown(routes, filename="route_Options.md", top_n=10):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# Top {top_n} Route Options\n\n")

        f.write(f"## Ship Used for Route Planning:\n\n")
        f.write(f"- Name: {selected_ship.ship_Name}\n")
        f.write(f"- Max Cargo Capacity: {selected_ship.ship_Max_Cargo} SCU\n")
        f.write(
            f"- Max Container Size: {selected_ship.ship_Max_Container} SCU\n")
        caps = ", ".join(selected_ship.ship_Capabilities)
        f.write(f"- Capabilities: {caps}\n\n")

        routes.sort(key=lambda r: r[2], reverse=True)

        for i, (selected_contracts, used_locations, total_pay, start_loc) in enumerate(routes[:top_n], 1):
            ordered_contracts = order_contracts_by_route(
                selected_contracts, start_loc)

            locations_order = [start_loc]

            visited = set(locations_order)
            for con in ordered_contracts:
                from_locs = con.from_Location if isinstance(
                    con.from_Location, list) else [con.from_Location]
                for loc in from_locs:
                    if loc not in visited:
                        locations_order.append(loc)
                        visited.add(loc)
                for _, _, dloc in con.deliveries:
                    if dloc not in visited:
                        locations_order.append(dloc)
                        visited.add(dloc)

            # --- New Route Guide section with numbered list and arrows ---
            route_guide_lines = []
            for idx, loc in enumerate(locations_order, 1):
                arrow = " -->" if idx <= len(locations_order) else ""
                route_guide_lines.append(f" {idx}. {loc.name}{arrow}")

            # Add closing loop to start location if not last
            if locations_order[-1] != start_loc:
                route_guide_lines.append(
                    f" {len(locations_order) + 1}. {start_loc.name}")

            f.write(f"## Route Option {i}\n\n")
            f.write(f"### Route Summary:\n\n")
            f.write(f"  - **Total Profit:** {total_pay:,} aUEC  \n")
            f.write(
                f"  - **Number of Contracts:** {len(selected_contracts)}  \n")
            f.write(
                f"  - **Total stops (unique locations):** {len(used_locations)}\n\n")

            f.write(f"#### Route Guide:\n")
            for line in route_guide_lines:
                f.write(f"{line}\n")
            f.write("\n")

            f.write("### Locations:\n")
            for loc in used_locations:
                f.write(f"  - {loc.name} on {loc.planet}\n")

            f.write("\n### Route Plan:\n")
            f.write(f"  - Start:\n    - {start_loc.name}\n\n")

            onboard_cargo = []

            for loc in locations_order:
                dropoff = [
                    cargo for cargo in onboard_cargo if cargo["to_loc"] == loc]
                onboard_cargo = [
                    cargo for cargo in onboard_cargo if cargo["to_loc"] != loc]

                pickups = []
                for con in ordered_contracts:
                    from_locs = con.from_Location if isinstance(
                        con.from_Location, list) else [con.from_Location]
                    if loc in from_locs:
                        pickups.extend(contract_cargo[con])

                onboard_cargo.extend(pickups)

                f.write(f"**{loc.name}:**\n\n")

                if dropoff:
                    f.write("  Dropoff:\n")
                    dropoff_summary = {}
                    total_dropoff = 0
                    for cargo in dropoff:
                        key = cargo['item']
                        dropoff_summary[key] = dropoff_summary.get(
                            key, 0) + cargo['amount']
                        total_dropoff += cargo['amount']
                    for item, amt in dropoff_summary.items():
                        f.write(f"   - {amt} SCU {item}\n")
                    f.write(f"\n   - **Total Dropoff: {total_dropoff} SCU**\n")
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
                        f.write(f"   - {amt} SCU {item} -> {dest}\n")
                    f.write(
                        f"\n   - **Total Pickup: {total_pickup} SCU**\n\n")
                else:
                    f.write("\n  Pickup:\n    - None\n\n")

            f.write("\n### Contracts (in recommended pickup/delivery order):\n\n")
            for con in ordered_contracts:
                from_locs = con.from_Location if isinstance(
                    con.from_Location, list) else [con.from_Location]
                from_loc_text = ", ".join(loc.name for loc in from_locs)
                lines = []
                lines.append(
                    f"- #### {con.contract_Rank} Rank - {con.contract_Type} {con.contract_Size} Cargo")
                lines.append(f"  - Type: {con.contract_Size}")
                lines.append("")
                lines.append("  - From:")
                lines.append(f"    - {from_loc_text}")
                lines.append("")
                lines.append("  - To:")
                for amount, item, location in con.deliveries:
                    lines.append(
                        f"    - {amount} SCU {item} -> {location.name} on {location.planet}")
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
    print(f"Using ship: {selected_ship.ship_Name}")
    print(f"Max Cargo: {selected_ship.ship_Max_Cargo} SCU, Max Container: {
          selected_ship.ship_Max_Container} SCU")
    print(f"Capabilities: {[cap for cap in selected_ship.ship_Capabilities]}")

    top_routes = find_top_routes(
        contracts, ship_Max_Cargo, max_Delivery_Locations, top_n=5)

    if not top_routes:
        print("No feasible routes found.")
        return

    full_routes = []
    for selected_contracts, used_locations, total_pay, start_loc in top_routes:
        backhauls = find_backhaul_contracts(
            selected_contracts, contracts, ship_Max_Cargo, max_Delivery_Locations, start_loc)

        for b in backhauls:
            if b not in selected_contracts:
                can_add, reason = can_add_contract_with_dynamic_cargo(
                    selected_contracts, b, ship_Max_Cargo, max_Delivery_Locations, start_loc=start_loc)
                if can_add:
                    selected_contracts.append(b)
                    from_locs = b.from_Location if isinstance(
                        b.from_Location, list) else [b.from_Location]
                    used_locations.update(from_locs)
                    for _, _, dloc in b.deliveries:
                        used_locations.add(dloc)
                    total_pay += b.contract_Pay

        full_routes.append(
            (selected_contracts, used_locations, total_pay, start_loc))

    full_routes.sort(key=lambda r: r[2], reverse=True)

    print(f"\nFound {len(full_routes)} route options.\n")

    for i, (selected_contracts, used_locations, total_pay, start_loc) in enumerate(full_routes, 1):
        print(f"Route Option {i}")
        print(f"Start Location: {start_loc.name}")
        print(f"Total Profit: {total_pay:,} aUEC")
        print(f"Contracts: {len(selected_contracts)}")
        print("----")

    save_routes_to_markdown(full_routes, top_n=5)


contract_cargo = {}


if __name__ == "__main__":
    def compute_contract_cargo(contracts_list):
        contract_cargo_dict = {}
        for con in contracts_list:
            cargo_list = []
            for amount, item, dloc in con.deliveries:
                cargo_list.append(
                    {"amount": amount, "item": item, "to_loc": dloc})
            contract_cargo_dict[con] = cargo_list
        return contract_cargo_dict

    contract_cargo = compute_contract_cargo(mc + hu)

    main()
