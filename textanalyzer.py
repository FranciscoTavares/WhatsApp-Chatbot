# -*- coding: utf-8 -*-
"""
Textanalyzer
Chatbot text analysis component

@author: Timon, Yunis, Ralph
"""

import random
import re
import wikipedia


sm = u'\U0001F642'  # Smiley

Begruessung = ('hi', 'hallo', 'hey', 'moin', 'moinsen', 'hello', 'servus', 'ciao', 'salut', 'jo')
Doch = ('doch')
Hae = ('hä', 'hä?', 'hää', 'häää')
Verneinung = ('nope', 'nichts', 'ne', 'nein', 'nö', 'noap', 'no', 'nicht', 'not')
Schule = ('schule')
Warum = ('warum', 'wieso')
Weil = ('weil baum', 'wegen dir', 'wieso nicht')
Kannst = ('kannst', 'könntest', 'kann' , 'konnte')
Nein = ('ne', 'nein', 'nö')
Ausdruecke = ('doof', 'scheiße', 'blöd', 'blöde', 'öde', 'öd', 'Adelheid', 'popo', 'kaka')
Jokes = ('alles was beine hat '+sm, 'ich nicht '+sm, 'du '+sm, 'ein bein '+sm, 'deine mudda mit mir ins Bett '+sm,
         'ich nicht mit dir '+sm)

HA = ('mathe', 'deutsch', 'latein', 'englisch', 'geo', 'geographie', 'erdkunde', 'physik')
#auf = ('auf', 'gemacht')
#haben = ('ham', 'haben', 'hatten', 'habt', 'hattet')
HAantwort = ('Buch S. ')
Hausaufgaben = HAantwort + str(random.randint(10,200)) + '/' + str(random.randint(1,13))

NewsTickerWitz = ('witz', 'witze', 'joke', 'jokes')
ntwitzlist = []
with open('newsticker.txt', 'r', encoding='utf-8') as ntwitz:
    for line in ntwitz.readlines():
        line = line.rstrip()  # remove trailing '\n'
        if line:
            ntwitzlist.append(line)

		 
def analyze_text(text):
    satz = text.lower()
    woerter = satz.split(' ')
    resp_title = ''  # title in bold + italics
    resp_msg = ''  # message below title (if present) only in italics
    resp = ''
    # first analyze words...
    for wort in woerter:
        wort = re.sub('[!?. #$@€]', '', wort)  # delete special characters
        if wort in Begruessung:
            resp = Begruessung[random.randint(0, len(Begruessung) -1)]
        elif wort in Doch:
            resp = 'oh'
        elif wort in Hae:
            resp = Hae[random.randint(0, len(Hae) - 1)]
        elif wort in Schule:
            resp = ('schule ist ' + (Ausdruecke[random.randint(0, len(Ausdruecke) - 1)]))
        elif wort in HA:  # TODO: specify using (HA + haben + auf)
            resp = Hausaufgaben
        #elif wort in ('was'):
        #	 resp = 'nichts'
        elif wort in Kannst:
            resp = Nein[random.randint(0, len(Nein) - 1)]
        elif wort in Warum:
            resp = Weil[random.randint(0, len(Weil) - 1)]
        elif wort in NewsTickerWitz:
            resp = ntwitzlist[random.randint(0, len(ntwitzlist) -1)]
        elif wort in Verneinung:
            resp = 'doch'
    # ...then check if whole sentence matches
    if satz in ('was get', 'was geht', 'wat geht'):
        resp = Jokes[random.randint(0, len(Jokes) - 1)]
    elif (satz.split(' '))[0] in 'wiki':
        wikipedia.set_lang('de')
        if True:  # if Internet connection available
            try:
                resp_msg = '_' + wikipedia.summary((satz.split(' '))[1], sentences=2) + '_'
            except wikipedia.exceptions.DisambiguationError as e:
                resp_msg = "FAIL! Wort war nicht eindeutig!"
            except wikipedia.exceptions.PageError as e:
                resp_msg = "MEGAFAIL! Wort gibt es nicht in Wikipedia!"
        else:
            resp_msg = '_' + (satz.split(' '))[1] + '_'
        resp = ((satz.split(' '))[1]).capitalize()
    elif satz in ('jmd on'):
        resp = Begruessung[random.randint(0, len(Begruessung) - 1)]

    if resp:  # add formatting for WhatsApp
        resp_title = '*_' + resp + '_*'

    return (resp_title, resp_msg)

