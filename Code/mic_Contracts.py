from myDefinitions import *
from myLocations import *

# Rookie Small Contracts
mic_Contract_1 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=planetary,
    contract_Size=extra_Small,
    from_Location=port_Tressler,
    deliveries=[(5, carbon, greycat_IV),
                (4, carbon, sakura_Gold)
                ],
    max_Container=1,
    contract_Pay=61500)

mic_Contract_2 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=planetary,
    contract_Size=extra_Small,
    from_Location=port_Tressler,
    deliveries=[(4, titan, greycat_IV),
                (3, titan, new_Babbage)
                ],
    max_Container=1,
    contract_Pay=61500)

mic_Contract_3 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=planetary,
    contract_Size=extra_Small,
    from_Location=port_Tressler,
    deliveries=[(5, quartz, greycat_IV),
                (4, quartz, sakura_Gold)
                ],
    max_Container=1,
    contract_Pay=61500)

mic_Contract_4 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=planetary,
    contract_Size=extra_Small,
    from_Location=port_Tressler,
    deliveries=[(5, alum, new_Babbage),
                (4, alum, sakura_Gold)
                ],
    max_Container=1,
    contract_Pay=61500)

mic_Contract_5 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=direct+planetary,
    contract_Size=small,
    from_Location=new_Babbage,
    deliveries=[(15, agri_Supplies, port_Tressler)
                ],
    max_Container=4,
    contract_Pay=34500)

mic_Contract_6 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=direct+planetary,
    contract_Size=extra_Small,
    from_Location=port_Tressler,
    deliveries=[(11, silicon, sakura_Gold)
                ],
    max_Container=1,
    contract_Pay=50250)

mic_Contract_7 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=direct+planetary,
    contract_Size=extra_Small,
    from_Location=port_Tressler,
    deliveries=[(11, titan, sakura_Gold)
                ],
    max_Container=1,
    contract_Pay=50250)

mic_Contract_8 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=direct+planetary,
    contract_Size=extra_Small,
    from_Location=port_Tressler,
    deliveries=[(10, carbon, sakura_Gold)
                ],
    max_Container=1,
    contract_Pay=50250)

mic_Contract_9 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=direct+planetary,
    contract_Size=extra_Small,
    from_Location=port_Tressler,
    deliveries=[(10, quartz, sakura_Gold)
                ],
    max_Container=1,
    contract_Pay=50250)

mic_Contract_10 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=direct+planetary,
    contract_Size=small,
    from_Location=port_Tressler,
    deliveries=[(10, agri_Supplies, microTech_D13)
                ],
    max_Container=4,
    contract_Pay=37250)

mic_Contract_11 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=direct+planetary,
    contract_Size=small,
    from_Location=port_Tressler,
    deliveries=[(18, hydrogen, microTech_D13)
                ],
    max_Container=4,
    contract_Pay=43750)

mic_Contract_12 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=direct+planetary,
    contract_Size=small,
    from_Location=microTech_D13,
    deliveries=[(10, agri_Supplies, port_Tressler),
                ],
    max_Container=4,
    contract_Pay=45000)

mic_Contract_13 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=direct+planetary,
    contract_Size=small,
    from_Location=port_Tressler,
    deliveries=[(15, agri_Supplies, new_Babbage),
                ],
    max_Container=4,
    contract_Pay=37250)

mic_Contract_14 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=direct+planetary,
    contract_Size=extra_Small,
    from_Location=port_Tressler,
    deliveries=[(7, alum, new_Babbage),
                ],
    max_Container=1,
    contract_Pay=50250)

mic_Contract_15 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=direct+planetary,
    contract_Size=small,
    from_Location=port_Tressler,
    deliveries=[(12, tin, sakura_Gold),
                ],
    max_Container=4,
    contract_Pay=37250)

mic_Contract_16 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=direct+planetary,
    contract_Size=small,
    from_Location=port_Tressler,
    deliveries=[(15, press, sakura_Gold), (13, food, sakura_Gold)
                ],
    max_Container=4,
    contract_Pay=43750)

mic_Contract_17 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=planetary,
    contract_Size=small,
    from_Location=port_Tressler,
    deliveries=[(6, tin, greycat_IV), (4, tin, sakura_Gold)
                ],
    max_Container=4,
    contract_Pay=48500)

mic_Contract_18 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=planetary,
    contract_Size=small,
    from_Location=port_Tressler,
    deliveries=[(4, agri_Supplies, rayari_Anvik), (5, agri_Supplies, rayari_Deltana)
                ],
    max_Container=4,
    contract_Pay=48500)

mic_Contract_19 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=planetary,
    contract_Size=small,
    from_Location=port_Tressler,
    deliveries=[(6, stim, rayari_McGrath), (4, stim, rayari_Cantwell)
                ],
    max_Container=4,
    contract_Pay=48500)

mic_Contract_20 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=planetary,
    contract_Size=small,
    from_Location=port_Tressler,
    deliveries=[(11, hydrogen, rayari_Cantwell), (15, hydrogen, rayari_Anvik)
                ],
    max_Container=4,
    contract_Pay=55000)

mic_Contract_21 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=planetary,
    contract_Size=small,
    from_Location=port_Tressler,
    deliveries=[(7, stim, greycat_IV), (5, stim, sakura_Gold)
                ],
    max_Container=4,
    contract_Pay=48500)

mic_Contract_22 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=direct+planetary,
    contract_Size=small,
    from_Location=port_Tressler,
    deliveries=[(11, stim, devlin_Scrap),
                ],
    max_Container=4,
    contract_Pay=37250)

mic_Contract_23 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=direct+planetary,
    contract_Size=small,
    from_Location=port_Tressler,
    deliveries=[(12, stim, microTech_D13),
                ],
    max_Container=4,
    contract_Pay=37250)

mic_Contract_24 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=planetary,
    contract_Size=extra_Small,
    from_Location=port_Tressler,
    deliveries=[(5, silicon, new_Babbage), (5, silicon, mic_L3)
                ],
    max_Container=1,
    contract_Pay=61500)

mic_Contract_25 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=direct+planetary,
    contract_Size=small,
    from_Location=port_Tressler,
    deliveries=[(8, press, devlin_Scrap), (14, food, devlin_Scrap)
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
    deliveries=[(11, silicon, mic_L3),
                ],
    max_Container=1,
    contract_Pay=63500)

mic_Contract_28 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=direct+solar,
    contract_Size=extra_Small,
    from_Location=mic_L2,
    deliveries=[(10, carbon, port_Tressler),
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
    deliveries=[(9, stim, mic_L3),
                ],
    max_Container=4,
    contract_Pay=44500)

mic_Contract_31 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=solar,
    contract_Size=small,
    from_Location=[mic_L4, mic_L1],
    deliveries=[(3, "Waste", port_Tressler),
                (3, "Waste", port_Tressler),
                (3, "Scrap", port_Tressler),
                (2, "Scrap", port_Tressler)
                ],
    max_Container=4,
    contract_Pay=50250)

mic_Contract_32 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=solar,
    contract_Size=small,
    from_Location=port_Tressler,
    deliveries=[(6, stim, mic_L4), (5, stim, mic_L2),
                ],
    max_Container=4,
    contract_Pay=50250)

mic_Contract_33 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=solar,
    contract_Size=extra_Small,
    from_Location=seraphim_Station,
    deliveries=[(4, carbon, port_Tressler), (4, carbon, everus_Harbor)
                ],
    max_Container=1,
    contract_Pay=63250)

mic_Contract_34 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=direct+solar,
    contract_Size=small,
    from_Location=seraphim_Station,
    deliveries=[(9, agri_Supplies, everus_Harbor),
                ],
    max_Container=4,
    contract_Pay=41750)

mic_Contract_35 = Contract(
    contract_Origin=microTech,
    contract_Rank=rookie,
    contract_Type=direct+interstellar,
    contract_Size=small,
    from_Location=everus_Harbor,
    deliveries=[(9, agri_Supplies, pyro_Gateway),
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
    deliveries=[(108, stim, port_Tressler),
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
    deliveries=[(84, silicon, port_Tressler),
                ],
    max_Container=8,
    contract_Pay=51250)

# Junior Small Contracts
mic_Contract_40 = Contract(
    contract_Origin=microTech,
    contract_Rank=junior,
    contract_Type=direct,
    contract_Size=small,
    from_Location=rayari_Deltana,
    deliveries=[(12, agri_Supplies, microTech_D13),
                ],
    max_Container=4,
    contract_Pay=52500)

mic_Contract_41 = Contract(
    contract_Origin=microTech,
    contract_Rank=junior,
    contract_Type=direct+local,
    contract_Size=small,
    from_Location=microTech_D13,
    deliveries=[(9, quantum, rayari_Cantwell), (7, hydro_Fuel, rayari_Cantwell), (7, ammo, rayari_Cantwell)
                ],
    max_Container=4,
    contract_Pay=60750)

mic_Contract_42 = Contract(
    contract_Origin=microTech,
    contract_Rank=junior,
    contract_Type=direct+local,
    contract_Size=small,
    from_Location=shubin_SMCa6,
    deliveries=[(6, "Waste", microTech_D13), (4, "Scrap", microTech_D13)
                ],
    max_Container=4,
    contract_Pay=52500)

mic_Contract_43 = Contract(
    contract_Origin=microTech,
    contract_Rank=junior,
    contract_Type=direct+local,
    contract_Size=small,
    from_Location=microTech_D13,
    deliveries=[        (13, press, shubin_SMCa6), (10, food, shubin_SMCa6)
    ],
    max_Container=4,
    contract_Pay=60750)

mic_Contract_44 = Contract(
    contract_Origin=microTech,
    contract_Rank=junior,
    contract_Type=direct+small,
    contract_Size=small,
    from_Location=microTech_D13,
    deliveries=[        (26, hydrogen, rayari_McGrath),
    ],
    max_Container=4,
    contract_Pay=60750)

mic_Contract_45 = Contract(
    contract_Origin=microTech,
    contract_Rank=junior,
    contract_Type=direct+local,
    contract_Size=small,
    from_Location=microTech_D13,
    deliveries=[        (11, stim, shubin_SMCa8),
    ],
    max_Container=4,
    contract_Pay=52500)

mic_Contract_46 = Contract(
    contract_Origin=microTech,
    contract_Rank=junior,
    contract_Type=direct+local,
    contract_Size=small,
    from_Location=microTech_D13,
    deliveries=[        (8, agri_Supplies, rayari_McGrath),
    ],
    max_Container=4,
    contract_Pay=52500)

mic_Contract_47 = Contract(
    contract_Origin=microTech,
    contract_Rank=junior,
    contract_Type=planetary,
    contract_Size=small,
    from_Location=[sakura_Gold, microTech_D13],
    deliveries=[        (2, waste, port_Tressler), (3, waste, port_Tressler), (3, scrap, port_Tressler), (2, scrap, port_Tressler)
    ],
    max_Container=4,
    contract_Pay=59750)

mic_Contract_48 = Contract(
    contract_Origin=microTech,
    contract_Rank=junior,
    contract_Type=planetary,
    contract_Size=small,
    from_Location=[rayari_McGrath, rayari_Cantwell],
    deliveries=[        (3, waste, port_Tressler), (2, waste, port_Tressler), (2, scrap, port_Tressler), (3, scrap, rayari_Cantwell)
    ],
    max_Container=4,
    contract_Pay=59750)

mic_Contract_49 = Contract(
    contract_Origin=microTech,
    contract_Rank=junior,
    contract_Type=planetary,
    contract_Size=small,
    from_Location=port_Tressler,
    deliveries=[        (5, press, sakura_Gold), (4, press, greycat_IV), (6, food, sakura_Gold), (6, food, greycat_IV)
    ],
    max_Container=4,
    contract_Pay=65250)

mic_Contract_50 = Contract(
    contract_Origin=microTech,
    contract_Rank=junior,
    contract_Type=direct+planetary,
    contract_Size=extra_Small,
    from_Location=devlin_Scrap,
    deliveries=[        (6, waste, port_Tressler),
    ],
    max_Container=1,
    contract_Pay=62000)

mic_Contract_51 = Contract(
    contract_Origin=microTech,
    contract_Rank=junior,
    contract_Type=planetary,
    contract_Size=small,
    from_Location=[rayari_Anvik,rayari_McGrath],
    deliveries=[        (6, agri_Supplies, port_Tressler), (6, agri_Supplies, port_Tressler)
    ],
    max_Container=4,
    contract_Pay=59750)

mic_Contract_52 = Contract(
    contract_Origin=microTech,
    contract_Rank=junior,
    contract_Type=planetary,
    contract_Size=small,
    from_Location=port_Tressler,
    deliveries=[        (7, press, rayari_McGrath),(3,press,rayari_Cantwell),(7,food,rayari_McGrath),(6,food,rayari_Cantwell)
    ],
    max_Container=4,
    contract_Pay=65250)

mic_Contract_53 = Contract(
    contract_Origin=microTech,
    contract_Rank=junior,
    contract_Type=planetary,
    contract_Size=small,
    from_Location=port_Tressler,
    deliveries=[        (4, hydro_Fuel, rayari_McGrath),(4, hydro_Fuel,rayari_Cantwell),(6,quantum,rayari_Cantwell),(6, ammo,rayari_McGrath)
    ],
    max_Container=4,
    contract_Pay=65250)

mic_Contract_54 = Contract(
    contract_Origin=microTech,
    contract_Rank=junior,
    contract_Type=solar,
    contract_Size=small,
    from_Location=[seraphim_Station,port_Tressler],
    deliveries=[        (6, agri_Supplies, everus_Harbor), (4, agri_Supplies, everus_Harbor)
    ],
    max_Container=4,
    contract_Pay=57000)

mic_Contract_55 = Contract(
    contract_Origin=microTech,
    contract_Rank=junior,
    contract_Type=direct+solar,
    contract_Size=extra_Small,
    from_Location=seraphim_Station,
    deliveries=[        (10, carbon, everus_Harbor),
    ],
    max_Container=1,
    contract_Pay=56250)

mic_Contract_56 = Contract(
    contract_Origin=microTech,
    contract_Rank=junior,
    contract_Type=direct+solar,
    contract_Size=small,
    from_Location=port_Tressler,
    deliveries=[        (22, press, seraphim_Station),
    ],
    max_Container=4,
    contract_Pay=52250)

mic_Contract_57 = Contract(
    contract_Origin=microTech,
    contract_Rank=junior,
    contract_Type=direct+solar,
    contract_Size=small,
    from_Location=port_Tressler,
    deliveries=[        (10, press, mic_L3), (7, food, mic_L3)
    ],
    max_Container=4,
    contract_Pay=49500)

mic_Contract_58 = Contract(
    contract_Origin=microTech,
    contract_Rank=junior,
    contract_Type=solar,
    contract_Size=small,
    from_Location=port_Tressler,
    deliveries=[        (5, press, mic_L5),
                (3, press, mic_L4),
                (7, food, mic_L5),
                (6, food, mic_L4)
    ],
    max_Container=4,
    contract_Pay=64500)

# Junior Medium Contracts
mic_Contract_59 = Contract(
    contract_Origin=microTech,
    contract_Rank=junior,
    contract_Type=direct+interstellar,
    contract_Size=medium,
    from_Location=everus_Harbor,
    deliveries=[        (104, agri_Supplies, terra_Gateway),
    ],
    max_Container=8,
    contract_Pay=59750)

mic_Contract_60 = Contract(
    contract_Origin=microTech,
    contract_Rank=junior,
    contract_Type=direct+interstellar,
    contract_Size=medium,
    from_Location=pyro_Gateway,
    deliveries=[        (86, tin, everus_Harbor),
    ],
    max_Container=8,
    contract_Pay=57500)

mic_Contract_61 = Contract(
    contract_Origin=microTech,
    contract_Rank=junior,
    contract_Type=direct+planetary,
    contract_Size=medium,
    from_Location=covalex_C05,
    deliveries=[        (52, waste, port_Tressler),(49, scrap, port_Tressler)
    ],
    max_Container=8,
    contract_Pay=69250)

mic_Contract_62 = Contract(
    contract_Origin=microTech,
    contract_Rank=junior,
    contract_Type=direct+planetary,
    contract_Size=medium,
    from_Location=port_Tressler,
    deliveries=[        (92, scrap, devlin_Scrap),
    ],
    max_Container=8,
    contract_Pay=73000)

mic_Contract_63 = Contract(
    contract_Origin=microTech,
    contract_Rank=junior,
    contract_Type=direct+planetary,
    contract_Size=medium,
    from_Location=port_Tressler,
    deliveries=[        (104, tin, new_Babbage),
    ],
    max_Container=8,
    contract_Pay=56000)

mic_Contract_64 = Contract(
    contract_Origin=microTech,
    contract_Rank=junior,
    contract_Type=direct+planetary,
    contract_Size=medium,
    from_Location=port_Tressler,
    deliveries=[        (94, silicon, new_Babbage),
    ],
    max_Container=8,
    contract_Pay=56000)

mic_Contract_65 = Contract(
    contract_Origin=microTech,
    contract_Rank=junior,
    contract_Type=solar,
    contract_Size=medium,
    from_Location=arc_L5,
    deliveries=[        (42, alum, everus_Harbor), (46, alum, port_Tressler)
    ],
    max_Container=8,
    contract_Pay=64250)

mic_Contract_66 = Contract(
    contract_Origin=microTech,
    contract_Rank=junior,
    contract_Type=solar,
    contract_Size=medium,
    from_Location=mic_L1,
    deliveries=[        (41, quartz, port_Tressler), (46, quartz, seraphim_Station)
    ],
    max_Container=8,
    contract_Pay=68250)

mic_Contract_67 = Contract(
    contract_Origin=microTech,
    contract_Rank=junior,
    contract_Type=direct+solar,
    contract_Size=medium,
    from_Location=mic_L1,
    deliveries=[        (99, quartz, port_Tressler),
    ],
    max_Container=8,
    contract_Pay=55250)

mic_Contract_68 = Contract(
    contract_Origin=microTech,
    contract_Rank=junior,
    contract_Type=solar,
    contract_Size=medium,
    from_Location=cru_L4,
    deliveries=[        (43, alum, baijini_Point), (42, alum, seraphim_Station)
    ],
    max_Container=8,
    contract_Pay=66750)

mic_Contract_69 = Contract(
    contract_Origin=microTech,
    contract_Rank=junior,
    contract_Type=direct+solar,
    contract_Size=medium,
    from_Location=cru_L1,
    deliveries=[        (99, alum, port_Tressler),
    ],
    max_Container=8,
    contract_Pay=57500)

mic_Contract_70 = Contract(
    contract_Origin=microTech,
    contract_Rank=junior,
    contract_Type=solar,
    contract_Size=medium,
    from_Location=hur_L2,
    deliveries=[        (44, quartz, seraphim_Station), (48, quartz, everus_Harbor)
    ],
    max_Container=8,
    contract_Pay=64500)

mic_Contract_71 = Contract(
    contract_Origin=microTech,
    contract_Rank=junior,
    contract_Type=direct+solar,
    contract_Size=medium,
    from_Location=arc_L5,
    deliveries=[        (81, alum, seraphim_Station),
    ],
    max_Container=8,
    contract_Pay=59500)

mic_Contract_72 = Contract(
    contract_Origin=microTech,
    contract_Rank=junior,
    contract_Type=solar,
    contract_Size=medium,
    from_Location=cru_L1,
    deliveries=[        (45, titan, seraphim_Station), (40, titan, port_Tressler)
    ],
    max_Container=8,
    contract_Pay=66750)

mic_Contract_73 = Contract(
    contract_Origin=microTech,
    contract_Rank=junior,
    contract_Type=solar,
    contract_Size=medium,
    from_Location=everus_Harbor,
    deliveries=[        (48, tin, baijini_Point), (43, tin, seraphim_Station)
    ], 
    max_Container=8,
    contract_Pay=69250)

mic_Contract_74 = Contract(
    contract_Origin=microTech,
    contract_Rank=junior,
    contract_Type=direct+solar,
    contract_Size=medium,
    from_Location=cru_L1,
    deliveries=[        (50, alum, baijini_Point), (51, titan, baijini_Point)
    ],
    max_Container=8,
    contract_Pay=57500)

mic_Contract_75 = Contract(
    contract_Origin=microTech,
    contract_Rank=junior,
    contract_Type=direct+solar,
    contract_Size=medium,
    from_Location=hur_L2,
    deliveries=[        (86, quartz, everus_Harbor),
    ],
    max_Container=8,
    contract_Pay=55250)

mic_Contract_76 = Contract(
    contract_Origin=microTech,
    contract_Rank=junior,
    contract_Type=direct+solar,
    contract_Size=medium,
    from_Location=everus_Harbor,
    deliveries=[        (109, tin, seraphim_Station),
    ],
    max_Container=8,
    contract_Pay=57750)

mic_Contract_77 = Contract(
    contract_Origin=microTech,
    contract_Rank=junior,
    contract_Type=direct+solar,
    contract_Size=medium,
    from_Location=cru_L1,
    deliveries=[        (83, titan, everus_Harbor),
    ],
    max_Container=8,
    contract_Pay=57500)

mic_Contract_78 = Contract(
    contract_Origin=microTech,
    contract_Rank=junior,
    contract_Type=direct+solar,
    contract_Size=medium,
    from_Location=everus_Harbor,
    deliveries=[        (91, stim, port_Tressler),
    ],
    max_Container=8,
    contract_Pay=87250)

# Member Small Contracts
mic_Contract_79 = Contract(
    contract_Origin=microTech,
    contract_Rank=member,
    contract_Type=planetary,
    contract_Size=small,
    from_Location=port_Tressler,
    deliveries=[(2, stim, shubin_SMCa6),
                (3, stim, rayari_Kaltag),
                (3, stim, rayari_Anvik),
                (2, stim, shubin_SMCa8)
    ],
    max_Container=4,
    contract_Pay=90750)

mic_Contract_80 = Contract(
    contract_Origin=microTech,
    contract_Rank=member,
    contract_Type=planetary,
    contract_Size=small,
    from_Location=port_Tressler,
    deliveries=[(4, stim, covalex_C05),
                (4, stim, sakura_Gold),
                (4, stim, greycat_IV),
    ],
    max_Container=4,
    contract_Pay=90250)

mic_Contract_81 = Contract(
    contract_Origin=microTech,
    contract_Rank=member,
    contract_Type=planetary,
    contract_Size=small,
    from_Location=[microTech_D13,microTech_D01,sakura_Gold,microTech_D13],
    deliveries=[(3, waste, port_Tressler),
                (2, scrap, port_Tressler),
                (2, waste, port_Tressler),
                (2, scrap, port_Tressler)
    ],
    max_Container=4,
    contract_Pay=95000)

mic_Contract_82 = Contract(
    contract_Origin=microTech,
    contract_Rank=member,
    contract_Type=planetary,
    contract_Size=small,
    from_Location=port_Tressler,
    deliveries=[(3, stim, sakura_Gold),
                (3, stim, microTech_D01),
                (2, stim, greycat_IV),
                (2, stim, microTech_D13)
    ],
    max_Container=4,
    contract_Pay=90750)

mic_Contract_83 = Contract(
    contract_Origin=microTech,
    contract_Rank=member,
    contract_Type=planetary,
    contract_Size=small,
    from_Location=port_Tressler,
    deliveries=[(7, press, sakura_Gold),
                (5, press, microTech_D13),
                (7, food, microTech_D01),
                (6, food, sakura_Gold)
    ],
    max_Container=4,
    contract_Pay=121750)

mic_Contract_84 = Contract(
    contract_Origin=microTech,
    contract_Rank=member,
    contract_Type=planetary,
    contract_Size=small,
    from_Location=port_Tressler,
    deliveries=[(5, hydro_Fuel, rayari_Kaltag),
                (2, hydro_Fuel, shubin_SMCa8),
                (9, quantum, shubin_SMCa6),
                (7, ammo, rayari_Anvik)
    ],
    max_Container=4,
    contract_Pay=123500)


mic_Contract_85 = Contract(
    contract_Origin=microTech,
    contract_Rank=member,
    contract_Type=planetary,
    contract_Size=small,
    from_Location=port_Tressler,
    deliveries=[(8, alum, sakura_Gold),
                (4, alum, greycat_IV),
                (5, alum, new_Babbage)
    ],
    max_Container=4,
    contract_Pay=99500)

mic_Contract_86 = Contract(
    contract_Origin=microTech,
    contract_Rank=member,
    contract_Type=planetary,
    contract_Size=small,
    from_Location=port_Tressler,
    deliveries=[(10, titan, new_Babbage),
                (9, titan, greycat_IV),
                (8, titan, sakura_Gold)
    ],
    max_Container=4,
    contract_Pay=99500)

mic_Contract_87 = Contract(
    contract_Origin=microTech,
    contract_Rank=member,
    contract_Type=planetary,
    contract_Size=small,
    from_Location=port_Tressler,
    deliveries=[(5, quartz, new_Babbage),
                (5, quartz, sakura_Gold), 
                (10, quartz, greycat_IV)
    ],
    max_Container=4,
    contract_Pay=99500)

mic_Contract_88 = Contract(
    contract_Origin=microTech,
    contract_Rank=member,
    contract_Type=planetary,
    contract_Size=small,
    from_Location=port_Tressler,
    deliveries=[(4, carbon, new_Babbage),
                (4, carbon, sakura_Gold),
                (4, carbon, greycat_IV)
    ],
    max_Container=4,
    contract_Pay=90250)

mic_Contract_89 = Contract(
    contract_Origin=microTech,
    contract_Rank=member,
    contract_Type=solar,
    contract_Size=small,
    from_Location=port_Tressler,
    deliveries=[(4, stim, mic_L5),
                (3, stim, mic_L3),
                (3, stim, mic_L2)
    ],
    max_Container=4,
    contract_Pay=96500)

mic_Contract_90 = Contract(
    contract_Origin=microTech,
    contract_Rank=member,
    contract_Type=solar,
    contract_Size=small,
    from_Location=[mic_L4, mic_L3, mic_L1, mic_L4],
    deliveries=[(3, waste, port_Tressler),
                (3, scrap, port_Tressler),
                (3, waste, port_Tressler),
                (2, scrap, port_Tressler)
    ],
    max_Container=4,
    contract_Pay=96500)

# Member Medium Contracts
mic_Contract_91 = Contract(
    contract_Origin=microTech,
    contract_Rank=member,
    contract_Type=direct+interstellar,
    contract_Size=medium,
    from_Location=magnus_Gateway,
    deliveries=[        (96, stim, everus_Harbor),
    ],
    max_Container=8,
    contract_Pay=101250)

mic_Contract_92 = Contract(
    contract_Origin=microTech,
    contract_Rank=member,
    contract_Type=planetary,
    contract_Size=medium,
    from_Location=[greycat_IV,covalex_C05,greycat_IV,covalex_C05],
    deliveries=[(27, waste, port_Tressler),
                (25, waste, port_Tressler),
                (26, scrap, port_Tressler),
                (21, scrap, port_Tressler)
    ],
    max_Container=8,
    contract_Pay=84000)

mic_Contract_93 = Contract(
    contract_Origin=microTech,
    contract_Rank=member,
    contract_Type=solar,
    contract_Size=medium,
    from_Location=cru_L1,
    deliveries=[(23, alum, port_Tressler),
                (26, alum, seraphim_Station),
                (22, titan, port_Tressler), 
                (24, titan, seraphim_Station),
    ],
    max_Container=8,
    contract_Pay=79250)

# Experienced Small Contracts
mic_Contract_95 = Contract(
    contract_Origin=microTech,
    contract_Rank=experienced,
    contract_Type=local,
    contract_Size=small,
    from_Location=[smo_13, smo_18, smo_22, smo_10],
    deliveries=[(2, waste, covalex_C05),
                (2, scrap, covalex_C05),
                (2, waste, covalex_C05),
                (2, scrap, covalex_C05)
    ],
    max_Container=4,
    contract_Pay=139000)

mic_Contract_96 = Contract(
    contract_Origin=microTech,
    contract_Rank=experienced,
    contract_Type=local,
    contract_Size=small,
    from_Location=covalex_C05,
    deliveries=[(5, press, smo_18),
                (7, press, smo_22),
                (5, food, smo_10), 
                (3, food, smo_13)
    ],
    max_Container=4,
    contract_Pay=150500)

mic_Contract_97 = Contract(
    contract_Origin=microTech,
    contract_Rank=experienced,
    contract_Type=local,
    contract_Size=small,
    from_Location=covalex_C05,
    deliveries=[(3, hydro_Fuel, smo_10),
                (4, hydro_Fuel, smo_13),
                (6, quantum, smo_18),
                (6, quantum, smo_22)
    ],
    max_Container=4,
    contract_Pay=163750)

mic_Contract_98 = Contract(
    contract_Origin=microTech,
    contract_Rank=experienced,
    contract_Type=local,
    contract_Size=small,
    from_Location=covalex_C05,
    deliveries=[(3, stim, smo_13),
                (2, stim, smo_10),
                (3, stim, smo_22),
                (2, stim, smo_18)
    ],
    max_Container=4,
    contract_Pay=139000)

mic_Contract_99 = Contract(
    contract_Origin=microTech,
    contract_Rank=experienced,
    contract_Type=planetary,
    contract_Size=small,
    from_Location=[shubin_SMCa8,rayari_Anvik,rayari_Kaltag,shubin_SMCa6],
    deliveries=[(3, waste, port_Tressler),
                (3,scrap, port_Tressler),
                (2, waste, port_Tressler),
                (3, scrap, port_Tressler)
    ],
    max_Container=4,
    contract_Pay=163750)

mic_Contract_100 = Contract(
    contract_Origin=microTech,
    contract_Rank=experienced,
    contract_Type=planetary,
    contract_Size=small,
    from_Location=port_Tressler,
    deliveries=[(6, press, microTech_D01),
                (3, press, sakura_Gold),
                (7, food, microTech_D13),
                (7, food, greycat_IV)
    ],
    max_Container=4,
    contract_Pay=123500)

mic_Contract_101 = Contract(
    contract_Origin=microTech,
    contract_Rank=experienced,
    contract_Type=planetary,
    contract_Size=small,
    from_Location=port_Tressler,
    deliveries=[(4, press, shubin_SMCa8),
                (6, press, rayari_Kaltag),
                (7, food, shubin_SMCa6),
                (6, food, rayari_Anvik)
    ],
    max_Container=4,
    contract_Pay=123500)

mic_Contract_102 = Contract(
    contract_Origin=microTech,
    contract_Rank=experienced,
    contract_Type=solar,
    contract_Size=small,
    from_Location=port_Tressler,
    deliveries=[(2, stim, mic_L1),
                (2, stim, mic_L3),
                (2, stim, mic_L2),
                (2, stim, mic_L5)
    ],
    max_Container=4,
    contract_Pay=93750)

mic_Contract_103 = Contract(
    contract_Origin=microTech,
    contract_Rank=experienced,
    contract_Type=solar,
    contract_Size=small,
    from_Location=port_Tressler,
    deliveries=[(5, press, mic_L2),
                (6, press, mic_L4),
                (6, food, mic_L1),
                (7, food, mic_L2)
    ],
    max_Container=4,
    contract_Pay=121000)

mic_Contract_104 = Contract(
    contract_Origin=microTech,
    contract_Rank=experienced,
    contract_Type=solar,
    contract_Size=small,
    from_Location=[mic_L1, mic_L2, mic_L4, mic_L5],
    deliveries=[(3, waste, port_Tressler),
                (3, scrap, port_Tressler),
                (3, waste, port_Tressler),
                (3, scrap, port_Tressler)
    ],
    max_Container=4,
    contract_Pay=93750)

mic_Contract_105 = Contract(
    contract_Origin=microTech,
    contract_Rank=experienced,
    contract_Type=solar,
    contract_Size=small,
    from_Location=port_Tressler,
    deliveries=[(4, press, mic_L3),
                (3, press, mic_L4),
                (6, food, mic_L1),
                (4, food, mic_L2)
    ],
    max_Container=4,
    contract_Pay=135250)


# Experienced Medium Contracts
mic_Contract_106 = Contract(
    contract_Origin=microTech,
    contract_Rank=experienced,
    contract_Type=direct+interstellar,
    contract_Size=medium,
    from_Location=pyro_Gateway,
    deliveries=[(269, press, everus_Harbor),
    ],
    max_Container=16,
    contract_Pay=163500)

mic_Contract_107 = Contract(
    contract_Origin=microTech,
    contract_Rank=experienced,
    contract_Type=direct+planetary,
    contract_Size=medium,
    from_Location=port_Tressler,
    deliveries=[(27, press, covalex_C05),
                (303, food, covalex_C05)
    ],
    max_Container=16,
    contract_Pay=163250)

mic_Contract_108 = Contract(
    contract_Origin=microTech,
    contract_Rank=experienced,
    contract_Type=direct+planetary,
    contract_Size=medium,
    from_Location=port_Tressler,
    deliveries=[(127, quantum, microTech_D01),
                (81, hydro_Fuel, microTech_D01),
                (101, ammo, microTech_D01)
    ],
    max_Container=16,
    contract_Pay=163250)

mic_Contract_109 = Contract(
    contract_Origin=microTech,
    contract_Rank=experienced,
    contract_Type=planetary,
    contract_Size=medium,
    from_Location=port_Tressler,
    deliveries=[(69, hydro_Fuel, greycat_IV),
                (50, hydrogen, microTech_D13),
                (96, quantum, microTech_D13),
                (95, ammo, greycat_IV)
    ],
    max_Container=16,
    contract_Pay=207000)

mic_Contract_110 = Contract(
    contract_Origin=microTech,
    contract_Rank=experienced,
    contract_Type=direct+planetary,
    contract_Size=medium,
    from_Location=new_Babbage,
    deliveries=[(83, quantum, port_Tressler),
                (127, hydro_Fuel, port_Tressler),
                (91, ammo, port_Tressler)
    ],
    max_Container=16,
    contract_Pay=160500)

mic_Contract_111 = Contract(
    contract_Origin=microTech,
    contract_Rank=experienced,
    contract_Type=direct+planetary,
    contract_Size=medium,
    from_Location=port_Tressler,
    deliveries=[(423, food, new_Babbage),
    ],
    max_Container=16,
    contract_Pay=163250)

mic_Contract_112 = Contract(
    contract_Origin=microTech,
    contract_Rank=experienced,
    contract_Type=planetary,
    contract_Size=medium,
    from_Location=[greycat_IV, covalex_C05,greycat_IV, covalex_C05],
    deliveries=[(27, waste, port_Tressler),
                (25, waste, port_Tressler),
                (26, scrap, port_Tressler), 
                (21, scrap, port_Tressler)
    ],
    max_Container=16,
    contract_Pay=84000)

mic_Contract_113 = Contract(
    contract_Origin=microTech,
    contract_Rank=experienced,
    contract_Type=direct+planetary,
    contract_Size=medium,
    from_Location=port_Tressler,
    deliveries=[(314, hydrogen, new_Babbage),
    ],
    max_Container=16,
    contract_Pay=163250)

mic_Contract_114 = Contract(
    contract_Origin=microTech,
    contract_Rank=experienced,
    contract_Type=direct+planetary,
    contract_Size=medium,
    from_Location=new_Babbage,
    deliveries=[(268, press, port_Tressler),
    ],
    max_Container=16,
    contract_Pay=160500)

mic_Contract_115 = Contract(
    contract_Origin=microTech,
    contract_Rank=experienced,
    contract_Type=direct+solar,
    contract_Size=medium,
    from_Location=port_Tressler,
    deliveries=[(291, press, everus_Harbor),
    ],
    max_Container=16,
    contract_Pay=165250)

mic_Contract_116 = Contract(
    contract_Origin=microTech,
    contract_Rank=experienced,
    contract_Type=direct+solar,
    contract_Size=medium,
    from_Location=baijini_Point,
    deliveries=[(265, press, everus_Harbor),
    ],
    max_Container=16,
    contract_Pay=162250)

mic_Contract_117 = Contract(
    contract_Origin=microTech,
    contract_Rank=experienced,
    contract_Type=direct+solar,
    contract_Size=medium,
    from_Location=port_Tressler,
    deliveries=[(131, quantum, mic_L2),
                (90, hydro_Fuel, mic_L2),
                (113, ammo, mic_L2)
    ],
    max_Container=16,
    contract_Pay=166500)

mic_Contract_118 = Contract(
    contract_Origin=microTech,
    contract_Rank=experienced,
    contract_Type=solar,
    contract_Size=medium,
    from_Location=port_Tressler,
    deliveries=[(49, hydro_Fuel, mic_L1),
                (54, hydro_Fuel, mic_L2),
                (92, quantum, mic_L2),
                (142, ammo, mic_L1)
    ],
    max_Container=16,
    contract_Pay=202250)

# Experienced Large Contracts
mic_Contract_119 = Contract(
    contract_Origin=microTech,
    contract_Rank=experienced,
    contract_Type=direct+interstellar,
    contract_Size=large,
    from_Location=terra_Gateway,
    deliveries=[(1597, food, everus_Harbor),
    ],
    max_Container=32,
    contract_Pay=247250)

mic_Contract_120 = Contract(
    contract_Origin=microTech,
    contract_Rank=experienced,
    contract_Type=direct+interstellar,
    contract_Size=large,
    from_Location=terra_Gateway,
    deliveries=[(558, carbon, magnus_Gateway),
    ],
    max_Container=32,
    contract_Pay=138250)

mic_Contract_121 = Contract(
    contract_Origin=microTech,
    contract_Rank=experienced,
    contract_Type=direct+interstellar,
    contract_Size=large,
    from_Location=everus_Harbor,
    deliveries=[(518, waste, pyro_Gateway),
    ],
    max_Container=32,
    contract_Pay=128000)

mic_Contract_122 = Contract(
    contract_Origin=microTech,
    contract_Rank=experienced,
    contract_Type=direct+interstellar,
    contract_Size=large,
    from_Location=everus_Harbor,
    deliveries=[(1975, food, pyro_Gateway),
    ],
    max_Container=32,
    contract_Pay=267000)

mic_Contract_123 = Contract(
    contract_Origin=microTech,
    contract_Rank=experienced,
    contract_Type=direct+interstellar,
    contract_Size=large,
    from_Location=pyro_Gateway,
    deliveries=[(1408, press, magnus_Gateway),
    ],
    max_Container=32,
    contract_Pay=267250)

mic_Contract_124 = Contract(
    contract_Origin=microTech,
    contract_Rank=experienced,
    contract_Type=direct+interstellar,
    contract_Size=large,
    from_Location=terra_Gateway,
    deliveries=[(2372, hydrogen, everus_Harbor),
    ],
    max_Container=32,
    contract_Pay=247250)

mic_Contract_125 = Contract(
    contract_Origin=microTech,
    contract_Rank=experienced,
    contract_Type=direct+interstellar,
    contract_Size=large,
    from_Location=everus_Harbor,
    deliveries=[(3403, hydrogen, magnus_Gateway),
    ],
    max_Container=32,
    contract_Pay=698750)

mic_Contract_126 = Contract(
    contract_Origin=microTech,
    contract_Rank=experienced,
    contract_Type=direct+interstellar,
    contract_Size=large,
    from_Location=magnus_Gateway,
    deliveries=[(622, waste, pyro_Gateway),
    ],
    max_Container=32,
    contract_Pay=141500)

mic_Contract_127 = Contract(
    contract_Origin=microTech,
    contract_Rank=experienced,
    contract_Type=direct+interstellar,
    contract_Size=large,
    from_Location=magnus_Gateway,
    deliveries=[(639, silicon, pyro_Gateway),
    ],
    max_Container=32,
    contract_Pay=154250)

mic_Contract_128 = Contract(
    contract_Origin=microTech,
    contract_Rank=experienced,
    contract_Type=direct+interstellar,
    contract_Size=large,
    from_Location=terra_Gateway,
    deliveries=[(3380, food, magnus_Gateway),
    ],
    max_Container=32,
    contract_Pay=698750)

mic_Contract_129 = Contract(
    contract_Origin=microTech,
    contract_Rank=experienced,
    contract_Type=solar,
    contract_Size=large,
    from_Location=everus_Harbor,
    deliveries=[(947, hydrogen, port_Tressler),
                (1244, hydrogen, baijini_Point)
    ],
    max_Container=32,
    contract_Pay=263750)

mic_Contract_130 = Contract(
    contract_Origin=microTech,
    contract_Rank=experienced,
    contract_Type=direct+solar,
    contract_Size=large,
    from_Location=everus_Harbor,
    deliveries=[(1902, food, seraphim_Station),
    ],
    max_Container=32,
    contract_Pay=245500)

mic_Contract_131 = Contract(
    contract_Origin=microTech,
    contract_Rank=experienced,
    contract_Type=direct+solar,
    contract_Size=large,
    from_Location=baijini_Point,
    deliveries=[(1878, food, everus_Harbor),
    ],
    max_Container=32,
    contract_Pay=248250)

mic_Contract_132 = Contract(
    contract_Origin=microTech,
    contract_Rank=experienced,
    contract_Type=direct+solar,
    contract_Size=large,
    from_Location=baijini_Point,
    deliveries=[(528, waste, everus_Harbor),
    ],
    max_Container=32,
    contract_Pay=127250)

mic_Contract_133 = Contract(
    contract_Origin=microTech,
    contract_Rank=experienced,
    contract_Type=direct+solar,
    contract_Size=large,
    from_Location=seraphim_Station,
    deliveries=[(2713, hydrogen, baijini_Point),
    ],
    max_Container=32,
    contract_Pay=247750)

mic_Contract_134 = Contract(
    contract_Origin=microTech,
    contract_Rank=experienced,
    contract_Type=solar,
    contract_Size=large,
    from_Location=[seraphim_Station, baijini_Point],
    deliveries=[(274, waste, everus_Harbor),
                (238, waste, everus_Harbor)
    ],
    max_Container=32,
    contract_Pay=136500)

# Automatically collect all mic_Contract_* variables into a list
microTech_contracts = [
    value for name, value in globals().items()
    if name.startswith("mic_Contract_")
]
