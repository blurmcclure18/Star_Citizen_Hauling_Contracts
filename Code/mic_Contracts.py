
from myLocations import *
from myDefinitions import *

# Rookie Contracts
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

# Automatically collect all mic_Contract_* variables into a list
microTech_contracts = [
    value for name, value in globals().items()
    if name.startswith("mic_Contract_")
]
