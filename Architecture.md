Architecture.md

### Data Flow Diagram (Text-based)
Raw CSV Files → Mage Extract Block → Transform Blocks → Export to PostgreSQL → Analytics Ready Tables

Inline-style: 
![alt text](https://github.com/https://github.com/Myoof/Brazilian-E-Commerce/pipeline_tree.png "Visual of the Pipeline Tree")

### Explanation of Each Pipeline Stage
- Extraction: Load CSVs for orders, payments, etc.
- Transformation:
  - Monthly revenue: aggregate by order timestamp
  - Customer segmentation: compute LTV, AOV, segments
  - Product popularity: aggregate sales and order count
- Loading: Export DataFrames to PostgreSQL with type mapping and schema management

First, I created a data transformer block that initialized all of the tables I would use in SQL through sqlalchemy. Then, I created a data loader block that loaded all 9 tables from the raw dataset into Mage AI that was connected to the first transformer block. In the third layer, there were five transformer blocks, each with a different purpose. The first and second were used to clean, standardize, and validate the data that was extracted. Then, I created transformer blocks that calculated product popularity rankings, monthly revenue trends, and customer lifetime value. The customer lifetime value was then pipelined into another transformer block that calculated customer segmentation. All four of these blocks were pipelined into their own exporter blocks which wrote to the SQL tables initialized in the beginning.

### Data Transformation Logic
- monthly_revenue: groupby(month), sum of payment_value
- customer_segmentation: total revenue, order count, average order value, segment buckets
- product_popularity: order count and revenue grouped by product_id

### Scheduling and Monitoring Approach
- Mage supports cron-style scheduling
- Use UI to schedule DAG
- Monitoring via block logs and status icons
