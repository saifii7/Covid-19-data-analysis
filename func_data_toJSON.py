import pandas as pd

#Function to convert all CSV files to JSON
def convert_toJSON(filename):
    print('READING CSV FILE')
    csv_df = pd.read_csv(filename)
    print('CONVERTING BACK TO JSON')
    csv_df.to_json('BackToJSON'+filename[:-4]+'.json', orient="records")

#calling convert_toJSON() to convert all created CSV files back to JSON
convert_toJSON('covid_vaccine_statewise.csv')
convert_toJSON('covid_19_india.csv')
print('All FILES DONE')
