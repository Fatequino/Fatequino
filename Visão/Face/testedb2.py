# Sugestão para futuros grupos: criar métodos para automatizar a leitura do arquivo, ou melhor, ler diretamente do banco na nuvem o arquivos de descritor facial

import pymongo
import numpy as np
from bson.binary import Binary
import pickle

client = pymongo.MongoClient("mongodb://FatequinoTeste:bFRw3bj2PCkeqEfK@testefatequinho-shard-00-00.vokp4.azure.mongodb.net:27017,testefatequinho-shard-00-01.vokp4.azure.mongodb.net:27017,testefatequinho-shard-00-02.vokp4.azure.mongodb.net:27017/<dbname>?ssl=true&replicaSet=atlas-y2tcer-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test

descritorFacial = np.load('./recursos/descritores_renan.npy')

# convert numpy array to Binary, store record in mongodb
descritorFacialBinario = Binary(pickle.dumps(descritorFacial, protocol=2), subtype=128 )
# get record from mongodb, convert Binary to numpy array
#descritorFacialNpy = pickle.loads(descritorFacialBinario)

collection = client.libraryDB.books  
booksData = [  
  
      {  
         "Nome":"Renan Vinicius Antoneli",  
         "RA": "1430481813052",  
         "DescritorFacial": descritorFacialBinario  
      }  
   ]  
  
#collection.insert_many(booksData)

print('Find all documents')  
for x in client.libraryDB.books.find():  
        descritorFacialNpy = pickle.loads(x['DescritorFacial'])
        print(descritorFacialNpy)