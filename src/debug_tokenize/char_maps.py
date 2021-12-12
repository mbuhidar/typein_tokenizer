"""
Type-in entry special character conversion and keyword token maps.
"""

# Dictionary for special character conversion from ahoy to petcat
AHOY_TO_PETCAT = {
    "{SC}": "{clr}",
    "{HM}": "{home}",
    "{CU}": "{up}",
    "{CD}": "{down}",
    "{CL}": "{left}",
    "{CR}": "{rght}",
    "{SS}": "{$a0}",
    "{IN}": "{inst}",
    "{RV}": "{rvon}",
    "{RO}": "{rvof}",
    "{BK}": "{blk}",
    "{WH}": "{wht}",
    "{RD}": "{red}",
    "{CY}": "{cyn}",
    "{PU}": "{pur}",
    "{GN}": "{grn}",
    "{BL}": "{blu}",
    "{YL}": "{yel}",
    "{OR}": "{orng}",
    "{BR}": "{brn}",
    "{LR}": "{lred}",
    "{G1}": "{gry1}",
    "{G2}": "{gry2}",
    "{LG}": "{lgrn}",
    "{LB}": "{lblu}",
    "{G3}": "{gry3}",
    "{F1}": "{f1}",
    "{F2}": "{f2}",
    "{F3}": "{f3}",
    "{F4}": "{f4}",
    "{F5}": "{f5}",
    "{F6}": "{f6}",
    "{F7}": "{f7}",
    "{F8}": "{f8}",
}

# Core Commodore BASIC tokens
CORE_TOKENS = (
    ('end',     128),
    ('for',     129),
    ('next',    130),
    ('data',    131),
    ('input#',  132),
    ('input',   133),
    ('dim',     134),
    ('read',    135),
    ('let',     136),
    ('goto',    137),
    ('run',     138),
    ('if',      139),
    ('restore', 140),
    ('gosub',   141),
    ('return',  142),
    ('rem',     143),
    ('stop',    144),
    ('on',      145),
    ('wait',    146),
    ('load',    147),
    ('save',    148),
    ('verify',  149),
    ('def',     150),
    ('poke',    151),
    ('print#',  152),
    ('print',   153),
    ('cont',    154),
    ('list',    155),
    ('clr',     156),
    ('cmd',     157),
    ('sys',     158),
    ('open',    159),
    ('close',   160),
    ('get',     161),
    ('new',     162),
    ('tab(',    163),
    ('to',      164),
    ('fn',      165),
    ('spc(',    166),
    ('then',    167),
    ('not',     168),
    ('step',    169),
    ('+',       170),
    ('-',       171),
    ('*',       172),
    ('/',       173),
    ('^',       174),
    ('and',     175),
    ('or',      176),
    ('>',       177),
    ('=',       178),
    ('<',       179),
    ('sgn',     180),
    ('int',     181),
    ('abs',     182),
    ('usr',     183),
    ('fre',     184),
    ('pos',     185),
    ('sqr',     186),
    ('rnd',     187),
    ('log',     188),
    ('exp',     189),
    ('cos',     190),
    ('sin',     191),
    ('tan',     192),
    ('atn',     193),
    ('peek',    194),
    ('len',     195),
    ('str$',    196),
    ('val',     197),
    ('asc',     198),
    ('chr$',    199),
    ('left$',   200),
    ('right$',  201),
    ('mid$',    202),
    ('go',      203),
)

TOKENS_V2 = CORE_TOKENS  # Case for Commodore BASIC v2.0 TODO: Add versions

# Tokens for special character designations used by petcat
PETCAT_TOKENS = (
    ('{clr}',  147),
    ('{home}',  19),
    ('{up}',   145),
    ('{down}',  17),
    ('{left}', 157),
    ('{rght}',  29),
    ('{$a0}',  160),
    ('{inst}', 148),
    ('{rvon}',  18),
    ('{rvof}', 146),
    ('{blk}',  144),
    ('{wht}',    5),
    ('{red}',   28),
    ('{cyn}',  159),
    ('{pur}',  156),
    ('{grn}',   30),
    ('{blu}',   31),
    ('{yel}',  158),
    ('{orng}', 129),
    ('{brn}',  149),
    ('{lred}', 150),
    ('{gry1}', 151),
    ('{gry2}', 152),
    ('{lgrn}', 153),
    ('{lblu}', 154),
    ('{gry3}', 155),
    ('{f1}',   133),
    ('{f2}',   134),
    ('{f3}',   135),
    ('{f4}',   136),
    ('{f5}',   137),
    ('{f6}',   138),
    ('{f7}',   139),
    ('{f8}',   140),
)
