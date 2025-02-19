# EC530_HW2

This project defines a set of RESTful APIs for managing **Users**, **Houses**, **Rooms**, and **Devices**. The focus is on API design, input validation, and error handling. It also includes unit tests and a GitHub Actions workflow for continuous integration.

## API Definitions

### Users
- **POST /users**: Create a new user.
- **GET /users/{user_id}**: Retrieve user details.

**Data Model:**
```json
{
    "id": "integer, unique",
    "username": "string, minimum 3 characters",
    "email": "string, valid email format"
}
