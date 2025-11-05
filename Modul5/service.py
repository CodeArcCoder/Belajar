# class user_service, sebagai class dimana kita akan membuat
constructor dan method untuk objek user
class user_service:
# def __init__ method adalah constructor dalam Python
# Dalam constructor, objek kita inisialisasikan memiliki
atribut username & password
# Selain inisialisasi, kita masukkan data melalui memory
dengan membuat python dictionary self.data
# Penggunan self disini adalah syntax python, dimana self
sebagai penunjuk objek yang sedang dipakai
def __init__(self, username, password):
self.username = username
self.password = password

self.data = {
"nama1kelompok??" : {
"username" : "nama1kelompok??",
"password" : "12345",
"role" : "mahasiswa"
},
"nama2kelompok??" : {
"username" : "nama2kelompok??",
"password" : "12345",
"role" : "dosen"
}
}
# Method untuk pengecekan kesesuaian input dengan data di
dictionary yang telah kita buat
def check_password(self):
for value in self.data:
if value == self.username:
get_data_user = self.data[value]
if self.password == get_data_user['password']:
return get_data_user
else:
return False

# Method untuk proses login dalam console
def login(self):
data = self.check_password()
if data:
print("\nWelcome", data['username'])
print("Logged in as:", data['role'])
else:
print("\nInvalid Login!\n")