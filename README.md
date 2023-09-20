# Invenetory App Using Django

# Links
https://invenetory.adaptable.app/main

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
    from .models import Item
    class mainTest(TestCase):
        def test_main_url_is_exist(self):
            response = Client().get('/main/')
            self.assertEqual(response.status_code, 200)

        def test_main_using_main_template(self):
            response = Client().get('/main/')
            self.assertTemplateUsed(response, 'main.html')
            
        def test_model_creation(self):
            item = Item.objects.create(name='Test Name',amount=0,description='Test Description',code=0,price=0)
            self.assertEqual(item.name, 'Test Name')
            self.assertEqual(item.amount, 0)
            self.assertEqual(item.description, 'Test Description')
            self.assertEqual(item.code, 0)
            self.assertEqual(item.price, 0)
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

## Deployment Adaptable

1. Membuka website Adaptable dan sign in with github.
2. Create new app dan Connect an Existing Repository.
3. Memilih invenetory dan branch main sebagai aplikasi yang mau di deploy.
4. Memilih python app template.
5. Memilih PostgeSQL untuk tipe database.
6. Memilih python version yang sesuai di sini `3.11`.
7. Mengisi start command sebagai berikut `python manage.py migrate && gunicorn shopping_list.wsgi`.
8. Memilih nama domain `invenetory`.
9. Centang bagian HTTP Listener Port.

---

## Relasi urls.py, views.py, models.py, html (MTV)

<img src=./images/baganpbp.png>

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

1. MVC (Model View Controller) adalah pola desain dalam membuat sebuah aplikasi dengan cara
memisahkan kode menjadi 3 bagian, yaitu Model, View, dan Controller.
    - Model:
        Model adalah bagian yang bertugas untuk mengelola data di database.
    - View:
        View yang bertugas untuk menampilkan response dari request yang diberikan.
    - Controller:
        Controller merupakan bagian yang menghubungkan antara model dan view.

</details>

<details>
<summary>MVT</summary>

1. MVT (Model View Template) adalah pola desain yang mirip dengan MVC. MVT berbeda dengan MVC pada bagian
controller. Peran controller diganti oleh template. Pada MVC, kita harus menulis semua kode kontrol tertentu. Sedangkan pada MVT bagian controller di handle oleh framework itu sendiri.
    - Model:
        Model adalah bagian yang bertugas untuk mengelola data di database.
    - View:
        View yang bertugas untuk menampilkan output dari data yang telah diproses.
    - Template:
        Sebuah file HTML yang merupakan struktur dari tampilan yang akan diberikan ke pengguna.
</details>

<details>
<summary>MVVM</summary>

1. MVVM (Model View ViewModel) adalah pola desain yang dikenalkan oleh Microsoft sebagai alternatif dari MVC.
MVVM berfokus untuk membedakan bagian logic dari program dan UI(User Interface) terpisah. Controller diganti
oleh ViewModel. ViewModel terdiri dari Model yang diubah menjadi View, dan berisi perintah dari view yang dapat memengaruhi model.
    - Model:
        Model adalah bagian yang bertugas untuk logika aplikasi dan mengelola data yang didapatkan dari
        ViewModel.
    - View:
        View yang bertugas untuk menentukan struktur, tata letak, teks, gambar dan element UI lainnya. View akan menginformasikan ViewModel apa yang dilakukan oleh pengguna.
    - ViewModel:
        ViewModel merupakan bagian yang menjadi perantara antara View dan Model.

</details>

---

## Apa Perbedaan antara form POST dan form GET dalam Django?

Form POST dan GET memiliki perbedaan sebagai berikut:   

- Keamanan Form POST lebih baik dibandingkan Form GET karena data tidak terlihat pada url bar, sedangkan
Form GET data terlihat pada url bar dan dapat dengan mudah dilihat.

- Form GET memiliki batasan jumlah data yang dapat dikirimkan. Sedangkan, form POST dapat mengirim data dengan
jumlah yang besar karena data dikirimkan ke body.

- Form GET digunakan ketika kita tidak ingin mengubah data, seperti pencarian. Sedangkan Form POST dapat kita
gunakan untuk mengubah data yang ada.

---

## Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

Perbedaan utama antara XML, JSON, dan HTML dalam pengiriman data adalah sebagai berikut:

- XML: 
    - XML (eXtensible Markup Language) menyimpan data dalam bentuk mirip sebuah tree yang memiliki satu root. 
    Bentuk dari XML mirip dengan HTML yang memiliki tag-tag. XML memiliki fleksibilitas lebih tinggi, tetapi
    lebih berat secara syntax. XML juga dapat menerima banyak tipe data, seperti images, charts, graph, dan masih banyak lagi.

- JSON: 
    - JSON (Javascript Object Notation) menyimpan data dalam bentuk dictionary objek yang memiliki key dan value. Data-data yang ada dipisah dengan koma. JSON juga lebih mudah dibaca karena strukturnya yang mirip
    dengan objek dalam Javascript.

- HTML: 
    - HTML berfungsi untuk menampilkan data-data yang ada dari JSON atau XML kepada client sehingga dapat dilihat pengguna.

---

## Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

- JSON lebih sering digunakan dalam pertukaran data antara aplikasi web modern karena JSON lebih mudah untuk dibaca dan lebih ringan sehingga lebih cepat. Format JSON juga lebih mudah diparse dan support untuk banyak
bahasa pemograman. Oleh karena itu, JSON lebih banyak digunakan dalam pertukaran data di aplikasi web modern.

---

## Implementasi Form, Views, Routing.

<details>
<summary>Membuat Form</summary>

1. Membuat base HTML template di root folder. Di sini saya menggunakan Tailwind CSS untuk styling
    ```html
    {% load static %}
    {% load static %}
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8" />
            <meta
                name="viewport"
                content="width=device-width, initial-scale=1.0"
            />
            <script src="https://cdn.tailwindcss.com"></script>
            {% block meta %}
            {% endblock meta %}
        </head>

        <body>
            {% block content %}
            {% endblock content %}
        </body>
    </html>
    ```
2. Add ke `settings.py` agar `base.html` visible sebagai templates.
    ```python

    TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
    ]
    ```

3. Membuat file `forms.py` pada direktori main untuk membuat ItemForm yang berisi model dan fields.
    ```python
    from django.forms import ModelForm
    from main.models import Item

    class ItemForm(ModelForm):
        class Meta:
            model = Item
            fields = ["name", "amount", "description","code","price"]
    ```

4. Membuat fungsi baru `create_item` di views.py yang menerima request, mengakses create_item.html, membuat form dengan ItemForm, validasi form, menyimpan form, dan redirect ke halaman main saat berhasil menyimpan data.
    ```python
    ...
    from django.shortcuts import render
    from django.http import HttpResponseRedirect
    from django.urls import reverse
    from django.http import HttpResponse
    from django.core import serializers

    def create_item(request):

    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)
    ```
5. Menambahkan path ke `urls.py` agar `create_item` dapat diakses.
    ```python
    from main.views import show_main, create_item
    path('create-item', create_item, name='create_item'),
    ```
6. Mengubah fungsi `show_main` pada `views.py` dengan memberikan semua item ke dalam context items.
    ```python
    ...
    from main.models import Item
    def show_main(request):
        items = Item.objects.all()
        context = {
            'nama_mahasiswa': 'Venedict Chen',
            'kelas': 'D',
            'items':items,
        }

        return render(request, "main.html", context)
    ```


7. Mengisi `create_item.html` dengan form yang sudah dibuat.
    ```html
    {% extends 'base.html' %} 
    
    {% block content %}
    <div class="flex flex-col items-center text-white t w-full bg-gray-600 h-screen ">
        
        <h5 class="text-3xl text-yellow-300 font-bold text-center mt-10 mb-14">Add New Item</h5>
        
        <div class="mr-20 text-black">
        <form method="POST">
        {% csrf_token %}
        <table>
            {{ form.as_table }}
            <tr>
            <td></td>
            <td >
        <input class="text-black font-semibold mt-10 rounded-lg px-5 bg-white" type="submit" value="Add Item"/>
            </td>
            </tr>
        </table>
    </form>
    </div>
    </div>

    {% endblock %}
    ```
8. Membuat `show_html.html` untuk menunjukkan data. Saya menambahkan back to main menu dan add item.
    ```html
    {% extends 'base.html' %} 

    {% block content %}
    <div class="flex flex-col px-12 py-24 min-h-screen text-white bg-gray-600">
        <h2 class="text-3xl text-yellow-300 font-bold mb-8">Your Items,</h2>
    <table class="table-fixed w-full border-collapse border border-white">
        <thead>
            <tr>
                <th class="border border-white px-4 py-2">Name</th>
                <th class="border border-white px-4 py-2">Amount</th>
                <th class="border border-white px-4 py-2">Description</th>
                <th class="border border-white px-4 py-2">Price</th>
            </tr>
        </thead>
        <tbody>
            {% for item in items %}
                <tr>
                    <td class="border border-white px-4 py-2">{{item.code}} - {{ item.name }}</td>
                    <td class="border border-white px-4 py-2">{{ item.amount }}</td>
                    <td class="border border-white px-4 py-2">{{ item.description }}</td>
                    <td class="border border-white px-4 py-2">{{ item.price }}</td>
                </tr>
            {% endfor %}
        </tbody>
    </table>

    <br />
    <div class="flex flex-row">
    <a href="{% url 'main:show_main' %}">
        <button class="text-black font-semibold rounded-lg bg-white py-2 px-2 mx-6">
            Back to Main Menu
        </button>
    </a>
    <a href="{% url 'main:create_item' %}">
        <button class="text-black rounded-lg font-semibold  bg-white py-2 px-2 mx-6">
            Add Items
        </button>
    </a>
    </div>
    </div>

    {% endblock %}
    ```
</details>
<details>
<summary>Menambahkan Fungsi di views.py</summary>

1. Menambahkan import `HttpResponse` dan `Serializer`.
    ```python
    ...
    from django.http import HttpResponse
    from django.core import serializers
    ```
2. Membuat fungsi untuk `show_html`.
    ```python
    def show_html(request):
        items = Item.objects.all()
        context = {'items':items}
        return render(request,"show_html.html",context)
    ```
3. Membuat fungsi untuk `show_xml` dengan return HttpResponse yang kita serialize dan parameter `content_type="application/xml`.
    ```python
    def show_xml(request):
        data = Item.objects.all()
        return HttpResponse(serializers.serialize("xml",data),content_type = "application/xml")
    ```
4. Membuat fungsi untuk `show_json` dengan return HttpResponse yang kita serialize dan parameter `content_type="application/json`.
    ```python
    def show_json(request):
        data = Item.objects.all()
        return HttpResponse(serializers.serialize("json",data),content_type= "application/json")

    ```
5. Membuat fungsi untuk `show_xml_by_id` dengan return HttpResponse yang kita serialize dan parameter `content_type="application/xml`. Kita filter object berdasarkan id.
    ```python
    def show_xml_by_id(request,id):
        data = Item.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml",data),content_type="application/xml")
    ```
6. Membuat fungsi untuk `show_json_by_id` dengan return HttpResponse yang kita serialize dan parameter `content_type="application/json`. Kita filter object berdasarkan id.
    ```python
    def show_json_by_id(request,id):
        data = Item.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json",data),content_type="application/json")
    ```
</details>

<details>
<summary>Menambahkan Routing di urls.py</summary>

1. Menambahkan import fungsi yang terlah dibuat pada `urls.py` di direktori main.
    ```python
    from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id,show_html
    ```
2. Menambahkan path dengan fungsi yang sudah dibuat sebelumnya. Menambahkan juga `<int:id>` untuk akses by_id.
    ```python
    urlpatterns = [
        path('', show_main, name='show_main'),
        path('create-item', create_item, name='create_item'),
        path('xml/',show_xml,name='show_xml'),
        path('html/',show_html,name='show_html'),
        path('json/',show_json,name='show_json'),
        path('xml/<int:id>/',show_xml_by_id,name='show_xml_by_id'),
        path('json/<int:id>/',show_json_by_id,name='show_json_by_id')
    ]
    ```
</details>

## Screenshot Postman

1. HTML
    - <img src=./images/fotohtml1.png >
    - <img src=./images/fotohtml2.png >
    - <img src=./images/fotohtml3.png >
    - <img src=./images/fotohtml4.png >
    - <img src=./images/fotohtml5.png >

2. XML
    - <img src=./images/fotoxml.png>
    - <img src=./images/fotoxml2.png>

3. JSON
    - <img src=./images/fotojson.png>
    - <img src=./images/fotojson2.png>
    - <img src=./images/fotojson3.png>

4. XML by ID
    - <img src=./images/fotoxmlid.png
5. JSON by ID
    - <img src=./images/fotojsonid.png>