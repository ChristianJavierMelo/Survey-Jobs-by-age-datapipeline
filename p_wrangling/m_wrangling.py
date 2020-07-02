import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup


def standardizeCountry(all):
    print('connecting to the website to scrape information...')
    url = 'https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Country_codes'
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    frame = soup.find_all('td')
    print('...receiving data...')
    countries = [item.text.replace('\n', '').replace(' ', '') for item in frame]
    countries_clean = list(filter(None, countries))
    row_split = 2
    print('...processing data...')
    rows_refactored = [countries_clean[x:x + row_split] for x in range(0, len(countries_clean), row_split)]
    df = pd.DataFrame(rows_refactored, columns=['Country', 'country_code'])
    print('...standardizing data...')
    df['country_code'] = df['country_code'].str.strip('()').astype(str)
    all['country_code'] = all['country_code'].replace({'GR': 'EL',
                                                       'GB': 'UK'})
    allone = pd.merge(all, df, on='country_code')
    print('...countries standardized!')
    return allone


def getjobtitle(allone):
    print('connecting to the API to receive standardized job titles...')
    jobs = allone['normalized_job_code'].unique()
    job_dict = []
    print('...receiving required data...')
    for id in jobs:
        response = requests.get(f'http://api.dataatwork.org/v1/jobs/{id}')
        job_dict.append(response.json())
    api_df = pd.DataFrame(job_dict)
    rename_api_df = api_df.rename(columns={'uuid': 'normalized_job_code',
                                           'title': 'Job_Title'})
    sort_df = rename_api_df.set_index('normalized_job_code')
    print('...processing data...')
    alltwo = sort_df.join(allone.set_index('normalized_job_code'), on='normalized_job_code').reset_index()
    alltwo['Job_Title'].fillna('unemployed', inplace=True)
    print('...jobs standardized!')
    return alltwo


def calculateAge(birthDate):
    today = pd.Timestamp('2016').year
    each_age = today - int(birthDate)
    return each_age


def realAge(alltwo):
    print('checking the data of age to the same format...')
    alltwo['age'] = alltwo['age'].str.replace('\D', '')
    print('...transforming data...')
    age = []
    for birth in alltwo['age']:
        if len(birth) == 4:
            age.append(calculateAge(birth))
        else:
            age.append(birth)
    alltwo['age'] = np.array(age)
    print('...age standardized!')
    return alltwo


def wrangling(all):
    standardizedC = standardizeCountry(all)
    standardizedJ = getjobtitle(standardizedC)
    standardizedA = realAge(standardizedJ)
    return standardizedA
