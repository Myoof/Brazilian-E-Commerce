-- Docs: https://docs.mage.ai/guides/sql-blocks
-- Create customer CLV table
CREATE TABLE IF NOT EXISTS customer_lifetime_value (
    customer_id TEXT PRIMARY KEY,
    total_revenue NUMERIC,
    num_orders INTEGER,
    avg_order_value NUMERIC,
    segment TEXT
);

-- Create product popularity table
CREATE TABLE IF NOT EXISTS product_popularity (
    product_id TEXT PRIMARY KEY,
    total_orders INTEGER,
    total_revenue NUMERIC
);

-- Create monthly revenue table
CREATE TABLE IF NOT EXISTS monthly_revenue (
    month TEXT PRIMARY KEY,
    revenue NUMERIC
);

-- Dummy select required by Mage to avoid export logic
SELECT 1 AS success;