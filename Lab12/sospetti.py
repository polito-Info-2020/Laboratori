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


def cerca_contatti(presenze, tizio):
    # cerco il tizio nella lista
    if tizio in presenze:
        dati_tizio = presenze[tizio]

        contatti = []
        # controlla le presenze di tutti gli altri clienti
        for (cliente, dati_cliente) in presenze.items():
            if cliente != tizio:
                if (dati_tizio['in'] <= dati_cliente['in'] <= dati_tizio['out'] or
                        dati_tizio['in'] <= dati_cliente['out'] <= dati_tizio['out']):
                    contatti.append((cliente, dati_cliente['tel']))
        return contatti
    else:
        return None


def main():
    presenze = leggi_presenze()
    sospetti = leggi_sospetti()

    for sospetto in sospetti:
        print(f'** Contatti del cliente: {sospetto}: **')

        contatti = cerca_contatti(presenze, sospetto)
        if contatti is not None:
            if len(contatti)==0:
                print(f'\tIl cliente {sospetto} non ha avuto contatti')
            else:
                for contatto in sorted(contatti):
                    print(f'\tContatto con {contatto[0]}, telefono {contatto[1]}')
        else:
            print(f'\tCliente {sospetto} non presente in archivio')


main()
