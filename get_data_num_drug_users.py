# 23.04.19

import os
import django
import csv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "drug_pjt.settings")

django.setup()

from dashboard_drug.models import NumDrugUser

CSV_PATH='./datas/dashboard/num_drug_users.csv'

with open(CSV_PATH, 'r',  encoding='utf-8') as file:
    
    data_rows = csv.reader(file, skipinitialspace=True)
    
    next(data_rows, None) 
    
    data_rows = list(filter(None, data_rows))
    
    for row in data_rows:
        if row[0] != None or row[0] !='':
            NumDrugUser.objects.update_or_create(
                years_drug_user = row[0],
                defaults = {
                    'years_drug_user' : row[0],
                    'num_drug_user' : row[1],
                }
            )
        else:
            continue

