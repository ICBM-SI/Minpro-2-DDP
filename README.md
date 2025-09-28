# Minpro-2-DDP

# Aditya Dwinugraha Yusniandra 2509116114 Mini Project CRUD - Sistem Pengelolaan Rental Mobil
 
# Flowchart:
![Flowchart Rental Baru](https://github.com/user-attachments/assets/2fe7ba86-1176-4cf6-8c0a-895cd07c86b2)

# Penjelasan:
# 1. Tampilan Awal (Login Sistem)
Untuk tampilan awal, user akan melihat tampilan sistem login dari program. Terdapat 2 role yang dapat dipilih, yaitu "Manager" dan "Karyawan". User dapat memilih opsi dengan meng-input angka 1 atau 2.

<img width="477" height="149" alt="image" src="https://github.com/user-attachments/assets/495f59f2-b6ff-41aa-8ade-113c9ff9c5fe" />

Jika memasukkan input selain angka tersebut maka program akan berhenti.

<img width="514" height="196" alt="image" src="https://github.com/user-attachments/assets/a14d5f1d-be99-431f-8078-7a5566368c51" />

# 2. Tampilan Menu - Manager
Jika memilih angka 1 *(manager)*, user harus memasukkan username & password yang benar, jika sudah maka user dapat mengakses menu sebagai manager. Jika salah memasukkan username atau password, maka sistem akan otomatis login sebagai karyawan.

<img width="308" height="296" alt="image" src="https://github.com/user-attachments/assets/49ff1942-ec9f-4963-8593-b4f8624078fb" />

**Jika Salah Login:**

<img width="326" height="277" alt="image" src="https://github.com/user-attachments/assets/71369d3b-d926-4e71-8193-a7e822383e10" />


Sebagai **manager**, user diberikan beberapa opsi seperti menambah data mobil rental, melihat daftar mobil, menghapus data mobil yang tersimpan, update data mobil, dan opsi untuk keluar dari sistem.

<img width="299" height="208" alt="image" src="https://github.com/user-attachments/assets/e2f4dc85-845f-4dd8-8e2d-bf5b9aa418fd" />



# 3. Tambah Mobil
Untuk opsi ke-1, **manager** dapat menambahkan data mobil baru kedalam list dengan memasukkan beberapa data seperti merk, model, tahun, serta harga sewa mobil. Jika sudah, maka data akan tersimpan kedalam database. Jika ingin kembali ke menu utama, user dapat menekan enter.

<img width="963" height="246" alt="image" src="https://github.com/user-attachments/assets/85f355c7-e572-486c-8fe0-0caa93ef5165" />

# 4. Lihat Daftar Mobil
Opsi ke-2, **manager** dapat melihat data-data mobil rental di dalam sistem, seperti harga sewa dan status mobil tersedia atau tidak. User bisa kembali ke menu utama dengan menekan enter.

<img width="511" height="249" alt="image" src="https://github.com/user-attachments/assets/9bba5179-b021-44f5-a3bf-40c7b376f80d" />

# 5. Perbarui Data Mobil
Opsi ke-3 yaitu memperbarui data mobil yang sudah tersimpan di dalam database, **manager** dapat mengubah data lama dan menggantinya dengan data baru, dan user juga dapat mengganti status mobil dari disewa atau tersedia. User dapat kembali ke menu dengan menekan enter.

<img width="977" height="446" alt="image" src="https://github.com/user-attachments/assets/ae476a53-d7cf-4c11-b23f-2a82c2e63026" />

# 6. Hapus Data Mobil
Opsi ke-4 berfungsi untuk menghapus data mobil yang ada di database, cukup dengan memasukkan input angka sesuai dengan yang ada pada list, maka data tersebut akan terhapus dan sistem akan menampilkan langsung daftar mobil yang baru. User bisa kembali ke menu dengan menekan enter.

<img width="542" height="442" alt="image" src="https://github.com/user-attachments/assets/6ab5b261-7606-4294-b4f4-ae643f26d710" />

# 7. Keluar dari sistem
Opsi terakhir atau ke-5, jika **manager** sudah selesai menggunakan sistem, user dapat keluar dengan menggunakan opsi ini.

<img width="514" height="202" alt="image" src="https://github.com/user-attachments/assets/4682ce96-ace7-42e7-ae18-b15f8b5deeef" />

# 8. Error Handling
Error Handling digunakan jika user memasukkan input yang tidak bisa/tidak sesuai yang diminta oleh sistem, seperti memasukkan angka yang salah, memasukkan input *string* di bagian angka, dan lain-lain.

<img width="305" height="227" alt="image" src="https://github.com/user-attachments/assets/031bafc7-b8eb-4a00-8e33-8c2f6624ae69" />
<img width="514" height="140" alt="image" src="https://github.com/user-attachments/assets/06eaa22f-07ac-4737-85aa-c031e76c069b" />

# Tampilan Sistem Jika Login Sebagai Karyawan

# 1. Tampilan Menu - Karyawan
Sama seperti login untuk manager, user harus memasukkan username & password yang benar untuk masuk ke sistem. Jika salah, maka program akan berhenti.

<img width="306" height="247" alt="image" src="https://github.com/user-attachments/assets/e29473ff-bb35-44d2-b96b-22304d4330e2" />

**Jika Salah Username atau Password**

<img width="507" height="139" alt="image" src="https://github.com/user-attachments/assets/8be85917-f68f-4725-a533-0323f4b3b5cf" />

Jika username & password sudah benar, maka user akan diperlihatkan menu utama dari sistem, berbeda dengan menu manager, karyawan hanya dapat mengakses fitur melihat daftar mobil dan memperbarui status mobil.

<img width="284" height="161" alt="image" src="https://github.com/user-attachments/assets/fd5d2be5-43ce-4b5e-8213-7e485b71518c" />


# 2. Lihat Daftar Mobil
Karyawan dapat melihat daftar mobil yang tersimpan di dalam sistem jika memilih opsi ke-1, dan dapat kembali ke menu dengan menekan enter.

<img width="476" height="221" alt="image" src="https://github.com/user-attachments/assets/285cc3ad-5e83-4276-bf47-9ecc25f7a472" />

# 3. Update Status Mobil
Jika memilih opsi ke-2, karyawan dapat melihat daftar mobil dan bisa memilih data yang ingin diubah statusnya dengan memasukkan nomor data yang tersedia di list.

<img width="496" height="334" alt="image" src="https://github.com/user-attachments/assets/ce01e819-d7cd-48f2-afb2-e589363a6efd" />

Jika karyawan memasukkan status mobil yang tidak sesuai, maka sistem akan

# 4. Keluar dari sistem
Sama seperti menu manager, user/karyawan bisa keluar dari sistem dengan memilih opsi ke-3 jika sudah selesai menggunakan.

<img width="507" height="66" alt="image" src="https://github.com/user-attachments/assets/474c3aa4-94a1-423c-baa6-f0dbdddcd920" />

