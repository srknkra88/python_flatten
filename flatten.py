"""
1- Bir listeyi düzleştiren (düzleştirme) fonksiyon programı.
Elemanları çeşitli, çok sayıda listelerden ([[3] gibi olabilir,)
scalamadan de olmaz. Anlamı:
girdi: [[1,'a',['kedi'],2],[[[3]],'köpek'],4,5]
çıktı: [1,'a','kedi',2,3,'köpek',4,5]
"""

def  düzleştir ( l ):
    if  type ( l ) == liste :
        dönüş [ düzleştirmedeki öğe  için  l' deki alt liste  için öğe ( alt liste ) ]     
    başka :
        dönüş [ l ]

      
 """
2- verilen listenin uygulanmayacak şekilde döndürülen bir programda.
Eğer listenin elemanlarının elemanlarının listesi, elemanların elemanlarını döndürün.
Anlamı:
giriş: [[1, 2], [3, 4], [5, 6, 7]]
çıktı: [[[7, 6, 5], [4, 3], [2, 1]]
"""

def  ters ( l ):
    if  type ( l ) == liste :
        l [:: - 1 ]] içindeki öğe için [ ters ( madde ) döndür   
    dönüş  l
