class FLAGS:
    GREEN = 1
    AMBER = 2
    RED = 0
    MEDIUM_RISK = 3
    WHITE = 4  # Data is missing for this field

def latest_financial_index(data: dict):
    for index, financial in enumerate(data.get("financials", [])):
        if financial.get("nature") == "STANDALONE":
            return index
    return 0

def total_revenue(data: dict, financial_index):
    try:
        financial_entry = data["financials"][financial_index]
        return financial_entry["pnl"]["lineItems"]["netRevenue"]
    except (IndexError, KeyError):
        return 0.0

def total_borrowing(data: dict, financial_index):
    try:
        financial_entry = data["financials"][financial_index]
        long_term_borrowings = financial_entry["bs"]["longTermBorrowings"]
        short_term_borrowings = financial_entry["bs"]["shortTermBorrowings"]
        total_borrowings = long_term_borrowings + short_term_borrowings
        
        total_rev = total_revenue(data, financial_index)
        return total_borrowings / total_rev if total_rev > 0 else 0
    except (IndexError, KeyError):
        return 0.0

def iscr(data: dict, financial_index):
    try:
        financial_entry = data["financials"][financial_index]
        profit_before_interest_and_tax = financial_entry["pnl"]["profitBeforeInterestAndTax"]
        depreciation = financial_entry["pnl"]["depreciation"]
        interest_expenses = financial_entry["pnl"]["interestExpenses"]
        
        return (profit_before_interest_and_tax + depreciation + 1) / (interest_expenses + 1)
    except (IndexError, KeyError):
        return 0.0

def iscr_flag(data: dict, financial_index):
    if iscr(data, financial_index) >= 2:
        return FLAGS.GREEN
    return FLAGS.RED

def total_revenue_5cr_flag(data: dict, financial_index):
    if total_revenue(data, financial_index) >= 50000000:
        return FLAGS.GREEN
    return FLAGS.RED

def borrowing_to_revenue_flag(data: dict, financial_index):
    ratio = total_borrowing(data, financial_index)
    if ratio <= 0.25:
        return FLAGS.GREEN
    return FLAGS.AMBER
