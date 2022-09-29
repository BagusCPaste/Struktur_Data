# mengecek apakah list L kosong atau tidak
x = []
x.append('hallo')
x.append('apa kabar')
x.append('semuanya')
print(x)
def is_empty():
    return x==[]
x.pop()
x.pop()
x.pop()
print(is_empty())
['hallo', 'apa kabar', 'semuanya']
True
s = []
s.append('hallo')
s.append('semuanya')
s.append('apa kabar')
print(s)

hapus = s.pop()
print('data terhapus: ', hapus)
print('data terbaru: ', s)
print('panjang stack: ', len(s))
def apakah_kosong():
    return s == []