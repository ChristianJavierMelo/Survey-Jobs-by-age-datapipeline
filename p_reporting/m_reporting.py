import os
import smtplib
import matplotlib.pyplot as plt
import seaborn as sns


# def plot_returns(report, x, y, length=8, width=14, title=''):
#     graphics = report.sort_values(x, ascending=False)
#     plt.figure(figsize=(width, length))
#     chart = sns.barplot(data=graphics, x=x, y=y)
#     plt.title(title + "\n", fontsize=16)
#     return chart

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
