# pyota-api
 Developing applications on top of IOTA Tangle made easy! Using Python (pyota).

Four easy steps:

1) Clone the api package to your local directory.

2) Initialize a Session object. Example: 
   from api.driver import Session
   session = Session(conn='https://durian.iotasalad.org:14265')

3) Upload any* data into Tangle. Example:
   session.data_to_tangle(data='Hello Tangle!', tag='TEST')
   
4) Copy the transaction hash output from the console log and verify via thetangle.org.
   https://thetangle.org/transaction/IRAQLYTFQWMDJGBGNHPVMZGZAF9KPUR9TAUXRLMULKZTVPYOBUPGOVBSSQQBMJIPFF9DBYQKSX9ZZ9999
