
# Expense Tracker Backend

A secure FastAPI backend for personal expense management. This application enables users to track, categorize, and analyze their expenses through a clean RESTful API. Built with Python's async capabilities and a robust MySQL database, it provides a solid foundation for expense tracking applications.
## 🚀 Features
User Management
 - Secure Registration & Authentication: Create accounts and authenticate using JWT tokens
 - Profile Management: View and update user information
 - Password Security: Bcrypt hashing with secure password update functionality

Expense Tracking
 - Comprehensive CRUD Operations: Create, read, update, and delete personal expenses
 - Categorization: Organize expenses by custom categories for better financial insights
 - Date-based Recording: Track expenses with specific dates for timeline analysis
 - User-specific Data: All expenses are securely linked to user accounts
Technical Features
 - Asynchronous Architecture: Built with async/await patterns for optimal performance and scalability
 - RESTful API Design: Clean, intuitive API endpoints following REST principles
 - Data Validation: Comprehensive request and response validation using Pydantic
 - CORS Support: Configured for cross-origin requests to work with frontend applications

## 🛠️ Technology Stack
 - FastAPI: Modern, fast web framework for building APIs with Python 
 - SQLAlchemy: SQL toolkit and Object-Relational Mapping (ORM) library
 - Pydantic: Data validation and settings management using Python type annotations
 - MySQL: Relational database for data storage (via aiomysql)
 - JWT: JSON Web Tokens for secure authentication
 - Bcrypt: Password hashing for secure credential storage
 - Uvicorn: ASGI server for serving the FastAPI application

## 🏁 Getting Started
Prerequisites
 - Python 3.7+: Required for FastAPI and async features
 - MySQL Server: Database for storing user and expense data
 - pip: Python package manager for installing dependencies
 - Virtual Environment: Recommended for isolated dependencies
 
    
## Installation

Clone the repository:

```bash
  git clone https://github.com/yourusername/Expense-Tracker-Backend.git
  cd Expense-Tracker-Backend
```

Set up a virtual environment:
```bash
  python -m venv venv

  # On Windows:
  venv\Scripts\activate

  # On macOS/Linux:
  source venv/bin/activate
```

Install dependencies:
```bash
  pip install -r requirements.txt
```

Configure the database:
 - Create a MySQL database
 - Database Schema Overview:
   - Users Table: Stores user account information including username, email, and hashed password.
   - Expenses Table: Stores expense records with a foreign key relationship to the Users table, ensuring each expense belongs to a specific user.

Update the connection string in database.py if needed:
```bash
  DATABASE_URL = "mysql+aiomysql://username:password@localhost/expense_tracker"
```

Run the application:
```bash
  fastapi dev main.py
```

Access the API documentation:
 - Interactive API docs: http://localhost:8000/docs
 - Alternative API docs: http://localhost:8000/redoc

## 📁 Project Structure
```bash
  expense_tracker/
├── main.py           # Application entry point and configuration
├── database.py       # Database connection and session management
├── models.py         # SQLAlchemy ORM models for database tables
├── schemas.py        # Pydantic schemas for request/response validation
├── crud.py           # Database CRUD operations
├── auth.py           # Authentication and authorization logic
└── routers/          # API route modules
    ├── __init__.py   # Package initialization
    ├── users.py      # User-related endpoints
    └── expenses.py   # Expense-related endpoints
```
## Key Components
 - main.py: Configures and initializes the FastAPI application, including middleware and routers
 - database.py: Sets up the database connection and provides session dependency
 - models.py: Defines SQLAlchemy ORM models that map to database tables
 - schemas.py: Contains Pydantic models for request/response validation and serialization
 - crud.py: Implements database operations for users and expenses
 - auth.py: Handles JWT token creation, validation, and user authentication
 - routers/: Contains modular API route definitions separated by resource type

## 🔒 Security Considerations
 - Password Hashing: All passwords are hashed using Bcrypt before storage
 - JWT Authentication: Secure token-based authentication with expiration
 - Resource Protection: Users can only access their own expenses
 - Input Validation: All inputs are validated using Pydantic schemas
 - CORS Configuration: Properly configured for secure cross-origin requests

