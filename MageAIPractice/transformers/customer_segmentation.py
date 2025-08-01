if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
import pandas as pd

@transformer
def transform_customer_segmentation(df_clv, *args, **kwargs):
    q33, q66 = df_clv['total_revenue'].quantile([0.33, 0.66])

    def segment(revenue):
        if revenue >= q66:
            return 'High'
        elif revenue >= q33:
            return 'Medium'
        return 'Low'

    df_clv['segment'] = df_clv['total_revenue'].apply(segment)
    return df_clv


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
