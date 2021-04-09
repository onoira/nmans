from nmans.config.const import GENERA
from nmans.config.models import RangeDict, Genera, Qualities, Config

default_genera = Genera(
    aer=dict((k, '') for k in GENERA['aer'].keys()),
    aqua=dict((k, '') for k in GENERA['aqua'].keys()),
    terra=dict((k, '') for k in GENERA['terra'].keys()),
)

default_qualities = Qualities.empty()

default_spectra = RangeDict({
    range(0, 2): {
        'o': "",
        'b': "",
        'a': "",
        'f': "",
        'g': "",
        'k': "",
        'm': "",
        'l': "",
        't': "",
        'y': "",
        'e': ""
    },
    range(2, 4): {
        'o': "",
        'b': "",
        'a': "",
        'f': "",
        'g': "",
        'k': "",
        'm': "",
        'l': "",
        't': "",
        'y': "",
        'e': ""
    },
    range(4, 6): {
        'o': "",
        'b': "",
        'a': "",
        'f': "",
        'g': "",
        'k': "",
        'm': "",
        'l': "",
        't': "",
        'y': "",
        'e': ""
    },
    range(6, 8): {
        'o': "",
        'b': "",
        'a': "",
        'f': "",
        'g': "",
        'k': "",
        'm': "",
        'l': "",
        't': "",
        'y': "",
        'e': ""
    },
    range(8, 10): {
        'o': "",
        'b': "",
        'a': "",
        'f': "",
        'g': "",
        'k': "",
        'm': "",
        'l': "",
        't': "",
        'y': "",
        'e': ""
    }
})

default_tempers = {
    'unintelligent': '',
    'migratory': '',
    'hibernator': '',
    'distinctive': '',
    'active': '',
    'erratic': '',
    'bold': '',
    'sedate': '',

    # Passive:
    'ambulatory': '',
    'amenable': '',
    'calm': '',
    'docile': '',
    'farsighted': '',
    'passive': '',
    'submissive': '',
    'unconcerned': '',
    'wise': '',
    'anxious': '',
    'cautious': '',
    'defensive': '',

    # Prey:
    'fearful': '',
    'prey': '',
    'shy': '',
    'skittish': '',
    'timid': '',

    # Predator (player):
    'aggressive': '',
    'cruel': '',
    'dangerous': '',
    'hostile': '',
    'reckless': '',
    'vicious': '',
    'violent': '',

    # Predator:
    'hunting': '',
    'predator': '',
    'stalking': '',
    'unpredictable': '',
    'volatile': ''
}

default_traits = {}

default_config = Config(
    genera=default_genera,
    http_from='',
    qualities=default_qualities,
    spectra=default_spectra,
    tempers=default_tempers,
    traits=default_traits
)
