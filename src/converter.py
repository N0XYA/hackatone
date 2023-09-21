import pandas as pd

input_xlsx_file = 'hackatone/posts (1).xlsx'
output_csv_file = 'hackatone/data.csv'


print('Conversion started')

df = pd.read_excel(input_xlsx_file)
df.to_csv(output_csv_file, index=False)

print('Conversion completed')
