import alapok
import szamolsa
import peldany


alapok.elso()
szamlista=szamolsa.lista_keszit()
szamolsa.lista_kiír(szamlista)
db=szamolsa.paratlan(szamlista)
min=szamolsa.min(szamlista)
max=szamolsa.max(szamlista)
szamolsa.kiíras(min,max,db)
szamolsa.fajlba_kiir(db)
peldany.peldany()