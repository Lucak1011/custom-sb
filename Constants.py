PORT = 6809  # 6810 for internet connection

TURN_RATE = 2  # deg / sec
TAXI_SPEED = 15  # knots
PUSH_SPEED = 5  # knots
CLIMB_RATE = 2500  # ft / min
DESCENT_RATE = -2000  # ft / min
HIGH_DESCENT_RATE = -3000  # ft / min

RADAR_UPDATE_RATE = 5  # per second

CCAMS_SQUAWKS = list(range(1410, 1478)) + list(range(2001, 2078)) + list(range(2201, 2278)) + list(range(2701, 2738))  # realistically way way more

# ACTIVE_AERODROMES = ["EGLL"]
# ACTIVE_RUNWAYS = {"EGLL": "09L"}
# ACTIVE_CONTROLLERS = ["EGLL_N_APP", "EGLL_S_APP", "EGLL_F_APP"]
# MASTER_CONTROLLER = "LON_D_CTR"
# MASTER_CONTROLLER_FREQ = "34905"

# ACTIVE_AERODROMES = ["EGPF"]
# ACTIVE_RUNWAYS = {"EGPF": "05"}
# ACTIVE_CONTROLLERS = ["EGPF_APP"]
# MASTER_CONTROLLER = "SCO_D_CTR"
# MASTER_CONTROLLER_FREQ = "35855"

# ACTIVE_AERODROME = "EGAA"
# ACTIVE_RUNWAY = "25"
# ACTIVE_CONTROLLERS = ["EGAA_APP", "EGAA_F_APP"]
# MASTER_CONTROLLER = "STC_A_CTR"
# MASTER_CONTROLLER_FREQ = "23775"

# ACTIVE_AERODROME = "EGKK"
# ACTIVE_RUNWAY = "26L"
# ACTIVE_CONTROLLERS = ["EGKK_APP", "EGKK_F_APP"]
# MASTER_CONTROLLER = "LON_D_CTR"
# MASTER_CONTROLLER_FREQ = "34905"

# ACTIVE_AERODROMES = ["EGNM"]
# ACTIVE_RUNWAYS = {"EGNM": "14"}
# ACTIVE_CONTROLLERS = ["EGNM_APP", "EGNM_F_APP"]
# MASTER_CONTROLLER = "MAN_NE_CTR"
# MASTER_CONTROLLER_FREQ = "35715"

# ACTIVE_AERODROME = "EGHI"
# ACTIVE_RUNWAY = "20"
# ACTIVE_CONTROLLERS = ["SOLENT_APP"]
# MASTER_CONTROLLER = "LTC_SW_CTR"
# MASTER_CONTROLLER_FREQ = "33180"

# ACTIVE_AERODROMES = ["EGJJ", "EGJB", "EGJA"]
# ACTIVE_RUNWAYS = {"EGJJ": "08", "EGJB": "09", "EGJA": "08"}
# ACTIVE_CONTROLLERS = ["EGJJ_C_APP", "EGJJ_S_APP"]
# MASTER_CONTROLLER = "LTC_SW_CTR"
# MASTER_CONTROLLER_FREQ = "33180"

# ACTIVE_AERODROMES = ["EGPH", "EGPF", "EGPK"]
# ACTIVE_RUNWAYS = {"EGPH": "06", "EGPF": "05", "EGPK": "12"}
# ACTIVE_CONTROLLERS = ["STC_E_CTR", "STC_W_CTR", "EGPH_APP", "EGPF_APP", "EGPK_APP"]  # 
# MASTER_CONTROLLER = "SCO_D_CTR"
# MASTER_CONTROLLER_FREQ = "35855"

# ACTIVE_AERODROMES = ["EGPH", "EGPF", "EGPK", "EGPD", "EGPE"]
# ACTIVE_RUNWAYS = {"EGPH": "06", "EGPF": "05", "EGPK": "12", "EGPD": "34", "EGPE": "05"}
# ACTIVE_CONTROLLERS = ["SCO_E_CTR", "STC_CTR"]
# MASTER_CONTROLLER = "SCO_D_CTR"
# MASTER_CONTROLLER_FREQ = "35855"

# ACTIVE_AERODROMES = ["EGKK", "EGLL", "EGSS", "EGGW"]
# ACTIVE_RUNWAYS = {"EGKK": "26L", "EGLL": "27R", "EGSS": "22", "EGGW": "07"}
# ACTIVE_CONTROLLERS = ["LTC_SW_CTR", "LTC_CTR", "LTC_S_CTR", "EGSS_APP", "EGGW_APP", "LTC_N_CTR", "LTC_SE_CTR", "EGKK_F_APP", "EGLL_S_APP", "EGLL_F_APP", "EGLL_N_APP", "EGKK_APP", "ESSEX_APP"]  # 
# MASTER_CONTROLLER = "LON_S_CTR"
# MASTER_CONTROLLER_FREQ = "29430"

# ACTIVE_AERODROMES = ["EGNX"]
# ACTIVE_RUNWAYS = {"EGNX": "09"}
# ACTIVE_CONTROLLERS = ["EGNX_APP", "EGNX_F_APP"]
# MASTER_CONTROLLER = "LON_M_CTR"
# MASTER_CONTROLLER_FREQ = "20025"

# ACTIVE_AERODROMES = ["EGLC", "EGMC"]
# ACTIVE_RUNWAYS = {"EGLC": "09", "EGMC": "05"}
# ACTIVE_CONTROLLERS = ["THAMES_APP", "EGMC_APP"]
# MASTER_CONTROLLER = "LON_E_CTR"
# MASTER_CONTROLLER_FREQ = "18480"

# ACTIVE_AERODROMES = ["EGNX", "EGBB"]
# ACTIVE_RUNWAYS = {"EGNX": "09", "EGBB": "33"}
# ACTIVE_CONTROLLERS = ["LTC_M_CTR", "EGNX_APP", "EGBB_APP"]
# MASTER_CONTROLLER = "LON_M_CTR"
# MASTER_CONTROLLER_FREQ = "20025"

ACTIVE_AERODROMES = ["EGFF"]
ACTIVE_RUNWAYS = {"EGFF": "12", "EGGD": "09"}
ACTIVE_CONTROLLERS = ["LON_W_CTR", "LON_WB_CTR", "EGFF_APP", "EGGD_APP"]
MASTER_CONTROLLER = "LON_M_CTR"
MASTER_CONTROLLER_FREQ = "20025"


INACTIVE_SECTORS = [
    "LTC_E_CTR",
    # "LTC_M_CTR",
    "LTC_NE_CTR",
    "LTC_NW_CTR",
    "LTC_SE_CTR",
    "LTC_SW_CTR",
    # "LON_W_CTR"
]

# OTHER_CONTROLLERS = []
OTHER_CONTROLLERS = [
    # ("EGPH_APP", "21205"),
    # ("EGPF_APP", "19100"),
    # ("EGPK_APP", "29450"),
    # ("EGPD_APP", "19055"),
    # ("EGPE_APP", "22605"),
    # ("EGPB_APP", "31300"),
    # ("EGKK_APP", "26825"),
    # ("EGLL_N_APP", "19730"),
    # ("ESSEX_APP", "20625"),

    ("BIRD_S1_CTR", "19700"),
    ("EURN_FSS", "33450"),
    ("EKDK_CTR", "36485"),
    ("EHAA_W_CTR", "25750"),
    ("EISN_CTR", "34260"),

    # ("LON_W_CTR", "26080"),
    ("LON_E_CTR", "18480"),
    ("LON_M_CTR", "20025"),
    ("LON_D_CTR", "34905"),
    ("LON_NW_CTR", "35580"),
    ("LON_NE_CTR", "28130"),
    ("LON_S_CTR", "29430"),

    # ("LTC_E_CTR", "21230"),
# #    ("LTC_M_CTR", "21030"),
    # ("LTC_NE_CTR", "18825"),
    # ("LTC_NW_CTR", "21280"),
    # ("LTC_SE_CTR", "20530"),
    # ("LTC_SW_CTR", "33180"),

    ("MAN_NE_CTR", "35715"),
# #    ("MAN_SE_CTR", "34430"),
#     ("MAN_W_CTR", "28055"),

    ("SCO_D_CTR", "35855"),
    # ("SCO_N_CTR", "29225"),
    ("SCO_R_CTR", "29100"),
    # ("SCO_S_CTR", "34755"),
    ("SCO_W_CTR", "32730"),

    ("STC_A_CTR", "23775"),
    # ("STC_W_CTR", "24825"),
    # ("STC_E_CTR", "30975")
]
# ACTIVE_CONTROLLER = "LON_S_CTR"
# MASTER_CONTROLLER = "EGLL_N_APP"
# MASTER_CONTROLLER_FREQ = "19730"


# DISABLE FEATURES
AUTO_ASSUME = False  # ALL COMMENTED OUT WILL NOT WORK AT ALL


TRANSITION_LEVEL = 7000

KILL_ALL_ON_HANDOFF = True
