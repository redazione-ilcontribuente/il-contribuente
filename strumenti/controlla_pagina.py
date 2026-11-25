#!/usr/bin/env python3
"""Controllo della prima pagina PRIMA di ogni push (Mario, 25/11/2026).

Uso: python3 strumenti/controlla_pagina.py [file.html ...]   (default: index.html)
Esce con codice 1 se la pagina è rotta: in quel caso NON pubblicare.

Controlla:
1. tag HTML bilanciati (nessun </div> in più o in meno);
2. ogni div.section con id sta dentro .main-col (altrimenti Primo piano e
   Confronto si sovrappongono, come il 25/11/2026);
3. una sola nota «Edizione … Orari italiani; eventi soggetti a cambiamenti.»
   (quella del giorno precedente va sostituita, non lasciata).
"""
import re
import sys
from html.parser import HTMLParser

VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link',
        'meta', 'source', 'track', 'wbr', 'param'}


class Check(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.errors, self.outside = [], [], []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = (a.get('class') or '').split()
        if tag == 'div' and 'section' in cls and a.get('id'):
            if not any('main-col' in (c or '').split() for _, c, _ in self.stack):
                self.outside.append((a['id'], self.getpos()[0]))
        if tag not in VOID:
            self.stack.append((tag, a.get('class'), self.getpos()[0]))

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        line = self.getpos()[0]
        if not self.stack or self.stack[-1][0] != tag:
            aperto = self.stack[-1] if self.stack else None
            self.errors.append(f'riga {line}: </{tag}> ma era aperto {aperto[0] + " (riga " + str(aperto[2]) + ")" if aperto else "niente"}')
            for i in range(len(self.stack) - 1, -1, -1):
                if self.stack[i][0] == tag:
                    del self.stack[i:]
                    break
        else:
            self.stack.pop()


def controlla(path):
    s = open(path, encoding='utf-8').read()
    p = Check()
    p.feed(s)
    p.close()
    errs = list(p.errors)
    errs += [f'tag non chiuso: <{t}> riga {l}' for t, _, l in p.stack]
    errs += [f'sezione #{i} (riga {l}) fuori da .main-col' for i, l in p.outside]
    note = re.findall(r'Edizione [^<]{0,60}?Orari italiani; eventi soggetti a cambiamenti', s)
    if path.endswith('index.html') and len(note) > 1:
        errs.append(f'{len(note)} note «Edizione … Orari italiani»: deve essercene una sola -> ' + ' | '.join(note))
    return errs


def main():
    files = sys.argv[1:] or ['index.html']
    ko = False
    for f in files:
        errs = controlla(f)
        if errs:
            ko = True
            print(f'ROTTA {f}:')
            for e in errs[:20]:
                print('  -', e)
        else:
            print(f'OK {f}')
    sys.exit(1 if ko else 0)


if __name__ == '__main__':
    main()
