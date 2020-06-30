import pandas as pd
from sqlalchemy.pool import StaticPool
from sqlalchemy import create_engine

def getall(path):
    print('connecting...')
    engine = create_engine(f'sqlite:///{path}', poolclass=StaticPool)
    header_tables = engine.table_names()
    for table in range(0, len(header_tables)):
        single = header_tables[table]
        query = f'SELECT * FROM {single}'
        data = pd.read_sql(query, con=engine)
        if table == 0:
            raw_data = data
        else:
            raw_data = pd.merge(raw_data, data, how='left', on='uuid')
    print('receiving...')
    raw_data.to_csv('data/raw/raw_data_compile.csv', index=False)
    print('copy saved')
    return raw_data