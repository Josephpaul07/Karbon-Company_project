import json
from rules import latest_financial_index, total_revenue, total_borrowing, iscr_flag, total_revenue_5cr_flag, borrowing_to_revenue_flag

def financial_analysis(data):
    result = {}
    financial_index = latest_financial_index(data)

    # Calculate various financial metrics
    result['total_revenue'] = total_revenue(data, financial_index)
    result['iscr_flag'] = iscr_flag(data, financial_index)
    result['total_revenue_5cr_flag'] = total_revenue_5cr_flag(data, financial_index)
    result['borrowing_to_revenue_flag'] = borrowing_to_revenue_flag(data, financial_index)

    return result
