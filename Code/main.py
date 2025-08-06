from mic_Contracts import *


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


for contract in microTech_contracts:
    print_Contract(contract)

# print_Contract(mic_Contract_1)
# print_Contract(mic_Contract_2)
# print_Contract(mic_Contract_3)
# total_Profit = mic_Contract_1.contract_Pay + mic_Contract_2.contract_Pay

# formatted_Total_Profit = '{:,}'.format(total_Profit)

# print("Total Profit:", formatted_Total_Profit, "aUEC")
