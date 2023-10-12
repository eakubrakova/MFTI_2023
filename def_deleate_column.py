import pandas as pd

customer_df = pd.DataFrame({
            'number': [0, 1, 2, 3, 4],
            'cust_id': [128, 1201, 9832, 4392, 7472],
            'cust_age': [13, 21, 19, 21, 60],
            'cust_sale': [0, 0, 0.2, 0.15, 0.3],
            'cust_year_birth': [2008, 2000, 2002, 2000, 1961],
            'cust_order': [1400, 14142, 900, 1240, 8430]
        })
def delete_columns(df, col=[]):
    for c in col:
        if c not in df.columns:
            return None
    
    # удаляем столбцы из таблицы
    new_df = df.drop(col, axis=1)
    
    return new_df
