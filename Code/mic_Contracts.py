
from myLocations import *
from myDefinitions import *

# Rookie Small Contracts
mic_Contract_1 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=planetary,
    contract_Size=extra_Small,
    from_Location=port_Tressler,
    deliveries=[(5, "Carbon", greycat_IV),
                (4, "Carbon", sakura_Gold)
                ],
    max_Container=1,
    contract_Pay=61500)

mic_Contract_2 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=planetary,
    contract_Size=extra_Small,
    from_Location=port_Tressler,
    deliveries=[(4, "Titanium", greycat_IV),
                (3, "Titanium", new_Babbage)
                ],
    max_Container=1,
    contract_Pay=61500)

mic_Contract_3 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=planetary,
    contract_Size=extra_Small,
    from_Location=port_Tressler,
    deliveries=[(5, "Quartz", greycat_IV),
                (4, "Quartz", sakura_Gold)
                ],
    max_Container=1,
    contract_Pay=61500)

mic_Contract_4 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=planetary,
    contract_Size=extra_Small,
    from_Location=port_Tressler,
    deliveries=[(5, "Aluminum", new_Babbage),
                (4, "Aluminum", sakura_Gold)
                ],
    max_Container=1,
    contract_Pay=61500)

mic_Contract_5 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=direct+planetary,
    contract_Size=small,
    from_Location=new_Babbage,
    deliveries=[(15, "Agricultural Supplies", port_Tressler)
                ],
    max_Container=4,
    contract_Pay=34500)

mic_Contract_6 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=direct+planetary,
    contract_Size=extra_Small,
    from_Location=port_Tressler,
    deliveries=[(11, "Silicon", sakura_Gold)
                ],
    max_Container=1,
    contract_Pay=50250)

mic_Contract_7 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=direct+planetary,
    contract_Size=extra_Small,
    from_Location=port_Tressler,
    deliveries=[(11, "Titanium", sakura_Gold)
                ],
    max_Container=1,
    contract_Pay=50250)

mic_Contract_8 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=direct+planetary,
    contract_Size=extra_Small,
    from_Location=port_Tressler,
    deliveries=[(10, "Carbon", sakura_Gold)
                ],
    max_Container=1,
    contract_Pay=50250)

mic_Contract_9 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=direct+planetary,
    contract_Size=extra_Small,
    from_Location=port_Tressler,
    deliveries=[(10, "Quartz", sakura_Gold)
                ],
    max_Container=1,
    contract_Pay=50250)

mic_Contract_10 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=direct+planetary,
    contract_Size=small,
    from_Location=port_Tressler,
    deliveries=[(10, "Agricultural Supplies", microTech_D13)
                ],
    max_Container=4,
    contract_Pay=37250)

mic_Contract_11 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=direct+planetary,
    contract_Size=small,
    from_Location=port_Tressler,
    deliveries=[(18, "Hydrogen", microTech_D13)
                ],
    max_Container=4,
    contract_Pay=43750)

mic_Contract_12 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=direct+planetary,
    contract_Size=small,
    from_Location=microTech_D13,
    deliveries=[(10, "Agricultural Supplies", port_Tressler),
                ],
    max_Container=4,
    contract_Pay=45000)

mic_Contract_13 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=direct+planetary,
    contract_Size=small,
    from_Location=port_Tressler,
    deliveries=[(15, "Agricultural Supplies", new_Babbage),
                ],
    max_Container=4,
    contract_Pay=37250)

mic_Contract_14 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=direct+planetary,
    contract_Size=extra_Small,
    from_Location=port_Tressler,
    deliveries=[(7, "Aluminum", new_Babbage),
                ],
    max_Container=1,
    contract_Pay=50250)

mic_Contract_15 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=direct+planetary,
    contract_Size=small,
    from_Location=port_Tressler,
    deliveries=[(12, "Tin", sakura_Gold),
                ],
    max_Container=4,
    contract_Pay=37250)

mic_Contract_16 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=direct+planetary,
    contract_Size=small,
    from_Location=port_Tressler,
    deliveries=[(15, "Pressurized Ice", sakura_Gold), (13, "Processed Food", sakura_Gold)
                ],
    max_Container=4,
    contract_Pay=43750)

mic_Contract_17 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=planetary,
    contract_Size=small,
    from_Location=port_Tressler,
    deliveries=[(6, "Tin", greycat_IV), (4, "Tin", sakura_Gold)
                ],
    max_Container=4,
    contract_Pay=48500)

mic_Contract_18 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=planetary,
    contract_Size=small,
    from_Location=port_Tressler,
    deliveries=[(4, "Agricultural Supplies", rayari_Anvik), (5, "Agricultural Supplies", rayari_Deltana)
                ],
    max_Container=4,
    contract_Pay=48500)

mic_Contract_19 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=planetary,
    contract_Size=small,
    from_Location=port_Tressler,
    deliveries=[(6, "Stims", rayari_McGrath), (4, "Stims", rayari_Cantwell)
                ],
    max_Container=4,
    contract_Pay=48500)

mic_Contract_20 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=planetary,
    contract_Size=small,
    from_Location=port_Tressler,
    deliveries=[(11, "Hydrogen", rayari_Cantwell), (15, "Hydrogen", rayari_Anvik)
                ],
    max_Container=4,
    contract_Pay=55000)

mic_Contract_21 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=planetary,
    contract_Size=small,
    from_Location=port_Tressler,
    deliveries=[(7, "Stims", greycat_IV), (5, "Stims", sakura_Gold)
                ],
    max_Container=4,
    contract_Pay=48500)

mic_Contract_22 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=direct+planetary,
    contract_Size=small,
    from_Location=port_Tressler,
    deliveries=[(11, "Stims", devlin_Scrap),
                ],
    max_Container=4,
    contract_Pay=37250)

mic_Contract_23 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=direct+planetary,
    contract_Size=small,
    from_Location=port_Tressler,
    deliveries=[(12, "Stims", microTech_D13),
                ],
    max_Container=4,
    contract_Pay=37250)

mic_Contract_24 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=planetary,
    contract_Size=extra_Small,
    from_Location=port_Tressler,
    deliveries=[(5, "Silicon", new_Babbage), (5, "Silicon", mic_L3)
                ],
    max_Container=1,
    contract_Pay=61500)

mic_Contract_25 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=direct+planetary,
    contract_Size=small,
    from_Location=port_Tressler,
    deliveries=[(8, "Pressurized Ice", devlin_Scrap), (14, "Processed Food", devlin_Scrap)
                ],
    max_Container=4,
    contract_Pay=43750)

mic_Contract_26 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=direct+planetary,
    contract_Size=small,
    from_Location=microTech_D01,
    deliveries=[(5, "Waste", port_Tressler), (7, "Scrap", port_Tressler)
                ],
    max_Container=4,
    contract_Pay=45000)

mic_Contract_27 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=direct+solar,
    contract_Size=extra_Small,
    from_Location=mic_L2,
    deliveries=[(11, "Silicon", mic_L3),
                ],
    max_Container=1,
    contract_Pay=63500)

mic_Contract_28 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=direct+solar,
    contract_Size=extra_Small,
    from_Location=mic_L2,
    deliveries=[(10, "Carbon", port_Tressler),
                ],
    max_Container=1,
    contract_Pay=45750)

mic_Contract_29 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=direct+solar,
    contract_Size=small,
    from_Location=mic_L3,
    deliveries=[(4, "Waste", port_Tressler), (5, "Scrap", port_Tressler)
                ],
    max_Container=4,
    contract_Pay=44500)

mic_Contract_30 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=direct+solar,
    contract_Size=small,
    from_Location=port_Tressler,
    deliveries=[(9, "Stims", mic_L3),
                ],
    max_Container=4,
    contract_Pay=44500)

mic_Contract_31 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=solar,
    contract_Size=small,
    from_Location=mic_L4, mic_L1,
    deliveries=[(3, "Waste", port_Tressler), (3, "Waste", port_Tressler), (3, "Scrap", port_Tressler), (2, "Scrap", port_Tressler),
                ],
    max_Container=4,
    contract_Pay=50250)

mic_Contract_32 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=solar,
    contract_Size=small,
    from_Location=port_Tressler,
    deliveries=[(6, "Stims", mic_L4), (5, "Stims", mic_L2),
                ],
    max_Container=4,
    contract_Pay=50250)

mic_Contract_33 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=solar,
    contract_Size=extra_Small,
    from_Location=seraphim_Station,
    deliveries=[(4, "Carbon", port_Tressler), (4, "Carbon", everus_Harbor)
                ],
    max_Container=1,
    contract_Pay=63250)

mic_Contract_34 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=direct+solar,
    contract_Size=small,
    from_Location=seraphim_Station,
    deliveries=[(9, "Agricultural Supplies", everus_Harbor),
                ],
    max_Container=4,
    contract_Pay=41750)

mic_Contract_35 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=direct+interstellar,
    contract_Size=small,
    from_Location=everus_Harbor,
    deliveries=[(9, "Agricultural Supplies", pyro_Gateway),
                ],
    max_Container=4,
    contract_Pay=40000)

# Rookie Medium Contracts
mic_Contract_36 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=direct+planetary,
    contract_Size=medium,
    from_Location=new_Babbage,
    deliveries=[(46, "Waste", port_Tressler), (55, "Scrap", port_Tressler)
                ],
    max_Container=8,
    contract_Pay=53000)

mic_Contract_37 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=direct+planetary,
    contract_Size=medium,
    from_Location=new_Babbage,
    deliveries=[(108, "Stims", port_Tressler),
                ],
    max_Container=8,
    contract_Pay=76500)

mic_Contract_38 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=solar,
    contract_Size=medium,
    from_Location=port_Tressler,
    deliveries=[(103, "Quartz (Raw)", mic_L2),
                ],
    max_Container=8,
    contract_Pay=51250)

mic_Contract_39 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=direct+solar,
    contract_Size=medium,
    from_Location=mic_L2,
    deliveries=[(84, "Silicon", port_Tressler),
                ],
    max_Container=8,
    contract_Pay=51250)

# Junior Small Contracts

# Automatically collect all mic_Contract_* variables into a list
microTech_contracts = [
    value for name, value in globals().items()
    if name.startswith("mic_Contract_")
]
