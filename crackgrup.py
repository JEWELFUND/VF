import os, sys, re, time, requests, calendar, random, bs4, uuid, json, subprocess
from bs4 import BeautifulSoup as parser

uidl =[]
if sys.platform.lower() == 'linux':
      os.system('clear')
      
def yes():
      coki=input('masukan cokies : ')
      user = input('uid grup: ')
      kocak("https://mbasic.facebook.com/groups/"+user,coki)
      
def kocak(url,cokies):
      data = parser(requests.Session().get(url,cookies={"cookie": cokies}).text, "html.parser")
      judul = re.findall("<title>(.*?)</title>",str(data))[0]
      print(judul)
      if str(judul) == 'Use basic mode':
            print('cokies berada dalam mode free')
      if str(judul) == 'Epsilon':
            print('cokies tidak dpt mengakses grup')
      if str(judul) == 'Kesalahan':
            print('cokies yg anda masukan salah')
      if str(judul) == 'Masuk Facebook' or str(judul) == 'Masuk Facebook | Facebook' or str(judul) == 'Masuk ke Facebook' or str(judul) == 'Log in to Facebook':
            print('cokies mokad')
      else:
            for isi in data.find_all("h3"):
                  for ids in isi.find_all("a",href=True):
                        if "profile.php" in ids.get("href"):uid = ids.get("href").split("=")[1].replace("&eav","");nama = ids.text
                        else:
                              if judul in ids.text:pass
                              else:uid,nama=ids.get("href").split("/")[1].split("?")[0],ids.text
                        if uid+'|'+nama in uidl:pass
                        else:uidl.append(uid+'|'+nama)          
      print('\rmengumpulkan %s uid'%(len(uidl)),end=' ')
      for x in data.find_all("a",href=True):
            if "Lihat Postingan Lainnya" in x.text:
                  kocak("https://mbasic.facebook.com"+x.get("href"),cokies)

yes()