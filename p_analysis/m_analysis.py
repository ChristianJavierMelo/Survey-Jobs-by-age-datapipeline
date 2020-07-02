import pandas as pd

pd.options.mode.chained_assignment = None


def grouptable(moreall, country):
    print('selecting columns according to the requirements...')
    first_table = moreall[['Country', 'Job_Title', 'age', 'uuid']]
    print('...making some calculations...')
    first_table.rename(columns={'uuid': 'Quantity'}, inplace=True)
    series_group = first_table.groupby(['Country', 'Job_Title', 'age'])['Quantity'].count()
    df_grouped = pd.DataFrame(series_group).reset_index()
    df_grouped['Percentage'] = df_grouped['Quantity'] / df_grouped['Quantity'].sum() * 1000
    print('...receiving columns...')
    if country == 'all':
        df_grouped = df_grouped.sort_values(['Percentage', 'age'], ascending=False)
        df_grouped['Percentage'] = df_grouped['Percentage'].round(2).astype(str) + '%'
        print(df_grouped)
        print('No country filter. Exported results to csv')
        df_grouped.to_csv('data/results/analysed_age_info.csv', index=False)
    else:
        df_grouped = df_grouped[df_grouped['Country'] == country]
        df_grouped['Percentage'] = df_grouped['Quantity'] / df_grouped['Quantity'].sum() * 1000
        df_grouped = df_grouped.sort_values(['Percentage', 'age'], ascending=False)
        df_grouped['Percentage'] = df_grouped['Percentage'].round(2).astype(str) + '%'
        print(df_grouped)
        print(f'Filtered by {country} and exported to csv')
        df_grouped.to_csv(f'data/results/{country}_analysed_age_info.csv', index=False)
    print('...Data analysis completed')
    return df_grouped
