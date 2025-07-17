# Heroes-And-Villains-Lab

**Developed at devCodeCamp**

A Django REST Framework web application for managing a database of superheroes and villains. This project implements full CRUD functionality with models linked by an Entity Relationship Diagram (ERD), enabling interaction through a RESTful API.

---

## Description

The application includes two main models—`Super` and `SuperType`—with a defined relationship. It supports CRUD operations on both models via API endpoints, allowing creation, retrieval, updating, and deletion of superhero and villain records. The API supports filtering supers by type (hero or villain) through query parameters.

---

## Features

- Web application implementing a RESTful API  
- Entity Relationship Diagram (ERD) guiding database design  
- Full CRUD functionality for supers and super types  
- Filtering and custom JSON responses  
- Admin site integration with seeded roles  
- Comprehensive API tested with Postman

---

## Technologies Used

- Python 3  
- Django  
- Django REST Framework  
- MySQL  
- Postman (API testing)

---

## Setup & Installation

1. **Clone the repository:**
    ```
    git clone https://github.com/thompsonmikej/Heroes-And-Villains-Lab.git
    cd Heroes-And-Villains-Lab
    ```

2. **Create and activate a virtual environment:**
    ```
    pipenv install
    pipenv shell
    ```

3. **Install dependencies:**
    ```
    pipenv install django djangorestframework mysqlclient mysql-connector-python==8.0.26
    ```

4. **Start Django project and apps:**
    ```
    django-admin startproject heroes_villains_project 
    python manage.py startapp supers
    python manage.py startapp super_types
    ```

5. **Configure database connection:**  
   - Create a `local_settings.py` file to keep sensitive data out of source control.  
   - Move `DATABASES` and `SECRET_KEY` settings from `settings.py` to `local_settings.py` and update credentials accordingly.

6. **Apply migrations:**
    ```
    python manage.py migrate
    ```

7. **Create a superuser and seed data:**
    ```
    python manage.py createsuperuser
    ```
    - Seed `SuperType` table with `"Hero"` and `"Villain"`.

8. **Run the development server:**
    ```
    python manage.py runserver
    ```

---

## Usage

- Access API endpoints to create, retrieve, update, or delete supers and super types.  
- Use query parameters to filter supers by type.  
- Manage data via the Django admin interface.  
- Test requests with Postman using the provided collection.

---

## Challenges & Lessons Learned

- Designed a clear data model using ERDs.  
- Built RESTful APIs with Django REST Framework, including filtering and custom responses.  
- Integrated database-backed applications with admin site and seed data.  
- Practiced secure project setup and dependency management with pipenv.

---

## Future Improvements

- Add authentication and permission layers to the API.  
- Implement pagination and ordering to enhance API usability.  
- Expand data models with related features (e.g., powers, alliances).  
- Create frontend UI consuming the REST API.

---

## Author

Feel free to reach out or connect:

**Michael Thompson**  
https://www.linkedin.com/in/thompsonmikej  
