# Soluzione proposta Lab 12

FILE_PRESENZE = 'presenze.txt'
FILE_SOSPETTI = 'sospetti.txt'


def leggi_presenze():
    presenze = {}  # dizionario. Chiave: nome, Valori: dict(telefono, data_in, data_out)
    file = open(FILE_PRESENZE, 'r')
    for line in file:
        campi = line.rstrip().split(',')
        nome = campi[0]
        record = {
            'tel': campi[1],
            'in': int(campi[2]),
            'out': int(campi[3])
        }
        presenze[nome] = record
    file.close()
    return presenze


def leggi_sospetti():
    sospetti = []
    file = open(FILE_SOSPETTI, 'r')
    for line in file:
        sospetti.append(line.strip())
    file.close()
    return sospetti


def cerca_contatti(presenze, sospetto):
    # cerco il tizio nella lista
    if sospetto in presenze:
        dati_sospetto = presenze[sospetto]

        contatti = []
        # controlla le presenze di tutti gli altri clienti
        for (cliente, dati_cliente) in presenze.items():
            if cliente != sospetto:
                if (dati_sospetto['in'] <= dati_cliente['in'] <= dati_sospetto['out'] or
                        dati_sospetto['in'] <= dati_cliente['out'] <= dati_sospetto['out'] or
                        (dati_cliente['in'] < dati_sospetto['in'] and dati_cliente['out'] > dati_sospetto['out'])):
                    contatti.append((cliente, dati_cliente['tel']))
        return contatti
    else:
        return None


# Soluzione alternativa con l'utilizzo di 'set' che rappresentano i giorni di presenza
def cerca_contatti_bis(presenze, sospetto):
    if sospetto not in presenze:
        return None

    giorni_sospetto = set(range(presenze[sospetto]['in'], presenze[sospetto]['out']+1))

    contatti = []
    for cliente in presenze:
        if cliente != sospetto:
            giorni_cliente = set(range(presenze[cliente]['in'], presenze[cliente]['out']+1))
            giorni_comuni = giorni_sospetto.intersection(giorni_cliente)
            if len(giorni_comuni)>0:
                contatti.append((cliente, presenze[cliente]['tel']))
    return contatti


def main():
    presenze = leggi_presenze()
    sospetti = leggi_sospetti()

    for sospetto in sospetti:
        print(f'** Contatti del cliente: {sospetto}: **')

        contatti = cerca_contatti(presenze, sospetto)
        if contatti is not None:
            if len(contatti) == 0:
                print(f'\tIl cliente {sospetto} non ha avuto contatti')
            else:
                for contatto in sorted(contatti):
                    print(f'\tContatto con {contatto[0]}, telefono {contatto[1]}')
        else:
            print(f'\tCliente {sospetto} non presente in archivio')


import time
start = time.perf_counter()
main()
stop = time.perf_counter()
print(f'Execution time: {(stop-start)*1000:.2}ms')
