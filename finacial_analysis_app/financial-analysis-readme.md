# Financial Analysis Web Application

This web application allows users to upload a JSON file containing financial data, perform analysis based on predefined rules, and display the results.

## Features

- Upload a financial data file (`data.json`).
- Analyze data using specific financial rules.
- Display results on a user-friendly webpage.

## Technologies Used

- **Flask** - A lightweight web framework for Python.
- **HTML** - For rendering frontend pages.
- **Python** - The core logic for financial data analysis.

## Project Structure

```
├── app.py                 # Main Flask app
├── model.py               # Financial analysis logic
├── rules.py               # Business rules for financial calculations
├── templates/             # HTML templates for frontend rendering
│   ├── upload.html        # Upload form page
│   └── results.html       # Results display page
├── data.json              # Sample data for analysis
├── README.md              # Project documentation
└── venv/                  # Virtual environment (not included in Git)
```

## Setup Instructions

### Prerequisites

- Python 3.x installed
- A virtual environment setup (`venv`)

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/financial-analysis-app.git
cd financial-analysis-app
```

### Step 2: Set up a Virtual Environment

```bash
python -m venv venv
```

### Step 3: Activate the Virtual Environment

- On **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- On **Linux/Mac**:
  ```bash
  source venv/bin/activate
  ```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Run the Application

```bash
python app.py
```

You can now access the app at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## How to Use

1. **Upload the Data**: On the home page, upload the `data.json` file containing financial data.
2. **View Results**: After submitting the file, you'll be redirected to a results page displaying the analysis in a structured format.

### Example JSON Format

Your `data.json` file should look like this:

```json
{
    "financials": [
        {
            "nature": "STANDALONE",
            "pnl": {
                "lineItems": {
                    "netRevenue": 60000000
                },
                "profitBeforeInterestAndTax": 1000000,
                "depreciation": 100000,
                "interestExpenses": 50000
            },
            "bs": {
                "longTermBorrowings": 3000000,
                "shortTermBorrowings": 1000000
            }
        }
    ]
}
```

## Screenshots

### Upload Page

[finacial_analysis_app/image/image2.png]

*Caption: The upload page where users can submit their financial data JSON file.*

### Results Page

[finacial_analysis_app/image/Image1.png]

*Caption: The results page displaying the financial analysis based on the uploaded data.*

## License

This project is licensed under the MIT License.
