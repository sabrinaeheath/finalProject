import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(r"C:\Users\sabri\Desktop\covidData.csv")

x = df['Week']
y1 = df['% of Specimens Positive for SARS-CoV-2']
y2 = df['% of Deaths due to Pneumonia, Influenza or COVID']
y3 = df['% of Visits for CLI (NSSP)']
y4 = df['% of Visits for ILI (ILINet)']
y5 = df['Laboratory-Confirmed COVID-19-associated hospitalization rate per 100,000']

plt.plot(x,y1, label="Percent Positive")
plt.plot(x,y2, label="Percent of Deaths")
plt.plot(x,y3, label="Percent of Visits for COVID-Like Illness")
plt.plot(x,y4, label="Percent of Visits for Influenza-Like Illness")
plt.plot(x,y5, label="Hospitilization Rate")       
 
plt.title('National COVID-19 Activity Indicators:\n March 1, 2020 - December 5, 2020', fontsize=20);
plt.legend(loc='upper right', fontsize=10);
plt.ylabel('Percent Positive, Percent Deaths, Percent Visits, and Hospitilization Rate', fontsize=10);
plt.xlabel('Week')

plt.show()                                                                              
