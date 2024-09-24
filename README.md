Inventory API
Stack
Python - 3.10.11
Django - 5.1.1
Database- PostgreSQL
Before attempting below steps make sure you have python installed in your system.

Download python 3.10.11 from here.

Steps to configure Project:
Step 1: Clone project:
Clone the project using below mentioned command.

Using HTTP: git clone https://github.com/Suhas822/inventory_management.git

Using SSH: git clone git@github.com:Suhas822/inventory_management.git

Step 2: Create a virtual env
python -m venv <env-name>

Note: For Debian/Ubuntu based systems you may need to install python3.10-venv

Step 3: Create .env file (Sample file included)
Create an env file and refer to sample.env file to get all the variables and fill them with the required values.

Step 4: Activate virtual environment
First go to the directory where venv is created then run the below command to activate the virtual env

For windows: <env-name>\Scripts\activate

For Linux: source <env-name>\bin\activate

Step 5: Install packages
Use below command to install required packages.

pip install -r requirements.txt

Step 6: Migrate all models to Database
Run the below mentioned command to migrate all database changes.

Setup Your database credentials in settings.py file
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "DATABASE_NAME",
        "USER": "DATABASE_USER",
        "PASSWORD": "DATABASE_PASSWORD",
        "HOST": "DATABASE_HOST",
        "PORT": "DATABASE_PORT",
    }
}
python manage.py migrate

Step 6: Run Django development server
The setup is done now and you can start the development server using below command.

python manage.py runserver
