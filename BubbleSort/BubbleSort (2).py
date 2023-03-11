##B
from prettytable import PrettyTable
import pandas as pd

data = pd.read_excel(r'./pertandingan-pialadunia2018.xlsx', engine='openpyxl')
data_list = data.values.tolist()


class pialadunia:
   def __init__(self,ambil):
       self.negara = ambil[0]
       self.tempat = ambil[1]
       self.jadwal = ambil[2]

tabelPD = PrettyTable(["Pertandingan","Tempat","Jadwal"])
daftarpd =[]
for i in range(len(data_list)):
   daftarpd.append(pialadunia(data_list[i]))


#### SORTING SECARA ASCENDING
##def urutJadwalAscen(daftar):
##   n = len(daftar)
##   for i in range (n):
##       for j in range(0,n-i-1):
##           if daftar[j].jadwal > daftar[j+1].jadwal:
##               daftar[j], daftar[j+1] = daftar[j+1], daftar[j]
##
##
##urutJadwalAscen(daftarpd)
##for i in daftarpd:
##   tabelPD.add_row([i.negara,i.tempat,i.jadwal])
##print(tabelPD)


## SORTING SECARA DESCENDING
def urutJadwalDescen(daftar):
   n = len(daftar)
   for i in range (n):
       for j in range(0,n-i-1):
           if daftar[j].jadwal < daftar[j+1].jadwal:
               daftar[j], daftar[j+1] = daftar[j+1], daftar[j]


urutJadwalDescen(daftarpd)
for i in daftarpd:
   tabelPD.add_row([i.negara,i.tempat,i.jadwal])
print(tabelPD)

