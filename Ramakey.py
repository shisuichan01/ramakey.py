import os
from time import sleep


a ='\033[92m'
b ='\033[91m'
c ='\033[0m'
os.system('clear')
print(a+'\t  Keyboard Pembantu')
print(b+'\t    Hallo iam Rama')
print('\t https://ramlan.xyz')
print(a+'+'*40)
print('\nWAIT GANS')
sleep(1)
print(b+'\n[!] Mengwait...')
sleep(1)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print(a+'DONE')
sleep(1)
print(b+'\nBerhasil...')
sleep(1)

key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
Rama = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
Rama.write(key)
Rama.close()
sleep(1)
print(a+'DONE')
sleep(1)
print(b+'\nBerhasil...')
sleep(2)
os.system('termux-reload-settings')


#Rama ID
