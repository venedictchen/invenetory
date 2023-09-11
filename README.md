# Invenetory App Using Django

# Links
blablabla

Assignment 2 for Platform Based Programming Lecture.

## Making the Django Project
<details>
<summary> Initiate Django Project </summary>

1. Create a new directory named `invenetory`.
    ```sh
    mkdir inventory
    cd inventory
    ```
2. Create new virtual environment.
    ```python
    python -m venv env
    ```
3. Activate virtual environment.
    - Windows:
        ```sh
        env\Scripts\activate.bat or env\Scripts\activate
        ```
    - Unix (Mac/Linux):
        ```sh
        source env/bin/activate
        ```
4. In the same directory make `requirements.txt` and add some dependencies.
    ```python
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ```
5. Install the dependencies with commands below. Don't forget to activate the virtual environment first.
    ```sh
    pip install -r requirements.txt
    ```
6. Make the new Django Project named `invenetory`.
    ```django
    django-admin startproject invenetory .
    ```


</details>
<details>
<summary> Configure and Testing Django Project to know is our Django Project working fine</summary>

1. Add `*` to `ALLOWED_HOST` at `settings.py`.
    ```python
    ...
    ALLOWED_HOSTS = ["*"]
    ...

    ```
2. Run the server to test.
    - Windows:
    ```python
    python manage.py runserver
    ```
    - Unix:
    ```
    ./manage.py runserver
    ```
3. Open `http://localhost:8000` if rocket animation found mean Django Project succesfully worked.

</details>