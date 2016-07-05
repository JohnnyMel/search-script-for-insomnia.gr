#script αναζήτησης αγγελιών για το insomnia.gr
Με αυτό το script μπορείτε να ψάξετε αγγελίες στο site με κριτήρια όπως τίτλος και εύρος τιμών.

#Dependencies
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

#Πως να το τρέξετε
```bash
python insomnia.py [-h] [-f] [-r] url query pages
```
Ό,τι είναι σε [] είναι προαιρετικό όρισμα.

Ορίσματα που απαιτούνται:

url                     το URL link της σελίδας με τις
                        αγγελίες π.χ.το URL των κινητών

query                   τα κριτήρια αναζήτησης π.χ.
                        "smartphone model" (μαζί με τα
                        εισαγωγικά)

pages                   σε πόσες σελίδες θα ψάξει

Προαιρετικά ορίσματα:

-h, --help            μήνυμα βοήθειας

-f, --filter          αφαιρεί τις αγγελίες που δεν
                      έχουν τιμή (αυτές που γράφουν "επικοινωνία")

-r, --range           εύρος τιμής π.χ. 50-200
