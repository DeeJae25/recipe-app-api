# Recipe

The Recipe API is a Django Rest Framework (DRF) backend application designed to manage and serve recipe-related data through a RESTful API. This app focuses on providing endpoints for creating, retrieving, updating, and deleting recipes.

The project incorporates Docker for containerization, GitHub for version control, Postman for API testing, Github actions for unit-testing, and various Django features for backend development.

**Technologies:**

- Docker
- Docker Compose
- Django
- Django REST Framework
- Swagger
- PostgreSQL
- Gitub and GitHub actions

### Database Configuration:

PostgreSQL service is configured using Docker Compose.
Django database configuration is set in settings.py, pulling values from environment variables defined in Docker Compose.

### Database Initialization:

Handled race conditions for database initialization to ensure a smooth project startup.

## API Endpoints

### User Authentication

- **Endpoint:** `/api/user/token/`
  - **Method:** POST
  - **Description:** Obtain a token for user authentication.

### User Profile Management
- Configured Django to use a custom user model.
- Normalized email addresses and encrypted passwords for improved security.

- **Endpoint:** `/api/user/create/`
  - **Methods:**
    - POST: Create a new user.
  - **Authentication:** None

- **Endpoint:** `/api/user/me/`
  - **Methods:**
    - GET: Retrieve user profile information.
    - PUT: Update user profile information.
    - PATCH: Update user profile information.
  - **Authentication:** Token-based

### Recipe Management

- **Endpoint:** `/api/recipe/recipes/`
  - With ingredients and tags query that filter out the desired recipe.
  - **Methods:**
    - GET: Retrieve a list of all recipes.
    - POST: Create a new recipe.
  - **Authentication:** Token-based

- **Endpoint:** `/api/recipe/recipes/{id}/`
  - **Methods:**
    - GET: Retrieve details of a specific recipe.
    - PUT: Update information for a specific recipe.
    - DELETE: Delete a specific recipe.
  - **Authentication:** Token-based

- **Endpoint:** `/api/recipe/recipes/{id}/upload-image/`
  - **Methods:**
    - POST: Upload Image of a specific recipe.
  - **Authentication:** Token-based

### Tag Management

- **Endpoint:** `/api/recipe/tags/`
  - **Methods:**
    - GET: Retrieve a list of all tags.
    - POST: Create a new tag.
  - **Authentication:** Token-based

- **Endpoint:** `/api/recipe/tags/{id}/`
  - **Methods:**
    - GET: Retrieve details of a specific tag.
    - PUT: Update information for a specific tag.
    - DELETE: Delete a specific tag.
  - **Authentication:** Token-based

### Ingredient Management

- **Endpoint:** `/api/recipe/ingredients/`
  - **Methods:**
    - GET: Retrieve a list of all ingredients.
    - POST: Create a new ingredient.
  - **Authentication:** Token-based

- **Endpoint:** `/api/recipe/ingredients/{id}/`
  - **Methods:**
    - GET: Retrieve details of a specific ingredient.
    - PUT: Update information for a specific ingredient.
    - DELETE: Delete a specific ingredient.
  - **Authentication:** Token-based

### Additional Features:

- Code refactoring for improved readability.
- Image upload functionality for recipes.
- Volume configuration for efficient static and media file storage.
- Recipe and ingredient filtering by tags and ingredients.
- Customized Open API schema for filter documentation.


## Usage

1. **Authentication:**
   - Obtain an authentication token by sending a POST request to `/api/user/token/` endpoint.

2. **User Profile:**
   - Manage user profile information using the `/api/user/me/` endpoint.

3. **Recipe Management:**
   - Create, retrieve, update, and delete recipes using the `/api/recipe/recipes/` endpoint.

4. **Tag Management:**
   - Manage tags using the `/api/recipe/tags/` endpoint.

5. **Ingredient Management:**
   - Manage ingredients using the `/api/recipe/ingredients/` endpoint.

**Next Steps:**

- Create a frontend to Use these APIs.
- Implement additional features and functionalities.
- Continuously improve code quality and documentation.


![IMG_20240208_014406](https://github.com/DeeJae25/recipe-app-api/assets/91014424/de108add-6158-436e-bfd3-be34be9ab8ee)

# **THANK YOU**
# **HAPPY CODING**

