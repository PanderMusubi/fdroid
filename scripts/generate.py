#!/usr/bin/env python3
'''Generate documentation on selected F-Droid apps.'''

from json import load

from pycountry import countries

skip = {'es': ('tostas', 'patatas', 'tapear', 'tapeo',
               'Machu', 'Picchu', 'Picchu.',
               'Roy', 'Roy.', 'Amanda',
               "'77",
               'todovía', 'pescadería', 'parking', 'juguetería',
               'EE.', 'UU.', 'Londres', 'Amberes', 'Utrecht', 'Róterdam', 'Ámsterdam',
               'bootcamp', 'halterofilia', 'spinning', 'surf', 'yoga',
               'bandoneón'),
        'en': ('theatre',
               'tapa',
               'Machu', 'Picchu', 'Picchu.',
               'bandoneon',
               'patatas', 'bavas', 'bravas.'),
        'nl': ('Noord-Amerikanen',
               "'77",
               'maracas',
               'patatas', 'Tapas', 'tapas', '"tapas"', 'tapas.', 'bravas', 'bravas.',
               'Machu', 'Picchu')}

def flag(lang):
    '''Get flag for language.'''
    lang = lang.upper()
    if lang == 'EN':
        lang = 'GB'
    return countries.get(alpha_2=lang).flag

def header(mado, references, headers, lang):
    for reference, value in sorted(references.items()):
        if reference != lang:
            if reference == 'en':
                mado.write(f'_{flag(reference)} {value} [README.md](README.md)_\n\n')
            else:
                mado.write(f'_{flag(reference)} {value} [README-{reference}.md](README-{reference}.md)_\n\n')
    mado.write(headers[lang])

def footer(mado, footers, lang):
    mado.write(footers[lang])

def read_json():
    '''Read the JSON file with all the data.'''
    with open('data.json') as file:  # pylint:disable=unspecified-encoding
        data = load(file)
        return data['references'], data['headers'], data['footers'], data['categories']

#periodical
#ev charging

def generate():
    '''Generate files'''

    references, headers, footers, categories = read_json()
    for lang in sorted(references):
        filename = f'README-{lang}.md'
        if lang == 'en':
            filename = 'README.md'
        with open(f'../{filename}', 'w') as mado:  # pylint:disable=unspecified-encoding
            header(mado, references, headers, lang)
            mado.write('<table>\n')
            for category in categories:
                mado.write(f'<tr><th colspan="2"><br>{category["name"][lang]}</th></tr>\n')
                for app in category['apps']:
                    mado.write(f'<tr><td><img alt="icon" width="64" src="icons/{app["id"]}.png"></td>\n')
                    mado.write(f'<td valign="top"><a target="_blank" href="https://f-droid.org/en/packages/{app["id"]}"><strong>{app["name"]}</strong></a><br>\n')
                    mado.write(f'{app["description"][lang]}</td></tr>\n')
            mado.write('</table>\n\n')
            footer(mado, footers, lang)

if __name__ == '__main__':
    generate()
