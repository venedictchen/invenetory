# Invenetory App Using Django

# Links
blablabla

Tugas 2 Mata Kuliah Pemograman Berbasis Platform.

---

## Membuat Projek Django 
<details>
<summary> Initialize Django Project </summary>

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

---

## Membuat App Main
<details>

<summary>Initialize Environment</summary>

1. Menjalankan virtual environment.
    - Windows:
        ```sh
        env\Scripts\activate.bat or env\Scripts\activate
        ```
    - Unix (Mac/Linux):
        ```sh
        source env/bin/activate
        ```
</details>

<details>

<summary>Membuat Aplikasi main dan templates</summary>

1.  Membuat aplikasi main dengan perintah startapp

    ```python
    python manage.py startapp main
    ```
2. Menambahkan aplikasi main ke INSTALLED_APPS di settings.py invenetory agar app dapat muncul.

    ```python
    INSTALLED_APPS = [
    ...,
    'main',
    ...
    ]    
    ```
3. Membuat direktorui baru dengan nama `templates`. 
4. Membuat file baru dengan nama `main.html` di dalam direktori templates.
</details>
<details>

<summary> Membuat Routing URL Aplikasi dan Projek</summary>

1. Membuat file baru `urls.py` di dalam direktori main.
    ```python
    from django.urls import path #Definisi pola URL
    from main.views import show_main #Fungsi dari views.py untuk tampilan

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    ```
2. Pada file `urls.py `di dalam `direktori invenetory` import fungsi `include` dari `django.urls`.
    ```python
    ...
    from django.urls import path, include 
    #Fungsi include untuk import rute URL dari aplikasi main ke dalam projek
    ...
    ```
3. Menambahkan rute URL untuk mengarahkan ke tampilan main di dalam variabel `urlpatterns`.
    ```python
    urlpatterns = [
    ...
    path('main/', include('main.urls')),
    ...
    ]
    ```
</details>

<details>
<summary>Membuat Model Aplikasi main dan migrasi</summary>

1. Membuat model pada direktori aplikasi main di `models.py`
    ```python
    from django.db import models

    class Item(models.Model):
    name = models.CharField(max_length=255)
    amount =  models.IntegerField()
    description = models.TextField()
    code = models.IntegerField()
    price = models.IntegerField()   
    ```
2. Melakukan migrasi agar Django dapat melacak perubahan model.
    ```python
    python manage.py makemigrations
    ```
    ```python
    python manage.py migrate
    ```
</details>

<details>
<summary>Membuat fungsi pada views.py</summary>

1. Menambahkan import pada file views.py di direktori main.
    ```python
    from django.shortcuts import render
    ```

2. Membuat fungsi show_main yang menerima request dan mengembalikan tampilan yang sesuai,
    ```python
    
    def show_main(request):
        context = {
            'name': 'Toshiba',
            'amount': '2',
            'description':'Flashdisk',
            'code':'2232',
            'price':'30000',
        } #Data yang akan dikirimkan ke tampilan

        return render(request, "main.html", context)

    ```
</details>

---

## Post Project To GitHub
<details>
<summary>gitignore ,init, add, commit, push</summary>
1. Menambahkan file `.gitignore`
    ```
    # Django
    *.log
    *.pot
    *.pyc
    __pycache__
    db.sqlite3
    media

    # Backup files
    *.bak 

    # If you are using PyCharm
    # User-specific stuff
    .idea/**/workspace.xml
    .idea/**/tasks.xml
    .idea/**/usage.statistics.xml
    .idea/**/dictionaries
    .idea/**/shelf

    # AWS User-specific
    .idea/**/aws.xml

    # Generated files
    .idea/**/contentModel.xml

    # Sensitive or high-churn files
    .idea/**/dataSources/
    .idea/**/dataSources.ids
    .idea/**/dataSources.local.xml
    .idea/**/sqlDataSources.xml
    .idea/**/dynamic.xml
    .idea/**/uiDesigner.xml
    .idea/**/dbnavigator.xml

    # Gradle
    .idea/**/gradle.xml
    .idea/**/libraries

    # File-based project format
    *.iws

    # IntelliJ
    out/

    # JIRA plugin
    atlassian-ide-plugin.xml

    # Python
    *.py[cod] 
    *$py.class 

    # Distribution / packaging 
    .Python build/ 
    develop-eggs/ 
    dist/ 
    downloads/ 
    eggs/ 
    .eggs/ 
    lib/ 
    lib64/ 
    parts/ 
    sdist/ 
    var/ 
    wheels/ 
    *.egg-info/ 
    .installed.cfg 
    *.egg 
    *.manifest 
    *.spec 

    # Installer logs 
    pip-log.txt 
    pip-delete-this-directory.txt 

    # Unit test / coverage reports 
    htmlcov/ 
    .tox/ 
    .coverage 
    .coverage.* 
    .cache 
    .pytest_cache/ 
    nosetests.xml 
    coverage.xml 
    *.cover 
    .hypothesis/ 

    # Jupyter Notebook 
    .ipynb_checkpoints 

    # pyenv 
    .python-version 

    # celery 
    celerybeat-schedule.* 

    # SageMath parsed files 
    *.sage.py 

    # Environments 
    .env 
    .venv 
    env/ 
    venv/ 
    ENV/ 
    env.bak/ 
    venv.bak/ 

    # mkdocs documentation 
    /site 

    # mypy 
    .mypy_cache/ 

    # Sublime Text
    *.tmlanguage.cache 
    *.tmPreferences.cache 
    *.stTheme.cache 
    *.sublime-workspace 
    *.sublime-project 

    # sftp configuration file 
    sftp-config.json 

    # Package control specific files Package 
    Control.last-run 
    Control.ca-list 
    Control.ca-bundle 
    Control.system-ca-bundle 
    GitHub.sublime-settings 

    # Visual Studio Code
    .vscode/* 
    !.vscode/settings.json 
    !.vscode/tasks.json 
    !.vscode/launch.json 
    !.vscode/extensions.json 
    .history
    ```
2. Melalukan `init`, `add`, `commit`, dan `push` ke github.
    ```sh
    git init
    git remote add origin https://github.com/venedictchen/invenetory.git
    git branch -M main
    git add .
    git commit -m "<message>"
    git push -u origin main

    ```
</details>

---

## Django Unit Testing

<details>
<summary>Membuat Unit Test</summary>

1. Membuat unit test pada berkas `tests.py` di direktori aplikasi main.
    ```python
    from django.test import TestCase, Client

    class mainTest(TestCase):
        def test_main_url_is_exist(self):
            response = Client().get('/main/')
            self.assertEqual(response.status_code, 200)

        def test_main_using_main_template(self):
            response = Client().get('/main/')
            self.assertTemplateUsed(response, 'main.html')
    ```
2. Menjalankan Test
    ```python
    python manage.py test
    ```
3. Apabila Test berhasil akan keluar informasi sebagai berikut.
    ```sh
    Found 3 test(s).
    Creating test database for alias 'default'...
    System check identified no issues (0 silenced).
    ...
    ----------------------------------------------------------------------
    Ran 3 tests in 0.209s

    OK
    Destroying test database for alias 'default'...
    ```
</details>

---

## Relasi urls.py, views.py, models.py, html (MTV)
<img src=baganpbp.png width = 800 height=500/>

1. HTTP Request akan diterima url.py dan akan diproses untuk mencari pola url dan method yang sesuai dengan request.
2. Pada views.py akan dijalankan logika method yang dibutuhkan.
3. Data akan diminta ke models.py dan models.py akan memberikan data yang dibutuhkan.
4. Proses write juga bisa dilakukan ke models.py tidak hanya read.
5. Selanjutnya template (.html) akan memberikan bentuk html ke views.py
6. Terakhir views.py akan memberikan HTTP Response berupa html.

---

## Mengapa kita memerlukan virtual environment?

Kita membutuhkan virtual environment agar tidak terjadinya tabrakan depedensi antar projek. Tabrakan
atau konflik yang dimaksud adalah adanya faktor luar, seperti python version. Dengan adanya virtual environment, maka setiap projek akan terisolasi sendiri dan memiliki
dependensi masing-masing.

## Apa itu MVC, MVT, MVVM?

<details>
<summary>MVC</summary>
</details>