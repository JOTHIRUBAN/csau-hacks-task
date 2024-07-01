import streamlit as st
import requests
import pandas as pd
from datetime import datetime


BASE_URL = "http://localhost:3000/expenses"


if "editing" not in st.session_state:
    st.session_state.editing = {}


def main():
    st.title("Expense Manager")
    page = st.sidebar.radio("Choose an action", ("Create", "Display", "Update", "Delete"))

    if page == "Create":
        st.subheader("Create a New Expense")
        expense_name = st.text_input("Expense Name")
        expense_category = st.text_input("Expense Category")
        amount = st.number_input("Amount", min_value=0.0)
        expense_date = st.date_input("Expense Date")
        if st.button("Add Expense"):
            new_expense = {
                "expense_name": expense_name,
                "expense_category": expense_category,
                "amount": amount,
                "expense_date": str(expense_date)
            }
            response = requests.post(BASE_URL, json=new_expense)
            if response.status_code == 201:
                st.success("Expense added successfully!")
            else:
                st.error("Error adding expense")

    elif page == "Display":
        st.subheader("All Expenses")

        response = requests.get(BASE_URL)
        if response.status_code == 200:
            expenses = response.json()

           
            months = ["All"] + list(range(1, 13))
            years = ["All"] + list(set(expense["expense_date"].split("-")[0] for expense in expenses))
            month = st.selectbox("Select Month", options=months, index=0)
            year = st.selectbox("Select Year", options=years, index=0)

           
            filtered_expenses = expenses
            if month != "All":
                filtered_expenses = [expense for expense in filtered_expenses if datetime.strptime(expense["expense_date"], "%Y-%m-%d").month == month]
            if year != "All":
                filtered_expenses = [expense for expense in filtered_expenses if expense["expense_date"].split("-")[0] == year]

           
            for ex in filtered_expenses:
                del ex['id']
            if filtered_expenses:
                df = pd.DataFrame(filtered_expenses)
                st.table(df)
            else:
                st.write("No expenses found for the selected period.")
        else:
            st.error("Error fetching expenses")

    elif page == "Update":
        st.subheader("Update an Expense")

        response = requests.get(BASE_URL)
        if response.status_code == 200:
            expenses = response.json()

            for expense in expenses:
                col1, col2, col3, col4, col5 = st.columns(5)
                col1.write(expense["expense_name"])
                col2.write(expense["expense_category"])
                col3.write(expense["amount"])
                col4.write(expense["expense_date"])
                if col5.button("Edit", key=f"edit_{expense['id']}"):
                    st.session_state.editing[expense["id"]] = True

            for expense in expenses:
                if st.session_state.editing.get(expense["id"], False):
                    expense_name = st.text_input("Expense Name", value=expense["expense_name"], key=f"name_{expense['id']}")
                    expense_category = st.text_input("Expense Category", value=expense["expense_category"], key=f"cat_{expense['id']}")
                    amount = st.number_input("Amount", value=float(expense["amount"]), key=f"amt_{expense['id']}")  # Convert to float
                    expense_date = st.date_input("Expense Date", value=datetime.strptime(expense["expense_date"], "%Y-%m-%d").date(), key=f"date_{expense['id']}")
                    if st.button("Save", key=f"save_{expense['id']}"):
                        updated_expense = {
                            "expense_name": expense_name,
                            "expense_category": expense_category,
                            "amount": amount,
                            "expense_date": str(expense_date)
                        }
                        response = requests.put(f"{BASE_URL}/{expense['id']}", json=updated_expense)
                        if response.status_code == 200:
                            st.success("Expense updated successfully!")
                            st.session_state.editing[expense["id"]] = False
                            st.experimental_rerun() 
                        else:
                            st.error("Error updating expense")

    elif page == "Delete":
        st.subheader("Delete an Expense")

        response = requests.get(BASE_URL)
        if response.status_code == 200:
            expenses = response.json()

            for expense in expenses:
                col1, col2, col3, col4, col5 = st.columns(5)
                col1.write(expense["expense_name"])
                col2.write(expense["expense_category"])
                col3.write(expense["amount"])
                col4.write(expense["expense_date"])
                if col5.button("Delete", key=f"del_{expense['id']}"):
                    response = requests.delete(f"{BASE_URL}/{expense['id']}")
                    if response.status_code == 204:
                        st.success("Expense deleted successfully!")
                        st.experimental_rerun()  
                    else:
                        st.error("Error deleting expense")

if __name__ == "__main__":
    main()
