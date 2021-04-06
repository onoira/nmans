from portmanteaur import default_headers, default_user_agent
from nmans import __author_email__, __name__, __version__

HEADERS = {
    **default_headers,
    'User-Agent': f'{default_user_agent} {__name__}/{__version__} ',
    'From': __author_email__
}
