
# Gemini Code Assist for Data Engineering  - Prompt 

## DAG_1 - ingest data from API to BigQuery

### 1. Prompt to Create Data Pipeline 

```
Create Airflow DAG that contain 2 tasks:
Objective is to collect data and upload Create/Append to BigQuery Table 
projec_id=`YOUR_PROJECT_ID`

1. Collect Data from API using PythonOperator
and Save results in GSC 
bucket_name=`dataai-folk-2001` 
folder=`raw/coingecko`
https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,tether&vs_currencies=usd,thb&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true

2. Upload data from GSC to BigQuery
destination_project_dataset_table=`gemini_assist_workshop.coingecko_price`
```
### 2. Chat with you code after prompt is done
```
Fix as the following 
- Add Schedule to interval to every monday,wenesday,friday 21:00 
- DAG's owner to `gemini-code-assist`
```

## DAG_2 - ingest data from Json File to BigQuery

```
Create Airflow DAG that contain 3 tasks:
projec_id=`YOUR_PROJECT_ID`
bucket_name=`deb-gemini-code-assist-YOUR_NAME` 
destination_project_dataset_table=`gemini_assist_workshop.customer_feedback`

1. Extract: Load data from path `customer_feedback.json` and convert to csv and upload to GCS 
folder=`raw/customer_feedback` using pythonOperator

2. Transform: 
Get data from raw and then clean and transform the customer_feedback data using pandas.
folder=`processed/customer_feedback\`
Add the following columns:
count_character, age : calculate from birthdate, and age_geration

3. Upload data to BigQuery 
```


## DAG_2 
2. Code Completeion for Airflow DAG
```
Add task to send LINE notication if the all the upstream task is Done.
```