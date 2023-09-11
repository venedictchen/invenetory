# Invenetory App Using Django

# Links
blablabla

Tugas 2 Mata Kuliah Pemograman Berbasis Platform.

## Making the Django Project
<details>
<summary> Membuat Projek Django </summary>

1. Membuat direktori baru dengan nama `invenetory`.
    ```sh
    mkdir inventory
    cd inventory
    ```
2. Membuat virtual environment baru.
    ```python
    python -m venv env
    ```
3. Aktivasi virtual environment.
    - Windows:
        ```sh
        env\Scripts\activate.bat atau env\Scripts\activate
        ```
    - Unix (Mac/Linux):
        ```sh
        source env/bin/activate
        ```
4. Dalam direktori yang sama membuat `requirements.txt` dan menambahkan beberapa dependencies.
    ```python
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ```
5. Install dependencies dengan perintah berikut dan mengaktifkan virtual environment sebelumnya.
    ```sh
    pip install -r requirements.txt
    ```
6. Membuat projek Django baru dengan nama `invenetory`.
    ```django
    django-admin startproject invenetory .
    ```


</details>
<details>
<summary> Configure and Testing Django Project untuk mengecek apakah Django Project kita berjalan</summary>

1. Menambahkan `*` ke `ALLOWED_HOST` di `settings.py` untuk keperluan deployment.
    ```python
    ...
    ALLOWED_HOSTS = ["*"]
    ...

    ```
2. Menjalankan server untuk melihat apakah Django Project berjalan.
    - Windows:
    ```python
    python manage.py runserver
    ```
    - Unix:
    ```
    ./manage.py runserver
    ```
3. Buka `http://localhost:8000` jika terdapat animasi roket maka Django Project sudah berjalan.

</details>

## Membuat App Main
<details>

<summary>Initialize</summary>

1. Menjalankan virtual environment.
    - Windows:
        ```sh
        env\Scripts\activate.bat or env\Scripts\activate
        ```
    - Unix (Mac/Linux):
        ```sh
        source env/bin/activate
        ```
<summary>Membuat aplikasi main</summary>

1. 





</details>