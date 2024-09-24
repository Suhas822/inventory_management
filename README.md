# Inventory API

### Stack
- **Python**: 3.10.11
- **Django**: 5.1.1
- **Database**: PostgreSQL

> **Note**: Ensure you have Python installed on your system before proceeding.

### Steps to Configure the Project

#### Step 1: Clone the Project
Clone the project using the following command:

- Using HTTP: 
  ```bash
  git clone https://github.com/Suhas822/inventory_management.git

- Using SSH: 
    ```bash
  git clone git@github.com:Suhas822/inventory_management.git
Step 2: Create a virtual env
python -m venv <env-name>

Note: For Debian/Ubuntu based systems you may need to install python3.10-venv



Step 3: Activate virtual environment
First go to the directory where venv is created then run the below command to activate the virtual env
    ```bash
        For windows: <env-name>\Scripts\activate
    ```bash
        For Linux: source <env-name>\bin\activate

Step 4: Install packages
Use below command to install required packages.

pip install -r requirements.txt

Step 5: Migrate all models to Database
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


### API 
- # register/ #
- # login/ #
- # token/refresh/ #
- # items/#
- # items/<int:pk>/#