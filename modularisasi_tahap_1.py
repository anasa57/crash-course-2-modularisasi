"""
Program menghitung luas segitia
luas-segitiga = alas * tinggi / 2
"""
alas = 10
tinggi =6
luas_segitiga = alas * tinggi / 2
print(f'segitiga dengan alas = {alas} cm, dan tinggi = {tinggi} cm, maka memiliki luas {luas_segitiga} cm')

print('\ndiketahui :')
print(f'- alas segitiga = {alas} cm')
print(f'- tinggi segitiga = {tinggi} cm')
print(f'- maka luas segitiga adalah = {luas_segitiga} cm')

print('\nmembuat fungsi hitung_luas_segtiga')
def hitung_luas_segtiga(alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga

alas = 10
tinggi = 6
print(f'Dengan menggunakan Fungsi luas segitiga dengan alas = {alas} cm, dan tinggi = {tinggi} cm, hasilnya = {hitung_luas_segtiga(alas,tinggi)}')
print(f'Menghitung luas segitiga dengan fungsi, hasilnya = {hitung_luas_segtiga(10,6)}')