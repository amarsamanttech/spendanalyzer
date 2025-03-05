import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("My Spend Analyzer")
st.write("Analyze your spending habits and spot leaks—upload your data or use our sample!")

# Dummy data reflecting Indian spending
data = pd.DataFrame({
    "Date": ["2025-02-01", "2025-02-02", "2025-02-03", "2025-02-04", "2025-02-05",
             "2025-02-06", "2025-02-07", "2025-02-08", "2025-02-09", "2025-02-10"],
    "Description": ["Dmart", "Auto fare", "Restaurant", "Electricity bill", "Movie ticket",
                    "Online shopping", "Groceries", "Taxi", "Dinner", "Phone bill"],
    "Category": ["Groceries", "Transportation", "Dining Out", "Utilities", "Entertainment",
                 "Shopping", "Groceries", "Transportation", "Dining Out", "Utilities"],
    "Amount": [500, 100, 300, 800, 200, 1500, 400, 150, 400, 600]
})
data["Date"] = pd.to_datetime(data["Date"])

# Let users upload their own CSV
uploaded_file = st.file_uploader("Upload your CSV (columns: Date, Description, Category, Amount)", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file, parse_dates=["Date"])

# Total spending
total_spending = data["Amount"].sum()
st.write(f"**Total Spending**: ₹{total_spending}")

# Bar chart: Spending by category
category_spending = data.groupby("Category")["Amount"].sum().sort_values(ascending=False)
fig1, ax1 = plt.subplots()
category_spending.plot(kind="bar", ax=ax1, color="skyblue")
ax1.set_title("Spending by Category")
ax1.set_xlabel("Category")
ax1.set_ylabel("Amount (INR)")
plt.xticks(rotation=45)
st.pyplot(fig1)

# Line chart: Daily spending trend
daily_spending = data.groupby("Date")["Amount"].sum()
fig2, ax2 = plt.subplots()
daily_spending.plot(kind="line", ax=ax2, marker="o", color="green")
ax2.set_title("Daily Spending Trend")
ax2.set_xlabel("Date")
ax2.set_ylabel("Amount (INR)")
plt.xticks(rotation=45)
st.pyplot(fig2)

# Spot spending leaks (top 3 categories)
st.write("**Potential Spending Leaks**:")
top_categories = category_spending.head(3)
suggestions = {
    "Shopping": "Try limiting online shopping or hunting for discounts.",
    "Utilities": "Switch to energy-efficient appliances to cut bills.",
    "Groceries": "Plan meals and buy in bulk to save.",
    "Dining Out": "Cook at home more or pick budget-friendly spots.",
    "Transportation": "Use public transport or carpool to reduce costs.",
    "Entertainment": "Explore free or low-cost entertainment options."
}
for category, amount in top_categories.items():
    percentage = (amount / total_spending) * 100
    st.write(f"- {category}: ₹{amount} ({percentage:.2f}% of total)")
    if category in suggestions:
        st.write(f"  *Tip*: {suggestions[category]}")