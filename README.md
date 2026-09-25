# 🚆 Railway Reservation System

A simple **Railway Reservation System** developed using **Python, Streamlit, and SQLite3**.

This application allows users to book railway tickets by entering passenger and journey details. The fare is calculated automatically based on the selected class and number of seats. All booking information is stored in an SQLite database and can be retrieved through the application.

## 📌 Project Overview

The main purpose of this project is to create a simple railway booking system where users can:

* Enter passenger details
* Select a train
* Select source and destination
* Choose journey date
* Select seat class
* Enter number of seats
* Calculate the total fare
* Store booking details in SQLite3
* Search bookings using Booking ID
* View all bookings
* Cancel a booking

## 🛠️ Technologies Used

* **Python**
* **Streamlit**
* **SQLite3**

## 📂 Project Structure

```text
Railway_Reservation/
│
├── app.py
├── railway.db
└── README.md
```

> `railway.db` is automatically created when the application is run for the first time.

## ✨ Features

### 1. Book Ticket

Users can enter:

* Passenger Name
* Phone Number
* Email
* Train Name
* Source
* Destination
* Journey Date
* Seat Class
* Number of Seats

The application calculates the fare automatically.

### 2. Fare Calculation

The fare depends on the selected class.

| Class          | Fare per Seat |
| -------------- | ------------: |
| Sleeper        |          ₹500 |
| AC 3 Tier      |         ₹1000 |
| AC 2 Tier      |         ₹1500 |
| AC First Class |         ₹2500 |

The total fare is calculated as:

```text
Total Fare = Number of Seats × Fare per Seat
```

### 3. Store Booking

After successful booking, the details are stored in the SQLite database.

Each booking receives a unique **Booking ID**.

### 4. Search Booking

Users can enter their Booking ID to retrieve their booking details.

The application displays:

* Passenger details
* Train details
* Journey details
* Seat class
* Number of seats
* Fare
* Booking status

### 5. View All Bookings

All bookings stored in the database can be viewed from the application.

### 6. Cancel Booking

Users can enter a Booking ID and cancel the ticket.

The booking status changes from:

```text
Confirmed
```

to:

```text
Cancelled
```

The booking record remains stored in the database.

## 🗄️ Database

The project uses **SQLite3** for storing booking information.

The main table is:

### `bookings`

| Column         | Description            |
| -------------- | ---------------------- |
| booking_id     | Unique booking ID      |
| passenger_name | Name of passenger      |
| phone          | Passenger phone number |
| email          | Passenger email        |
| train_name     | Selected train         |
| source         | Starting station       |
| destination    | Destination station    |
| journey_date   | Date of journey        |
| seat_class     | Selected class         |
| seats          | Number of seats        |
| fare_per_seat  | Fare for one seat      |
| total_fare     | Total booking fare     |
| booking_status | Confirmed or Cancelled |

## ▶️ How to Run the Project

### Step 1: Install Python

Make sure Python is installed on your computer.

Check it using:

```bash
python --version
```

### Step 2: Install Streamlit

Open Command Prompt or Terminal and run:

```bash
pip install streamlit
```

SQLite3 is included with Python, so no separate installation is required.

### Step 3: Open the Project Folder

Go to the project folder:

```bash
cd Railway_Reservation
```

### Step 4: Run the Application

Run:

```bash
streamlit run app.py
```

The application will open in your browser.

## 🔄 Application Flow

```text
User
  ↓
Enter Passenger Details
  ↓
Select Train & Journey Details
  ↓
Select Class & Number of Seats
  ↓
Fare Calculation
  ↓
Confirm Booking
  ↓
Store Data in SQLite3
  ↓
Generate Booking ID
  ↓
Search / View / Cancel Booking
```

## 📸 Main Application Sections

The application contains four main sections:

```text
1. Book Ticket
2. Search Booking
3. View All Bookings
4. Cancel Booking
```

## 🎯 Project Objective

The objective of this project is to understand how a Python-based web application can interact with a database.

Through this project, I worked with:

* Streamlit UI components
* Python functions and conditions
* SQLite3 database
* SQL `INSERT` queries
* SQL `SELECT` queries
* SQL `UPDATE` queries
* Database transactions using `commit()`
* Retrieving data from a database
* Basic application and database integration

## 🚀 Future Improvements

Some features that can be added in the future:

* User login and registration
* Train management
* Real-time seat availability
* Prevent booking more seats than available
* PNR generation
* Payment system
* Ticket download as PDF
* Different fares based on route
* Passenger-wise booking history
* Admin dashboard
* Booking date and time
* Improved UI and ticket confirmation page

## 👩‍💻 Author

**Sanchita Hasure**

B.Sc. Mathematics | Data Science & Data Analytics

Skills: Python, SQL, Excel, Power BI, Tableau


[alt text](diagram.png)