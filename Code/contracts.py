# Location Class


class Location:
    def __init__(self, name, location_type, planet):
        self.name = name
        self.location_type = location_type
        self.planet = planet


# String Location Types
planetary = "Planetary"
solar = "Solar"
interstellar = "Interstellar"
direct = "Direct "

# String Contract Ranks
rookie = "Rookie"
junior = "Junior"
member = "Member"
experienced = "Experienced"
senior = "Senior"

# String Contract Sizes
extra_Small = "Extra Small"
small = "Small"
medium = "Medium"
large = "Large"

# String Location Names (Planets)
microTech = "microTech"
hurston = "Hurston"
crusader = "Crusader"
arccorp = "ArcCorp"

# Pickup and Delivery Locations

# Solar Locations

# Major Stations
port_Tressler = Location("Port Tressler", solar, microTech)
everus_Harbor = Location("Everus Harbor", solar, hurston)
seraphim_Station = Location("Seraphim Station", solar, crusader)
baijini_Point = Location("Baijini Point", solar, arccorp)

# Lagrange Points

# microTech
mic_L1 = Location("MIC-L1", solar, "None")
mic_L2 = Location("MIC-L2", solar, "None")
mic_L3 = Location("MIC-L3", solar, "None")
mic_L4 = Location("MIC-L4", solar, "None")
mic_L5 = Location("MIC-L5", solar, "None")

# Crusader
cru_L1 = Location("CRU-L1", solar, "None")
cru_L4 = Location("CRU-L4", solar, "None")

# ArcCorp
arc_L5 = Location("ARC-L5", solar, "None")

# Hurston
hur_L2 = Location("HUR-L2", solar, "None")

# Interstellar Locations
pyro_Gateway = Location("Pyro Gateway", interstellar, "None")
terra_Gateway = Location("Terra Gateway", interstellar, "None")
magnus_Gateway = Location("Magnus Gateway", interstellar, "None")

# Planet Locations (microTech)
new_Babbage = Location(
    'New Babbage', planetary, microTech)

sakura_Gold = Location(
    'Sakura Sun Goldenrod Workcenter', planetary, microTech)

greycat_IV = Location(
    'Greycat Stanton IV Production Complex-A', planetary, microTech)

covalex_C05 = Location(
    "Covalex Distribution Center S4DC05", planetary, microTech)

microTech_D01 = Location(
    'microTech Logistics Depot S4LD01', planetary, microTech)

microTech_D13 = Location(
    'microTech Logistics Depot S4LD13', planetary, microTech)

rayari_Deltana = Location(
    'Rayari Deltana Research Outpost', planetary, microTech)

# Surrounding Planets (microTech)
rayari_Anvik = Location(
    'Rayari Anvik Research Outpost', planetary, "Calliope")

shubin_SMCa6 = Location(
    'Shubin Mining Facility SMCa-6', planetary, "Calliope")

shubin_SMCa8 = Location(
    'Shubin Mining Facility SMCa-8', planetary, "Calliope")

rayari_McGrath = Location(
    'Rayari McGrath Research Outpost', planetary, "Clio")

rayari_Cantwell = Location(
    'Rayari Cantwell Research Outpost', planetary, "Clio")

devlin_Scrap = Location(
    'Devlin Scrap & Salvage', planetary, "Euterpe")


# Update the constructor signature


class Contract:
    def __init__(self, contract_Origin, contract_Rank, contract_Type, contract_Size, from_Location, deliveries, max_Container, contract_Pay):
        self.contract_Origin = contract_Origin
        self.contract_Rank = contract_Rank
        self.contract_Type = contract_Type
        self.contract_Size = contract_Size
        self.from_Location = from_Location
        # List of tuples: [(amount, item, location), ...]
        self.deliveries = deliveries
        self.max_Container = max_Container
        self.contract_Pay = contract_Pay


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


# Rookie Contracts
rook_Contract_1 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=planetary,
    contract_Size=extra_Small,
    from_Location=port_Tressler,
    deliveries=[
        (5, "Carbon", greycat_IV),
        (4, "Carbon", sakura_Gold)
    ],
    max_Container=1,
    contract_Pay=61500)

rook_Contract_2 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=planetary,
    contract_Size=extra_Small,
    from_Location=port_Tressler,
    deliveries=[
        (4, "Titanium", greycat_IV),
        (3, "Titanium", new_Babbage)
    ],
    max_Container=4,
    contract_Pay=61500)

rook_Contract_3 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=direct+planetary,
    contract_Size=small,
    from_Location=new_Babbage,
    deliveries=[
        (15, "Agricultural Supplies", port_Tressler)
    ],
    max_Container=4,
    contract_Pay=34500)

if len(rook_Contract_2.deliveries) < 2:
    print("1 delivery location")
elif len(rook_Contract_2.deliveries) >= 2:
    print("2 or more delivery locations")

print_Contract(rook_Contract_1)
print_Contract(rook_Contract_2)
print_Contract(rook_Contract_3)
total_Profit = rook_Contract_1.contract_Pay + rook_Contract_2.contract_Pay

formatted_Total_Profit = '{:,}'.format(total_Profit)

print("Total Profit:", formatted_Total_Profit, "aUEC")
