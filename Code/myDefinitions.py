# String Location Types
local = "Local"
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

# String Supplies Names
agri_Supplies = "Agricultural Supplies"
carbon = "Carbon"
tin = "Tin"
alum = "Aluminum"
titan = "Titanium"
silicon = "Silicon"
quartz = "Quartz"
hydrogen = "Hydrogen"
press = "Pressurized Ice"
food = "Processed Food"
stim = "Stims"
waste = "Waste"
scrap = "Scrap"
quantum = "Quantum Fuel"
ammo = "Ship Ammunition"
hydro_Fuel = "Hydrogen Fuel"
iron = "Iron (Ore)"
raw = "Quartz (Raw)"


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
