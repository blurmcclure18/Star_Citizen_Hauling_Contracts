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


def can_add_contract_with_dynamic_cargo(selected_contracts, candidate_contract, ship_Max_Cargo, max_Delivery_Locations):
    """
    Returns (True, "") if candidate_contract can be added without exceeding cargo or location constraints,
    otherwise (False, reason_string).
    """
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

    # Check delivery locations count constraint
    unique_delivery_locations = set()
    for con in all_contracts:
        for _, _, dloc in con.deliveries:
            unique_delivery_locations.add(dloc)

    if len(unique_delivery_locations) > max_Delivery_Locations:
        return (False, f"Exceeded max delivery locations: {len(unique_delivery_locations)} > {max_Delivery_Locations}")

    onboard = []

    for loc in loc_order:
        # Dropoff cargo destined for this loc
        onboard = [cargo for cargo in onboard if cargo['to_loc'] != loc]

        # Pickup cargo whose from_Location includes this loc
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


def select_contracts(filtered_contracts, ship_Max_Cargo, max_Delivery_Locations):
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
            selected_contracts, c, ship_Max_Cargo, max_Delivery_Locations)
        if can_add:
            selected_contracts.append(c)

    used_locations = set()
    for con in selected_contracts:
        for _, _, dloc in con.deliveries:
            used_locations.add(dloc)

    total_pay = sum(c.contract_Pay for c in selected_contracts)
    return selected_contracts, used_locations, total_pay


def find_best_start_location(contracts, ship_Max_Cargo, max_Delivery_Locations):
    """
    Tries all from_Location options in contracts and returns the best route
    """
    # Collect all unique from locations (support single and list)
    unique_from_locations = set()
    for c in contracts:
        from_locs = c.from_Location if isinstance(
            c.from_Location, list) else [c.from_Location]
        for loc in from_locs:
            unique_from_locations.add(loc)

    best_route = None
    best_total_pay = 0

    for start_loc in unique_from_locations:
        # Filter contracts that start from start_loc (including multi-from)
        filtered_contracts = [
            c for c in contracts if (
                (c.from_Location == start_loc)
                or (isinstance(c.from_Location, list) and start_loc in c.from_Location)
            )
        ]

        selected_contracts, used_locations, total_pay = select_contracts(
            filtered_contracts, ship_Max_Cargo, max_Delivery_Locations)

        if total_pay > best_total_pay:
            best_total_pay = total_pay
            best_route = (selected_contracts, used_locations,
                          total_pay, start_loc)

    return best_route


def find_backhaul_contracts(selected_contracts, all_contracts, ship_Max_Cargo, max_Delivery_Locations):
    delivery_locations = set()
    for con in selected_contracts:
        for _, _, dloc in con.deliveries:
            delivery_locations.add(dloc)

    backhaul_candidates = []
    for con in all_contracts:
        if con in selected_contracts:
            continue

        from_locs = con.from_Location if isinstance(
            con.from_Location, list) else [con.from_Location]

        from_locs_set = set(from_locs)
        overlap = from_locs_set.intersection(delivery_locations)

        if overlap:
            # DEBUG: Print overlapping from locations with delivery locations
            print(f"# DEBUG - overlapping from locations with delivery locations")
            print(f"[DEBUG] Contract from {', '.join(loc.name for loc in from_locs)} overlaps delivery locs: {
                  ', '.join(loc.name for loc in overlap)}")
            print(f"# End DEBUG\n")
            # End DEBUG

            can_add, reason = can_add_contract_with_dynamic_cargo(
                selected_contracts, con, ship_Max_Cargo, max_Delivery_Locations)
            if can_add:
                # DEBUG: Accepted backhaul contract info
                print(f"# DEBUG - accepted backhaul contract")
                print(f"[DEBUG] Contract accepted as backhaul: from {
                      ', '.join(loc.name for loc in from_locs)}")
                print(f"# End DEBUG\n")
                # End DEBUG
                backhaul_candidates.append(con)
            else:
                # DEBUG: Rejected backhaul contract with reason
                print(f"# DEBUG - rejected backhaul contract with reason")
                print(f"[DEBUG] Contract rejected as backhaul: from {
                      ', '.join(loc.name for loc in from_locs)} - Reason: {reason}")
                print(f"# End DEBUG\n")
                # End DEBUG

    return backhaul_candidates


def order_contracts_by_route(selected_contracts, start_loc):
    """
    Orders contracts starting at start_loc, then visits delivery locations in
    order they appear in the selected contracts. Used for route planning.
    """
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
    # Find the best route considering all contracts
    best_route = find_best_start_location(
        contracts, ship_Max_Cargo, max_Delivery_Locations)

    if not best_route:
        print("No feasible route found.")
        return

    selected_contracts, used_locations, total_pay, start_loc = best_route

    # Attempt to add backhaul contracts if possible
    backhauls = find_backhaul_contracts(
        selected_contracts, contracts, ship_Max_Cargo, max_Delivery_Locations)
    if backhauls:
        print(f"\nAdding {len(backhauls)} backhaul contracts.")
        for b in backhauls:
            selected_contracts.append(b)
            for _, _, dloc in b.deliveries:
                used_locations.add(dloc)
            total_pay += b.contract_Pay

    print("\nSelection complete.")
    print(f"Selected {len(selected_contracts)} contracts")
    print(f"Total delivery amount: N/A (calculated dynamically)")
    print(f"Total Profit: {total_pay:,} aUEC")
    print("Delivery locations:")
    for loc in used_locations:
        print(f"- {loc.name} on {loc.planet}")

    print("\nContracts:")
    for con in selected_contracts:
        print_Contract(con)

    routes = [(selected_contracts, used_locations, total_pay, start_loc)]
    save_routes_to_markdown(routes, top_n=1)


if __name__ == "__main__":
    main()
