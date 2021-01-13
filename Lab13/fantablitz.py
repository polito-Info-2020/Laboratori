# Soluzione proposta alla simulazione d'esame "Fantablitz"

from random import shuffle

PEZZI = {'F': 'Fantasma', 'T': 'Topo', 'L': 'Libro', 'P': 'Poltrona', 'B': 'Bottiglia'}
COLORI = {'b': 'Bianco', 'r': 'Rosso', 'a': 'Azzurro', 'g': 'Grigio', 'v': 'Verde'}

OGGETTI = {'Fb', 'Pr', 'Bv', 'Tg', 'La'}  # pezzi fisici da selezionare

FILE_CARTE = 'carte.txt'


def leggi_carte(file):
    try:
        fmazzo = open(file, 'r')
    except IOError:
        print(f'Impossibile aprire il file {file}')
        exit()

    mazzo = []
    for riga in fmazzo:
        carte = riga.rstrip().split()
        if (len(carte) == 2 and len(carte[0]) == 2 and carte[0][0] in PEZZI and carte[0][1] in COLORI
                and len(carte[1]) == 2 and carte[1][0] in PEZZI and carte[1][1] in COLORI):
            mazzo.append(carte)
        else:
            print('Riga non valida - ignorata: ' + riga)
    fmazzo.close()
    return mazzo


def descrizione_carta(sigla):
    return PEZZI[sigla[0]] + ' ' + COLORI[sigla[1]]


def scegli_pezzo(carte):
    # verifica se è uno dei pezzi fisici
    if carte[0] in OGGETTI:
        return carte[0]
    elif carte[1] in OGGETTI:
        return carte[1]
    else:
        for pezzo in OGGETTI:
            if pezzo[0] == carte[0][0] or pezzo[0] == carte[1][0]:
                pass  # la forma è uguale ad una delle figure sulla carta
            elif pezzo[1] == carte[0][1] or pezzo[1] == carte[1][1]:
                pass  # il colore è uguale ad una delle figure sulla carta
            else:
                return pezzo  # è lui!!
    raise ValueError('Non ho trovato il pezzo')  # non dovrebbe mai arrivare qui...


def main():
    mazzo = leggi_carte(FILE_CARTE)
    shuffle(mazzo)
    for carte in mazzo:
        print('Carta: ' + descrizione_carta(carte[0]) + ' + ' + descrizione_carta(carte[1]), end='')
        pezzo = scegli_pezzo(carte)
        print(' -> Prendere: ' + descrizione_carta(pezzo))


main()
