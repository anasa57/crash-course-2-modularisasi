# from geometri.segitiga import hitung_luas_segtiga
# import geometri.segitiga as gs
from geometri.lingkaran import hitung_luas_lingkaran, info as info_lingkaran
from geometri.persegipanjang import hitung_luas_persegipanjang, info as info_persegipanjang
from geometri.segitiga import hitung_luas_segtiga, info as info_segitiga

print(info_persegipanjang())
print(f'hitung luas persegipanjang dengan panjang 10 cm dan lebar 3 cm = {hitung_luas_persegipanjang(10,3)} cm')

print(f'\n{info_segitiga()}')
print(f'hitung luas segitiga dengan alas 11 cm dan tinggi 3 cm = {hitung_luas_segtiga(11,3)} cm')

print(f'\n{info_lingkaran()}')
print(f'hitung luas lingkaran = {hitung_luas_lingkaran(2)}')