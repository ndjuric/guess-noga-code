# guess-noga-code
try to guess NOGA/NACE code from company activity description with n-grams

cd ngrams/  
bunzip2 1.gram.bz2  
bunzip2 2.gram.bz2  
bunzip2 3.gram.bz2  
cd ../api/  
python api.py  
  
curl 'http://localhost:1990/guess/?description=L%27acquisizione%2C+la+detenzione%2C+l%27amministrazione%2C+la+gestione+e+la+cessione+di+partecipazioni+ad+altre+societ%C3%A0+nazionali+e%2Fo+estere+nonch%C3%A9+il+loro+finanziamento.+Svolgere+attivit%C3%A0+commerciale+all%27estero%3B+acquistare%2C+gestire+e+vendere+titoli+e+prodotti+finanziari+nell%27ambito+dell%27amministrazione+del+proprio+patrimonio%3B+acquistare%2C+gestire+e+locare+a+terzi+beni+immobili.+Partecipare+ad+altre+imprese.'  

or go to http://localhost:1990/

