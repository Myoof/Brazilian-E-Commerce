if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
import pandas as pd

@transformer
def transform_data_quality_checks(data, *args, **kwargs):
    df_customers, df_geo, df_order_items, df_payments, df_reviews, df_orders, df_products, df_sellers, df_category_translation = data


    checks = {
        'orders_unique': df_orders['order_id'].is_unique,
        'no_null_order_ids': df_orders['order_id'].notna().all(),
        'positive_payments': (df_payments['payment_value'] >= 0).all(),
        'products_no_null': df_order_items['product_id'].notna().all()
    }

    return pd.DataFrame([checks])

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
