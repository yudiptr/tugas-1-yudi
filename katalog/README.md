## Assignment 2

Link hasil deploy dapat dilihat [di sini](https://tugas1yudi.herokuapp.com/).
<br>(add /katalog for the work)

## Bagan
![Bagan](../static/hero.png?raw=true)
Request yang diberikan oleh user akan diterima oleh url dan diarahkan ke views laman yang bersangkutan. Sesudah diterima oleh views, fungsi yang berada pada views akan dijalankan dan mengquery data yang dengan models.py sebagai penghubung. Setelah data diambil, data akan direturn sebagai response dan hasilnya akan dirender oleh template untuk diperlihatkan ke user atau client.

## Virtual Environment
### Mengapa kita menggunakan virtual environment
venv atau virtual environment dari python merupakan environtment manager yang membuat sebuah scope virtual yang terisolasi. venv ini akan mengisolasi packages dan dependancies yang ada di project. Saat kita membuat project, enc akan memastikan seluruh data yang ada di library project tidak akan berubah pada storage local kita dan hanya akan berubah di virtual environtment env.

### Apakah bisa membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Mengingat penjelasan env tadi yang akan menampung update packages dan dependancies di virtual environmentnya. Jika kita tidak menggunakannya, maka saat kita menjalankan atau mengupdate, otomatis update packages dan dependancies tersebut akan langsung mengubah data yang ada di local storage kita dan berpotensi terciptanya perbendaan versi dari data" tersebut.

## Poin 1 - 4
### 1. views.py
Pada template, sudah disediakan /katalog yang nanti file htmlnya akan kita render dengan memanggil function yang sudah kita buat (show_catalog) dan me-return hasil rendernya. Pada views ini, akan mengambil semua data yang ada di database dan menambahkan beberapa variable penting seperti nama dan npm. Variable tersebut kita simpan dalam scope context dan kita bawa kedalam fungsi render sebagai parameter tambahan untuk dibawa ke html.

### 2. urls.py
First of all, kita menambahkan path('katalog/', include('katalog.urls')) pada urls yang berada pada product-django. Hal ini dilakukan untuk meroute '/katalog' agar menjalankan function show_catalog yang ada di katalog.views.py.

### 3. katalog.html
Dalam katalog/views.py, render akan dilakukan di katalog.html. Karena pada saat render kita juga menambahkan data tambahan berupa nama dan npm, maka untuk menggunakannya kita memerlukan curly brackets untuk menggunakan sebuah variable "{{nama}} dan {{npm}}". Selain itu, kita juga menggunakan for loop untuk mengambil data" yang ada pada database yang kita simpan dengan nama list_barang.

### 4. Deploy
Untuk mendeploy, saya meng-connect-kan repo github ini ke heroku dan langsung mendeploynya. Setelah itu, diperlukan juga untuk memasukkan variable `HEROKU_APP_NAME` dan `HEROKU_API_KEY` di github secret -> actions agar dapat terhubung secara langsung ke heroku.
