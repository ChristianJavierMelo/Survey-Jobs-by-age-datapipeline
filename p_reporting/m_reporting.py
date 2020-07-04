import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def TopAmountSurveys(report):
     print('drawing basic chart of surveys...')
     grouped4 = report.groupby(['Country'])['Quantity'].count()
     df_grouped4 = pd.DataFrame(grouped4).reset_index()
     df_grouped4_sorted = df_grouped4.sort_values(by='Quantity', ascending=False)
     graphic_amountsurveys_country = df_grouped4_sorted.head(10)
     title = 'Top 10 amount of surveys per country'
     graphics = graphic_amountsurveys_country.sort_values('Quantity', ascending=False)
     plt.figure(figsize=(15, 8))
     chart_amountsurveys = sns.barplot(data=graphics, x='Country', y='Quantity')
     plt.title(title + "\n", fontsize=16)
     file_name = 'data/results/' + title + '.png'
     fig = chart_amountsurveys.get_figure()
     fig.savefig(file_name)
     print('...basic chart saved!')
     return chart_amountsurveys

def TopUnemployedCountry(report):
     print('drawing other basic chart...')
     grouped3 = report.groupby(['Country', 'Job_Title'])['Quantity'].count()
     df_grouped3 = pd.DataFrame(grouped3).reset_index()
     df_grouped3_sorted = df_grouped3.sort_values(by='Quantity', ascending=False)
     graphic_unem_country = df_grouped3_sorted.head(10)
     title = 'Top 10 amount of unemployed per country'
     graphics = graphic_unem_country.sort_values('Quantity', ascending=False)
     plt.figure(figsize=(15, 8))
     chart_unem_country = sns.barplot(data=graphics, x='Country', y='Quantity')
     plt.title(title + "\n", fontsize=16)
     file_name = 'data/results/' + title + '.png'
     fig = chart_unem_country.get_figure()
     fig.savefig(file_name)
     print('...last basic chart saved!')
     return chart_unem_country

def Top5JobTitles(report, country):
     print('drawing basic chart...')
     grouped = report.groupby(['Job_Title'])['Quantity'].count()
     df_grouped = pd.DataFrame(grouped).reset_index()
     df_grouped_desc_onlyJobs = df_grouped[df_grouped.Job_Title != 'unemployed']
     graphic_job = df_grouped_desc_onlyJobs.head()
     title = f'Top 5 job titles in {country}'
     graphics = graphic_job.sort_values('Quantity', ascending=False)
     plt.figure(figsize=(15, 8))
     chart_job = sns.barplot(data=graphics, x='Job_Title', y='Quantity')
     plt.title(title + "\n", fontsize=16)
     file_name = 'data/results/' + title + '.png'
     fig = chart_job.get_figure()
     fig.savefig(file_name)
     print('...chart saved!')
     return chart_job

def reporting(report, country):
     if country == 'all':
          return TopAmountSurveys(report), TopUnemployedCountry(report)
     else:
          return Top5JobTitles(report, country)



# def send(file, time):
#     if not "emailPassword" in os.environ:
#         raise ValueError("You should pass a email password")
#
#     gmail_user = os.environ["email"]
#     gmail_password = os.environ["emailPassword"]
#
#     try:
#         server = smtplib.SHTP_SSL('smtp.gmail.com', 465)
#         server.ehlo()
#         server.login(gmail_user, gmail_password)
#         print("connected to gmail servers")
#     except:
#         print("Something went wrong...")
