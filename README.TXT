These scripts are meant to be used in the following order:

1. Create the tickerfile
Fetch the list of companies from Oslo Bors.
Open it in a pdf reader and copy the table data to a plain text file.
Then run: 
>python pickle_selskapsliste.py <textfile> oslobors.pickle

2. Import the ticker data for all companies:
>python import_tickerdata.py oslobors.pickle

3. Create the joined-closed data:
>python create_joined_closed.py oslobors.pickle

4. Then plot the correlation data:
>python create_correlationplot.py

