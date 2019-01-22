# pyota-api
 Developing Python applications on top of IOTA Tangle made easy! Built on top of [PyOTA](https://github.com/iotaledger/iota.lib.py).

**Four easy steps:**

1) Clone the api package to your local directory.


2) Initialize a Session object. Example:
```
   from api.driver import Session
   session = Session(conn='https://durian.iotasalad.org:14265')
```


3) Upload any data* into Tangle. Example:
```
   session.data_to_tangle(data='Hello Tangle!', tag='TEST')
```
Data currently successfully tested for string (i.e. JSON) and pandas DataFrame (i.e. CSV file). Next step is allow this method upload any Python data structure into the Tangle. 


4) Copy the transaction hash output from the console log and verify via thetangle.org. See the example [here](https://thetangle.org/transaction/IRAQLYTFQWMDJGBGNHPVMZGZAF9KPUR9TAUXRLMULKZTVPYOBUPGOVBSSQQBMJIPFF9DBYQKSX9ZZ9999).


**Next possible steps:**

1) Incorporate MAM Ultra Lite features. See blog post [here](https://medium.com/coinmonks/iota-mam-ultra-lite-493d8d1fb71a).

2) Enable IOTA token value transactions.

3) Enable data batch processing into Tangle.

4) Bug fixing.
   
