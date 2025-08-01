if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
import pandas as pd
from sqlalchemy import create_engine, text

@transformer
def initialize_postgres_tables(*args, **kwargs):
    engine = create_engine('postgresql://mage:mage123@localhost:5432/mage_db')

    with engine.begin() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS monthly_revenue (
                monthofyear TEXT PRIMARY KEY,
                revenue NUMERIC
            );
        """))

        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS customer_lifetime_value (
                customer_id TEXT PRIMARY KEY,
                total_revenue NUMERIC,
                num_orders INTEGER,
                avg_order_value NUMERIC,
                segment TEXT
            );
        """))

        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS product_popularity (
                product_id TEXT PRIMARY KEY,
                total_orders INTEGER,
                total_revenue NUMERIC
            );
        """))

        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS customer_segmentation (
                customer_id TEXT PRIMARY KEY,
                total_revenue NUMERIC,
                num_orders INTEGER,
                avg_order_value NUMERIC,
                segment TEXT CHECK(segment IN ('High', 'Medium', 'Low'))
            );
        """))

    # Confirmation tables are created
    return {'status': 'Tables created'}