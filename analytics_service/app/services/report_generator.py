import pandas as pd
from datetime import timedelta

class ReportGenerator:
    @staticmethod
    def generate_sales_report(deals_data):
        df = pd.DataFrame(deals_data)
        
        report = {
            "total_revenue": df['amount'].sum(),
            "deals_closed": len(df[df['stage'] == 'closed']),
            "conversion_rate": len(df[df['stage'] == 'closed']) / len(df) * 100,
            "top_customers": df.groupby('customer_id')['amount'].sum().nlargest(5).to_dict()
        }
        return report