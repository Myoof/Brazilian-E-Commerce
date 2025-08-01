# Brazilian E-Commerce Data Engineering Take-Home
This project implements an end-to-end data pipeline using Mage AI and PostgreSQL to enable business intelligence from raw e-commerce transaction data. The pipeline automates ETL processes for customer segmentation, revenue trend analysis, and product popularity insights.

## Overview and Insights:

**Tech used:** Magi AI, Python (Pandas, sqlalchemy), SQL (PostgreSQL)

The objective of this project was to familiarize myself with Mage AI and fundamental data engineering practices. I used a publically available dataset for Brazilian E-Commerce (link below) which consisted of nine files recording the data for things like orders, customers, purchase metadata, and even geolocation. Using Mage AI, I was able to extract the data from my local machine, perform basic operations to find useful metrics like customer segmentation and product popularity insights, and finally export that data back into PostgreSQL databases I had initialized earlier. My main approach was to take the project step by step, learning how to use the Mage AI UI and how to create an efficient pipeline. I went through several iterations of minimizing the amount of blocks I used to increasing modularization until I found a way to organize my pipeline in an intuitive and efficient manner. Given more time, I would have implemented unit tests as well as additional metrics such as customer retention, revenue based on geography, and seasonal or annual trends.

### Objectives
1. Clean and validate raw transactional data
2. Transform data into insightful metrics
3. Load results into a PostgreSQL warehouse
4. Support incremental and scheduled pipeline runs

### Key Features and Capabilities
1. Modular block-based Mage AI design
2. PostgreSQL data warehouse integration
3. Monthly revenue, segmentation, and product analytics
4. Supports full and incremental updates
5. Inline validation tests for data quality

### Assumptions and Limitations
1. Data is assumed to be consistent and in expected format
2. No streaming or real-time data support
3. No UI/dashboard layer included
4. Assumes local PostgreSQL setup

It was an incredible experience working mainly within the Mage AI user interface which allowed me to do everything from creating visual block-based coding for managing modularization to scheduling my pipeline to run automatically. In the end, I created a full end-to-end ETL pipeline from scratch using nothing but Mage AI and the raw dataset from kaggle.com.

**Dataset:** https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce?resource=download

## Setup and Installation
*(may vary depending on machine)*

### 1. PostgreSQL Installation/Initialization

### 2. Download MageAiPractice (From this repository)
- cd to the local folder `MageAIPractice`

### 3. Mage AI Installation and Initialization
- Run `pip install mage-ai` in terminal
- Run `createdb mage_db`
- Run `cd MageAIPractice`
- Run `mage start MageAIPractice`
- Navigate in the Mage AI UI to "io_config.yaml"
  - REPLACE the PostgreSQL section with:
   `PostgresSQL
    POSTGRES_CONNECT_TIMEOUT: 10
    POSTGRES_DBNAME: mage_db
    POSTGRES_SCHEMA: public # Optional
    POSTGRES_USER: mage
    POSTGRES_PASSWORD: mage123
    POSTGRES_HOST: localhost
    POSTGRES_PORT: 5432`
- (Optional) To troubleshoot, run `psql -U mage -d mage_db` in the Mage AI terminal to enter SQL commands manually

### 4. Pipeline Execution
- Simply set any of the triggers to active and allow it to run until all blocks are executed


## Resources:
These are the resources I was provided and used to learn how to use Mage AI and create this project.

**Mage AI Documentation:** [https://github.com/alecortega/palettable](https://docs.mage.ai/)

**Pandas:** [https://github.com/alecortega/twitter-battle](https://pandas.pydata.org/docs/)

**PostgreSQL:** [https://github.com/alecortega/patch-panel](https://www.postgresql.org/docs/)



