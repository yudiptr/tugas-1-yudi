# My Watchlist
[Deployment Link for Assignment 3](http://tugas2yudi.herokuapp.com/mywatchlist/)

# Perbedaan JSON, XML, dan HTML
* HTML (Hypertext Markup Language) merupakan markup languange yang merepresentasikan data dalam element tree untuk ditampilkan dalam bentuk web dan bisa dikustomisasi cara penyajiannya

* JSON (JavaScript Object Notation) adalah format dalam bentuk JavaScript untuk merepresentasikan data dengan bentuk yang efisien yang terdiri dari key dan value, tetapi kurang rapih dilihat. Karena tidak menggunakan tag seperti xml dan html, JSON lebih cepat pengaksesannya dan mudah dibaca mesin

* XML (Extensive Markup Language) juga merupakan salah satu bahasa yang digunakan untuk menyimpan dan mengantarkan data. Penyimpanan yang dilakukan XML mirip seperti HTML yang lebih mudah dibaca dengan menggunakan tag-tag.

# Alasan diperlukan data delivery dalam pengimplementasian platform
Dalam kesatuan platform, pasti terjadi pertukaran data user dengan data yang ada di server. Dengan menggunakan data delivery tersebut, tentu mempermudah kita untuk melakukan pengiriman data. Pengiriman data bisanya menggunakan format HTML, XML, ataupun JSON agar data yang dideliver bisa diterima dengan baik oleh user dan mudah dipahami berbagai programming language serta mudah didevelop :D.

# Implementasi
1. Membuat aplikasi 'mywatchlist' dengan menjalankan perintah `python manage.py startapp mywatchlist` di folder main atau root
2. Mengroute url dengan menambahkan `path('mywatchlist/', include('mywatchlist.urls'))` untuk menghubungkan urlpatterns yang ada pada project_django dengan mywatchlist serta menambahkan mywatchlist pada `installed_app` yang ada di setting.py. Selanjutnya, melakukan path route dalam mywatchlist/urls.py agar terhubung dengan fungsi yang akan dijalankan pada mywatchlist/views.py
3. Membuat model data pada mywatchlist/models.py dengan fields `watched_movie, movie_name, movie_rating, movie_date, movie_review`. Selanjutnya, melakukan migrasi dengan melakukan command `python manage.py makemigrations` dan `python manage.py migrate`.

## Postman
### HTML
![HTML]("../static/mywatch_html.png?raw=true")

### JSON
![JSON]("../static/mywatch_json.png?raw=true")
<br/><br/>

### XML
![XML]("../static/mywatch_xml.png?raw=true")
<br/><br/>
