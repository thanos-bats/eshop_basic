# SQL Queries Documentation

This document contains all the SQL queries used in the application, particularly for the dashboard statistics and other operations.

## Table Creation

### Users Table
```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(80) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    is_admin BOOLEAN DEFAULT FALSE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_username (username),
    INDEX idx_is_admin (is_admin),
    INDEX idx_username_is_admin (username, is_admin)
);
```

### Products Table
```sql
CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(80) UNIQUE NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_name (name),
    INDEX idx_stock (stock),
    INDEX idx_name_stock (name, stock)
);
```

### Purchases Table
```sql
CREATE TABLE purchases (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    INDEX idx_user_id (user_id),
    INDEX idx_created_at (created_at),
    INDEX idx_user_created (user_id, created_at)
);
```

### Purchase Products
```sql
CREATE TABLE purchase_products (
    purchase_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (purchase_id, product_id),
    FOREIGN KEY (purchase_id) REFERENCES purchases(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);
```

## SQL Queries

1. **Get Total Products Count**
```sql
SELECT COUNT(*) as total_products
FROM products;
```

2. **Get Available Products Count**
```sql
SELECT COUNT(*) as available_products
FROM products
WHERE stock > 0;
```

3. **Get Out of Stock Products Count**
```sql
SELECT COUNT(*) as out_of_stock_products
FROM products
WHERE stock = 0;
```

4. **Get Top 2 Most Purchased Products**
```sql
SELECT 
    p.id,
    p.name,
    p.price,
    SUM(pp.quantity) as total_quantity_sold
FROM products p
JOIN purchase_products pp ON p.id = pp.product_id
GROUP BY p.id, p.name, p.price
ORDER BY total_quantity_sold DESC
LIMIT 2;
```

5. **Get Total Purchases Count**
```sql
SELECT COUNT(*) as total_purchases
FROM purchases;
```

6. **Get Total Revenue**
```sql
SELECT COALESCE(SUM(total_amount), 0) as total_revenue
FROM purchases;
```

7. **Get Total Stock Across All Products**
```sql
SELECT COALESCE(SUM(stock), 0) as total_stocks
FROM products;
```

8. **Check if Username Exists**
```sql
SELECT COUNT(*) as user_count
FROM users
WHERE username = %s;
```

9. **Get User by Username**
```sql
SELECT *
FROM users
WHERE username = %s;
```

10. **Get All Products**
```sql
SELECT id, name, price, stock, created_at
FROM products;
```

11. **Get Product by ID**
```sql
SELECT id, name, price, stock, created_at
FROM products
WHERE id = %s;
```

12. **Update Product Stock**
```sql
UPDATE products
SET stock = stock - %s
WHERE id = %s AND stock >= %s;
```

13. **Get User's Purchase History**
```sql
SELECT 
    p.id,
    p.total_amount,
    p.created_at,
    pp.product_id,
    pp.quantity,
    pp.price
FROM purchases p
JOIN purchase_products pp ON p.id = pp.purchase_id
WHERE p.user_id = %s;
```

14. **Create New Purchase**
```sql
INSERT INTO purchases (user_id, total_amount, created_at)
VALUES (%s, %s, NOW());

INSERT INTO purchase_products (purchase_id, product_id, quantity, price)
VALUES (%s, %s, %s, %s);
```

## Note
The `%s` placeholders are replaced with actual values when executed
