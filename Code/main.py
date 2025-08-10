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
    lines.append(f"    - {con.from_Location.name}")
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

contracts = mc
chosen_location = port_Tressler

filtered_contracts = [
    c for c in contracts if c.from_Location == chosen_location]

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
    print(f"Checking contract {idx}: Pay={c.contract_Pay}, Amount={amount}, "
          f"Locations={len(locs)}, Profitability={profit:.2f}")
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

total_pay = sum(c.contract_Pay for c in selected_contracts)
print("\nSelection complete.")
print(f"Selected {len(selected_contracts)} contracts")
print(f"Total delivery amount: {used_amount} SCU")
print("Delivery locations:")
for loc in used_locations:
    print(f"- {loc.name} on {loc.planet}")

formatted_Total_Profit = '{:,}'.format(total_pay)

print("\nContracts:")

for con in selected_contracts:
    print_Contract(con)

print("Total Profit:", formatted_Total_Profit, "aUEC")
