from hyphen import Hyphenator
from hyphen.dictools import *

# Download and install some dictionaries in the default directory using the default
# repository, usually the OpenOffice website
for lang in ['pt_BR']:
    if not is_installed(lang): install(lang)
# Create some hyphenators
pt_br = Hyphenator('pt_BR')

word = input("Digite a palavra: ")

silabas = pt_br.syllables(word)

print(silabas)