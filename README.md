# ETL Batch Processing

ETL Batch Processing ini adalah sebuah proyek Python yang digunakan untuk mengekstrak, mentransformasi, dan memuat data ke data warehouse (DWH). Proyek ini mengautomasi proses ETL dalam bentuk batch, mendukung koneksi ke database PostgreSQL, dan memanfaatkan berbagai library seperti Pandas, SQLAlchemy, dan psycopg2 untuk memproses data dalam batch.


## 🚀 Fitur
- **Koneksi Database**: Mendukung koneksi ke database sumber dan DWH.
- **Ekstraksi Data**: Membaca data menggunakan query SQL.
- **Transformasi Data**: Menggunakan Pandas untuk manipulasi dan analisis data (dapat dikembangkan lebih lanjut).
- **Ingestion ke DWH**: Memuat data hasil transformasi ke DWH.



## 🛠️ Teknologi
- Python 3.12
- Pandas
- SQLAlchemy
- SQLParse



## 📂 Struktur Proyek

Berikut adalah contoh README.md untuk kode ETL yang Anda bagikan:

markdown
Copy code
# ETL Service

ETL Service adalah sebuah script Python sederhana untuk mengekstrak data dari database sumber, melakukan transformasi data, dan memuatnya ke database data warehouse (DWH). Script ini dirancang untuk menangani proses ETL secara otomatis menggunakan library populer seperti Pandas dan SQLAlchemy.

---

## 🚀 Fitur
- **Koneksi Database**: Mendukung koneksi ke database sumber dan DWH.
- **Ekstraksi Data**: Membaca data menggunakan query SQL.
- **Transformasi Data**: Menggunakan Pandas untuk manipulasi dan analisis data (dapat dikembangkan lebih lanjut).
- **Ingestion ke DWH**: Memuat data hasil transformasi ke DWH.



## 🛠️ Teknologi
- Python
- Pandas
- SQLAlchemy
- SQLParse



## 📂 Struktur Proyek
├── query/ 
    ├── query.sql # Query SQL untuk membaca data dari sumber 
    ├── dwh_design.sql # Query untuk mendesain skema DWH 
├── main.py # Script utama ETL 
├── connection.py # Modul untuk koneksi ke database 
├── requirements.txt # Dependencies yang diperlukan untuk menjalankan proyek



### Jalankan script berikut untuk menginstall dependencies
```
pip install -r requirements.txt
```



## ⚙️ Konfigurasi
### 1.Buat file `config.json`
File ini menyimpan informasi kredensial database dan diabaikan oleh Git. 
Contoh formatnya adalah sebagai berikut:
```
{
    "marketplace_prod": {
        "host": "",
        "db": "",
        "user": "",
        "password": "",
        "port": ""
    },
    "dwh": {
        "host": "",
        "db": "",
        "user": "",
        "password": "",
        "port": ""
    }
}
```

### 2. Pastikan file sql tersedia
- `query/query.sql`: Berisi query untuk membaca data dari Data Source.
- `query/dwh_design.sql`: Berisi query untuk mendesain skema di DWH.

 

## How To Run
### 1. Clone the repository
```
git clone https://github.com/Mafarasya/Mini-project-batch-processing.git
cd Mini-project-batch-processing
```
### 2. Execute the main script
```
python main.py
```
