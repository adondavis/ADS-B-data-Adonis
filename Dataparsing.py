import pandas
import pandas as pds
import csv

#calls file and seperates with delimiter by tab
file_open = open('/Users/adonisdavis/Documents/PCIP/ADS-B-data-Adonis/data_Fri 04 Jun 2021 12:00:00 am.csv')
data_file = csv.reader(file_open, delimiter='\t')


#clears all data that does not include the important subjects
for data in data_file:
    if data.__contains__( 'hexid' and 'indent' and 'alt' and 'position' and 'alt_gnss' and 'speed' and
                         'track' and 'nav_qnh' and 'emergency'):
        print(data)

    else:
        print("Not enough Data")







