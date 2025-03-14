# E-Shop Basic Application

This application provides basic eshop functionality including user management, product management, and purchase handling.
Is built with Python Flask, MySQL, and Docker.

## Architecture

The application consists of three main components:

1. **API Service** (Flask)
   - Handles HTTP requests
   - Provides RESTful endpoints for user management, products, purchases, and statistics

2. **Database Service** (MySQL)
   - Stores all application data
   - Runs MySQL 8.0.33

3. **Database Initialization Service**
   - Runs once to set up the initial database schema
   - Creates necessary tables and initial data

## Running the Application

Create a `.env` file in the root directory with the following variables:

```env
DB_PASS=your_password
DB_NAME=eshop
DB_HOST=localhost
DB_USER=root
JWT_SECRET_KEY=your_jwt_secret
```
### Using Docker

1. Build and start all services:
```bash
docker-compose up -d
```

2. The application will be available at:
   - API: http://localhost:3000
   - Database: localhost:3306

### Local Development

#### Requirements

- Docker Engine
- Python 3.9
- MySQL

1. Install Python dependencies in both folders:
```bash
# Install database dependencies
cd database
pip install -r requirements.txt

# Install API dependencies
cd ../eshop_api
pip install -r requirements.txt
```

2. Start MySQL locally
3. Run the database initialization script:
```bash
cd database
python init_db.py
```

4. Start the Flask application:
```bash
cd eshop_api
python app.py
```

## API Endpoints

### User management
- `POST /register` - Register a new user
- `POST /login` - Login user and get JWT token

### Products
- `GET /products` - Get all products
- `GET /public/dashboard` - Get public dashboard statistics including:
  - Total number of products
  - Number of available products
  - Number of out-of-stock products
  - Top 2 most purchased products with their total quantities sold

### Purchases
- `GET /purchases` - Get user's purchase history
- `POST /purchase` - Create new purchase
- `GET /admin/dashboard` - Get admin dashboard statistics (requires admin access) including:
  - Total number of purchases
  - Total revenue
  - Total stock across all products