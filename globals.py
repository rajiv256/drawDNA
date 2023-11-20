PUNCT = {
    'SPACE': ' ',
    'LEFTB': '(',
    'RIGHTB': ')',
    'PLUS': '+',
    'ASTERIX': '*', }

FONT_KWARGS = {
    'font': ('Courier', 15, 'bold'),
    'align': 'center',
    'move': False}

WHEREAMI = {
    'BOTTOM': 1,
    'TOP': -1}

WHICHWAY = {
    'LEFT2RIGHT': 1,
    'RIGHT2LEFT': -1

}
DOMAIN_PATTERN = "[a-zA-Z0-9\(+\*_]+|\)"  # TODO: Check if the pattern works