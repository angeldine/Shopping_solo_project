# A Shopping Solo Project in Python with Django
A Python Django driven shopping website for Furniture sales. The datasource contains 2000 records of products, customer, order and shipping details.
The data was gotten from Kaggle open datat source. The products are of different categories and they are displayed on the 
home page for users to view, add to cart and make payment.  The Model-View-Template architecture pattern has been followed. 
The database used in this application is SQLite3. Chart.js packages have been used to perform data visualization.


## Production and Repo links to the web application
Github Repository: git@github.com:angeldine/Shopping_solo_project.git
Render : https://shopping-solo-project.onrender.com

## Features of the application.
This is a Django based web application of a Furniture Store named Diamondz Furnitures. This store allows guest to view products available in the store, but only registered customers and admin can
make purchases from the store. There is a login page to login into your account or register if you are a new user.
Once logged in users can have access to store products and functions like adding products to cart, viewing and checking out.
Staff users can view dashboard information, add products and delete products.
Below highlights detailed guidelines of how to configure the application.

## Set up your environment
        git clone git@github.com:angeldine/Shopping_solo_project.git
        source .venv/bin/activate # this activates the virtual environment
        pip install --upgrade pip [ this is optional]  # this installs pip, and upgrades it if required.


## You need to create an admin account
        python3 manage.py createsuperuser
        follow the instructions to add username, email and password.
        Once successful, go ahead and run the server

## To run the server:
        python3 manage.py runserver
## To run the server in Codio:
        python3 manage.py runserver 0.0.0.0:8000



## Requirements

All the packages and libraries required for this application to run can be found in requirements.txt file.

## Demo

The application is deployed and you can find it using the below link:
[Shopping_solo_project](https://shopping-solo-project.onrender.com)
