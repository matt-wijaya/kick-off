Tautan : https://matthew-wijaya-kickoff.pbp.cs.ui.ac.id/

--------------TUGAS 2--------------------

(1)
Dalam mengerjakan checklist yang diberikan, saya mulai dengan melakukan setup pada aplikasi terlebih dahulu, hal ini saya lakukan dengan membuat repository, membuat projek Django baru, dan melakukan konfigurasi database, server, dan lainnya. Lalu, saya lanjutkan dengan menjalankan routing pada bagian proyek agar aplikasi "main" bisa dijalankan. Saya melakukan hal ini dengan menambahkan include() di dalam file urls.py main project, sehingga setiap request yang masuk bisa diarahkan ke main nantinya. Selanjutnya. saya membuat sebuah model di dalam models.py bernama Product sesuai dengan atribut yang diminta dan menambahkan atribut yang saya rasa perlu yaitu "stock". Setelah itu, saya melakukan makemigrations dan migrate supaya database dapat dikonversi sesuai dengan model yang saya buat sebelumnya. 

Lalu, saya membuat function show_main di views.py. Hal ini dilakukan supaya nama aplikasi saya, nama saya, dan kelas saya dapat di display di website. Agar function bisa diakses, saya menambahkan path di urls.py agar dapat diakses dan ditampilkan ke pengguna dalam bentuk HTML. Saya melakukan push ke Github dan PWS setelah semuanya selesai dilakukan

(2)
![Bagan](images/BAGAN.jpg)
Alur request client ke web berbasis Django dapat dijelaskan di dalam bagan di atas. Pertama, pengguna mengirim request ke server ketika mereka ingin meakses sebuah web, kemudian request diproses oleh urls.py agar dapat mengeksekusi fungsi sesuai yang dituju, kemudian dipass ke view yang akan menjalankan logic programnya. Jika program butuh akses model, views.py akan mengirim request untuk meminta kebutuhannya. Hasil yang sudah diproses akan diisi ke dalam template HTML dan dikirim kembali ke peramban web milik client. Pada dasarnya, urls.py berperan memetakan jalur, views.py mengolah function-function yang ada, dan models.py memenuhi request dari views.py sesuai kebutuhan, hasil yang dikirim berupa HTML yang dapat dilihat oleh client.

(3)
settings.py berperan untuk konfigurasi proyek Django. File tersebut digunakan untuk mendelegasikan aplikasi apa saja yang aktif, konfigurasi database, mendefinisikan letak template, dan keamanan serta autentikasi, termasuk mereka hosts yang diberikan izin untuk mengakses.

(4)
Migrasi database pada Django dilakukan dengan mengeksekusi makemigrations dan migrate. Proses ini harus dilakukan setiap kali ada perubahan pada model untuk mengupdate berkas migration yang nantinya akan mengubah struktur database sesuai yang ada di dalam models, sehingga keduanya tetap sinkron. Database jadi bisa terus diupdate seiring dengan development aplikasi berjalan, tidak perlu diubah lagi secara manual.

(5)
Django dijadikan sebagai framework pertama karena isinya lengkap dan terstruktur dari bawaan. Salah satu alasan yang mendasar adalah karena API yang dibuat oleh Django dapat menghubungkan antara piranti web dan juga aplikasi mobile melalui flutter. Selain itu, Django juga bersifat open source, cepat, dan aman. Berbagai template juga tersedia sehingga pemula, seperti saya dan mahasiswa lainnya, bisa fokus ke dalam memahami web development tanpa berkutat di bagian yang menyulitkan karena membangun dari 0.

(6)
SAaya rasa tutorialnya sudah dipresentasikan dengan baik, yang saya suka dari tutorial di mata kuliah ini adalah bahwa file-file yang harus dibuka untuk diedit diberitahukan di bagian awal dari instruksi, sehingga tidak ada kekeliruan yang tidak perlu akibat kesalahan file karena nama yang serupa. Namun, sebagai saran, jika ada warning, tolong dipastikan tidak ada pemisah antara warning dengan instruksinya, karena saya ingat kemarin saya sempat mengeksekusi suatu perintah yang seharusnya ada titik di belakangnya, tapi warningnya terletak lebih ke bawah sehingga tidak terbaca. Selain itu, semuanya sudah sangat baik. Terima kasih!

--------------TUGAS 3--------------------

(1)
Data delivery diperlukan dalam implementasi sebuah platform karena pada dasarnya platform tidak mungkin berdiri sendiri tanpa adanya interaksi dengan komponen lain. Sebagai contoh, semisal kita ingin mendisplay html yang sudah dirender oleh views sesuai request user di halaman browser pengguna, maka harus ada data delivery yang dilakukan dari server django kita ke browser pengguna agar dapat ditampilkan. Selain itu, seperti pada implementasi form di tugas ini, setelah pengguna menambahkan produk di halaman form, maka akan terjadi data delivery yang mengupdate xml yang akan didisplay ke user, karena itulah data delivery dibutuhkan.

(2)
Menurut saya, JSON lebih baik. Melihat kode yang ditampilkan, JSON dapat lebih mudah dibaca dan dipahami dibandingkan XML. XML sendiri memiliki lebih banyak syntax-syntax yang bermanfaat bagi eksekusi program tapi terasa redundan bagi pembaca dan penulis code. Hal ini mungkin menjadi salah satu alasan mengapa JSON bisa lebih populer dibandingkan XML. JSON juga dapat lebih banyak digunakan di aplikasi web atau mobile dan struktur data yang lebih sederhana.

(3)
Method is_valid() pada form Django berfungsi sebagai pemeriksaan akhir sebelum dilakukan save. Pada contoh, jika kita tinjau dari kode berikut di views.py
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')
Pada fungsi tersebut, is_valid berfungsi untuk memeriksa apakah data yang diinput sudah benar. Jika kita bedah lebih dalam, is_valid akan mengecek bahwa apakah data tidak None dan files tidak None. Selain itu, akan dicek juga apakah file memiliki error atau tidak. Dalam konteks di aplikasi ini, melalui is_valid, program akan mencek apakah data yang ingin didaftarkan sudah sesuai dengan requirements dari moidels dan forms.

(4)
csrf_token berguna untuk melindungi aplikasi dari cross site request forgery, ini berupa serangan yang dilakukan dengan memalsukan request dari browser user yang sudah berhasil login kedalam aplikasi. Jika tidak ada csrf_token, skenario yang dapat terjadi adalah bahwa hacker dapat mengakses tab lain di browser yang telah login dengan kredensial user, ia akan mengirim request ke web dan mengubah alur informasinya dari ke browser user menjadi ke channel miliknya. Dalam kode, csrf token digunakan dalam kode di add_item.html. Cara kerjanya adalah Django menghasilkan sebuah token rahasia yang disimpan di dua tempat, sebagai cookie dan di hasil render HTML. Ketika user mengisi form dan mengklik Add Item, browser akan mengirimkan request ke server. Setelah itu, sebelum Django memproses data ke view, token akan dicocokan terlebih dahulu sebelum diproses untuk mencegah adanya pengambilan data secara ilegal.

(5)
Dalam Tugas 3 ini, saya melakukan modifikasi sebagai berikut: Saya mengkonfigurasi .html sehingga terdapat template base yang nantinya digunakan untuk semua berkas html yang ada, termasuk di dalamnya adalah main.html. Selain itu, saya membuat sebuah model form untuk menyimpan data menjadi sebuah objek. 

Setelah itu, saya juga membuat dua fungsi baru, yaitu add item dan show item. Add item dibuat untuk menghasilkan form yang menambah data item ketika ada item yang disubmit, sedangkan show item digunakan untuk mengambil item berdasarkan primary key yang adalah idnya. Saya juga menambahkan bagian content di dalam main.html untuk menampilkan data items dan tombol Add Items, serta memodifikasi templates sebagai media menampilkan items dan details. 

Terakhir, saya menambahkan 4 fungsi baru pada views.py yaitu untuk mengembalikan request dalam bentuk xml, json, dan juga variasi fungsi untuk memfilternya berdasarkan id. Kemudian, saya melakukan routing melalui urls.py dan mempush semuanya ke github dan PWS.

(6)
Tidak, semuanya sudah bagus

POSTMAN_XML: ![Postman with an XML response](images/POSTMAN_XML.png)

POSTMAN_JSON: ![Postman with a JSON response](images/POSTMAN_JSON.png)

POSTMAN_XML_BYID: ![Postman with an XML response filtered by ID](images/POSTMAN_XML_BYID.png)

POSTMAN_JSON_BYID: ![Postman with a JSON response filtered by ID](images/POSTMAN_JSON_BYID.png)

---
## Tugas Individu 4

# (1)
Django AuthenticationForm berguna untuk meningkatkan keamanan dari website dengan menambahkan autentikasi sekaligus mensimplifikasi proses login dari user. Form ini menyediakan dua field secara langsung yaitu username dan password. Dalam Form ini terdapat aspek keamanan yang sudah dikelola secara built-in dari Django sendiri, termasuk bagian utama yaitu memeriksa kredensial pengguna, tanpa perlu konfigurasi tambahan. Selain itu, Autentikasi juga dapat diimplementasika melalui backend dari web sehingga pemberian otorisasi juga dapat dilakukan melalui backend.

Namun, kekurangan yang dimiliki adalah bahwa Form ini masih bersifat sangat mendasar dan terbatas di field username dan password, jika ingin ada opsi lain untuk masuk ke dalam web, maka harus dikonfigurasikan sendiri. 

# (2)
Perbedaan antara autentikasi dan otorisasi menurut saya bersifat berkelanjutan, autentikasi dilakukan untuk memverifikasi kredensial dari user. Tujuan utamanya adalah untuk memastikan pengguna benar-benar mereka yang memiliki akun dan menolak apabila ada percobaan akses dengan kredensial yang tidak sesuai melampaui batas tertentu. Di sisi lain, otorisasi adalah pemberian akses bagi user yang telah berhasil melalui proses autentikasi sesuai dengan masing-masing role yang mereka miliki. Apakah mereka hanya berperan sebagai viewers atau mereka dapat mengedit konten-konten yang ada di dalam website akan disesuikan di proses otorisasi. Perbedaan hak ases yang dimiliki oleh user yang belum login dan yang sudah login juga dibedakan setelah melalui proses otorisasi.

# (3)
Cookies dapat meningkatkan user experience dari seorang pengguna web karena menyimpan informasi seperti login credentials dan juga preferensi ketika user kembali mengakses website tersebut melalui penyimpanan di dalam browser. Hal ini memudahkan pembuat website dalam mengetahui apa minat user sehingga tampilan web dapat disesuaikan dengan apa yang disukai oleh user. Selain itu, cookies relatif lebih mudah diakses karena disimpan di browser milik user. 

Kekurangan yang dimiliki cookies adalah bahwa bagaimana data dapat dihapus oleh pengguna dan juga memiliki resiko keamanan apabila digunakan untuk menyimpan data sensitif karena sifatnya yang tidak langsung dibuang ketika browser dimatikan.

Di sisi lain, session adalah data user yang disimpan di server, membuatnya lebih aman dan ideal untuk menyimpan informasi yang sementara atau yang bersifat sensitif. Selain itu, yang membuatnya lebih aman dari cookies juga adalah bahwa session akan diterminate secara otomatis setelah usernya inaktif atau memang diprogram untuk dihancurkan, posisinya yang berada di server juga membuatnya tidak terekspos langsung ke pengguna. Hal ini membuatnya akan sulit untuk digali oleh peretas karena akan langsung hilang dan tidak bertahan di browser seperti informasi yang disimpan di dalam cookies. Kekurangan dari session adalah karena alokasi memorinya yang terpusat di server dan dapat menjadi beban yang menumpuk bagi server apabila aktif dalam jumlah banyak.

# (4)
Aman apabila juga ada aksi kooperatif dari user, peretasan yang dilakukan melalui informasi yang disimpan di dalam web umumnya dilakukan ketika user mengakses suatu tautan yang dapat langsung mengeksekusi script yang ditetapkan oleh peretas. Selain itu, bisa terjadi manipulasi data yang berada di dalam cookies untuk menredirect informasi dari website agar informasi dikirimkan kepada peretas. 

Penanganan melalui Django dapat dilakukan dengan adanya token CSRF yang dimiliki oleh kedua belah pihak yang berinteraksi yaitu client dan server. Hal ini dapat meminimalisir akses yang tidak terautorisasi apabila CSRF token yang dimiliki tidak sesuai. Selain itu, Django mayoritas menggunakan session dalam implementasinya, dan cookies hanya sebagai perantara berupa ID yang terenkripsi dan sulit diretas, hal ini dapat mencegah terjadinya manipulasi.

# (5)
Dalamm menyelesaikan tugas ini, pertama saya membuat tiga fungsi view di views.py untuk register, login, dan logout. Fungsi register dibuat menggunakan sistem bawaan Django yaitu UserCreationForm untuk menyimpan user baru. Selain itu, fungsi login akan menggunakan authenticationform untuk memeriksa kredensial dari user. Logout user juga menggunakan sistem bawaan dari Django untuk meng-end session. Setiap fungsi kemudian dipetakan ke urls.py dan template HTML sederhana juga ditambahkan untuk page regis dan login.

Lalu, saya menghubungkan data dengan user dengan memodifikasi models.py. Pada Product saya menambahkan sebauh field store yang melink dengan User. Ini akan memetakan pengguna dengan produk yang mereka tambahkan, kemudian saya lakukan makemigrations dan migrate untuk mengkonfigurasi database. Setelah itu, saya melakukan percobaan pembuatan akun dan penambahan produk oleh masing-masing user.

Terakhir, saya memodifikasi views.py untuk menampilkan last session dan cookie. Saya mengambil informasi pengguna dari request.user dan mendisplaynya melalui template. Saya atur cookie last login session dengan menambahkannya di function login_user setelah berhasil diautentikasi. cookie akan dihapus apabila pengguna logout dari akun milik mereka.



