#!/usr/bin/python3
'''
Created: 26/03/2022
Author : Leo Manangka
'''

import requests
from bs4 import BeautifulSoup

def informasi():
    print('\033[96m' + '''
    n             = Nomina: kata benda
    a             = Adjektiva: kata yang menjelaskan nomina atau pronomina
    p             = Partikel: kelas kata yang meliputi kata depan, kata 
                    sambung, kata seru, kata sandang, ucapan salam
    v             = kata kerja
    pron          = Pronomina: kelas kata yang meliputi kata ganti, kata 
                    tunjuk, dan kata tanya
    num           = Numeralia: kata bilangan
    Ek            = Ekonomi dan Keuangan
    Ling          = Linguistik
    cak           = Cakapan: menandai kata yang digunakan dalam ragam takbaku
    Psi           = Psikologi
    Fis           = Fisika
    Bio           = Biologi
    akr           = akronim
    prakategorial = kata tidak dipakai dalam bentuk dasarnya
    ''' + '\033[0m')

def kamus():
    if  'Entri tidak ditemukan.' in soup.find_all('h4')[1].text:
        print('\033[1m' + soup.find_all('h4')[1].text + "\n" + '\033[0m')
    elif 'Entri tidak ditemukan.' not in soup.find_all('h4')[1].text and 'memudahkan pencarian Anda' in soup.find_all('li')[4].text:
        print('\033[1m' + soup.find('i').text,"cari:",soup.find_all('font')[1].text + '\033[0m')
    else:
        konten=soup.find_all('li')[4:]
        del konten[-3:]
        for li in konten:
            print('\033[1m' + li.text + "\n" + '\033[0m')

if __name__ == '__main__':
    kata=input('\033[1m' + "Cari Kata: " + '\033[0m')
    for i in range(0, len(kata),1):
        if kata[i]==' ':
            kata=kata.replace(kata[i],'-')

    kbbi='https://kbbi.kemdikbud.go.id/entri/%s'% kata
    header={'User-Agent':'BOT'}
    resp=requests.get(kbbi,headers=header)
    soup=BeautifulSoup(resp.text,'html.parser')

    if resp.status_code==200:
        print('\033[92m' + "Success!\n" + '\033[0m')
    else:
        print('\033[91m' + "An error has occured\n" + '\033[0m',resp) 

    informasi()
    kamus()
