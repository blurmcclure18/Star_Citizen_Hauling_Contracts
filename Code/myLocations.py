from myDefinitions import *

# Location Class


class Location:
    def __init__(self, name, location_type, planet):
        self.name = name
        self.location_type = location_type
        self.planet = planet


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
arc_L1 = Location("ARC-L1", solar, "None")

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

rayari_Kaltag = Location(
    'Rayari Kaltag Research Outpost', planetary, "Calliope")

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

smo_10 = Location(
    'Shubin Mining Facility SMO-10', planetary, microTech)

smo_13 = Location(
    'Shubin Mining Facility SMO-13', planetary, microTech)

smo_18 = Location(
    'Shubin Mining Facility SMO-18', planetary, microTech)

smo_22 = Location(
    'Shubin Mining Facility SMO-22', planetary, microTech)
