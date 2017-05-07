# script αναζήτησης αγγελιών για το insomnia.gr
Με αυτό το script μπορείτε να ψάξετε αγγελίες στο site με κριτήρια όπως τίτλος και εύρος τιμών.

# Dependencies
Για να τρέξετε το script πρέπει να έχετε τα παρακάτω:
* beautifulsoup4
* requests

Για να τα κατεβάσετε:
```bash
sudo pip install beautifulsoup4
sudo pip install requests
```
Αν δεν έχετε το pip (ubuntu):
```bash
sudo apt-get install python-pip
```

# Πως να το τρέξετε
```bash
python insomnia.py [-h] [-f] [-r] url query pages
```
Ό,τι είναι σε [] είναι προαιρετικό όρισμα.

Ορίσματα που απαιτούνται:

url: το URL link της σελίδας με τις αγγελίες (π.χ.το URL των κινητών)

query: τα κριτήρια αναζήτησης (π.χ. "smartphone model" μαζί με τα εισαγωγικά)

pages: σε πόσες σελίδες θα ψάξει (π.χ. 5)

Προαιρετικά ορίσματα:

-h, --help: μήνυμα βοήθειας

-f, --filter: αφαιρεί τις αγγελίες που δεν έχουν τιμή (αυτές που γράφουν "επικοινωνία")

-r, --range: εύρος τιμών (π.χ. 50-200)

# Παραδείγματα

1) Εύρεση των αγγελιών με τίτλο "LG G4" στην σελίδα με τις αγγελίες των LG (ψάχνει τις 10 πρώτες σελίδες):

Σημείωση: Η αναζήτηση είναι case insensitive
```bash
python insomnia.py http://www.insomnia.gr/classifieds/mobile/lg/ "lg g4" 10
```
2) Εύρεση των αγγελιών με τίτλο "LG G4" στην σελίδα με τις αγγελίες των LG (εμφανίζει μόνο αυτές που έχουν τιμή, δηλ. απαλοίφει αυτές που γράφουν "επικοινωνία"):
```bash
python insomnia.py http://www.insomnia.gr/classifieds/mobile/lg/ "lg g4" 10 -f
```
3) Εύρεση των αγγελιών με τίτλο "galaxy s6" στην σελίδα με τις αγγελίες των Samsung ψάχνοντας τις 5 πρώτες σελίδες (με εύρος τιμών 100-300 ευρώ):
```bash
python insomnia.py http://www.insomnia.gr/classifieds/mobile/samsung/ "galaxy s6" 5 -r 100-300
```
