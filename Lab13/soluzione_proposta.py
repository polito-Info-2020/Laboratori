# print(open('carte.txt', 'r').read())

NOME = { 'F': 'Fantasma', 'T': 'Topo', 'P': 'Poltrona', 'B': 'Bottiglia', 'L': 'Libro'}
COLORE = { 'b': 'Bianco', 'r': 'Rosso', 'a': 'Azzurro', 'g': 'Grigio', 'v': 'Verde'}
#print(NOME)
#print(COLORE)

OGGETTI = ['Bv', 'Tg', 'Fb', 'La', 'Pr']

NOME_FILE = 'carte.txt'

def main():
    mazzo = leggi_mazzo(NOME_FILE)
    # print(mazzo)
    for carta in mazzo:
        oggetto = trova_oggetto(carta)
        print(f'Carta: {NOME[carta[0][0]]} {COLORE[carta[0][1]]} + ', end='')
        print(f'{NOME[carta[1][0]]} {COLORE[carta[1][1]]} ', end='')
        print(f'-> Prendere: {NOME[oggetto[0]]} {COLORE[oggetto[1]]}')


def trova_oggetto(carta):
    if carta[0] in OGGETTI:
        return carta[0]
    elif carta[1] in OGGETTI:
        return carta[1]
    else:
        for oggetto in OGGETTI:  # oggetto: 'Tv'
            if (oggetto[0] != carta[0][0] and oggetto[0] != carta[1][0] and
                oggetto[1] != carta[0][1] and oggetto[1] != carta[1][1]):
                    return oggetto
    return None   # non capita mai...


def leggi_mazzo(nome_file):
    try:
        infile = open(nome_file, 'r')
    except IOError:
        print('Impossibile aprire il file')
        exit()
        
    mazzo = []
    for line in infile:
        carta = line.strip().split()
        # carta = [ 'Tr', 'Bv']
        # print(carta)
        mazzo.append(carta)
    infile.close()
    return mazzo
    
main()