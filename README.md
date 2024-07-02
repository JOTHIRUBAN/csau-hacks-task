# Expense Manager

## Overview

Expense Manager is a web application designed to help users manage their expenses efficiently. The application allows users to create, view, update, and delete expense records through a user-friendly interface. The backend is built using Express.js and PostgreSQL, while the frontend utilizes Streamlit.

## Features

- **Create Expense**: Users can add new expenses by specifying the name, category, amount, and date.
- **Display Expenses**: View all expenses with options to filter by month and year.
- **Update Expense**: Edit existing expense records.
- **Delete Expense**: Remove expense records from the database.

## Technologies Used

- **Backend**: 
  - Node.js
  - Express.js
  - PostgreSQL
  - Cors
  - Body-Parser

- **Frontend**: 
  - Streamlit
  - Pandas
  - Requests
  - Datetime

## Installation and Setup

### Backend

1. **Clone the repository:**
   ```bash
   git clone https://github.com/JOTHIRUBAN/csau-hacks-task.git
   cd csau-hacks-task/backend
   
2. **Install dependencies:**
   ```bash
    Copy code
    npm install

4. **Set up PostgreSQL database:**

    Ensure PostgreSQL is installed and running. Create a database named postgres and configure the connection in the Pool configuration.
3. **Run the Server**
   ```bash
    node app.js

### Frontend

1. **Navigate to the frontend directory:**
	```bash
		Copy code
		cd ../frontend

2. **Run the Streamlit app:**

   ```bash
		Copy code
		streamlit run app.py
   
The frontend will run on http://localhost:8501.

# API Endpoints

**GET /expenses:** 

Retrieve all expenses.

**POST /expenses:**

Create a new expense.

**PUT /expenses/:id:**

Update an existing expense.

**DELETE /expenses/:id:**

Delete an expense.

# Usage
## Create Expense:

Navigate to the "Create" section.
Fill in the details and click "Add Expense".

## Display Expenses:

Go to the "Display" section.
Filter expenses by month and year if needed.

## Update Expense:

In the "Update" section, click "Edit" next to the expense you want to update.
Modify the details and save.

## Delete Expense:

In the "Delete" section, click "Delete" next to the expense you want to remove.

The backend server will run on http://localhost:3000.


 
