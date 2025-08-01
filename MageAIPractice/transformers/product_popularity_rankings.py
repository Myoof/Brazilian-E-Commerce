if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
import pandas as pd

@transformer
def transform_product_popularity(data, *args, **kwargs):
    df_customers, df_geo, df_order_items, df_payments, df_reviews, df_orders, df_products, df_sellers, df_category_translation = data
    df_grouped = df_order_items.groupby('product_id').agg(
        total_orders=('order_id', 'count'),
        total_revenue=('price', 'sum')
    )
    df_grouped = df_grouped.sort_values(by='total_orders', ascending=False).reset_index()
    return df_grouped


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
