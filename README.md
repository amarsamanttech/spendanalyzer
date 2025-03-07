# Spend Analyzer

A simple tool to analyze your spending habits, spot leaks, and visualize trends. Built with Python and Streamlit, this app is designed with Indian users in mind but can be adapted for anyone looking to gain insights into their finances.

---

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- **Python 3.6 or higher**
- **Streamlit**
- **Pandas**
- **Matplotlib**

Install the required Python libraries using this command:

```bash
pip install streamlit pandas matplotlib
```
## Setup

Follow these steps to get the app running on your local machine:

Download the code: Clone this repository or download the spend_analyzer.py file.

Run the app: Open your terminal, navigate to the directory containing spend_analyzer.py, and execute:

```bash
streamlit run spend_analyzer.py
```

This will launch the app in your default web browser.

## Usage

Follow these steps to use the Spend Analyzer:

1. **Explore with sample data**: The app includes pre-loaded sample data reflecting typical Indian spending (e.g., groceries, transportation, dining out). You can test the app’s features without uploading your own data.

2. **Prepare your own data**: To analyze your personal expenses, create a CSV file with the following columns:
   - `Date` (in `YYYY-MM-DD` format, e.g., `2025-02-15`)
   - `Description` (text, e.g., "Dmart", "Auto fare")
   - `Category` (text, e.g., "Groceries", "Transportation")
   - `Amount` (numeric, e.g., `500`, `100`)

3. **Upload your data**: Click the "Upload your CSV" button in the app and select your CSV file.

4. **View insights**: After loading your data, the app will display:
   - **Total spending**: Your overall expenditure.
   - **Bar chart**: Spending breakdown by category.
   - **Line chart**: Daily spending trends over time.
   - **Spending leaks**: Identifies your top 3 spending categories with tailored tips to save money.

## Notes
- **Data format**: Ensure your CSV has the exact column names (`Date`, `Description`, `Category`, `Amount`) and the `Date` is in `YYYY-MM-DD` format. Errors may occur if the format is incorrect.
- **Currency**: The app assumes amounts are in Indian Rupees (INR), but calculations work with any currency as long as it’s consistent.
- **Tips**: Suggestions for reducing spending are based on common Indian spending patterns but are broadly applicable.

## Contributing
Want to improve the Spend Analyzer? Feel free to fork this repository and submit pull requests with new features, code enhancements, or better savings tips. Contributions are always welcome!

