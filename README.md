This is a Django-based project that utilizes JWT authentication, API documentation with Swagger, and includes core apps like authentication and orders. The project uses the Django REST Framework (DRF) for API management, and integrates third-party tools such as djoser and drf_yasg for authentication and API schema/documentation generation.

## Features
- JWT Authentication using rest_framework_simplejwt ( https://django-rest-framework-simplejwt.readthedocs.io/en/latest/ )
- API Documentation using Swagger (drf_yasg)  ( https://drf-yasg.readthedocs.io/en/stable/ )
- Custom User Model in the authentication app
- Modular App Structure with apps like authentication and orders

## Installation

####Clone the repository:


```bash
git clone DRF_api_restaurant-pizza
cd DRF_api_restaurant-pizza
```
####Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
####Install dependencies:

```bash
pip install -r requirements.txt
```

## API Documentation
Swagger-based API documentation is available once the server is running. Access it at /swagger/ or /redoc/ for different API views.
