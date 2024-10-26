# Django Shopify App

This project is a Django-based application for managing products and customers for a Shopify e-shop. It provides basic CRUD operations for `Product` and `Customer` models through RESTful API endpoints. The application is designed to be hosted on AWS Elastic Beanstalk and uses MySQL on AWS RDS for data storage.

## Project Structure

- **Repository Name**: `django-spotify-app`
- **Poetry Project Name**: `shopify-app`
- **Django Project Name**: `shopify_app`
- **Database**: MySQL on AWS RDS (configured for production); local MySQL database used for development.

## Setup and Configuration

### 1. Initial Setup

- **Django Setup**: Created a Django project named `shopify_app`.
- **Poetry**: Used Poetry for package management and dependency handling.
- **MySQL Configuration**:
  - Configured a local MySQL database for development.
  - Set up a MySQL RDS instance on AWS for deployment.
  - Configured environment-specific database settings for local and production use.
    ```
    CREATE DATABASE shopifydb CHARACTER SET UTF8;
    CREATE USER 'my_local_user'@'localhost' IDENTIFIED BY 'my_local_password'; #in case you want your own user/password
    GRANT ALL PRIVILEGES ON my_local_db.* TO 'my_local_user'@'localhost';
    FLUSH PRIVILEGES; 
    ```
   - Replace `my_local_db`, `my_local_user`, and `my_local_password` with your chosen database name, username, and password.

### 2. Models

Created models for:
- **Product**: Stores information about products, including `title`, `description`, `price`, and `stock_quantity`.
- **Customer**: Stores customer details, including `first_name`, `last_name`, and `email`.

### 3. CRUD API Endpoints

Using Django REST Framework, we implemented the following API endpoints:

#### Product Endpoints

- **POST** `/products/` - Create a new product
- **GET** `/products/<pk>/` - Retrieve a product by ID
- **PUT** `/products/<pk>/update/` - Update a product by ID
- **DELETE** `/products/<pk>/delete/` - Delete a product by ID

#### Customer Endpoints

- **POST** `/customers/` - Create a new customer
- **GET** `/customers/<pk>/` - Retrieve a customer by ID
- **PUT** `/customers/<pk>/update/` - Update a customer by ID
- **DELETE** `/customers/<pk>/delete/` - Delete a customer by ID

### 4. Testing with Sample Data

- Added sample entries for both `Product` and `Customer` to test the endpoints and confirm functionality.
- Set up the Django admin interface for managing products and customers.

## Next Steps

1. **Deploy to AWS Elastic Beanstalk**: Configure and deploy the application to AWS Elastic Beanstalk, setting up environment variables and database connections.
2. **Enhance API Functionality**:
   - Implement additional fields and business logic for the `Product` and `Customer` models as needed.
   - Add more complex queries and filtering options to the API endpoints.
3. **Integrate with Shopify API**:
   - Set up API calls to interact with Shopify’s API, enabling synchronization of products and orders.
4. **Add Authentication**:
   - Implement user authentication (e.g., token-based or OAuth) for secure access to the API endpoints.
5. **Error Handling and Validation**:
   - Improve validation and error handling for robustness in production.

## Requirements

- **Python**: 3.12+
- **Django**: 5.x
- **Django REST Framework**: Installed via Poetry
- **MySQL**: Local MySQL for development, AWS RDS MySQL for production

## Running the Application

### Local Development

1. **Set up a virtual environment** with Poetry:
```
poetry install
django-shopify-app
```

2. Run migrations:
```
python manage.py migrate
```

3. Start the development server:
``` 
python manage.py runserver
```

### API Testing
```
The CRUD endpoints can be tested using tools like curl, Postman, or by directly accessing URLs with sample data:

Example: http://127.0.0.1:8000/product/1
```