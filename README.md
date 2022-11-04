<div align="center">
  <img src="https://raw.githubusercontent.com/Braincore-id/IndoTWEEST/main/logo.png" width="250" height="250">
  <h3 align="center">IndoTWEEST</h3>
  <p align="center">
    Indonesian Tweet Stopwords
  </p>
</div>

<hr>

Proyek ini di-inisialisasi oleh Braincore.id sebagai kontribusi dalam pengembangan dataset stopwords sosial media Twitter untuk memudahkan penelitian yang menggunakan dataset dari platform tersebut demi kemajuan NLP Indonesia.

# Kontribusi
Tata cara kontribusi dapat dibaca pada dokumen berikut [ini](https://t.co/5amYqcBHO9)

1. Clone terlebih dahulu git ini menggunakan command `git clone https://github.com/Braincore-id/IndoTWEES.git`

2. **Bagi yang memang sudah memiliki kumpulan stopwords yang ingin ditambahkan dapat melewati tahap 2**. Jalankan [Colab](https://colab.research.google.com/drive/13hWqc5Ltrv4f6dmtqAIZhtJbviDgD81u?usp=sharing) berikut untuk dijadikan acuan *stopwords* apa saja yang ingin dimasukkan

3. Setelah mendapatkan kumpulan *stopwords*, masukkan kumpulan *stopwords* tersebut kedalam file **.txt** dengan format sebagai berikut
```
<stopword A>
<stopword B>
<stopword C>
...
...

```
4. Jalankan perintah `python add_csv.py --new_stopwords <file.txt>`. Untuk lebih jelas mengenai *argparse* apa saja yang dapat digunakan bisa menggunakan perintah `python add_csv.py --help`

5. Lakukan *pull request* sehingga hasil stopwords akan ditambahkan kedalam final stopwords


# Task List
- [ ] *Support* csv dan format lain sebagai format file untuk menambahkan stopwords
- [ ] Penghitung Stopwords otomatis di README.md
- [ ] Pembaruan otomatis pada *Terakhir diperbarui* pada README.md

