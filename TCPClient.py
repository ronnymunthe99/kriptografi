import socket

plaintext = input('\nPlain text: ')
nim = input('2 Digit NIM terakhir: ')

plaintextBiner = list(
  map(
    lambda huruf: bin(huruf)[2:].zfill(8),
    bytearray(plaintext.encode())
  )
)

nimBiner = ''.join(
  map(
    lambda angka: bin(int(angka))[2:].zfill(4),
    list(nim)
  )
)

print('\nPlaintext: ', plaintext)
print('Plaintext biner: ', ' '.join(plaintextBiner))
print('\nNIM (kunci): ', nim)
print('NIM (kunci) biner: ', nimBiner)

enkripsi = list(
  map(
    lambda huruf: bin(
      int(huruf, 2) ^ int(nimBiner, 2)
    )[2:].zfill(8),
    plaintextBiner
  )
)
print('\nEnkripsi ECB XOR: ', ' '.join(enkripsi))

serverPort = 12000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('\nKoneksi ke server')
clientSocket.connect(('127.0.0.1', serverPort))

print('Mengirim ke server')
clientSocket.send(''.join(enkripsi).encode())

clientSocket.close()
