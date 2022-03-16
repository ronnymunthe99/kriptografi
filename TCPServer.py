import socket
from textwrap import wrap

nim = input('\nMasukkan 2 digit NIM terakhir: ')

nimBiner = ''.join(
  map(
    lambda angka: bin(int(angka))[2:].zfill(4),
    list(nim)
  )
)

print('NIM (kunci): ', nim)
print('NIM (kunci) biner: ', nimBiner)

serverPort = 12000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('127.0.0.1', serverPort))

serverSocket.listen(1)
print('\nMemulai server TCP, menunggu koneksi dari client...')

connectionSocket, addr = serverSocket.accept()
print('Koneksi berhasil, sedang menerima data...')

data = connectionSocket.recv(1024)
print('Data berhasil diterima, data yang diterima: ', data.decode())

terenkripsi = data.decode()
terenkripsi_geser = terenkripsi[1:] + '0'
print('Geser bit ke kiri: ', terenkripsi_geser)

terenkripsi_geser = wrap(terenkripsi_geser, 8)
plaintext = ''.join(
  map(
    lambda huruf: chr(int(huruf, 2)),
    terenkripsi_geser
  )
)
print('\nHasil plaintext: ', plaintext)

dekripsi = list(
  map(
    lambda huruf: bin(
      int(huruf, 2) ^ int(nimBiner, 2)
    )[2:].zfill(8),
    wrap(data.decode(), 8)
  )
)
print('Hasil dekripsi biner: ', ' '.join(dekripsi))

plaintext = ''.join(
  map(
    lambda huruf: chr(int(huruf, 2)),
    dekripsi
  )
)
print('Hasil dekripsi plaintext: ', plaintext)

connectionSocket.close()
