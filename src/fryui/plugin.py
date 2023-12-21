from .color import dump
from fryhcs.css.color import radix_colors as radix

radix_colored_regular = set(['tomato', 'red', 'ruby', 'crimson', 'pink', 'plum', 'purple', 'violet', 'iris', 'indigo', 'blue', 'cyan', 'teal', 'jade', 'green', 'grass', 'brown', 'orange' ])
radix_colored_bright = set(['sky', 'mint', 'lime', 'yellow', 'amber'])
radix_colored_metal = set(['gold', 'bronze'])

radix_colored_colors = radix_colored_regular.union(radix_colored_bright, radix_colored_metal)

radix_base_pure = set(['gray'])
radix_base_desaturated = set(['mauve', 'slate', 'sage', 'olive', 'sand'])

radix_base_colors = radix_base_pure.union(radix_base_desaturated)

radix_colors = radix_colored_colors.union(radix_base_colors)

def get_base_color(primary):
    if primary in ('tomato', 'red', 'ruby', 'crimson', 'pink', 'plum', 'purple', 'violet',):
        return 'mauve'
    elif primary in ('iris', 'indigo', 'blue', 'sky', 'cyan',):
        return 'slate'
    elif primary in ('teal', 'jade', 'mint', 'green',):
        return 'sage'
    elif primary in ('grass', 'lime',):
        return 'olive'
    elif primary in ('yellow', 'amber', 'orange', 'brown', 'gold', 'bronze',):
        return 'sand'
    else:
        return 'gray'

def get_content_color(color):
    content_colors = {
        'sky': radix['slate-12'],
        'mint': radix['sage-12'],
        'lime': radix['olive-12'],
        'yellow': radix['sand-12'],
        'amber': radix['sand-12'],
    }
    if color in content_colors:
        return content_colors[color]
    if color in radix_colored_colors:
        return 'white'
    raise RuntimeError("Only support colored color step 9 content")


theme = {
    'primary':   'blue',
    'secondary': 'green',
    'accent':    'grass',
    'info':      'sky',
    'success':   'jade',
    'warning':   'yellow',
    'error':     'tomato',
}

def base_css(theme=theme):
    base, colored = check_theme(theme)
    common_style = {}
    light_style = {
        'color-scheme': 'light',
        '--base':         dump(radix[f'{base}-1']),
        '--base-content': dump(radix[f'{base}-12']),
    }
    dark_style = {
        'color-scheme': 'dark',
        '--base':         dump(radix[f'{base}-dark-1']),
        '--base-content': dump(radix[f'{base}-dark-12']),
    }
    for name, value in colored.items():
        common_style[f'--{name}'] = dump(radix[f'{value}-9'])
        common_style[f'--{name}-content'] = dump(get_content_color(value))
    allcolors = {'base':base, **colored}
    for name, value in allcolors.items():
        for i in range(1, 13):
            light_style[f'--{name}-{i}'] = dump(radix[f'{value}-{i}'])
            light_style[f'--{name}-a{i}'] = dump(radix[f'{value}-a{i}'])
            dark_style[f'--{name}-{i}'] = dump(radix[f'{value}-dark-{i}'])
            dark_style[f'--{name}-a{i}'] = dump(radix[f'{value}-dark-a{i}'])
    return {
        ':root': common_style,
        ':root, [data-scheme="light"]': light_style,
        '[data-scheme="dark"]': dark_style,
    }


def check_theme(theme):
    curr = dict(theme)
    if not all(n in semantic_names for n in curr.keys()):
        raise RuntimeError("theme should only have one of the 8 semantic names")
    base = curr.pop('base', None)
    if 'primary' not in curr:
        raise RuntimeError("'primary' should be in theme")
    if not all(v in radix_colored_colors for v in curr.values()):
        raise RuntimeError("all semantic colors other than 'base' should be one of radix non-gray colors")
    if not base:
        base = get_base_color(curr['primary'])
    elif base not in radix_base_colors:
        raise RuntimeError("'base' color should be one of radix gray colors")
    return base, curr

semantic_names = set(['primary', 'secondary', 'accent', 'base', 'info', 'success', 'warning', 'error'])

def colors():
    suffixes = ['', '-content'] + [f'-{i}' for i in range(1, 13)] + [f'-a{i}' for i in range(1, 13)]
    return {f'{name}{suffix}': f'rgb(var(--{name}{suffix}))'
            for suffix in suffixes
            for name  in semantic_names}
