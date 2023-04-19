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
        [ ===] Creating virtual environment...created virtual environment CPython3.11.3.final.0-64 in 3255ms
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

    * `django` is our web framework.
    * `python-dotenv` is a package that allows us to load environment variables from a `.env` file. This will be used in our development environment to store our email credentials. We will explore how to send email in production in a later tutorial.

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

1. Reload Window of VS Code so it discovers the new virtual environment:
    1. Open the Command Palette (`Ctrl + Shift + P`)
    1. Select `Developer: Reload Window`

1. Open the Command Palette (`Ctrl + Shift + P`)

1. Select `Python: Select Interpreter`

1. Select the workspace directory.

1. Select the virtual environment created in step 3.

1. Ensure the virtual environment is indicated in the status bar when [`config/urls.py`](./config/urls.py), or one of the other python modules, is in focus.

1. Open integrated terminal in project root directory:
    1. `Ctrl + Shift + ~`
    1. Select the workspace directory.

        ```powershell
        PS C:\Users\FlynntKnapp\Programming\django-send-mail> & C:/Users/FlynntKnapp/.virtualenvs/django-send-mail-C_09iW5g/Scripts/Activate.ps1
        (django-send-mail) PS C:\Users\FlynntKnapp\Programming\django-send-mail>
        ```

1. Verify the Django basic skeleton app runs on development server (optional):

    1. Open debug tab:
        * `Ctrl + Shift + D`

    1. Add a debug configuration for the workspace directory.

    1. Run the debug configuration.

    1. Open server root in browser:
        * <http://localhost:8000/>

    1. Verify Django Green Rocket is displayed.

    1. Stop the debug configuration server.

1. Use integrated terminal to create a new django app.

1. Create a django app, `mailer` for use with the project `config` module:
    * `django-admin startapp mailer`

        ```powershell
        (django-send-mail) PS C:\Users\FlynntKnapp\Programming\django-send-mail> django-admin startapp mailer      
        (django-send-mail) PS C:\Users\FlynntKnapp\Programming\django-send-mail>
        ```

1. Add a [`.env`](./.env) file to the project root directory:
    * Resource:
        * <https://pypi.org/project/python-dotenv/>
    * This file will contain the email credentials for the development environment.
    * This file will contain a mailgun-validated email address, which we have already validated with mailgun. NOTE: Instructions for validating an email address with mailgun are not included in this tutorial.

    ```env
    EMAIL_HOST = <your email host>
    EMAIL_PORT = <your email port>
    EMAIL_HOST_USER = <your email host user>
    EMAIL_HOST_PASSWORD = <your email host password>

    MY_VALIDATED_EMAIL = <your email validated by mailgun>
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
    # Import the `send_mail` function so we can use it to send an email
    from django.core.mail import send_mail
    # Import the `os` module so we can use it to access environment variables
    import os

    def welcome_email(request):
        """
        Use the `send_mail` function to send an email to a user's mailgun-validated email address.

        The arguments are as follows:
        * `subject` - The subject of the email
        * `message` - The body of the email
        * `from_email` - The email address of the sender
        * `recipient_list` - A list of email addresses of the recipients
            * This example uses only one email address, which is retrieved via the environment variable `MY_VALIDATED_EMAIL`.
        """

        # Call Django's `send_mail` function to send an email
        send_mail(
            # `subject`
            'Welcome to Django - In Subject',
            # `message`
            'This is a welcome email from Django - In Body',
            # `from_email`
            'admin@fakeemail.app',
            # `recipient_list`
            [os.getenv('MY_VALIDATED_EMAIL')],
        )
    ```

1. Start Django shell and use the `welcome_email` function to send an email:
    * `python manage.py shell`

    1. Commands to paste into the shell:

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
    >>> from django.http import HttpRequest
    >>> from mailer.views import welcome_email
    >>> request = HttpRequest()
    >>> welcome_email(request)
    >>>
    ```

## Demonstrate this Project
