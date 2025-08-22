Farm Inventory & Sales Tracker API 🧑‍🌾💰
Welcome to the Farm Inventory & Sales Tracker API! This project is a backend solution built with Django and Django REST Framework (DRF) to help manage farm products, track sales, and handle different user roles (Admin, Farmer, Customer).

📝 Project Description
This API provides a robust backend for a farm management system. It allows for the creation, tracking, and management of farm products and their sales. Key functionalities include distinct user roles to control access and data manipulation, ensuring that each type of user (Admin, Farmer, Customer) has appropriate permissions.

✨ Features
Custom User Model: Extends Django's AbstractUser with a role field (admin, farmer, customer).
Product Management: API endpoints for managing farm products (create, view, update, delete).
Sales Tracking: API endpoints for recording and viewing sales transactions.
Role-Based Access Control (RBAC):
Admins: Full CRUD access to all users, products, and sales.
Farmers: CRUD access to their own products, read-only access to relevant sales.
Customers: Read-only access to products, no direct access to sales.
Authentication: Token-based authentication using DRF.
Django Admin: Fully integrated admin interface for easy data management.