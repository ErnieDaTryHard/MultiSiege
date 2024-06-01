import enum
import os

GLOBAL_SETTINGS = './global_settings.json'
SENTRY_LOCATION = os.path.abspath('./sentries')

SIEGE_APP_ID = 359550

DEPOT_DOWNLOADER = os.path.abspath(os.path.join(os.getcwd(), "assets", "DepotDownloader", "DepotDownloader.exe"))
Y1SX_Y6S4_CRACKS = os.path.abspath(os.path.join(os.getcwd(), "assets", "cracks", "Y1SX_Y6S2"))
Y6S3_CRACK = os.path.abspath(os.path.join(os.getcwd(), "assets", "cracks", "Y6S3"))
Y6S4_Y8SX_CRACKS = os.path.abspath(os.path.join(os.getcwd(), "assets", "cracks", "Y6S4_Y8SX"))

SCIPTFILE="""
Set oWS = WScript.CreateObject("WScript.Shell") 
sLinkFile = "{name}"
Set oLink = oWS.CreateShortcut(sLinkFile)
oLink.TargetPath = "{targetpath}"
oLink.Save
"""

class MyEnumMeta(enum.EnumMeta): 
    def __contains__(cls, item): 
        try:
            cls(item)
        except ValueError:
            return False
        else:
            return True

class SiegeVersions(enum.Enum, metaclass=MyEnumMeta):
    """
    Enum for all of the siege versions available to be downloaded.
    """
    VANILLA = "Y1S0"
    BLACK_ICE = "Y1S1"
    DUST_LINE = "Y1S2"
    SKULL_RAIN = "Y1S3"
    RED_CROW = "Y1S4"
    VELVET_SHELL = "Y2S1"
    HEALTH = "Y2S2"
    BLOOD_ORCHID = "Y2S3"
    WHITE_NOISE = "Y2S4"
    CHIMERA = "Y3S1"
    PARABELLUM = "Y3S2"
    GRIM_SKY = "Y3S3"
    WIND_BASTION = "Y3S4"
    BURNT_HORIZON = "Y4S1"
    PHANTOM_SIGHT = "Y4S2"
    EMBER_RISE = "Y4S3"
    SHIFTING_TIDES = "Y4S4"
    VOID_EDGE = "Y5S1"
    STEEL_WAVE = "Y5S2"
    SHADOW_LEGACY = "Y5S3"
    NEON_DAWN = "Y5S4"
    CRIMSON_HEIST = "Y6S1"
    NORTH_STAR = "Y6S2"
    CRYSTAL_GUARD = "Y6S3"
    HIGH_CALIBRE = "Y6S4"
    DEMON_VEIL = "Y7S1"
    VECTOR_GLARE = "Y7S2"
    BRUTAL_SWARM = "Y7S3"
    SOLAR_RAID = "Y7S4"
    COMMANDING_FORCE = "Y8S1"
    DREAD_FACTOR = "Y8S2"
    HEAVY_METTLE = "Y8S3"
    DEEP_FREEZE = "Y8S4"
    DEADLY_OMEN = "Y9S1"

class SiegeDepots(enum.IntEnum):
    """
    Lists of siege depots we need to download content from Steam.
    
    SKU_RUS is used for the localisation of ex - Soviet countries.
    """
    CONTENT = 359551
    SKU_RUS = 377238
    SKU_WW = 377237

class SiegeManifests_CONTENT(enum.IntEnum):
    """
    Manifests IDs for the `CONTENT` depot.
    """
    VANILLA = 3893422760579204530
    BLACK_ICE = 3893422760579204530
    DUST_LINE = 2206497318678061176
    SKULL_RAIN = 5851804596427790505
    RED_CROW = 8569920171217002292
    VELVET_SHELL = 8006071763917433748
    HEALTH = 708773000306432190
    BLOOD_ORCHID = 1613631671988840841
    WHITE_NOISE = 4221297486420648079
    CHIMERA = 4701787239566783972
    PARABELLUM = 8765715607275074515
    GRIM_SKY = 7781202564071310413
    WIND_BASTION = 7659555540733025386
    BURNT_HORIZON = 5935578581006804383
    PHANTOM_SIGHT = 5408324128694463720
    EMBER_RISE = 7869081741739849703
    SHIFTING_TIDES = 1842268638395240106
    VOID_EDGE = 6296533808765702678
    STEEL_WAVE = 893971391196952070
    SHADOW_LEGACY = 3089981610366186823
    NEON_DAWN = 3711873929777458413
    CRIMSON_HEIST = 7485515457663576274
    NORTH_STAR = 6304700868033912207
    CRYSTAL_GUARD = 6526531850721822265
    HIGH_CALIBRE = 8627214406801860013
    DEMON_VEIL = 2178080523228113690
    VECTOR_GLARE = 133280937611742404
    BRUTAL_SWARM = 5906302942203575464
    SOLAR_RAID = 1819898955518120444
    COMMANDING_FORCE = 5863062164463920572
    DREAD_FACTOR = 1575870740329742681
    HEAVY_METTLE = 3005637025719884427
    DEEP_FREEZE = 4957295777170965935
    DEADLY_OMEN = 1140469899661941149

class SiegeManifests_SKU_RUS(enum.IntEnum):
    """
    Manifest IDs for the `SKU_RUS` depot.
    """
    VANILLA = 6835384933146381100
    BLACK_ICE = 5362991837480196824
    DUST_LINE = 3040224537841664111
    SKULL_RAIN = 7597187834633512926
    RED_CROW = 912564683190696342
    VELVET_SHELL = 2687181326074258760
    HEALTH = 8542242518901049325
    BLOOD_ORCHID = 5927780489446635852
    WHITE_NOISE = 8175359039160965183
    CHIMERA = 4768963659370299631
    PARABELLUM = 7995779530685147208
    GRIM_SKY = 5465169470949211447
    WIND_BASTION = 5406593359909338734
    BURNT_HORIZON = 1384328559966859661
    PHANTOM_SIGHT = 3326664059403997209
    EMBER_RISE = 9016692046802024636
    SHIFTING_TIDES = 510172308722680354
    VOID_EDGE = 3070256018494753206
    STEEL_WAVE = 6938478745264725185
    SHADOW_LEGACY = 4020038723910014041
    NEON_DAWN = 3560446343418579092
    CRIMSON_HEIST = 6130917224459224462
    NORTH_STAR = 6767916709017546201
    CRYSTAL_GUARD = 5161489294178683219
    HIGH_CALIBRE = 2074678920289758165
    DEMON_VEIL = 1970003626423861715
    VECTOR_GLARE = 1363132201391540345
    BRUTAL_SWARM = 4500117484519539380
    SOLAR_RAID = 5107849703917033235
    COMMANDING_FORCE = 1252692309389076318
    DREAD_FACTOR = 4977529482832011357
    HEAVY_METTLE = 2579928666708989224
    DEEP_FREEZE = 8339919149418587132
    DEADLY_OMEN = 1619182300337183882

class SiegeManifests_SKU_WW(enum.IntEnum):
    """
    Manifest IDs for `SKU_WW` depot.
    """
    VANILLA = 8358812283631269928
    BLACK_ICE = 5188997148801516344
    DUST_LINE = 2303064029242396590
    SKULL_RAIN = 5819137024728546741
    RED_CROW = 3576607363557872807
    VELVET_SHELL = 2248734317261478192
    HEALTH = 5875987479498297665
    BLOOD_ORCHID = 6708129824495912434
    WHITE_NOISE = 8748734086032257441
    CHIMERA = 5071357104726974256
    PARABELLUM = 6507886921175556869
    GRIM_SKY = 5562094852451837435
    WIND_BASTION = 6502258854032233436
    BURNT_HORIZON = 8356277316976403078
    PHANTOM_SIGHT = 693082837425613508
    EMBER_RISE = 3546781236735558235
    SHIFTING_TIDES = 299124516841461614
    VOID_EDGE = 4736360397583523381
    STEEL_WAVE = 4367817844736324940
    SHADOW_LEGACY = 85893637567200342
    NEON_DAWN = 4713320084981112320
    CRIMSON_HEIST = 7890853311380514304
    NORTH_STAR = 2525708706057497155
    CRYSTAL_GUARD = 4859695099882698284
    HIGH_CALIBRE = 2637055726475611418
    DEMON_VEIL = 8323869632165751287
    VECTOR_GLARE = 1363132201391540345
    BRUTAL_SWARM = 6425223567680952075
    SOLAR_RAID = 4466027729495813039
    COMMANDING_FORCE = 3275824905781062648
    DREAD_FACTOR = 3558972082517836520
    HEAVY_METTLE = 2068160275622519212
    DEEP_FREEZE = 7646647065987620875
    DEADLY_OMEN = 1959067516419454682

class CrackType(enum.Enum):
    Y1SX_Y6S2 = "Y1SX_Y6S2"
    Y6S3 = "Y6S3"
    Y6S4_Y8SX = "Y6S4_Y8SX"

class SiegeVersion_CrackTypes(enum.Enum):
    VANILLA = CrackType.Y1SX_Y6S2
    BLACK_ICE = CrackType.Y1SX_Y6S2
    DUST_LINE = CrackType.Y1SX_Y6S2
    SKULL_RAIN = CrackType.Y1SX_Y6S2
    RED_CROW = CrackType.Y1SX_Y6S2
    VELVET_SHELL = CrackType.Y1SX_Y6S2
    HEALTH = CrackType.Y1SX_Y6S2
    BLOOD_ORCHID = CrackType.Y1SX_Y6S2
    WHITE_NOISE = CrackType.Y1SX_Y6S2
    CHIMERA = CrackType.Y1SX_Y6S2
    PARABELLUM = CrackType.Y1SX_Y6S2
    GRIM_SKY = CrackType.Y1SX_Y6S2
    WIND_BASTION = CrackType.Y1SX_Y6S2
    BURNT_HORIZON = CrackType.Y1SX_Y6S2
    PHANTOM_SIGHT = CrackType.Y1SX_Y6S2
    EMBER_RISE = CrackType.Y1SX_Y6S2
    SHIFTING_TIDES = CrackType.Y1SX_Y6S2
    VOID_EDGE = CrackType.Y1SX_Y6S2
    STEEL_WAVE = CrackType.Y1SX_Y6S2
    SHADOW_LEGACY = CrackType.Y1SX_Y6S2
    NEON_DAWN = CrackType.Y1SX_Y6S2
    CRIMSON_HEIST = CrackType.Y1SX_Y6S2
    NORTH_STAR = CrackType.Y1SX_Y6S2
    CRYSTAL_GUARD = CrackType.Y6S3
    HIGH_CALIBRE = CrackType.Y6S4_Y8SX
    DEMON_VEIL = CrackType.Y6S4_Y8SX
    VECTOR_GLARE = CrackType.Y6S4_Y8SX
    BRUTAL_SWARM = CrackType.Y6S4_Y8SX
    SOLAR_RAID = CrackType.Y6S4_Y8SX
    COMMANDING_FORCE = CrackType.Y6S4_Y8SX
    DREAD_FACTOR = CrackType.Y6S4_Y8SX
    HEAVY_METTLE = CrackType.Y6S4_Y8SX
    DEEP_FREEZE = CrackType.Y6S4_Y8SX
    DEADLY_OMEN = CrackType.Y6S4_Y8SX


class Status(enum.Enum):
    """
    Enum to return status codes for if the function was successful.
    """
    SUCCESS = 0
    FAIL = 1

class LogLevel(enum.Enum):
    """
    List of log levels that will be used in the program.
    """
    INFO = "INFO"
    DEBUG = "DEBUG"
    WARNING = "WARNING"
    ERROR = "ERROR"

class Mode(enum.Enum, metaclass=MyEnumMeta):
    """
    Enum for the mode the program is in (light or dark mode)
    """
    USE_SYSTEM_SETTING = "USE_SYSTEM_SETTING"
    LIGHT = "LIGHT"
    DARK = "DARK"