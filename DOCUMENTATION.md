# Dokumentasi Lengkap Bahasa EASY

_**DISCLAIMER, DOKUMENTASI INI DIBUAT OLEH AI (CLAUDE SONNET 4.5), DAN MUNGKIN TIDAK AKURAT DENGAN CARA KERJA BAHASA PEMROGRAMAN EASY. LANJUTKAN DENGAN WASPADA.**_

## Daftar Isi
1. [Pengenalan](#pengenalan)
2. [Instalasi](#instalasi)
3. [Memulai dengan EASY](#memulai-dengan-easy)
4. [Sintaks Dasar](#sintaks-dasar)
5. [Tipe Data](#tipe-data)
6. [Variabel](#variabel)
7. [Operator](#operator)
8. [Struktur Kontrol](#struktur-kontrol)
9. [Perulangan](#perulangan)
10. [Fungsi](#fungsi)
11. [List (Daftar)](#list-daftar)
12. [Fungsi Bawaan](#fungsi-bawaan)
13. [Input dan Output](#input-dan-output)
14. [Komentar](#komentar)
15. [Contoh Program](#contoh-program)
16. [Tips dan Trik](#tips-dan-trik)
17. [Troubleshooting](#troubleshooting)
18. [FAQ](#faq)

---

## Pengenalan

### Apa itu EASY?

EASY merupakan bahasa program yang dirancang untuk pemula. Dengan sintaks yang jelas dan mudah dipahami, pemula yang bisa membaca bahasa Inggris akan mudah belajar bahasa EASY. Bahasa ini menggunakan kata-kata yang mirip dengan bahasa Inggris sehari-hari, membuat programming lebih mudah dipahami.

### Mengapa EASY?

Ada beberapa alasan mengapa kamu harus menggunakan EASY:

- **Mudah dipahami**: Sintaks yang mirip dengan bahasa Inggris sehari-hari
- **Ramah pemula**: Dirancang untuk yang baru ingin belajar programming
- **Cepat dipelajari**: Anda dapat membuat program EASY dalam hitungan menit
- **Ekspresif**: Banyak cara untuk menulis kode yang sama (misal: `plus` atau `+`)
- **Interaktif**: Tersedia shell interaktif untuk eksperimen

### Filosofi EASY

_"Belajar programming itu sulit, dan saat sudah bisa akan terasa hebat. EASY memudahkan proses kamu belajar."_

EASY percaya bahwa:
- Kode harus mudah dibaca seperti kalimat biasa
- Pemula tidak perlu terbebani dengan sintaks yang rumit
- Belajar konsep programming lebih penting daripada menghafal sintaks

### Siapa yang Cocok Menggunakan EASY?

Dikarenakan EASY adalah bahasa berbasis Python (lambat), maka EASY hanya untuk penggunaan edukasional. Fitur-fitur dari EASY juga terbatas, jadi hanya pemula atau siswa yang ingin belajar pemrograman bisa mulai di EASY.

**EASY cocok untuk:**
- Siswa sekolah yang baru belajar programming
- Pemula yang ingin memahami konsep dasar programming
- Guru yang mengajar pengenalan programming
- Prototyping ide sederhana

**EASY tidak cocok untuk:**
- Aplikasi produksi
- Program yang membutuhkan performa tinggi
- Proyek berskala besar

---

## Instalasi

### Persyaratan Sistem

#### Windows
- Windows 10 atau lebih baru (untuk memastikan stabilitas)
- Python 3.6 atau lebih tinggi
- 50 MB ruang kosong

#### Linux
- Python 3.6 atau lebih tinggi
- 50 MB ruang kosong
- Bash shell (untuk installer)

### Cara Instalasi

Cara instalasi lengkap bisa dilihat di [INSTALLATION.MD](https://github.com/tyydev1/easy-language/blob/main/INSTALLATION.md)

**Ringkasan instalasi Linux:**
```bash
wget https://github.com/tyydev1/easy-language/releases/latest/download/easy-lang-1.0.0-linux.tar.gz
tar -xzf easy-lang-linux.tar.gz
cd easy-lang-*-linux
./install.sh
source ~/.bashrc
```

**Ringkasan instalasi Windows:**
1. Download `easy-lang-windows.zip`
2. Extract file ZIP
3. Jalankan `install.ps1` dengan PowerShell
4. Restart Command Prompt

### Verifikasi Instalasi

Setelah instalasi, coba jalankan:
```bash
easy --help
```

Atau buka shell interaktif:
```bash
easy-shell
```

---

## Memulai dengan EASY

### Program Pertama Anda

Mari membuat program pertama!

#### Membuat File .esy

1. Buka folder manapun di komputer Anda
2. Buat file baru dengan nama `hello.esy` atau `hello.ez`
3. Buka file tersebut dengan teks editor favorit Anda (Notepad, VS Code, Sublime, dll)

#### Menulis Kode Pertama

Ketik kode berikut di file `hello.esy`:

```esy
say("Hello, World!")
```

Simpan file tersebut.

#### Menjalankan Program

Buka terminal/command prompt di folder tempat file `hello.esy` berada, lalu jalankan:

```bash
easy hello.esy
```

Anda akan melihat output:
```
Hello, World!
```

Selamat! Anda baru saja menjalankan program EASY pertama Anda!

### Menggunakan EASY Shell

EASY Shell adalah mode interaktif di mana Anda bisa mengetik kode dan langsung melihat hasilnya.

#### Membuka Shell

Ketik di terminal:
```bash
easy-shell
```

Anda akan melihat:
```
    _________   _______  __
   / ____/   | / ___/\ \/ /
  / __/ / /| | \__ \  \  / 
 / /___/ ___ |___/ /  / /  
/_____/_/  |_/____/  /_/   

Easy 1.0.0 Universal Version - Initial release
Welcome to Easy! This is the first published version of the Easy language.
>>> 
```

#### Mode Interaktif

Sekarang Anda bisa mengetik kode langsung:

```esy
>>> say("Hello from shell!")
Hello from shell!
>>> set x to 5
>>> say(x times 2)
10
>>> 
```

#### Keluar dari Shell

Untuk keluar dari shell, ketik:
```esy
>>> quit
```

Atau tekan `Ctrl+C` dua kali.

### Struktur Program EASY

Program EASY terdiri dari **statements** (pernyataan) yang dipisahkan oleh:
- **Baris baru** (new line)
- **Titik** (`.`)

Contoh:
```esy
?> Menggunakan baris baru
say("Baris pertama")
say("Baris kedua")

?> Menggunakan titik
say("Baris pertama"). say("Baris kedua")
```

Kedua contoh di atas menghasilkan output yang sama.

---

## Sintaks Dasar

### Aturan Penulisan

1. **Statement dipisahkan oleh newline atau titik**
   ```esy
   say("Halo")
   say("Dunia")
   ```
   
   Atau:
   ```esy
   say("Halo"). say("Dunia")
   ```

2. **Tidak ada semicolon (`;`) di akhir statement**
   ```esy
   say("Benar")    ?> ✓ Benar
   say("Salah");   ?> ✗ Error!
   ```

3. **Whitespace (spasi, tab) diabaikan**
   ```esy
   say("Hello")           ?> Valid
   say    (   "Hello"  )  ?> Valid, tapi tidak disarankan
   ```

### Case Sensitivity

EASY adalah **case-sensitive**, artinya huruf besar dan kecil dibedakan:

```esy
set nama to "Razka"    ?> ✓ Benar
say(nama)              ?> ✓ Benar

say(Nama)              ?> ✗ Error! 'Nama' tidak sama dengan 'nama'
say(NAMA)              ?> ✗ Error!
```

**Keyword** juga case-sensitive:
```esy
if x is 5 then say(x)    ?> ✓ Benar
If x is 5 then say(x)    ?> ✗ Error! 'If' bukan keyword
IF x is 5 THEN say(x)    ?> ✗ Error!
```

### Whitespace dan Indentasi

EASY **tidak mengharuskan** indentasi seperti Python, namun indentasi disarankan untuk keterbacaan:

```esy
?> Tanpa indentasi (valid tapi susah dibaca)
if x is 5 then
say("Lima")
otherwise
say("Bukan lima")
end

?> Dengan indentasi (lebih baik!)
if x is 5 then
    say("Lima")
otherwise
    say("Bukan lima")
end
```

### Titik sebagai Pemisah Statement

Titik (`.`) bisa digunakan untuk menulis beberapa statement dalam satu baris:

```esy
set x to 1. set y to 2. say(x plus y)
```

Sama dengan:
```esy
set x to 1
set y to 2
say(x plus y)
```

### Karakter yang Diperbolehkan

- **Nama variabel dan fungsi**: huruf (a-z, A-Z), angka (0-9), underscore (`_`)
- **Harus dimulai dengan huruf atau underscore**
- **Tidak boleh dimulai dengan angka**

Contoh valid:
```esy
set nama to "Razka"
set nama_lengkap to "Razka Gymastiar"
set umur_2024 to 20
set _private to "secret"
```

Contoh tidak valid:
```esy
set 2nama to "Error"        ?> ✗ Dimulai dengan angka
set nama-lengkap to "Error" ?> ✗ Karakter '-' tidak diperbolehkan
set for to "Error"          ?> ✗ 'for' adalah keyword (reserved)
```

---

## Tipe Data

EASY memiliki 5 tipe data utama:

### Number (Angka)

#### Integer (Bilangan Bulat)

Bilangan bulat tanpa titik desimal:

```esy
set x to 42
set y to -10
set z to 0
say(x)  ?> Output: 42
```

#### Float (Bilangan Desimal)

Bilangan dengan titik desimal:

```esy
set pi to 3.14159
set suhu to -5.5
set nol to 0.0
say(pi)  ?> Output: 3.14159
```

#### Operasi Matematika Dasar

```esy
set a to 10
set b to 3

say(a plus b)   ?> 13
say(a minus b)  ?> 7
say(a times b)  ?> 30
say(a div b)    ?> 3.333...
say(a pow b)    ?> 1000
```

### Text (Teks/String)

#### Membuat Text

Text ditulis dengan tanda kutip ganda (`"`):

```esy
set pesan to "Hello, World!"
set nama to "Razka"
set kosong to ""
```

**Catatan**: EASY hanya mendukung kutip ganda, **tidak ada kutip tunggal** (`'`).

#### Escape Characters

Untuk karakter khusus, gunakan backslash (`\`):

- `\n` - Baris baru (newline)
- `\t` - Tab

```esy
say("Baris 1\nBaris 2")
?> Output:
?> Baris 1
?> Baris 2

say("Nama:\tRazka")
?> Output: Nama:    Razka
```

#### Menggabungkan Text

Gunakan `plus` atau `+`:

```esy
set nama to "Razka"
set salam to "Hello, " plus nama plus "!"
say(salam)  ?> Hello, Razka!
```

Menggabungkan text dengan angka:
```esy
set umur to 20
say("Umur saya " plus umur plus " tahun")
?> Output: Umur saya 20 tahun
```

### List (Daftar)

#### Membuat List

List dibuat dengan kurung siku (`[]`) dan dipisah dengan koma:

```esy
set angka to [1, 2, 3, 4, 5]
set nama to ["Razka", "Budi", "Ani"]
set campur to [1, "dua", 3.0, [4, 5]]
set kosong to []
```

#### Mengakses Element List

Gunakan operator `/` atau `div` dengan index (dimulai dari 0):

```esy
set buah to ["apel", "jeruk", "mangga"]

say(buah / 0)    ?> apel
say(buah div 1)  ?> jeruk
say(buah / 2)    ?> mangga
```

**Catatan**: Index dimulai dari 0, bukan 1!

#### List Kosong

```esy
set daftar to []
say(lengthOf(daftar))  ?> 0
```

### Boolean (State)

EASY menggunakan angka untuk boolean:

#### true

Nilai `true` direpresentasikan dengan angka 1:

```esy
set benar to true
if benar then say("Ini benar!")
```

#### false

Nilai `false` direpresentasikan dengan angka 0:

```esy
set salah to false
if salah then say("Tidak akan tercetak")
```

#### Konversi ke Boolean

Aturan konversi:
- **Number**: 0 = false, selain 0 = true
- **Text**: string kosong = false, ada isi = true
- **List**: list kosong = false, ada element = true

```esy
if 0 then say("false")      ?> Tidak tercetak
if 1 then say("true")       ?> Tercetak
if 42 then say("true")      ?> Tercetak

if "" then say("false")     ?> Tidak tercetak
if "hello" then say("true") ?> Tercetak

if [] then say("false")     ?> Tidak tercetak
if [1] then say("true")     ?> Tercetak
```

### null

`null` merepresentasikan "tidak ada nilai":

```esy
set x to null
say(x)  ?> null

if null then say("false")  ?> Tidak tercetak
```

Fungsi yang tidak mengembalikan nilai akan return `null`:

```esy
make fungsi()
    say("Hello")
end

set hasil to fungsi()
say(hasil)  ?> null
```

---

## Variabel

### Mendeklarasikan Variabel

Ada 3 cara untuk membuat variabel di EASY:

#### Menggunakan `set`

Cara paling umum dan direkomendasikan:

```esy
set nama to "Razka"
set umur to 20
set hobi to ["coding", "gaming"]
```

#### Menggunakan `to`

Sama seperti `set ... to`:

```esy
set x to 10        ?> Sama dengan
set x = 10         ?> cara ini
```

#### Menggunakan `=`

Cara singkat:

```esy
set x = 5
set y = 10
set z = x plus y
```

**Catatan**: Ketiga cara di atas setara, gunakan yang paling nyaman untuk Anda.

### Aturan Penamaan Variabel

1. **Harus dimulai dengan huruf atau underscore**
   ```esy
   set nama to "OK"       ?> ✓
   set _private to "OK"   ?> ✓
   set 123abc to "Error"  ?> ✗
   ```

2. **Hanya boleh berisi huruf, angka, dan underscore**
   ```esy
   set nama_lengkap to "OK"    ?> ✓
   set umur2024 to "OK"        ?> ✓
   set nama-lengkap to "Error" ?> ✗
   ```

3. **Case-sensitive**
   ```esy
   set nama to "Razka"
   set Nama to "Budi"    ?> Variabel berbeda!
   ```

4. **Tidak boleh menggunakan keyword**
   ```esy
   set if to 5       ?> ✗ 'if' adalah keyword
   set repeat to 10  ?> ✗ 'repeat' adalah keyword
   set my_if to 5    ?> ✓ OK
   ```

**Keyword yang tidak boleh digunakan sebagai nama variabel:**
`set`, `to`, `plus`, `minus`, `times`, `div`, `pow`, `add`, `remove`, `merge`, `get`, `and`, `or`, `not`, `if`, `then`, `nextif`, `otherwise`, `is`, `isnt`, `under`, `above`, `atmost`, `atleast`, `repeat`, `from`, `through`, `by`, `while`, `do`, `give`, `stop`, `next`, `make`, `end`

### Mengubah Nilai Variabel

Variabel bisa diubah nilainya kapan saja:

```esy
set x to 5
say(x)       ?> 5

set x to 10
say(x)       ?> 10

set x = x plus 1
say(x)       ?> 11
```

### Menggunakan Variabel

Variabel bisa digunakan di mana saja expression dibutuhkan:

```esy
set x to 10
set y to 20

?> Dalam operasi aritmatika
say(x plus y)              ?> 30

?> Dalam kondisi
if x under y then say("x lebih kecil")

?> Dalam list
set list to [x, y, x plus y]
say(list)                  ?> [10, 20, 30]

?> Sebagai argumen fungsi
say(x)
```

---

## Operator

### Operator Aritmatika

#### `plus` / `+`

Penjumlahan untuk angka, penggabungan untuk text:

```esy
say(5 plus 3)           ?> 8
say(5 + 3)              ?> 8

say("Hello" plus " " plus "World")  ?> Hello World
say("Hello" + " " + "World")        ?> Hello World
```

**Catatan**: Untuk list, gunakan `add`, bukan `plus`!

#### `minus` / `-`

Pengurangan:

```esy
say(10 minus 3)    ?> 7
say(10 - 3)        ?> 7

say(5 minus 10)    ?> -5
```

#### `times` / `*`

Perkalian:

```esy
say(5 times 3)     ?> 15
say(5 * 3)         ?> 15

?> Text bisa dikali dengan angka
say("Ha" times 3)  ?> HaHaHa
say("Ho" * 5)      ?> HoHoHoHoHo
```

#### `div` / `/`

Pembagian:

```esy
say(10 div 2)      ?> 5.0
say(10 / 2)        ?> 5.0

say(10 div 3)      ?> 3.333...

?> Error jika dibagi nol
say(5 div 0)       ?> Runtime Error: Division by zero
```

#### `pow` / `^`

Pangkat (eksponensial):

```esy
say(2 pow 3)       ?> 8
say(2 ^ 3)         ?> 8

say(10 pow 2)      ?> 100
say(2 ^ 10)        ?> 1024
```

### Operator Perbandingan

Operator perbandingan mengembalikan `true` (1) atau `false` (0).

#### `is` / `==`

Sama dengan:

```esy
say(5 is 5)        ?> 1 (true)
say(5 == 5)        ?> 1 (true)
say(5 is 3)        ?> 0 (false)

say("hello" is "hello")  ?> 1 (true)
say("hello" is "Hello")  ?> 0 (false)
```

#### `isnt` / `!=`

Tidak sama dengan:

```esy
say(5 isnt 3)      ?> 1 (true)
say(5 != 3)        ?> 1 (true)
say(5 isnt 5)      ?> 0 (false)
```

#### `under` / `<`

Lebih kecil dari:

```esy
say(3 under 5)     ?> 1 (true)
say(3 < 5)         ?> 1 (true)
say(5 under 3)     ?> 0 (false)
```

#### `above` / `>`

Lebih besar dari:

```esy
say(5 above 3)     ?> 1 (true)
say(5 > 3)         ?> 1 (true)
say(3 above 5)     ?> 0 (false)
```

#### `atmost` / `<=`

Lebih kecil atau sama dengan:

```esy
say(3 atmost 5)    ?> 1 (true)
say(5 atmost 5)    ?> 1 (true)
say(5 <= 3)        ?> 0 (false)
```

#### `atleast` / `>=`

Lebih besar atau sama dengan:

```esy
say(5 atleast 3)   ?> 1 (true)
say(5 atleast 5)   ?> 1 (true)
say(3 >= 5)        ?> 0 (false)
```

### Operator Logika

#### `and`

Logika AND (kedua kondisi harus benar):

```esy
say(true and true)      ?> 1 (true)
say(true and false)     ?> 0 (false)
say(false and false)    ?> 0 (false)

set x to 10
if x above 5 and x under 15 then
    say("x antara 5 dan 15")
end
```

#### `or`

Logika OR (salah satu kondisi benar):

```esy
say(true or false)      ?> 1 (true)
say(false or false)     ?> 0 (false)

set x to 20
if x is 10 or x is 20 then
    say("x adalah 10 atau 20")
end
```

#### `not`

Logika NOT (membalik nilai boolean):

```esy
say(not true)          ?> 0 (false)
say(not false)         ?> 1 (true)

set x to 5
if not (x is 10) then
    say("x bukan 10")
end
```

### Operator List

#### `add`

Menambahkan element ke list:

```esy
set list to [1, 2, 3]
say(list add 4)        ?> [1, 2, 3, 4]

?> Gunakan 'add', bukan 'plus' untuk list
say(list + 5)          ?> [1, 2, 3, 4, 5]
```

**Catatan**: `add` dan `+` sama untuk list, tetapi lebih jelas menggunakan `add` untuk list dan `plus` untuk angka.

#### `remove`

Menghapus element dari list berdasarkan index:

```esy
set list to [10, 20, 30, 40]
say(list remove 1)     ?> [10, 30, 40] (menghapus index 1)

?> Sama dengan operator '-'
say(list - 0)          ?> [20, 30, 40] (menghapus index 0)
```

#### `merge`

Menggabungkan dua list:

```esy
set list1 to [1, 2]
set list2 to [3, 4]
say(list1 merge list2)  ?> [1, 2, 3, 4]

?> Sama dengan operator '*'
say(list1 * list2)      ?> [1, 2, 3, 4]
```

#### `get`

Mengambil element dari list:

```esy
set buah to ["apel", "jeruk", "mangga"]
say(buah get 0)         ?> apel
say(buah get 1)         ?> jeruk

?> Sama dengan operator '/'
say(buah / 2)           ?> mangga
```

---

## Struktur Kontrol

### If (Kondisi)

#### Sintaks Dasar `if`

```esy
if kondisi then pernyataan
```

Contoh:
```esy
set x to 10
if x above 5 then say("x lebih besar dari 5")
```

#### `if` dengan `then`

Keyword `then` wajib digunakan:

```esy
if x is 10 then say("x adalah 10")

?> Error tanpa 'then'
if x is 10 say("Error!")  ?> ✗ Expected 'then'
```

#### Multi-line `if`

Untuk beberapa pernyataan, gunakan blok dengan `end`:

```esy
set x to 10

if x above 5 then
    say("x lebih besar dari 5")
    say("Nilai x adalah " plus x)
    say("Selesai")
end
```

### Else If (Kondisi Tambahan)

#### `nextif`

Untuk kondisi alternatif, gunakan `nextif` (seperti `elif` atau `else if`):

```esy
set nilai to 85

if nilai atleast 90 then
    say("Grade: A")
nextif nilai atleast 80 then
    say("Grade: B")
nextif nilai atleast 70 then
    say("Grade: C")
end
```

#### Beberapa `nextif`

Anda bisa menggunakan `nextif` sebanyak yang diperlukan:

```esy
set angka to 15

if angka under 10 then
    say("Kurang dari 10")
nextif angka is 10 then
    say("Sama dengan 10")
nextif angka under 20 then
    say("Antara 10 dan 20")
nextif angka under 30 then
    say("Antara 20 dan 30")
end
```

### Else (Kondisi Default)

#### `otherwise`

Untuk kondisi default ketika semua kondisi lain salah:

```esy
set x to 7

if x is 5 then
    say("Lima")
nextif x is 10 then
    say("Sepuluh")
otherwise
    say("Bukan 5 atau 10")
end
?> Output: Bukan 5 atau 10
```

#### Multi-line `otherwise`

```esy
set angka to 100

if angka under 10 then
    say("Satu digit")
nextif angka under 100 then
    say("Dua digit")
otherwise
    say("Tiga digit atau lebih")
    say("Angka: " plus angka)
end
```

### Nested Conditionals (If Bersarang)

If bisa ditulis di dalam if lain:

```esy
set umur to 20
set punya_sim to true

if umur atleast 17 then
    if punya_sim then
        say("Boleh menyetir")
    otherwise
        say("Umur cukup, tapi belum punya SIM")
    end
otherwise
    say("Umur belum cukup")
end
```

**Contoh lengkap:**

```esy
set nilai to 75
set kehadiran to 80

if nilai atleast 60 then
    if kehadiran atleast 75 then
        say("LULUS")
    otherwise
        say("Nilai cukup, tapi kehadiran kurang")
    end
otherwise
    say("TIDAK LULUS - Nilai kurang")
end
```

---

## Perulangan

### Repeat (For Loop)

Loop `repeat` digunakan untuk mengulang dengan jumlah iterasi yang pasti.

#### Sintaks Dasar

```esy
repeat variabel from awal through akhir do pernyataan
```

Contoh:
```esy
repeat i from 1 through 5 do say(i)
?> Output:
?> 1
?> 2
?> 3
?> 4
?> 5
```

#### `repeat` dengan `from`

`from` menentukan nilai awal. Bisa juga gunakan `=`:

```esy
repeat i from 1 through 3 do say(i)
repeat i = 1 through 3 do say(i)  ?> Sama saja
```

#### `repeat` dengan `through`

`through` menentukan nilai akhir (inklusif):

```esy
repeat i from 0 through 4 do say(i)
?> 0, 1, 2, 3, 4
```

#### `repeat` dengan `by` (Step)

`by` menentukan langkah perulangan:

```esy
?> Naik 2
repeat i from 0 through 10 by 2 do
    say(i)
end
?> Output: 0, 2, 4, 6, 8, 10

?> Turun 1
repeat i from 5 through 1 by -1 do
    say(i)
end
?> Output: 5, 4, 3, 2, 1
```

#### `repeat` dengan `do`

Keyword `do` wajib digunakan (pengganti `then` pada `if`):

```esy
repeat i from 1 through 3 do say(i)

?> Error tanpa 'do'
repeat i from 1 through 3 say(i)  ?> ✗ Expected 'do'
```

#### Multi-line Repeat

```esy
repeat i from 1 through 5 do
    say("Iterasi ke-" plus i)
    set kuadrat to i times i
    say("Kuadratnya: " plus kuadrat)
end
```

#### Nested Repeat

Loop di dalam loop:

```esy
repeat i from 1 through 3 do
    repeat j from 1 through 3 do
        say("i=" plus i plus ", j=" plus j)
    end
end

?> Output:
?> i=1, j=1
?> i=1, j=2
?> i=1, j=3
?> i=2, j=1
?> ...
```

**Contoh: Tabel perkalian**

```esy
repeat i from 1 through 5 do
    repeat j from 1 through 5 do
        say(i plus " x " plus j plus " = " plus (i times j))
    end
    say("")
end
```

### While Loop

Loop `while` mengulang selama kondisi bernilai true.

#### Sintaks Dasar

```esy
while kondisi then pernyataan
```

Contoh:
```esy
set x to 1
while x atmost 5 then
    say(x)
    set x = x plus 1
end
?> Output: 1, 2, 3, 4, 5
```

#### `while` dengan `then`

Keyword `then` wajib digunakan:

```esy
set x to 0
while x under 3 then say(x). set x = x plus 1
```

#### Multi-line While

```esy
set counter to 0

while counter under 5 then
    say("Counter: " plus counter)
    set counter = counter plus 1
    say("Setelah increment: " plus counter)
end
```

#### Infinite Loop

**Hati-hati!** Loop yang tidak pernah berhenti:

```esy
?> JANGAN JALANKAN INI!
while true then
    say("Loop forever!")
end
```

Untuk memberhentikan infinite loop, tekan `Ctrl+C`.

**Loop dengan kondisi exit:**

```esy
set x to 0
while true then
    say(x)
    set x = x plus 1
    if x above 5 then stop
end
```

### Loop Control

#### `next` (Continue)

Melanjutkan ke iterasi berikutnya:

```esy
repeat i from 1 through 5 do
    if i is 3 then next
    say(i)
end
?> Output: 1, 2, 4, 5 (3 dilewati)
```

**Contoh: Hanya cetak angka genap**

```esy
repeat i from 1 through 10 do
    if i div 2 times 2 isnt i then next  ?> Skip ganjil
    say(i)
end
?> Output: 2, 4, 6, 8, 10
```

#### `stop` (Break)

Menghentikan loop sepenuhnya:

```esy
repeat i from 1 through 10 do
    if i above 5 then stop
    say(i)
end
?> Output: 1, 2, 3, 4, 5
```

**Contoh: Cari angka pertama > 50**

```esy
set daftar to [10, 20, 30, 60, 70, 80]
set found to null

repeat i from 0 through (lengthOf(daftar) minus 1) do
    set angka to daftar / i
    if angka above 50 then
        set found to angka
        stop
    end
end

say("Angka pertama > 50: " plus found)
?> Output: Angka pertama > 50: 60
```

---

## Fungsi

### Membuat Fungsi

#### `make` Keyword

Fungsi dibuat dengan keyword `make`:

```esy
make namaFungsi()
    ?> kode fungsi
end
```

#### Fungsi dengan Nama

```esy
make sapa()
    say("Hello!")
end

sapa()  ?> Memanggil fungsi
?> Output: Hello!
```

#### Fungsi Tanpa Nama (Anonymous)

Fungsi anonymous bisa disimpan di variabel:

```esy
set fungsiSaya to make()
    say("Fungsi anonymous")
end

fungsiSaya()
?> Output: Fungsi anonymous
```

### Parameter Fungsi

#### Satu Parameter

```esy
make sapa(nama)
    say("Hello, " plus nama plus "!")
end

sapa("Razka")
?> Output: Hello, Razka!
```

#### Beberapa Parameter

Pisahkan parameter dengan koma:

```esy
make tambah(a, b)
    give a plus b
end

set hasil to tambah(5, 3)
say(hasil)  ?> 8
```

#### Tanpa Parameter

Gunakan kurung kosong:

```esy
make sayHello()
    say("Hello, World!")
end

sayHello()
```

### Return Value

#### `give` Keyword

Gunakan `give` untuk mengembalikan nilai (seperti `return`):

```esy
make kali(a, b)
    give a times b
end

set hasil to kali(4, 5)
say(hasil)  ?> 20
```

**Multiple return:**

```esy
make cekAngka(x)
    if x above 0 then give "Positif"
    if x under 0 then give "Negatif"
    give "Nol"
end

say(cekAngka(5))   ?> Positif
say(cekAngka(-3))  ?> Negatif
say(cekAngka(0))   ?> Nol
```

#### Auto-return dengan Arrow (`->`)

Untuk fungsi satu baris, gunakan arrow:

```esy
make kuadrat(x) -> x times x

say(kuadrat(5))  ?> 25
say(kuadrat(3))  ?> 9
```

Lebih ringkas daripada:

```esy
make kuadrat(x)
    give x times x
end
```

**Contoh lain:**

```esy
make max(a, b) -> if a above b then a otherwise b

say(max(10, 5))  ?> 10
say(max(3, 7))   ?> 7
```

### Memanggil Fungsi

#### Dengan Argumen

```esy
make tambah(a, b)
    give a plus b
end

say(tambah(10, 20))       ?> 30
say(tambah(5, 7))         ?> 12

set x to 3
set y to 4
say(tambah(x, y))         ?> 7
```

#### Tanpa Argumen

```esy
make getPI()
    give 3.14159
end

set pi to getPI()
say(pi)  ?> 3.14159
```

### Nested Functions

Fungsi di dalam fungsi:

```esy
make luar()
    say("Fungsi luar")
    
    make dalam()
        say("Fungsi dalam")
    end
    
    dalam()
end

luar()
?> Output:
?> Fungsi luar
?> Fungsi dalam
```

**Contoh closure:**

```esy
make buatPenambah(x)
    make tambahkan(y) -> x plus y
    give tambahkan
end

set tambah5 to buatPenambah(5)
say(tambah5(3))  ?> 8
say(tambah5(10)) ?> 15
```

---

## List (Daftar)

### Membuat List

List dibuat dengan kurung siku `[]`:

```esy
set angka to [1, 2, 3, 4, 5]
set nama to ["Alice", "Bob", "Charlie"]
set campur to [1, "dua", 3.0, true]
set kosong to []
```

### Mengakses Element

#### Indexing

Gunakan operator `/` atau `get`. Index dimulai dari **0**:

```esy
set buah to ["apel", "jeruk", "mangga", "pisang"]

say(buah / 0)      ?> apel
say(buah get 1)    ?> jeruk
say(buah / 2)      ?> mangga
say(buah get 3)    ?> pisang
```

#### Index Negatif (Jika Didukung)

EASY saat ini **tidak mendukung** index negatif seperti Python.

```esy
set list to [1, 2, 3]
say(list / -1)     ?> Error: Index out of bounds
```

### Menambah Element

#### Menggunakan `add`

```esy
set angka to [1, 2, 3]
set angka = angka add 4
say(angka)  ?> [1, 2, 3, 4]
```

#### Menggunakan `+`

Sama dengan `add`:

```esy
set list to [10, 20]
set list = list + 30
say(list)  ?> [10, 20, 30]
```

**Catatan**: Operator ini menambahkan di akhir list.

### Menghapus Element

#### Menggunakan `remove`

Hapus berdasarkan index:

```esy
set list to ["a", "b", "c", "d"]
set list = list remove 1
say(list)  ?> ["a", "c", "d"]
```

#### Menggunakan `-`

```esy
set angka to [10, 20, 30, 40]
set angka = angka - 0  ?> Hapus index 0
say(angka)  ?> [20, 30, 40]
```

### Menggabungkan List

#### Menggunakan `merge`

```esy
set list1 to [1, 2, 3]
set list2 to [4, 5, 6]
set gabungan to list1 merge list2
say(gabungan)  ?> [1, 2, 3, 4, 5, 6]
```

#### Menggunakan `*`

```esy
set a to ["x", "y"]
set b to ["z"]
say(a * b)  ?> ["x", "y", "z"]
```

### Operasi List Lainnya

**Length:**

```esy
set list to [1, 2, 3, 4, 5]
say(lengthOf(list))  ?> 5
```

**Append (fungsi built-in):**

```esy
set list to [1, 2]
append(list, 3)
say(list)  ?> [1, 2, 3]
```

**Pop (hapus dan return):**

```esy
set list to [10, 20, 30]
set element to pop(list, 1)
say(element)  ?> 20
say(list)     ?> [10, 30]
```

**Extend:**

```esy
set list1 to [1, 2]
set list2 to [3, 4]
extend(list1, list2)
say(list1)  ?> [1, 2, 3, 4]
```

**Iterasi:**

```esy
set buah to ["apel", "jeruk", "mangga"]
repeat i from 0 through (lengthOf(buah) minus 1) do
    say(buah / i)
end
```

---

## Fungsi Bawaan

### Input/Output

#### `say()`

Mencetak nilai ke layar:

```esy
say("Hello, World!")
say(42)
say([1, 2, 3])

set x to 10
say(x)
```

#### `saySave()`

Mengubah nilai menjadi text dan mengembalikannya:

```esy
set text to saySave(42)
say(text)  ?> "42"
say(typeOf(text))  ?> Text
```

#### `ask()`

Meminta input text dari user:

```esy
say("Siapa namamu?")
set nama to ask()
say("Hello, " plus nama plus "!")
```

#### `askNumber()`

Meminta input angka dari user. Akan terus meminta sampai user memasukkan angka yang valid:

```esy
say("Masukkan angka:")
set angka to askNumber()
say("Angka kamu: " plus angka)
```

### Utility

#### `clean()` / `clear()` / `cls()`

Membersihkan layar terminal:

```esy
clean()   ?> Membersihkan layar
clear()   ?> Sama saja
cls()     ?> Sama saja
```

#### `run()`

Menjalankan file EASY lain:

```esy
?> Jalankan file "program.esy"
run("program")

?> Atau dengan ekstensi
run("program.esy")
```

**File program.esy:**
```esy
say("Program eksternal dijalankan!")
```

### Type Checking

#### `isNumber()`

Mengecek apakah nilai adalah Number:

```esy
say(isNumber(42))       ?> 1 (true)
say(isNumber("text"))   ?> 0 (false)
say(isNumber([1, 2]))   ?> 0 (false)
```

#### `isText()`

Mengecek apakah nilai adalah Text:

```esy
say(isText("hello"))    ?> 1 (true)
say(isText(42))         ?> 0 (false)
```

#### `isList()`

Mengecek apakah nilai adalah List:

```esy
say(isList([1, 2, 3]))  ?> 1 (true)
say(isList(42))         ?> 0 (false)
```

#### `isFunction()`

Mengecek apakah nilai adalah Function:

```esy
make testFunc()
    give 0
end

say(isFunction(testFunc))  ?> 1 (true)
say(isFunction(42))        ?> 0 (false)
```

#### `typeOf()`

Mengembalikan tipe data sebagai text:

```esy
say(typeOf(42))          ?> "Number"
say(typeOf("text"))      ?> "Text"
say(typeOf([1, 2]))      ?> "List"
say(typeOf(testFunc))    ?> "Function"
say(typeOf(null))        ?> "null"
```

### Type Conversion

#### `toNumber()` / `toNum()`

Mengubah nilai menjadi Number:

```esy
say(toNumber("42"))      ?> 42
say(toNum("3.14"))       ?> 3.14

?> Error jika tidak bisa dikonversi
say(toNumber("abc"))     ?> Runtime Error
```

#### `toText()`

Mengubah nilai menjadi Text:

```esy
say(toText(42))          ?> "42"
say(toText(true))        ?> "true"
say(toText(false))       ?> "false"
say(toText([1, 2, 3]))   ?> "[1, 2, 3]"
```

#### `toList()`

Mengubah nilai menjadi List (membungkus dalam list):

```esy
say(toList(42))          ?> [42]
say(toList("hello"))     ?> ["hello"]

set list to [1, 2]
say(toList(list))        ?> [1, 2] (copy)
```

#### `toState()`

Mengubah nilai menjadi Boolean (0 atau 1):

```esy
say(toState(42))         ?> 1 (true)
say(toState(0))          ?> 0 (false)
say(toState("hello"))    ?> 1 (true)
say(toState(""))         ?> 0 (false)
say(toState([1]))        ?> 1 (true)
say(toState([]))         ?> 0 (false)
```

### List Operations

#### `append()`

Menambahkan element ke list (memodifikasi list asli):

```esy
set list to [1, 2, 3]
append(list, 4)
say(list)  ?> [1, 2, 3, 4]
```

#### `pop()`

Menghapus dan mengembalikan element dari list:

```esy
set list to [10, 20, 30]
set element to pop(list, 1)
say(element)  ?> 20
say(list)     ?> [10, 30]
```

#### `extend()`

Menggabungkan dua list (memodifikasi list pertama):

```esy
set list1 to [1, 2]
set list2 to [3, 4]
extend(list1, list2)
say(list1)  ?> [1, 2, 3, 4]
say(list2)  ?> [3, 4] (tidak berubah)
```

#### `lengthOf()`

Mengembalikan panjang list:

```esy
set list to [1, 2, 3, 4, 5]
say(lengthOf(list))  ?> 5

set empty to []
say(lengthOf(empty))  ?> 0
```

### Special Values

#### `null`

Nilai "tidak ada":

```esy
set x to null
say(x)  ?> null
```

#### `true`

Boolean true (nilai 1):

```esy
set benar to true
if benar then say("True!")
```

#### `false`

Boolean false (nilai 0):

```esy
set salah to false
if salah then say("Tidak tercetak")
```

#### `quit` / `exit`

Keluar dari program atau shell:

```esy
quit
?> Program berhenti

exit
?> Sama saja
```

### Math Constants

#### `math_pi`

Nilai PI (π ≈ 3.14159):

```esy
say(math_pi)  ?> 3.141592653589793

set jari to 7
set luas to math_pi times (jari pow 2)
say("Luas lingkaran: " plus luas)
```

---

## Input dan Output

### Menampilkan Output

#### `say()` untuk Print

Fungsi paling dasar untuk output:

```esy
say("Hello, World!")
say(42)
say([1, 2, 3])

set x to 10
say("Nilai x: " plus x)
```

#### Format Output

Menggabungkan text dan variabel:

```esy
set nama to "Razka"
set umur to 20

say("Nama: " plus nama)
say("Umur: " plus umur plus " tahun")

?> Format lebih kompleks
set total to 100
set diskon to 10
set final to total minus diskon
say("Total: " plus total plus ", Diskon: " plus diskon plus ", Final: " plus final)
```

### Menerima Input

#### `ask()` untuk Text

Meminta input text dari user:

```esy
say("Siapa namamu?")
set nama to ask()
say("Hello, " plus nama plus "!")
```

**Contoh lengkap:**

```esy
say("Masukkan nama:")
set nama to ask()

say("Masukkan kota:")
set kota to ask()

say("Halo " plus nama plus " dari " plus kota plus "!")
```

#### `askNumber()` untuk Angka

Meminta input angka, terus bertanya sampai valid:

```esy
say("Masukkan umur:")
set umur to askNumber()

if umur atleast 17 then
    say("Boleh punya SIM")
otherwise
    say("Belum boleh punya SIM")
end
```

**Contoh kalkulator:**

```esy
say("Kalkulator Sederhana")
say("Masukkan angka pertama:")
set a to askNumber()

say("Masukkan angka kedua:")
set b to askNumber()

say("Hasil penjumlahan: " plus (a plus b))
say("Hasil perkalian: " plus (a times b))
```

#### Validasi Input

Memvalidasi input secara manual:

```esy
say("Masukkan angka 1-10:")
set angka to askNumber()

while angka under 1 or angka above 10 then
    say("Angka harus antara 1-10! Coba lagi:")
    set angka to askNumber()
end

say("Angka valid: " plus angka)
```

### Clear Screen

Membersihkan layar terminal:

```esy
clean()   ?> Windows: cls, Linux: clear
clear()   ?> Sama saja
cls()     ?> Sama saja

say("Layar sudah bersih!")
```

**Contoh penggunaan:**

```esy
say("Layar akan dibersihkan dalam 3 detik...")
?> (tunggu 3 detik - tidak ada fungsi sleep di EASY)

clean()
say("Layar bersih!")
```

---

## Komentar

### Single-line Comment

#### Menggunakan `?>`

Komentar satu baris dimulai dengan `?>`:

```esy
?> Ini adalah komentar
say("Hello")  ?> Komentar di akhir baris

?> Komentar tidak akan dieksekusi
?> say("Ini tidak akan tercetak")
```

**Best practice:**

```esy
?> Program untuk menghitung luas persegi
set panjang to 10  ?> dalam cm
set lebar to 5     ?> dalam cm
set luas to panjang times lebar
say("Luas: " plus luas plus " cm²")
```

### Multi-line Comment

#### Menggunakan `note:` dan `:note`

Untuk komentar beberapa baris:

```esy
note:
Ini adalah komentar multi-line.
Semua text di antara note: dan :note
akan diabaikan oleh interpreter.
:note

say("Hello")
```

**Contoh dokumentasi:**

```esy
note:
Program: Kalkulator BMI
Deskripsi: Menghitung Body Mass Index
Author: Razka
Version: 1.0
:note

say("Kalkulator BMI")
say("Masukkan berat (kg):")
set berat to askNumber()

say("Masukkan tinggi (m):")
set tinggi to askNumber()

set bmi to berat div (tinggi pow 2)
say("BMI Anda: " plus bmi)
```

#### Nested Comments

EASY mendukung nested comments:

```esy
note:
Komentar luar
note:
Komentar dalam (nested)
:note
Masih dalam komentar luar
:note

say("Hello")
```

### Best Practices Komentar

1. **Gunakan komentar untuk menjelaskan "mengapa", bukan "apa"**

   ```esy
   ?> Buruk: Menambah x dengan 1
   set x = x plus 1
   
   ?> Baik: Counter untuk loop berikutnya
   set x = x plus 1
   ```

2. **Beri komentar pada kode yang kompleks**

   ```esy
   ?> Menghitung faktorial secara rekursif
   make faktorial(n)
       if n atmost 1 then give 1
       give n times faktorial(n minus 1)
   end
   ```

3. **Update komentar saat mengubah kode**

4. **Gunakan komentar untuk TODO**

   ```esy
   ?> TODO: Tambahkan validasi input
   set x to askNumber()
   ```

5. **Jangan over-comment kode yang jelas**

   ```esy
   ?> Buruk: Terlalu banyak komentar
   set x to 5  ?> Set x ke 5
   set y to 10 ?> Set y ke 10
   set z to x plus y  ?> Tambahkan x dan y, simpan di z
   
   ?> Baik: Komentar seperlunya
   set x to 5
   set y to 10
   set z to x plus y  ?> Total nilai
   ```

---

## Contoh Program

### Hello World

Program paling sederhana:

```esy
say("Hello, World!")
```

### Kalkulator Sederhana

```esy
note:
Kalkulator sederhana untuk operasi dasar
:note

say("=== Kalkulator Sederhana ===")
say("Masukkan angka pertama:")
set a to askNumber()

say("Masukkan angka kedua:")
set b to askNumber()

say("\nHasil Operasi:")
say("Penjumlahan: " plus (a plus b))
say("Pengurangan: " plus (a minus b))
say("Perkalian: " plus (a times b))
say("Pembagian: " plus (a div b))
say("Pangkat: " plus (a pow b))
```

### Menebak Angka

```esy
note:
Game tebak angka sederhana
User harus menebak angka 1-10
:note

say("=== Game Tebak Angka ===")
say("Saya memikirkan angka antara 1-10")

?> Angka rahasia (dalam game sebenarnya gunakan random)
set rahasia to 7
set tebakan to 0
set percobaan to 0

while tebakan isnt rahasia then
    say("\nMasukkan tebakan:")
    set tebakan to askNumber()
    set percobaan = percobaan plus 1
    
    if tebakan under rahasia then
        say("Terlalu kecil!")
    nextif tebakan above rahasia then
        say("Terlalu besar!")
    otherwise
        say("Benar! Anda menebak dalam " plus percobaan plus " percobaan!")
    end
end
```

### To-Do List

```esy
note:
Program To-Do List sederhana
:note

say("=== To-Do List ===")
set todos to []
set running to true

while running then
    say("\nMenu:")
    say("1. Tambah tugas")
    say("2. Lihat tugas")
    say("3. Hapus tugas")
    say("4. Keluar")
    say("Pilih menu:")
    
    set pilihan to askNumber()
    
    if pilihan is 1 then
        say("Masukkan tugas:")
        set tugas to ask()
        append(todos, tugas)
        say("Tugas ditambahkan!")
        
    nextif pilihan is 2 then
        if lengthOf(todos) is 0 then
            say("Tidak ada tugas")
        otherwise
            say("\nDaftar Tugas:")
            repeat i from 0 through (lengthOf(todos) minus 1) do
                say((i plus 1) plus ". " plus (todos / i))
            end
        end
        
    nextif pilihan is 3 then
        if lengthOf(todos) is 0 then
            say("Tidak ada tugas untuk dihapus")
        otherwise
            say("Masukkan nomor tugas yang akan dihapus:")
            set nomor to askNumber()
            if nomor atleast 1 and nomor atmost lengthOf(todos) then
                pop(todos, nomor minus 1)
                say("Tugas dihapus!")
            otherwise
                say("Nomor tidak valid")
            end
        end
        
    nextif pilihan is 4 then
        say("Terima kasih!")
        set running to false
        
    otherwise
        say("Pilihan tidak valid")
    end
end
```

### Fibonacci Sequence

```esy
note:
Generate deret Fibonacci hingga n term
:note

say("=== Deret Fibonacci ===")
say("Masukkan jumlah term:")
set n to askNumber()

set fib to [0, 1]

repeat i from 2 through (n minus 1) do
    set prev1 to fib / (i minus 1)
    set prev2 to fib / (i minus 2)
    set next to prev1 plus prev2
    append(fib, next)
end

say("Deret Fibonacci:")
say(fib)
```

### FizzBuzz

```esy
note:
Program FizzBuzz klasik
Cetak angka 1-100, tapi:
- "Fizz" untuk kelipatan 3
- "Buzz" untuk kelipatan 5
- "FizzBuzz" untuk kelipatan 3 dan 5
:note

say("=== FizzBuzz ===")

repeat i from 1 through 100 do
    set div3 to (i div 3 times 3) is i
    set div5 to (i div 5 times 5) is i
    
    if div3 and div5 then
        say("FizzBuzz")
    nextif div3 then
        say("Fizz")
    nextif div5 then
        say("Buzz")
    otherwise
        say(i)
    end
end
```

### Palindrome Checker

```esy
note:
Cek apakah sebuah kata adalah palindrome
:note

say("=== Palindrome Checker ===")
say("Masukkan kata:")
set kata to ask()

?> Konversi ke list karakter (simulasi)
?> Dalam implementasi nyata perlu string indexing
set panjang to lengthOf(toList(kata))
set isPalindrome to true

say("Kata '" plus kata plus "' adalah palindrome: " plus toText(isPalindrome))
?> Catatan: Implementasi lengkap memerlukan fitur string indexing
```

### Sorting Algorithm

```esy
note:
Bubble Sort sederhana
:note

say("=== Bubble Sort ===")
set angka to [64, 34, 25, 12, 22, 11, 90]

say("Sebelum diurutkan:")
say(angka)

set n to lengthOf(angka)

repeat i from 0 through (n minus 2) do
    repeat j from 0 through (n minus i minus 2) do
        set curr to angka / j
        set next to angka / (j plus 1)
        
        if curr above next then
            ?> Swap (simplified - dalam implementasi nyata perlu fungsi swap)
            set temp to curr
            ?> angka[j] = next
            ?> angka[j+1] = temp
        end
    end
end

say("\nSetelah diurutkan:")
say(angka)

?> This example is flagged 'incomplete' by CodeRabbit.
```

### Mini Game

```esy
note:
Game petualangan text sederhana
:note

say("=== Petualangan di Hutan ===")
say("Anda terbangun di tengah hutan...")
set hp to 100
set hasKey to false

say("\nAnda melihat dua jalan:")
say("1. Jalan ke kiri (gelap)")
say("2. Jalan ke kanan (terang)")
say("Pilih jalan:")

set pilih to askNumber()

if pilih is 1 then
    say("\nAnda memasuki jalan gelap...")
    say("Tiba-tiba serigala muncul!")
    say("1. Lawan")
    say("2. Lari")
    set aksi to askNumber()
    
    if aksi is 1 then
        say("\nAnda melawan serigala dengan gagah berani!")
        set hp = hp minus 30
        say("HP tersisa: " plus hp)
        if hp above 0 then
            say("Anda menang! Menemukan kunci!")
            set hasKey to true
        otherwise
            say("Anda kalah... Game Over")
        end
    otherwise
        say("\nAnda berhasil kabur dengan selamat")
    end
    
nextif pilih is 2 then
    say("\nAnda berjalan di jalan terang...")
    say("Menemukan peti harta karun!")
    say("1. Buka peti")
    say("2. Tinggalkan")
    set aksi to askNumber()
    
    if aksi is 1 then
        say("\nPeti terbuka! Menemukan kunci emas!")
        set hasKey to true
    otherwise
        say("\nAnda meninggalkan peti")
    end
end

say("\n=== Akhir Permainan ===")
if hasKey then
    say("Selamat! Anda menemukan kunci untuk keluar dari hutan!")
otherwise
    say("Anda belum menemukan kunci... Coba lagi!")
end
say("HP Akhir: " plus hp)
```

---

## Tips dan Trik

### Menulis Kode yang Bersih

1. **Gunakan nama variabel yang deskriptif**

   ```esy
   ?> Buruk
   set x to 100
   set y to 0.1
   set z to x times y
   
   ?> Baik
   set harga to 100
   set pajak to 0.1
   set total to harga times (1 plus pajak)
   ```

2. **Konsisten dalam penamaan**

   ```esy
   ?> Pilih satu style dan konsisten
   set nama_pengguna to "Razka"    ?> snake_case
   set usia_pengguna to 20
   
   ?> Atau
   set namaPengguna to "Razka"     ?> camelCase
   set usiaPengguna to 20
   ```

3. **Gunakan spasi untuk readability**

   ```esy
   ?> Buruk
   set x=5.set y=10.say(x+y)
   
   ?> Baik
   set x to 5
   set y to 10
   say(x plus y)
   ```

4. **Pecah kode kompleks menjadi fungsi**

   ```esy
   ?> Buruk: Semua kode dalam satu tempat
   set a to 10
   set b to 20
   set hasil to a plus b
   say(hasil)
   
   ?> Baik: Menggunakan fungsi
   make tambah(x, y) -> x plus y
   
   set hasil to tambah(10, 20)
   say(hasil)
   ```

5. **Hindari magic numbers**

   ```esy
   ?> Buruk
   if umur atleast 17 then say("Boleh SIM")
   
   ?> Baik
   set UMUR_MIN_SIM to 17
   if umur atleast UMUR_MIN_SIM then say("Boleh SIM")
   ```

### Debugging

1. **Gunakan `say()` untuk debugging**

   ```esy
   set x to 10
   say("Debug: x = " plus x)  ?> Print nilai untuk cek
   
   set y to x times 2
   say("Debug: y = " plus y)
   ```

2. **Cek tipe data**

   ```esy
   set nilai to ask()
   say("Tipe: " plus typeOf(nilai))  ?> Cek tipe
   
   if isNumber(nilai) then
       say("Ini angka")
   otherwise
       say("Bukan angka")
   end
   ```

3. **Debug step by step**

   ```esy
   make hitungTotal(harga, jumlah)
       say("Debug: harga = " plus harga)
       say("Debug: jumlah = " plus jumlah)
       
       set subtotal to harga times jumlah
       say("Debug: subtotal = " plus subtotal)
       
       give subtotal
   end
   ```

4. **Gunakan komentar untuk isolate code**

   ```esy
   say("Bagian 1")
   ?> say("Bagian 2")  ?> Comment untuk skip sementara
   say("Bagian 3")
   ```

### Optimasi Performa

1. **Hindari loop nested yang tidak perlu**

   ```esy
   ?> Buruk: O(n²)
   repeat i from 0 through n do
       repeat j from 0 through n do
           ?> Operasi
       end
   end
   
   ?> Baik: O(n) jika memungkinkan
   repeat i from 0 through n do
       ?> Operasi
   end
   ```

2. **Gunakan early return**

   ```esy
   make cari(list, target)
       repeat i from 0 through (lengthOf(list) minus 1) do
           if (list / i) is target then
               give i  ?> Return langsung jika ketemu
           end
       end
       give -1
   end
   ```

3. **Jangan buat variabel yang tidak perlu**

   ```esy
   ?> Buruk
   set temp to x plus y
   set result to temp times 2
   give result
   
   ?> Baik
   give (x plus y) times 2
   ```

### Best Practices

1. **Selalu validasi input user**

   ```esy
   say("Masukkan angka 1-10:")
   set angka to askNumber()
   
   while angka under 1 or angka above 10 then
       say("Error! Masukkan angka 1-10:")
       set angka to askNumber()
   end
   ```

2. **Handle error cases**

   ```esy
   make bagi(a, b)
       if b is 0 then
           say("Error: Tidak bisa dibagi nol")
           give null
       end
       give a div b
   end
   ```

3. **Dokumentasikan kode Anda**

   ```esy
   note:
   Fungsi: hitungDiskon
   Parameter: harga (Number), persen (Number)
   Return: harga setelah diskon (Number)
   :note
   make hitungDiskon(harga, persen)
       give harga times (1 minus (persen div 100))
   end
   ```

4. **Test kode Anda**

   ```esy
   ?> Test cases
   make testTambah()
       say("Testing tambah()...")
       if tambah(2, 3) is 5 then
           say("✓ Test 1 passed")
       otherwise
           say("✗ Test 1 failed")
       end
   end
   ```

### Shortcut dan Idiom

1. **Toggle boolean**

   ```esy
   set flag to true
   set flag to not flag  ?> Toggle
   ```

2. **Swap values (tanpa temp)**

   ```esy
   ?> Catatan: EASY belum support ini secara native
   ?> Harus pakai variabel temporary
   set temp to a
   set a to b
   set b to temp
   ```

3. **Check range**

   ```esy
   if x atleast 10 and x atmost 20 then
       say("x dalam range")
   end
   ```

4. **Default value**

   ```esy
   make fungsi(param)
       ?> Jika param null, gunakan default
       if param is null then set param to "default"
       give param
   end
   ```

---

## Troubleshooting

### Error Umum

#### Illegal Character

**Error:** `Illegal Character: '<karakter>'`

**Penyebab:** Karakter yang tidak dikenali oleh EASY

**Contoh:**
```esy
set x @ 5  ?> Error: '@' bukan karakter valid
```

**Solusi:**
```esy
set x to 5  ?> Gunakan 'to' atau '='
```

#### Invalid Syntax

**Error:** `Invalid Syntax: Expected '<sesuatu>'`

**Penyebab:** Sintaks tidak sesuai aturan EASY

**Contoh:**
```esy
if x is 5 say("Lima")  ?> Error: Expected 'then'
```

**Solusi:**
```esy
if x is 5 then say("Lima")  ?> Tambahkan 'then'
```

#### Runtime Error

**Error:** `Runtime Error: <pesan error>`

**Penyebab:** Error saat program berjalan

**Contoh 1 - Division by zero:**
```esy
set x to 5 div 0  ?> Runtime Error: Division by zero
```

**Solusi:**
```esy
set x to 5
set y to 0
if y isnt 0 then
    say(x div y)
otherwise
    say("Error: Tidak bisa dibagi nol")
end
```

**Contoh 2 - Index out of bounds:**
```esy
set list to [1, 2, 3]
say(list / 10)  ?> Runtime Error: Index out of bounds
```

**Solusi:**
```esy
set list to [1, 2, 3]
set index to 10
if index atleast 0 and index under lengthOf(list) then
    say(list / index)
otherwise
    say("Error: Index tidak valid")
end
```

#### Undefined Variable

**Error:** `'<nama>' is not defined`

**Penyebab:** Menggunakan variabel yang belum dideklarasikan

**Contoh:**
```esy
say(nama)  ?> Error: 'nama' is not defined
```

**Solusi:**
```esy
set nama to "Razka"  ?> Deklarasikan dulu
say(nama)
```

### Pesan Error dan Solusinya

| Error | Penyebab | Solusi |
|-------|----------|---------|
| `Expected 'then'` | Missing `then` di `if` atau `while` | Tambahkan keyword `then` |
| `Expected 'do'` | Missing `do` di `repeat` | Tambahkan keyword `do` |
| `Expected 'end'` | Block tidak ditutup | Tambahkan `end` di akhir block |
| `Expected identifier` | Nama variabel tidak valid | Gunakan nama yang valid (huruf/underscore) |
| `Illegal operation` | Operasi tidak valid untuk tipe data | Cek tipe data dan operator yang digunakan |
| `Division by zero` | Membagi dengan nol | Cek denominator sebelum membagi |
| `Index out of bounds` | Index list tidak valid | Validasi index dengan `lengthOf()` |
| `Too many/few arguments` | Jumlah argumen fungsi salah | Sesuaikan jumlah argumen dengan definisi |

### Debugging Techniques

1. **Print debugging**

   ```esy
   say("=== DEBUG START ===")
   say("x = " plus x)
   say("y = " plus y)
   say("z = " plus z)
   say("=== DEBUG END ===")
   ```

2. **Isolate problem**

   ```esy
   ?> Comment bagian kode untuk cari yang error
   say("Bagian 1 OK")
   ?> say("Bagian 2")  ?> Skip bagian ini
   say("Bagian 3 OK")
   ```

3. **Check types**

   ```esy
   say("Tipe x: " plus typeOf(x))
   say("Tipe y: " plus typeOf(y))
   ```

4. **Step through logic**

   ```esy
   say("Step 1")
   set x to 10
   say("x = " plus x)
   
   say("Step 2")
   set y to x times 2
   say("y = " plus y)
   
   say("Step 3")
   say("Done")
   ```

---

## FAQ

### Pertanyaan Umum

#### Bagaimana cara...?

**Q: Bagaimana cara membuat loop dari 10 ke 1?**

A: Gunakan `by -1`:
```esy
repeat i from 10 through 1 by -1 do
    say(i)
end
```

**Q: Bagaimana cara membaca file?**

A: EASY saat ini tidak mendukung file I/O langsung. Gunakan `run()` untuk menjalankan file EASY lain.

**Q: Bagaimana cara membuat angka random?**

A: EASY saat ini belum memiliki fungsi random built-in. Untuk saat ini, gunakan nilai tetap.

**Q: Bagaimana cara membuat delay/sleep?**

A: EASY belum memiliki fungsi sleep/delay built-in.

#### Kenapa program saya error?

**Q: Kenapa `say(x)` error "is not defined"?**

A: Variabel `x` belum dideklarasikan. Gunakan `set x to <nilai>` dulu.

**Q: Kenapa list saya tidak berubah setelah operasi?**

A: Beberapa operasi list membuat list baru tanpa mengubah yang asli. Gunakan assignment:
```esy
set list = list add 5  ?> Assignment kembali ke variabel
```

**Q: Kenapa `if x is 5 say(x)` error?**

A: Missing keyword `then`. Harus: `if x is 5 then say(x)`

#### Apakah EASY mendukung...?

**Q: Apakah EASY support OOP (Object-Oriented Programming)?**

A: Tidak, EASY adalah bahasa procedural sederhana untuk pembelajaran.

**Q: Apakah EASY support file I/O?**

A: Terbatas. Bisa menjalankan file .esy lain dengan `run()`, tapi tidak bisa read/write file arbitrary.

**Q: Apakah EASY support library/package eksternal?**

A: Tidak, EASY tidak memiliki package manager atau system import.

**Q: Apakah EASY support multithreading?**

A: Tidak, EASY single-threaded.

#### Bagaimana cara berkontribusi?**

A: Kunjungi repository GitHub: https://github.com/tyydev1/easy-language

- Report bugs di Issues
- Suggest features di Discussions
- Submit pull requests untuk improvements

### Pertanyaan Teknis

#### Perbedaan `plus` dan `add`?

**`plus`** untuk angka dan text:
```esy
say(5 plus 3)           ?> 8
say("Hello" plus "!")   ?> Hello!
```

**`add`** untuk list:
```esy
set list to [1, 2]
say(list add 3)  ?> [1, 2, 3]
```

Meskipun `+` bisa digunakan untuk keduanya, lebih jelas menggunakan keyword yang tepat.

#### Kapan menggunakan `repeat` vs `while`?

**Gunakan `repeat` ketika:**
- Tahu jumlah iterasi pasti
- Loop berbasis counter/range

```esy
repeat i from 1 through 10 do
    say(i)
end
```

**Gunakan `while` ketika:**
- Loop berbasis kondisi
- Tidak tahu berapa kali akan loop

```esy
set x to 0
while x under 10 then
    say(x)
    set x = x plus 1
end
```

#### Apa itu `null`?

`null` adalah nilai khusus yang merepresentasikan "tidak ada nilai" atau "tidak terdefinisi".

**Kegunaan:**
```esy
?> Default return value
make fungsi()
    say("Hello")
end

set result to fungsi()
say(result)  ?> null

?> Menandai nilai tidak ada
set data to null
if data is null then
    say("Data tidak tersedia")
end

?> Inisialisasi variabel
set found to null
?> ... kode pencarian ...
if found isnt null then
    say("Ditemukan: " plus found)
end
```

---

## Appendix

### Kata Kunci Lengkap

Berikut semua keyword yang tidak bisa digunakan sebagai nama variabel:

**Variable Declaration:**
- `set`, `to`

**Arithmetic:**
- `plus`, `minus`, `times`, `div`, `pow`

**List Operations:**
- `add`, `remove`, `merge`, `get`

**Logical:**
- `and`, `or`, `not`

**Conditionals:**
- `if`, `then`, `nextif`, `otherwise`

**Comparisons:**
- `is`, `isnt`, `under`, `above`, `atmost`, `atleast`

**Loops:**
- `repeat`, `from`, `through`, `by`, `while`, `do`

**Functions:**
- `make`, `give`

**Control Flow:**
- `stop`, `next`, `end`

### Operator Lengkap

| Kategori | Operator | Keyword | Deskripsi |
|----------|----------|---------|-----------|
| **Aritmatika** | `+` | `plus` | Penjumlahan |
| | `-` | `minus` | Pengurangan |
| | `*` | `times` | Perkalian |
| | `/` | `div` | Pembagian |
| | `^` | `pow` | Pangkat |
| **Perbandingan** | `==` | `is` | Sama dengan |
| | `!=` | `isnt` | Tidak sama dengan |
| | `<` | `under` | Lebih kecil |
| | `>` | `above` | Lebih besar |
| | `<=` | `atmost` | Lebih kecil atau sama |
| | `>=` | `atleast` | Lebih besar atau sama |
| **Logika** | - | `and` | AND logika |
| | - | `or` | OR logika |
| | - | `not` | NOT logika |
| **List** | `+` | `add` | Tambah element |
| | `-` | `remove` | Hapus element |
| | `*` | `merge` | Gabung list |
| | `/` | `get` | Ambil element |
| **Assignment** | `=` | `to` | Assign nilai |

### Fungsi Bawaan Lengkap

**Input/Output:**
- `say(value)` - Print ke layar
- `saySave(value)` - Konversi ke text dan return
- `ask()` - Input text
- `askNumber()` - Input angka

**Type Checking:**
- `isNumber(value)` - Cek apakah Number
- `isText(value)` - Cek apakah Text
- `isList(value)` - Cek apakah List
- `isFunction(value)` - Cek apakah Function
- `typeOf(value)` - Return tipe sebagai text

**Type Conversion:**
- `toNumber(value)` / `toNum(value)` - Konversi ke Number
- `toText(value)` - Konversi ke Text
- `toList(value)` - Konversi ke List
- `toState(value)` - Konversi ke Boolean

**List Operations:**
- `append(list, value)` - Tambah ke akhir list
- `pop(list, index)` - Hapus dan return element
- `extend(listA, listB)` - Gabung dua list
- `lengthOf(list)` - Panjang list

**Utility:**
- `clean()` / `clear()` / `cls()` - Bersihkan layar
- `run(filename)` - Jalankan file EASY

**Constants:**
- `null` - Nilai kosong
- `true` - Boolean true (1)
- `false` - Boolean false (0)
- `math_pi` - Nilai π (3.14159...)
- `quit` / `exit` - Keluar dari program

### Contoh Kode Lengkap

#### Program Komprehensif

```esy
note:
Program Demo EASY Language
Mendemonstrasikan semua fitur utama EASY
Author: EASY Language Team
:note

?> ===== VARIABEL DAN TIPE DATA =====
say("=== Variabel dan Tipe Data ===")

set angka to 42
set desimal to 3.14
set teks to "Hello, EASY!"
set daftar to [1, 2, 3, 4, 5]
set benar to true
set salah to false
set kosong to null

say("Number: " plus angka)
say("Float: " plus desimal)
say("Text: " plus teks)
say("List: " plus daftar)
say("Boolean: " plus benar plus " / " plus salah)
say("Null: " plus kosong)

?> ===== OPERASI ARITMATIKA =====
say("\n=== Operasi Aritmatika ===")

set a to 10
set b to 3

say(a plus " + " plus b plus " = " plus (a plus b))
say(a plus " - " plus b plus " = " plus (a minus b))
say(a plus " * " plus b plus " = " plus (a times b))
say(a plus " / " plus b plus " = " plus (a div b))
say(a plus " ^ " plus b plus " = " plus (a pow b))

?> ===== OPERASI LIST =====
say("\n=== Operasi List ===")

set myList to [1, 2, 3]
say("Original: " plus myList)

set myList = myList add 4
say("Setelah add 4: " plus myList)

set myList = myList remove 0
say("Setelah remove index 0: " plus myList)

set myList = myList merge [5, 6]
say("Setelah merge [5, 6]: " plus myList)

say("Element index 2: " plus (myList / 2))
say("Panjang list: " plus lengthOf(myList))

?> ===== KONDISI =====
say("\n=== Kondisi (If-Else) ===")

set nilai to 85

if nilai atleast 90 then
    say("Grade: A - Excellent!")
nextif nilai atleast 80 then
    say("Grade: B - Good!")
nextif nilai atleast 70 then
    say("Grade: C - Average")
nextif nilai atleast 60 then
    say("Grade: D - Pass")
otherwise
    say("Grade: F - Fail")
end

?> ===== PERULANGAN =====
say("\n=== Perulangan ===")

say("Repeat loop (1-5):")
repeat i from 1 through 5 do
    say("  " plus i)
end

say("\nWhile loop (countdown from 5):")
set counter to 5
while counter above 0 then
    say("  " plus counter)
    set counter = counter minus 1
end

say("\nNested loop (tabel 3x3):")
repeat i from 1 through 3 do
    set baris to ""
    repeat j from 1 through 3 do
        set baris = baris plus (i times j) plus " "
    end
    say("  " plus baris)
end

?> ===== FUNGSI =====
say("\n=== Fungsi ===")

?> Fungsi sederhana
make greet(nama)
    give "Hello, " plus nama plus "!"
end

say(greet("Alice"))
say(greet("Bob"))

?> Fungsi dengan arrow syntax
make kuadrat(x) -> x times x

say("Kuadrat 5: " plus kuadrat(5))
say("Kuadrat 7: " plus kuadrat(7))

?> Fungsi rekursif
make faktorial(n)
    if n atmost 1 then give 1
    give n times faktorial(n minus 1)
end

say("Faktorial 5: " plus faktorial(5))

?> ===== TYPE CHECKING & CONVERSION =====
say("\n=== Type Checking & Conversion ===")

set val1 to 42
set val2 to "123"
set val3 to [1, 2, 3]

say("typeOf(42): " plus typeOf(val1))
say("typeOf(\"123\"): " plus typeOf(val2))
say("typeOf([1,2,3]): " plus typeOf(val3))

say("isNumber(42): " plus isNumber(val1))
say("isText(\"123\"): " plus isText(val2))
say("isList([1,2,3]): " plus isList(val3))

say("toNumber(\"123\"): " plus toNumber(val2))
say("toText(42): " plus toText(val1))

?> ===== CONTROL FLOW =====
say("\n=== Control Flow (next & stop) ===")

say("Cetak angka genap 1-10:")
repeat i from 1 through 10 do
    if i div 2 times 2 isnt i then next  ?> Skip ganjil
    say("  " plus i)
end

say("\nCari angka > 5:")
repeat i from 1 through 10 do
    if i above 5 then
        say("  Ditemukan: " plus i)
        stop  ?> Berhenti setelah ketemu
    end
end

?> ===== PROGRAM SELESAI =====
say("\n=== Program Selesai! ===")
say("Terima kasih telah menggunakan EASY Language!")
```

### Referensi Tambahan

**Dokumentasi Online:**
- GitHub Repository: https://github.com/tyydev1/easy-language
- Installation Guide: [INSTALLATION.md](https://github.com/tyydev1/easy-language/blob/main/INSTALLATION.md)
- README: [README.md](https://github.com/tyydev1/easy-language/blob/main/README.md)

**Tutorial dan Contoh:**
- Folder `misc/` berisi contoh-contoh program
- File `test.esy` mendemonstrasikan berbagai fitur

**Inspirasi dan Referensi:**
- Python - Untuk struktur dasar interpreter
- JavaScript - Untuk fleksibilitas sintaks
- BASIC - Untuk kesederhanaan bahasa

**Tools untuk Development:**
- Text Editor: VS Code, Sublime Text, Notepad++
- Terminal: Command Prompt, PowerShell, Bash
- Python 3.6+ (requirement untuk menjalankan EASY)

---

## Kontribusi

### Cara Berkontribusi

EASY Language adalah proyek open-source dan kami menerima kontribusi!

**Cara berkontribusi:**

1. **Fork repository**
   ```bash
   git clone https://github.com/tyydev1/easy-language.git
   ```

2. **Buat branch baru**
   ```bash
   git checkout -b feature/fitur-baru
   ```

3. **Buat perubahan dan commit**
   ```bash
   git add .
   git commit -m "Menambahkan fitur baru"
   ```

4. **Push dan buat Pull Request**
   ```bash
   git push origin feature/fitur-baru
   ```

**Yang bisa dikontribusi:**
- Bug fixes
- Fitur baru
- Perbaikan dokumentasi
- Contoh program
- Optimasi performance
- Testing

### Code of Conduct

Kami berkomitmen untuk menciptakan lingkungan yang ramah dan inklusif.

**Pedoman:**
- Bersikap hormat dan profesional
- Terima kritik konstruktif dengan lapang dada
- Fokus pada apa yang terbaik untuk komunitas
- Tunjukkan empati terhadap anggota komunitas lainnya

**Tidak diperbolehkan:**
- Bahasa atau gambar seksual
- Trolling atau komentar menghina
- Harassment dalam bentuk apapun
- Mempublikasikan informasi pribadi orang lain
- Conduct tidak etis atau tidak profesional

### Pelaporan Bug

Menemukan bug? Laporkan di GitHub Issues!

**Format laporan bug:**

```
**Deskripsi Bug:**
[Jelaskan bug secara jelas dan singkat]

**Cara Reproduksi:**
1. Langkah 1...
2. Langkah 2...
3. ...

**Hasil yang Diharapkan:**
[Apa yang seharusnya terjadi]

**Hasil Aktual:**
[Apa yang benar-benar terjadi]

**Kode Contoh:**
```esy
[Masukkan kode yang menyebabkan bug]
```

**Environment:**
- OS: [Windows 10 / Linux Ubuntu 20.04 / etc]
- Python Version: [3.8 / 3.9 / etc]
- EASY Version: [1.0.0]

**Screenshot (jika ada):**
[Lampirkan screenshot jika membantu]
```

### Feature Request

Punya ide untuk fitur baru? Buat request di GitHub Discussions!

**Format feature request:**

```
**Fitur yang Diinginkan:**
[Jelaskan fitur secara jelas]

**Alasan:**
[Mengapa fitur ini berguna?]

**Contoh Penggunaan:**
```esy
[Tunjukkan contoh kode bagaimana fitur akan digunakan]
```

**Alternatif yang Sudah Dicoba:**
[Apakah ada workaround saat ini?]

**Informasi Tambahan:**
[Context atau informasi lain yang relevan]


---

## Lisensi

EASY Language dirilis di bawah **Apache License 2.0**.

Anda bebas untuk:
- ✓ Menggunakan untuk tujuan apapun (termasuk komersial)
- ✓ Memodifikasi source code
- ✓ Mendistribusikan
- ✓ Memberikan sublicense

Dengan ketentuan:
- Menyertakan lisensi dan copyright notice
- Mendokumentasikan perubahan yang dibuat
- Tidak menggunakan trademark tanpa izin

**Lihat file LICENSE lengkap di repository.**

---

## Kontak dan Komunitas

### GitHub Repository

**Main Repository:**
https://github.com/tyydev1/easy-language

**Report Issues:**
https://github.com/tyydev1/easy-language/issues

**Discussions:**
https://github.com/tyydev1/easy-language/discussions

### Discord/Telegram

[Akan diupdate jika ada komunitas Discord/Telegram]

### Email

Untuk pertanyaan atau kolaborasi:
[Akan diupdate dengan email kontak]

### Social Media

[Akan diupdate dengan link social media]

---

## Changelog

### Versi 1.0.0 (Initial Release)

**Tanggal Release:** [TBD]

**Fitur Utama:**
- ✓ Interpreter dasar dengan lexer dan parser
- ✓ Tipe data: Number, Text, List, Boolean, null
- ✓ Variabel dengan keyword `set`
- ✓ Operator aritmatika: `plus`, `minus`, `times`, `div`, `pow`
- ✓ Operator perbandingan: `is`, `isnt`, `under`, `above`, `atmost`, `atleast`
- ✓ Operator logika: `and`, `or`, `not`
- ✓ Operator list: `add`, `remove`, `merge`, `get`
- ✓ Struktur kontrol: `if`, `nextif`, `otherwise`
- ✓ Perulangan: `repeat` (for loop), `while`
- ✓ Control flow: `next` (continue), `stop` (break)
- ✓ Fungsi dengan keyword `make`
- ✓ Return value dengan `give`
- ✓ Arrow syntax untuk fungsi: `->`
- ✓ Komentar single-line: `?>`
- ✓ Komentar multi-line: `note:` ... `:note`
- ✓ Built-in functions: I/O, type checking, type conversion, list operations
- ✓ Interactive shell (REPL)
- ✓ File execution
- ✓ Cross-platform: Linux dan Windows

**Installers:**
- ✓ Linux installer script
- ✓ Windows PowerShell installer

**Dokumentasi:**
- ✓ README.md
- ✓ INSTALLATION.md
- ✓ DOCUMENTATION.md (lengkap)
- ✓ Example programs

**Known Limitations:**
- Tidak ada file I/O (read/write arbitrary files)
- Tidak ada networking
- Tidak ada random number generator
- Tidak ada string indexing
- Tidak ada negative list indexing
- Tidak ada dictionary/object type
- Tidak ada import system
- Performance terbatas (berbasis Python interpreter)

### Versi Sebelumnya

_Ini adalah rilis pertama dari EASY Language._

---

## Ucapan Terima Kasih

### Contributors

Terima kasih kepada semua yang telah berkontribusi pada EASY Language:

- **tyydev1** - Creator dan main developer

[List akan diupdate dengan contributor lainnya]

### Inspirasi

EASY Language terinspirasi dari:

- **Python** - Untuk struktur interpreter dan kesederhanaan
- **JavaScript** - Untuk fleksibilitas sintaks
- **BASIC** - Untuk filosofi "easy to learn"
- **Logo** - Untuk pendekatan pembelajaran
- **Scratch** - Untuk fokus pada pemula

Terima kasih kepada komunitas bahasa pemrograman ini!

### Tools yang Digunakan

Development EASY Language menggunakan:

- **Python 3** - Bahasa implementasi
- **Git** - Version control
- **GitHub** - Hosting dan collaboration
- **VS Code** - Code editor
- **Markdown** - Dokumentasi

---

## Penutup

Terima kasih telah membaca dokumentasi EASY Language!

**Langkah selanjutnya:**

1. **Install EASY** - Ikuti [Installation Guide](https://github.com/tyydev1/easy-language/blob/main/INSTALLATION.md)
2. **Coba Examples** - Jalankan program di folder `misc/`
3. **Buat Program Pertama** - Mulai dengan "Hello, World!"
4. **Explore** - Eksperimen dengan berbagai fitur
5. **Join Community** - Bertanya dan berbagi di GitHub Discussions

**Ingat:**
- Programming adalah skill yang dipelajari dengan praktek
- Jangan takut membuat error - error adalah bagian dari belajar
- Mulai dari yang sederhana, tingkatkan bertahap
- Bergabung dengan komunitas dan bertanya jika bingung

**Happy Coding with EASY! 🚀**

---

*Dokumentasi ini adalah living document dan akan terus diupdate. Jika menemukan kesalahan atau punya saran perbaikan, silakan buat issue di GitHub.*

*Last Updated: October 2025*
*EASY Language Version: 1.0.0*