from hyphen import Hyphenator
from hyphen.dictools import *

for lang in ['pt_BR']:
    if not is_installed(lang): install(lang)

pt_br = Hyphenator('pt_BR')

word = input("Digite a palavra: ")

silabas = pt_br.syllables(word)

print(silabas)