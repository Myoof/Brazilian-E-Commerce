# Instructions.md
### Also refer to README.md for additional instructions
## Detailed Environment Setup Steps
1. Install Python 3.9+  
2. Install Mage AI:
```bash
pip install mage-ai
```

3. Clone the repository and install requirements:
```bash
git clone https://github.com/yourusername/ecommerce-pipeline.git
cd ecommerce-pipeline
pip install -r requirements.txt
```

4. Set up PostgreSQL:
```bash
# macOS (using Homebrew)
brew install postgresql
brew services start postgresql

# Create DB and user
createdb mage_db
psql -c "CREATE USER mage WITH PASSWORD 'mage123';"
psql -c "GRANT ALL PRIVILEGES ON DATABASE mage_db TO mage;"
```

## Database Configuration
- Default schema: `public`
- PostgreSQL connection settings configured in `io_config.yaml`:
```yaml
default:
  POSTGRES_DBNAME: mage_db
  POSTGRES_SCHEMA: public
  POSTGRES_USER: mage
  POSTGRES_PASSWORD: mage123
  POSTGRES_HOST: localhost
  POSTGRES_PORT: 5432
```

- Tables created by the DDL transformer:
  - `customer_segmentation`
  - `product_popularity`
  - `monthly_revenue`

## Required Dependencies
- `pandas`
- `sqlalchemy`
- `psycopg2-binary`
- `mage-ai`

## Troubleshooting Common Issues
###These are issues that I ran into, althought depending on the dependencies and local machine it may differ

| Issue                        | Explanation                                                   | Resolution                                                                 |
|-----------------------------|---------------------------------------------------------------|---------------------------------------------------------------------------|
| **UndefinedColumn error**   | DataFrame column names don't match table schema               | Ensure transformer returns correct names (e.g., `'month'` not `'_month'`) |
| **No tables in PostgreSQL** | DDL block not executed or failed silently                     | Re-run `ddl_create_all_tables` block                                      |
| **Permission Denied**       | PostgreSQL user lacks privileges                              | Check `GRANT` and ownership                                               |
| **Cannot connect to DB**    | Host/port/user mismatch or Postgres not running               | Validate `io_config.yaml` and PostgreSQL status                           |
| **Kernel Issues**           | Old Mage kernel state blocking execution                      | Restart kernel via Mage UI                                                |
| **Duplicate Primary Keys**  | Aggregation or key logic is incorrect                         | Validate grouping logic or use `.drop_duplicates()`                       |
