import pandas as pd


def convert_toCSV(filename):
    print('READING JSON FILE')
    json_df = pd.read_json(filename)
    print('CONVERTING  BACK TO CSV FILE')
    json_df.to_csv('BackToCSV'+filename[:-5]+'.csv', index=False)



convert_toCSV('covid_vaccine_statewise.json')
convert_toCSV('covid_19_india.json')
