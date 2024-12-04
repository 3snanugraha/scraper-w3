# W3Schools HTML Scraper

Scraper sederhana untuk mengambil tutorial HTML dari W3Schools dan mengkonversinya ke format Markdown.

## Fitur

- Mengambil konten tutorial HTML dari W3Schools secara otomatis
- Mengkonversi konten HTML ke format Markdown
- Menyimpan hasil scraping dalam file Markdown terpisah
- Mendukung elemen-elemen HTML seperti heading, paragraf, list, dan code blocks
- Membersihkan format teks secara otomatis

## Cara Penggunaan

1. Pastikan Python sudah terinstall di sistem anda
2. Install dependencies yang dibutuhkan:
```bash
pip install beautifulsoup4
```
3. Jalankan script dengan perintah:
```bash
python scrape.py
```
## Konfigurasi

Terdapat 3 variabel utama yang bisa disesuaikan:
- `b_url`: URL dasar W3Schools (default: 'https://www.w3schools.com/html/')
- `n_url`: Halaman awal scraping (default: 'html_intro.asp')
- `s_url`: Halaman akhir scraping (default: 'html_exam.asp')

## Struktur Output

- Hasil scraping akan disimpan dalam folder `data/`
- Format penamaan file: `[nomor]_[judul_halaman].md`
- Setiap file berisi konten dalam format Markdown

## Fungsi Utama

1. `clean_text()`: Membersihkan format teks
2. `html_to_markdown()`: Mengkonversi elemen HTML ke format Markdown
3. `start()`: Fungsi utama untuk melakukan scraping dan menyimpan hasil

## Elemen yang Didukung

- Heading (H1, H2, H3)
- Paragraf
- Unordered list
- Code blocks
- Example blocks dari W3Schools

## Catatan

- Script akan membuat folder `data/` secara otomatis jika belum ada
- Proses scraping berjalan secara rekursif dari halaman awal hingga halaman akhir
- Setiap halaman yang berhasil di-scrape akan ditampilkan progressnya di console
