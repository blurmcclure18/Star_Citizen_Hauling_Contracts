# Location Class
class Location:
    def __init__(self, name, location_type, planet):
        self.name = name
        self.location_type = location_type
        self.planet = planet


# String Location Names
microTech = "microTech"
hurston = "Hurston"
crusader = "Crusader"
planetary = "Planetary"
solar = "Solar"
interstellar = "Interstellar"

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

# Pickup and Delivery Locations

# Solar Locations
port_Tressler = Location("Port Tressler", solar, microTech)
everus_Harbor = Location("Everus Harbor", solar, hurston)
seraphim_Station = Location("Seraphim Station", solar, crusader)
mic_L1 = Location("MIC-L1", solar, microTech)
mic_L2 = Location("MIC-L2", solar, microTech)
mic_L3 = Location("MIC-L3", solar, microTech)
mic_L4 = Location("MIC-L4", solar, microTech)
mic_L5 = Location("MIC-L5", solar, microTech)

# Interstellar Locations
pyro_Gateway = Location("Pyro Gateway", interstellar, "None")

# Planet Locations (microTech)
new_Babbage = Location('New Babbage', planetary, microTech)
sakura_Gold = Location('Sakura Sun Goldenrod Workcenter', planetary, microTech)
greycat_IV = Location('Greycat Stanton IV Production Complex-A', planetary, microTech)
microTech_D01 = Location('microTech Logistics Depot S4LD01', planetary, microTech)
microTech_D13 = Location('microTech Logistics Depot S4LD13', planetary, microTech)
rayari_Deltana = Location('Rayari Deltana Research Outpost', planetary, microTech)

# Surrounding Planets (microTech)
rayari_Anvik = Location('Rayari Anvik Research Outpost', planetary, "Calliope")
rayari_McGrath = Location('Rayari McGrath Research Outpost', planetary, "Clio")
rayari_Cantwell = Location('Rayari Cantwell Research Outpost', planetary, "Clio")
devlin_Scrap = Location('Devlin Scrap & Salvage', planetary, "Euterpe")
shubin_SMCa6 = Location('Shubin Mining Facility SMCa-6', planetary, "Calliope")


# Create Contracts

#class Contract:
#    def __init__(self,contract_Origin, contract_Rank, contract_Type, contract_Size, from_Location, to_Location, contract_Supplies, max_Container, contract_Pay):
#        self.contract_Origin = contract_Origin
#        self.contract_Rank = contract_Rank
#        self.contract_Type = contract_Type
#        self.contract_Size = contract_Size
#        self.from_Location = from_Location
#        self.to_Location = to_Location
#        self.contract_Supplies = contract_Supplies
#        self.max_Container = max_Container
#        self.contract_Pay = contract_Pay

# Update the constructor signature
class Contract:
    def __init__(self, contract_Origin, contract_Rank, contract_Type, contract_Size,
                 from_Location, deliveries, max_Container, contract_Pay):
        self.contract_Origin = contract_Origin
        self.contract_Rank = contract_Rank
        self.contract_Type = contract_Type
        self.contract_Size = contract_Size
        self.from_Location = from_Location
        self.deliveries = deliveries  # List of tuples: [(amount, item, location), ...]
        self.max_Container = max_Container
        self.contract_Pay = contract_Pay

#        def __str__(self):
#            delivery_str = '\n'.join([
#            f"     - {amount} {item} -> {location.name} on {location.planet}"
#            for (amount, item, location) in self.deliveries
#        ])
#
#        return (
#f"""- #### {self.contract_Rank} Rank - {self.contract_Type} {self.contract_Size} Cargo
#   - Type: {self.contract_Size}
#   
#   - From: 
#     - {self.from_Location.name}
#  
#   - To:
#{delivery_str}
#     
#   - Pay: {self.contract_Pay} aUEC
#""")

# Rookie Contracts
rook_Contract_1 = Contract(
    contract_Origin = microTech, 
    contract_Rank = rookie, 
    contract_Type = planetary, 
    contract_Size = extra_Small, 
    from_Location = port_Tressler, 
    deliveries = [
        ("5 SCU", "Carbon", greycat_IV), 
        ("4 SCU", "Carbon", sakura_Gold)
    ], 
    max_Container = "1 SCU", 
    contract_Pay = "61,500")

print(rook_Contract_1.contract_Origin)
