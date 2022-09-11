## Assignment 2

Link hasil deploy dapat dilihat [di sini](https://tugas1yudi.herokuapp.com/).
(add /katalog for the work)

## Bagan
![Bagan](../static/hero.png?raw=true)
Request yang diberikan oleh user akan diterima oleh url dan diarahkan ke views laman yang bersangkutan. Sesudah diterima oleh views, fungsi yang berada pada views akan dijalankan dan mengquery data yang dengan models.py sebagai penghubung. Setelah data diambil, data akan direturn sebagai response dan hasilnya akan dirender oleh template untuk diperlihatkan ke user atau client.