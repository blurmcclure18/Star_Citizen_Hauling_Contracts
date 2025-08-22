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


def can_add_contract_with_dynamic_cargo(selected_contracts, candidate_contract, ship_Max_Cargo, max_Delivery_Locations, ignore_max_locations=False):
    """
    Returns (True, "") if candidate_contract can be added without exceeding cargo or location constraints,
    otherwise (False, reason_string).

    If ignore_max_locations=True, max delivery locations constraint is skipped.
    """
    all_contracts = selected_contracts + [candidate_contract]

    loc_order = []

    def add_loc(loc):
        if loc not in loc_order:
            loc_order.append(loc)

    # Build location order from pickups and deliveries
    for con in all_contracts:
        from_locs = con.from_Location if isinstance(
            con.from_Location, list) else [con.from_Location]
        for loc in from_locs:
            add_loc(loc)

    for con in all_contracts:
        for _, _, dloc in con.deliveries:
            add_loc(dloc)

    # Check delivery locations count constraint only if NOT ignoring it
    if not ignore_max_locations:
        unique_delivery_locations = set()
        for con in all_contracts:
            for _, _, dloc in con.deliveries:
                unique_delivery_locations.add(dloc)

        if len(unique_delivery_locations) > max_Delivery_Locations:
            return (False, f"Exceeded max delivery locations: {len(unique_delivery_locations)} > {max_Delivery_Locations}")

    onboard = []

    for loc in loc_order:
        # Dropoff cargo for this loc
        onboard = [cargo for cargo in onboard if cargo['to_loc'] != loc]

        # Pickup cargo ONLY for deliveries whose paired from_Location == loc
        for con in all_contracts:
            from_locs = con.from_Location if isinstance(
                con.from_Location, list) else [con.from_Location]
            deliveries = con.deliveries
            for idx, pickup_loc in enumerate(from_locs):
                if loc == pickup_loc:
                    amount, item, dloc = deliveries[idx]
                    onboard.append(
                        {'amount': amount, 'item': item, 'to_loc': dloc})

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
    unique_from_locations = set()
    for c in contracts:
        from_locs = c.from_Location if isinstance(
            c.from_Location, list) else [c.from_Location]
        for loc in from_locs:
            unique_from_locations.add(loc)

    best_route = None
    best_total_pay = 0

    for start_loc in unique_from_locations:
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

        if any(loc in delivery_locations for loc in from_locs):
            # Backhaul contracts ignore max delivery location limit
            can_add, reason = can_add_contract_with_dynamic_cargo(
                selected_contracts, con, ship_Max_Cargo, max_Delivery_Locations, ignore_max_locations=True)
            if can_add:
                backhaul_candidates.append(con)

    return backhaul_candidates


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


def simulate_route_with_debug(selected_contracts, start_loc, ship_Max_Cargo, debug_file):
    """
    Simulates the route with detailed debug output written to debug_file.
    Cargo pickups are done per contract *all at once* at a location.
    """
    loc_order = []
    loc_set = set()

    def add_loc(loc):
        if loc not in loc_set:
            loc_set.add(loc)
            loc_order.append(loc)

    # Build location order from pickups and deliveries
    for con in selected_contracts:
        from_locs = con.from_Location if isinstance(
            con.from_Location, list) else [con.from_Location]
        for loc in from_locs:
            add_loc(loc)
    for con in selected_contracts:
        for _, _, dloc in con.deliveries:
            add_loc(dloc)

    onboard_cargo = []

    with open(debug_file, "w", encoding="utf-8") as f:
        f.write(f"[DEBUG] Starting route simulation from {start_loc.name}\n")

        for loc in loc_order:
            f.write(f"[DEBUG] Location: {loc.name}\n")
            # Dropoff cargo
            dropoff = [
                cargo for cargo in onboard_cargo if cargo["to_loc"] == loc]
            if dropoff:
                f.write("  Dropoff cargo:\n")
                for cargo in dropoff:
                    f.write(
                        f"    - {cargo['amount']} SCU {cargo['item']} destined for {cargo['to_loc'].name}\n")
                # Remove dropped off cargo
                onboard_cargo = [
                    cargo for cargo in onboard_cargo if cargo["to_loc"] != loc]
            else:
                f.write("  No cargo to drop off.\n")

            # Group pickups by contract at this location
            pickups_by_contract = {}
            for con in selected_contracts:
                from_locs = con.from_Location if isinstance(
                    con.from_Location, list) else [con.from_Location]
                deliveries = con.deliveries
                for idx, pickup_loc in enumerate(from_locs):
                    if pickup_loc == loc:
                        if con not in pickups_by_contract:
                            pickups_by_contract[con] = []
                        pickups_by_contract[con].append(deliveries[idx])

            # Try to pickup cargo contract-by-contract
            for con, pickups in pickups_by_contract.items():
                total_pickup = sum(amount for amount, _, _ in pickups)
                current_load = sum(cargo['amount'] for cargo in onboard_cargo)

                f.write(f"  Trying pickup: {total_pickup} SCU total from contract at {
                        loc.name} (current load: {current_load} SCU)\n")

                if current_load + total_pickup <= ship_Max_Cargo:
                    for amount, item, dloc in pickups:
                        onboard_cargo.append(
                            {'amount': amount, 'item': item, 'to_loc': dloc})
                        f.write(f"  Picked up cargo: {amount} SCU {
                                item}, new load: {current_load + amount} SCU\n")
                        current_load += amount
                else:
                    f.write(f"  [DEBUG] Cannot pickup: would exceed capacity {
                            current_load + total_pickup} > {ship_Max_Cargo}\n")

            total_load = sum(cargo['amount'] for cargo in onboard_cargo)
            f.write(f"  Cargo onboard after {loc.name}: {total_load} SCU\n\n")


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
                    deliveries = con.deliveries
                    for idx, pickup_loc in enumerate(from_locs):
                        if loc == pickup_loc:
                            amount, item, dloc = deliveries[idx]
                            pickups.append({
                                "amount": amount,
                                "item": item,
                                "from_loc": pickup_loc,
                                "to_loc": dloc,
                                "contract": con
                            })

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

    # Write debug simulation of final route to test_debug_route.md
    simulate_route_with_debug(
        selected_contracts, start_loc, ship_Max_Cargo, "test_debug_route.md")

    routes = [(selected_contracts, used_locations, total_pay, start_loc)]
    save_routes_to_markdown(routes, top_n=1)


if __name__ == "__main__":
    main()
