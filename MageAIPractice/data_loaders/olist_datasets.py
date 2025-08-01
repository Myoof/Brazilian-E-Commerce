from mage_ai.io.file import FileIO
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
import pandas as pd
import os
import time
import logging
from sqlalchemy import create_engine


engine = create_engine("postgresql://mage:mage123d@localhost:5432/mage_db")
with engine.connect() as conn:
    result = conn.execute("SELECT 1")
    print(result.fetchone())



def load_generic(file_path, required_columns=None):
    '''
    Template for logging extraction metrics (row counts, file sizes, processing time)

    Helper function when loading each file, implements basic error handling, data validation,
    and extraction metrics. Takes in the file path as a string and the required column as the
    string value of a list index 
    '''

    start_time = time.time()
    try: #Used to validate data
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}") #Ensures file exists
        
        file_size = os.path.getsize(file_path) / (1024 * 1024) #File Size, 1024^2 is MB
        df = pd.read_csv(file_path)

        if required_columns:
            for col in required_columns: #Ensures primary key is available
                assert col in df.columns, f"Missing required column: {col}"

        row_count = df.shape[0] #Row Count
        elapsed_time = round(time.time() - start_time, 2) #Elapsed Time
        logging.info(f"[{os.path.basename(file_path)}] {row_count} rows, {file_size:.2f} MB, {elapsed_time} sec")
        # print(row_count)
        # print(file_size)
        # print(elapsed_time)
        return df #Returns meta data for extraction metrics

    except Exception as e: #Validation
        logging.error(f"[{file_path}] Failed to load: {e}")
        raise


@data_loader
def load_data_from_file(*args, **kwargs):
    """
    Template for loading data from filesystem.
    Load data from 1 file or multiple file directories.

    For multiple directories, use the following:
        FileIO().load(file_directories=['dir_1', 'dir_2'])

    Docs: https://docs.mage.ai/design/data-loading#fileio
    """
    file_paths = [
        ('data/olist_customers_dataset.csv', 'customer_id'),
        ('data/olist_geolocation_dataset.csv', 'geolocation_zip_code_prefix'),
        ('data/olist_order_items_dataset.csv', 'order_id'),
        ('data/olist_order_payments_dataset.csv', 'order_id'),
        ('data/olist_order_reviews_dataset.csv', 'review_id'),
        ('data/olist_orders_dataset.csv', 'order_id'),
        ('data/olist_products_dataset.csv', 'product_id'),
        ('data/olist_sellers_dataset.csv', 'seller_id'),
        ('data/product_category_name_translation.csv', 'product_category_name'),
    ]
    return [load_generic(path[0], [path[1]]) for path in file_paths]
    # return [FileIO().load(path) for path in file_paths]

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
