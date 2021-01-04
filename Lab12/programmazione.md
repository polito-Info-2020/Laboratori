# Laboratorio 12 (simulazione d'esame)

## Parte di Programmazione

Si vuole realizzare un programma Python che permetta ad un hotel di tener traccia di eventuali contatti "Covid-19".

L'hotel dispone di un file di testo, denominato `presenze.txt`, che contiene, per ogni riga, le informazioni di un
diverso cliente dell'hotel. Ciascuna riga contiene 4 campi separati da virgola. Il primo campo è il nome del cliente, il
secondo il numero di cellulare, ed i restanti due campi sono il giorno d'ingresso ed il giorno di uscita del cliente
dall'hotel. Per semplicità, i giorni di ingresso ed uscita sono rappresentati da numeri interi (tra 1 e 366). Si può
assumere che il file sia privo di errori.

Il programma deve permettere all'hotel di ricercare eventuali contatti di eventuali clienti diagnosticati "positivo" al
Covid-19. A tale scopo, dato il nome di un cliente, deve visualizzare a video il nome ed il numero di telefono di
tutti gli altri clienti dell'hotel che hanno soggiornato per almeno un giorno insieme a quel cliente. L'elenco deve
essere visualizzato ordinato alfabeticamente per nome del cliente.

I clienti "positivi" di cui ricercare i contatti sono memorizzati, uno per riga, nel file `positivi.txt`. Per ciascuna
delle righe di questo file deve essere fatta la ricerca e deve essere stampato l'elenco di cui sopra. Si distingua il
caso in cui il cliente positivo non abbia avuto contatti con altri clienti visualizzando il testo come nell'esempio
seguente.

### Esempio

Sia dato il file `presenze.txt` seguente:

```
Mario Rossi, 3471234567, 100, 110
Paolo Verdi, 3353334444, 105, 112
Maria Azzurri, 3398887777, 98, 104
Anna Neri, 06989855, 95, 100
Guido Guidi, 3331112221, 90, 93
```

Supponendo che il file `positivi.txt` abbia il seguente contenuto:

```
Anna Neri
Paolo Verdi
Guido Guidi
```

Il programma dovrà generare in output:

```
** Contatti del cliente: Anna Neri: **
	Contatto con Maria Azzurri, telefono  3398887777
	Contatto con Mario Rossi, telefono  3471234567
** Contatti del cliente: Paolo Verdi: **
	Contatto con Mario Rossi, telefono  3471234567
** Contatti del cliente: Guido Guidi: **
	Fortunatamente Guido Guidi non ha avuto contatti
```
