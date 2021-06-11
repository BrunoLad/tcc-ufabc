import csv
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth() # client_secrets.json need to be in the same directory as the script
drive = GoogleDrive(gauth)

fileList = drive.ListFile({'q': "'1dCBT3jrG0BYyVYMTCc-JjuutOkjLDDNZ' in parents and trashed=false"}).GetList()
fileNames = map(lambda file: file['title'].removesuffix('.txt'), fileList)
authorBookList = map(lambda file: file.split('___', 1), fileNames)
print(os.getcwd())
with open(os.getcwd() + '/books.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Autor', 'Título'])
    for pair in authorBookList:
        writer.writerow(pair)
#for file in fileList:
#  print('Title: %s, ID: %s' % (file['title'], file['id']))

#data = fileList[0].GetContentString()
#print(data)
