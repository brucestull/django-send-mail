# Django Send Mail Example

Example of a simple use of Django's 'send_mail' method.

## Browser Links

* <http://localhost:8000/>

## Creation of this Project

1. Prerequisites:
    * Python
    * Pipenv

1. Add [`.gitignore`](./.gitignore) file to the project root directory:
    * Resources:
        * Choose which types of frameworks, IDEs, etc. to determine ignored files:
            * <https://www.toptal.com/developers/gitignore/>
        * Direct link to the `.gitignore` file for this project:
            * <https://www.toptal.com/developers/gitignore/api/python,django,visualstudiocode>

1. Open a terminal in the project root directory:

    ```powershell
    PS C:\Users\FlynntKnapp\Programming\django-send-mail>
    ```

1. Create a virtual environment for the project and install `django` and `python-dotenv`:
    * `pipenv install django python-dotenv`

        ```powershell
        PS C:\Users\FlynntKnapp\Programming\django-send-mail> pipenv install django python-dotenv
        Loading .env environment variables...
        Creating a virtualenv for this project...
        Pipfile: C:\Users\FlynntKnapp\Programming\django-send-mail\Pipfile
        Using C:/Users/FlynntKnapp/AppData/Local/Programs/Python/Python311/python.exe (3.11.3) to create virtualenv...
        [  ==] Creating virtual environment...created virtual environment CPython3.11.3.final.0-64 in 421ms
        creator CPython3Windows(dest=C:\Users\FlynntKnapp\.virtualenvs\django-send-mail-C_09iW5g, clear=False, no_vcs_ignore=False, global=False)
        seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\FlynntKnapp\AppData\Local\pypa\virtualenv)
            added seed packages: pip==23.0.1, setuptools==67.6.1, wheel==0.40.0
        activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

        Successfully created virtual environment!
        Virtualenv location: C:\Users\FlynntKnapp\.virtualenvs\django-send-mail-C_09iW5g
        Creating a Pipfile for this project...
        Installing django...
        Resolving django...
        Installing...
        Adding django to Pipfile's [packages] ...
        Installation Succeeded
        Installing python-dotenv...
        Resolving python-dotenv...
        Installing...
        Adding python-dotenv to Pipfile's [packages] ...
        Installation Succeeded
        Pipfile.lock not found, creating...                                                                                                                                                
        Locking [packages] dependencies...
        Building requirements...
        Resolving dependencies...
        Success!
        Locking [dev-packages] dependencies...                                                                                                                                             
        Updated Pipfile.lock (ee8f20c4f45059fb7a591579220ccd2990b002ec094c04d8c719ba67e91fa119)!
        Installing dependencies from Pipfile.lock (1fa119)...
        To activate this project's virtualenv, run pipenv shell.
        Alternatively, run a command inside the virtualenv with pipenv run.
        PS C:\Users\FlynntKnapp\Programming\django-send-mail>
        ```

1. Activate the virtual environment:
    * `pipenv shell`

        ```powershell
        PS C:\Users\FlynntKnapp\Programming\django-send-mail> pipenv shell
        Loading .env environment variables...
        Loading .env environment variables...
        Launching subshell in virtual environment...
        PowerShell 7.3.4
        PS C:\Users\FlynntKnapp\Programming\django-send-mail>
        ```

1. Create a Django project:
    * `django-admin startproject config .`

        ```powershell
        PS C:\Users\FlynntKnapp\Programming\django-send-mail> django-admin startproject config .
        PS C:\Users\FlynntKnapp\Programming\django-send-mail>
        ```

1. Open one of the python modules in the project in VS Code:
    * We are opening the [`config/urls.py`](./config/urls.py) module in this example.

1. Ensure focus is in the [`config/urls.py`](./config/urls.py) module in VS Code.

1. Reload VS Code Window so it discovers the new virtual environment:
    1. Open the Command Palette (`Ctrl + Shift + P`)
    1. Select `Developer: Reload Window`

1. Open the Command Palette (`Ctrl + Shift + P`)

1. Select `Python: Select Interpreter`

1. Select the workspace directory.

1. Select the virtual environment created in step 3.

1. Open integrated terminal in project root directory:
    1. `Ctrl + Shift + ~`
    1. Select the workspace directory.

1. Open debug tab:
    * `Ctrl + Shift + D`

1. Add a debug configuration for the workspace directory.

1. Run the debug configuration.

1. Open server root in browser:
    * <http://localhost:8000/>

1. Verify Django Green Rocket is displayed.

1. Use integrated terminal to create a new django app:
    * `django-admin startapp mailer`

        ```powershell
        (django-send-mail) PS C:\Users\FlynntKnapp\Programming\django-send-mail> django-admin startapp mailer      
        (django-send-mail) PS C:\Users\FlynntKnapp\Programming\django-send-mail>
        ```

1. Add a [`.env`](./.env) file to the project root directory:
    * Resource:
        * <https://pypi.org/project/python-dotenv/>

    ```env
    EMAIL_HOST = <your email host>
    EMAIL_PORT = <your email port>
    EMAIL_HOST_USER = <your email host user>
    EMAIL_HOST_PASSWORD = <your email host password>
    ```

1. Add the email configurations to [`config/settings.py`](./config/settings.py) module:
    * Resource:
        * <https://docs.djangoproject.com/en/3.2/topics/email/>

    ```python
    import os
    from dotenv import load_dotenv

    load_dotenv()

    EMAIL_HOST = os.getenv('EMAIL_HOST')
    EMAIL_PORT = os.getenv('EMAIL_PORT')
    EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
    EMAIL_USE_TLS = True
    ```

1. Create a `welcome_email` function in the [`mailer/views.py`](./mailer/views.py) module:
    * Resource:
        * <https://docs.djangoproject.com/en/3.2/topics/email/>

    ```python
    from django.core.mail import send_mail
    from django.http import HttpResponse

    def welcome_email(request):
        send_mail(
            'Welcome to Django',
            'This is a welcome email from Django.',
            'admin@mailer.app',
            [<your mailgun-validated email>],
        )

1. Start Django shell and use the `welcome_email` function to send an email:
    * `python manage.py shell`

    * Commands to paste into the shell:

        ```python
        from django.http import HttpRequest
        from mailer.views import welcome_email
        request = HttpRequest()
        welcome_email(request)
        
        ```

    ```powershell
    (django-send-mail) PS C:\Users\FlynntKnapp\Programming\django-send-mail> python manage.py shell
    Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    (InteractiveConsole)
    >>> from django.core.mail import send_mail
    >>> from django.http import HttpRequest
    >>> from mailer.views import welcome_email
    >>> request = HttpRequest()
    >>> welcome_email(request) 
    <HttpResponse status_code=200, "text/html; charset=utf-8">
    >>>
    ```

## Demonstrate this Project
