# Dictionary.md

### Source Data Schemas (examples)
- **orders.csv**:
  - order_id (str)
  - order_purchase_timestamp (datetime)
- **payments.csv**:
  - order_id (str)
  - payment_value (float)

### Transformed Data Schemas
- **monthly_revenue**:
  - month (text, PK)
  - revenue (numeric)
- **customer_segmentation**:
  - customer_id (text, PK)
  - total_revenue (numeric)
  - num_orders (int)
  - avg_order_value (numeric)
  - segment (text: High, Medium, Low)
- **product_popularity**:
  - product_id (text, PK)
  - total_orders (int)
  - total_revenue (numeric)

### Business Logic for Derived Metrics
- Revenue = SUM(payment_value)
- AOV = total_revenue / num_orders
- Segment = Quantile-based split on total_revenue

### Data Quality Rules Implemented
- No nulls in primary key fields
- Check segment values in {High, Medium, Low}
- Valid timestamps for aggregation
