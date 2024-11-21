import os
import connection
import sqlparse
import pandas as pd


if __name__ == '__main__':
    # Connection data source
    name_source = 'marketplace_prod'
    conf = connection.config(name_source)
    # Create connection
    conn, engine = connection.get_conn(conf, "DataSource")
    cursor = conn.cursor() # Run SQL Query Syntax

    # Connection to dwh
    name_source_dwh = 'dwh'
    conf_dwh = connection.config(name_source_dwh)
    conn_dwh, engine_dwh = connection.get_conn(conf_dwh, "DataDestination")
    cursor_dwh = conn_dwh.cursor()

    # Get Query string
    path_query = os.path.join(os.getcwd(), 'query')
    query = sqlparse.format(
        open(os.path.join(path_query, 'query.sql'), 'r').read(), strip_comments = True
    ).strip()

    dwh_design = sqlparse.format(
        open(os.path.join(path_query, 'dwh_design.sql'), 'r').read(), strip_comments = True
    ).strip()

    try:
        # Get Data
        print('[INFO] ETL Service is running...')
        df = pd.read_sql(query, engine)
        print(df)

        # Create Schema dwh
        cursor_dwh.execute(dwh_design)
        conn_dwh.commit()

        # Data Ingestion -> dwh
        df.to_sql(
            'dim_orders',
            engine_dwh,
            schema='public',
            if_exists='replace', # override
            index=False
        )

    except Exception as e:
        print('[ERROR] Failed to run ETL Service..')
        print(str(e))



    

