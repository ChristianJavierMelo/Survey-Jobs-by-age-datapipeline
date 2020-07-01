import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

def standardizeCountry(all):
    print('starting with country standardize...')
    url = 'https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Country_codes'
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    frame = soup.find_all('td')
    countries = [item.text.replace('\n', '').replace(' ', '') for item in frame]
    countries_clean = list(filter(None, countries))
    row_split = 2
    rows_refactored = [countries_clean[x:x + row_split] for x in range(0, len(countries_clean), row_split)]
    df = pd.DataFrame(rows_refactored, columns=['Country', 'country_code'])
    df['country_code'] = df['country_code'].str.strip('()').astype(str)
    all['country_code'] = all['country_code'].replace({'GR': 'EL',
                                                       'GB': 'UK'})
    allone = pd.merge(all, df, on='country_code')
    print('receiving countries standardized...')
    return allone

def getjobtitle(allone):
    print('starting with job standardize...')
    jobs = allone['normalized_job_code'].unique()
    job_dict = []
    for id in jobs:
        response = requests.get(f'http://api.dataatwork.org/v1/jobs/{id}')
        job_dict.append(response.json())
    api_df = pd.DataFrame(job_dict)
    rename_api_df = api_df.rename(columns={'uuid': 'normalized_job_code',
                                               'title': 'Job_Title'})
    sort_df = rename_api_df.set_index('normalized_job_code')
    alltwo = sort_df.join(allone.set_index('normalized_job_code'), on='normalized_job_code').reset_index()
    alltwo['Job_Title'].fillna('unemployed', inplace=True)
    print('receiving jobs standardized...')
    return alltwo

def calculateAge(birthDate):
    today = pd.Timestamp('2016').year
    each_age = today-int(birthDate)
    return each_age

def realAge(alltwo):
    print('starting with age standardize...')
    alltwo['age'] = alltwo['age'].str.replace('\D', '')
    age = []
    for birth in alltwo['age']:
        if len(birth) == 4:
            age.append(calculateAge(birth))
        else:
            age.append(birth)
    alltwo['age'] = np.array(age)
    print('receiving age standardized...')
    return alltwo

def wrangling(all):
    standardizedC = standardizeCountry(all)
    standardizedJ = getjobtitle(standardizedC)
    standardizedA = realAge(standardizedJ)
    return standardizedA