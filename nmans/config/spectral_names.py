from nmans.models import RangeDict

# Each of the five ranges is assigned one of the five invasions of Ireland.
# Names are selected arbitrarily and then ordered alphabetically and assigned
# from hottest -> coldest.
SPECTRAL_NAMES = RangeDict({
    range(0, 2): {  # fomoire
        'o': "balor",
        'b': "bres",
        'a': "cichol",
        'f': "conand",
        'g': "dedomnann",
        'k': "delbaeth",
        'm': "eithne",
        'l': "elatha",
        't': "indech",
        'y': "neit",
        'e': "ochtraillach"
    },
    range(2, 4): {  # nemedh
        'o': "ainninn",
        'b': "beoan",
        'a': "beothach",
        'f': "erglan",
        'g': "fuamnach",
        'k': "larbonel",
        'm': "lobath",
        'l': "macha",
        't': "nemed",
        'y': "semion",
        'e': "starn"
    },
    range(4, 6): {  # tuatha
        'o': "banba",
        'b': "brigit",
        'a': "dagda",
        'f': "danu",
        'g': "eriu",
        'k': "fohla",
        'm': "lugh",
        'l': "midir",
        't': "morrigan",
        'y': "nuada",
        'e': "ogma"
    },
    range(6, 8): {  # firbolg
        'o': "eochaid",
        'b': "fiacha",
        'a': "fodbgen",
        'f': "gann",
        'g': "genann",
        'k': "oengus",
        'm': "rudraige",
        'l': "sengann",
        't': "slanga",
        'y': "sreng",
        'e': "tailtiu"
    },
    range(8, 10): {  # miledh
        'o': "amairgin",
        'b': "colphta",
        'a': "dil",
        'f': "eberdonn",
        'g': "eberfinn",
        'k': "erannan",
        'm': "erech",
        'l': "eremon",
        't': "fial",
        'y': "ir",
        'e': "mil"
    }
})
