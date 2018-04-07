# The purpose of this script to automate the process of getting 2 csv files from an email everyday and storing a "clean" version automatically every day.
# Step 1: Write a VBA script to download the email attachments based on specific conditions and store them. This was a weekend project for me since I have never coded in VBA before so Google is your best friend
# Step 2: Once your VBA script is good to go this is where Python takes over and you can start cleaning up your data
# Step 3: I really hope this script serves your purpose and please let me know on improvements as my background is Mathematics not CS so I would love feedback

import csv
import os
import glob
import pandas as pd
import datetime

# Here we are storing our Raw Net Consumed data from the email to a dataframe with the proper encoding
os.chdir(r''.replace('\\','/'))
df_Net_Consumed = pd.read_csv('', delimiter='\t', engine = 'c', encoding = 'utf-16')

# This removes whitespaces from the column names
df_Net_Consumed.columns = df_Net_Consumed.columns.str.replace(' ','_')

# Here we store yesterdays aggregated file into a dataframe
os.chdir(r''.replace('\\','/'))
df_Aggregated_Net_Consumed = pd.read_csv('')

# Here we aggregate todays data with yesterdays and formate the date
data_Net_Consumed = df_Net_Consumed.append(df_Aggregated_Net_Consumed, ignore_index=True)
data_Net_Consumed[''] = pd.to_datetime(data_Net_Consumed.<>)
data_Net_Consumed[''] = data_Net_Consumed[''].dt.strftime('%m/%d/%Y')
data_Net_Consumed[''] = pd.to_datetime(data_Net_Consumed.<>)
data_Net_Consumed[''] = data_Net_Consumed[''].dt.strftime('%m/%d/%Y')

# Here we save the aggreagted file to a csv and overwrite yesterdays
data_Net_Consumed.to_csv('', index = False)

# Here we are storing our Raw Non Net Consumed data from the email to a dataframe
os.chdir(r''.replace('\\','/'))
df_Non_Net_Consumed = pd.read_csv('', delimiter='\t', engine = 'c', encoding = 'utf-16')

# This removes whitespaces from the column names
df_Non_Net_Consumed.columns = df_Non_Net_Consumed.columns.str.replace(' ','_')

# Here we store yesterdays aggregated file into a dataframe
os.chdir(r''.replace('\\','/'))
df_Aggregated_Non_Net_Consumed = pd.read_csv('')

# Here we aggregate todays data with yesterdays and formate the date
data_Non_Net_Consumed = df_Non_Net_Consumed.append(df_Aggregated_Non_Net_Consumed, ignore_index=True)
data_Non_Net_Consumed[''] = pd.to_datetime(data_Non_Net_Consumed.<>)
data_Non_Net_Consumed[''] = data_Non_Net_Consumed[''].dt.strftime('%m/%d/%Y')

# Here we save the aggreagted file to a csv and overwrite yesterdays
data_Non_Net_Consumed.to_csv('', index = False)

