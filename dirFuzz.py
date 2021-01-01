#imports
import requests
import os.path
#assign inputs
url = input('Url: (e.g www.url.com )\n>>')
if 'http://' or 'https://' not in url[0:8]:
    url = 'http://' + url
ext = input('Extention: Example ( .php - .html ) ,leave empty for dictionary fuzzing\n>>')
if ext == '':
    ext = False
else:
    if ext[0] != '.':
        ext = '.' + ext
#read file
while True:
    wlist = input('Worldlist : ( path/to/file.extention ) \n>>')
    if os.path.isfile(wlist):
        wlistLines = open(wlist, 'r').readlines()
        break
    print('Not a valid file path! , Try again..')
#loop requests
count = 0
for i in range(0,len(wlistLines)):
    enum=wlistLines[i].replace('\n','')
    if ext:
        r = requests.get(url+'/'+enum+ext)
    else:
        r = requests.get(url+'/'+enum)
    if r.status_code != 404:
        print('\033[32m FOUND: ' + url + '/' + enum+ext + ' - ' + str(r.status_code))
    else:
        count+=1
if count == len(wlistLines):
    print('\n\n\n---No matches found---')
    

 
   

   
