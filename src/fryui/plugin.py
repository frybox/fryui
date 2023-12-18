from .color import is_dark, content_color, focus_color, dump

def name_to_selector(name):
    def convert(theme):
        if theme == 'default':
            return 'html'
        return f'html[data-theme="{theme}"]'
    names = [convert(n.strip()) for n in name.split(',')]
    return ', '.join(names)

def value_to_style(value):
    style = {}
    primary   = value['primary']
    secondary = value['secondary']
    accent    = value['accent']
    neutral   = value['neutral']
    base100   = value['base-100']
    info      = value['info']
    success   = value['success']
    warning   = value['warning']
    error     = value['error']
    if is_dark(base100):
        style['color-scheme'] = 'dark'
    else:
        style['color-scheme'] = 'light'
    style['--p']   = dump(primary)
    style['--pc']  = dump(content_color(primary))
    style['--pf']  = dump(focus_color(primary))
    style['--s']   = dump(secondary)
    style['--sc']  = dump(content_color(secondary))
    style['--sf']  = dump(focus_color(secondary))
    style['--a']   = dump(accent)
    style['--ac']  = dump(content_color(accent))
    style['--af']  = dump(focus_color(accent))
    style['--n']   = dump(neutral)
    style['--nc']  = dump(content_color(neutral))
    style['--nf']  = dump(focus_color(neutral))
    style['--b1']  = dump(base100)
    style['--b2']  = dump(focus_color(base100))
    style['--b3']  = dump(focus_color(focus_color(base100)))
    style['--bc']  = dump(content_color(base100))
    style['--in']  = dump(info)
    style['--inc'] = dump(content_color(info))
    style['--inf'] = dump(focus_color(info))
    style['--su']  = dump(success)
    style['--suc'] = dump(content_color(success))
    style['--suf'] = dump(focus_color(success))
    style['--wa']  = dump(warning)
    style['--wac'] = dump(content_color(warning))
    style['--waf'] = dump(focus_color(warning))
    style['--er']  = dump(error)
    style['--erc'] = dump(content_color(error))
    style['--erf'] = dump(focus_color(error))
    return style

def base_css():
    base = {}
    for name, value in themes.items():
        name = name_to_selector(name)
        value = value_to_style(value)
        base[name] = value
    return base

themes = {
    'light, default': {
        'primary':   '#4a00ff',
        'secondary': '#ff00d3',
        'accent':    '#00d7c0',
        'neutral':   '#2b3440',
        'base-100':  '#ffffff',
        'info':      '#00b6ff',
        'success':   '#00a96e',
        'warning':   '#ffbe00',
        'error':     '#ff5861',
    },
    'dark': {
        'primary':   '#7480ff',
        'secondary': '#ff52d9',
        'accent':    '#00cdb8',
        'neutral':   '#2a323c',
        'base-100':  '#1d232a',
        'info':      '#00b6ff',
        'success':   '#00a96e',
        'warning':   '#ffbe00',
        'error':     '#ff5861',
    },
}

def colors():
    return {
        'primary':            'rgb(var(--p))',
        'primary-content':    'rgb(var(--pc))',
        'primary-focus':      'rgb(var(--pf))',
        'secondary':          'rgb(var(--s))',
        'secondary-content':  'rgb(var(--sc))',
        'secondary-focus':    'rgb(var(--sf))',
        'accent':             'rgb(var(--a))',
        'accent-content':     'rgb(var(--ac))',
        'accent-focus':       'rgb(var(--af))',
        'neutral':            'rgb(var(--n))',
        'neutral-content':    'rgb(var(--nc))',
        'neutral-focus':      'rgb(var(--nf))',
        'base-100':           'rgb(var(--b1))',
        'base-200':           'rgb(var(--b2))',
        'base-300':           'rgb(var(--b3))',
        'base-content':       'rgb(var(--bc))',
        'info':               'rgb(var(--in))',
        'info-content':       'rgb(var(--inc))',
        'info-focus':         'rgb(var(--inf))',
        'success':            'rgb(var(--su))',
        'success-content':    'rgb(var(--suc))',
        'success-focus':      'rgb(var(--suf))',
        'warning':            'rgb(var(--wa))',
        'warning-content':    'rgb(var(--wac))',
        'warning-focus':      'rgb(var(--waf))',
        'error':              'rgb(var(--er))',
        'error-content':      'rgb(var(--erc))',
        'error-focus':        'rgb(var(--erf))',
    }
