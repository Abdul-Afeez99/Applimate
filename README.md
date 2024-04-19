# Applimate
Applimate is an application tracker manager that helps job seekers manage and track their job applications

## Setting Up the Backend on your local environment.
This project uses [Poetry](https://python-poetry.org/) - **A PYTHON PACKAGING AND DEPENDENCY MANAGER**
1. Clone the repository to your PC
2. Run the command below to set up your poetry project
> poetry init
3. Activate the virtual environment using the command below
> poetry shell
4. Install the dependencies on your local env using the command
> poetry install
5. create a .env file to store secret keys and private keys
6. To makemigrations, run
> py manage.py makemigrations
7. To migrate the database, run
> py manage.py migrate
8. To run the server, run
> py manage.py runserver 
