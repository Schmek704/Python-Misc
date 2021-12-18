# The below snippet explains how to work within Googles Big Query SQL engine and online datasets

# import Google Big Query Library
from google.cloud import bigquery

# Create a "Client" object to use within the program
client = bigquery.Client()

# This code snippet will fetch and explore the entire dataset that is being worked in
# Construct a reference to the dataset
dataset_ref = client.dataset("XXXX", project="bigquery-public-data") # XXXX = data set from Google BigQuery site, project name can be dynamic as well 
# API request - fetch the dataset that was defined in the previous step
dataset = client.get_dataset(dataset_ref) 
# Create a "tables" list of all the tables in the fecthed dataset
tables = list(client.list_tables(dataset))
# This will print names of all tables in the dataset for exploration
for table in tables:  
    print(table.table_id)
    
# This code will then explore specific tables within the dataset that was fetched above
# Construct a reference to the the table needed
table_ref = dataset_ref.table("XXXXX") # XXXX is the name of the specific table you want to explore
# API request - fetch the table that was defined in the previous step
table = client.get_table(table_ref)
# Preview the first five lines of the table
client.list_rows(table, max_results=5).to_dataframe() # This is the same as calling the head() function in a pd df

# This code will create a SQL query to apply to the table that was examined in the above step
# create the SQL query in a python string, changing XXX to a string to identify this specific query 
XXX_query = """
    SELECT
    FROM
    GROUP BY
    HAVING
    ORDER BY """ # Your code goes here, the """ tells Pyton that everything inside those quotation marks is one string, indentation and returns will not matter
# below will take the SQL command variable above and prepare the request, the safe_config will ensure the amount of data requested does not exceeda specified amount
safe_config = bigquery.QueryJobConfig(maximum_bytes_billed=XXXX) #XXXX is the bytes limit, for example 10**10 would set it to 1 GB
query_job = client.query(XXX_query) # this sets the query_job to be an executable variable
# the below will then take the query variable and execute it, and return it in a pandas dataframe
XXX_results = query_job.to_dataframe() # change XXX to a name that is specific to this query result, will return the query into a pandas df
XXX_results.head() # allows for more exploration of the results

    
