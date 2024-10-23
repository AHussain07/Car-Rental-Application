# Car Rental and Listing System

## Overview
This project is a **Car Rental and Listing System** developed using Python's **Tkinter** for the graphical user interface (GUI) and **SQLite** for database management. It allows users to sign up, log in, hire cars, and list their cars for others to rent. The app includes several features like filtering cars by price and duration, managing bookings, and rating rented cars.

## Technologies Used
- **Python 3.x**: The primary programming language used to build the application.
- **Tkinter**: For building the GUI of the application.
- **SQLite**: A lightweight, disk-based database used to store user information, car listings, bookings, and reviews.
- **Pillow (PIL)**: Used for handling images within the application (if image handling is included).
- **ttk**: Part of Tkinter, used for enhanced treeview for listings.

## Features
- **User Authentication**: Login and signup functionality to allow users to securely access the system.
- **Car Listing**: Users can list their cars for rent, specifying details such as brand, model, location, price, and duration.
- **Car Hiring**: Users can browse available cars, apply filters (by price or duration), and hire cars if available.
- **Bookings Management**: Users can view their bookings, cancel them, and rate the cars they've rented.
- **Ratings & Reviews**: The app allows users to give ratings for cars they have hired, which are displayed for others to see.

## Prerequisites
To run this project, you need the following installed on your system:
- **Python 3.x**
- **Tkinter** (comes pre-installed with Python)
- **SQLite3** (comes pre-installed with Python)
- **Pillow** (if images are used)

## How to Download and Run the Project

1. **Clone the Repository**:
   If the project is hosted on a version control system like GitHub, clone it using:
   ```bash
   git clone https://github.com/AHussain07/Car-Rental-Application.git
   ```
   If you have the files locally, ensure all the files are placed in the same directory.
   
3. **Install Required Dependencies**:
   You need to install any dependencies like Pillow (if used). You can install it using pip:
   ```bash
   pip install Pillow
4. ***Run the Application***:
   After ensuring all dependencies are installed, navigate to the project directory and run the application:
   ```bash
   python index.py

## Testing the Project

1. **Signup**: When you first run the program, create a new account by clicking the "JOIN" button and filling in the required information.
2. **Login**: Use the login functionality to sign in using your credentials.
3. **Hiring a Car**: After logging in, browse available cars and hire one by selecting it and confirming the booking.
4. **Listing a Car**: If you own a car, you can list it for others to rent.
5. **Bookings & Reviews**: Check the bookings section to manage your bookings or leave a review for a car you rented.
6. **Exiting**: Click "EXIT" to close the application.

## Database Management

The project uses SQLite for data storage. The database file `CAR DB.db` manages:
- **USER_INFO**: Stores user details like username, password, address, and ID.
- **CARS_LISTED**: Contains details of cars listed for hire.
- **BOOKINGS**: Manages the records of car hires.
- **REVIEWS**: Stores the ratings and reviews left by users for cars they've rented.

  
   
