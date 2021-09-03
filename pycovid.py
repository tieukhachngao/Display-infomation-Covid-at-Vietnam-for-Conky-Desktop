#-*- coding: utf-8 -*-
import os.path
import re
import argparse
import pandas as pd
from datetime import date,timedelta
# Khanh Hoa
YESTERDAY = (date.today() -timedelta(days=1)).strftime("%-d") + '/' + (date.today() -timedelta(days=1)).strftime("%-m")
TODAY = date.today().strftime("%-d") + '/' + date.today().strftime("%-m")
def get_regex(group):
    file =  os.path.expanduser("~/.cache/covid/covid19_2021_by_map.js");
    data  = open(file,'r')
    str = data.read()
    match = r"\bKhánh Hòa[^,\"]*\",\"(\w+|)\",\"(\w+|)\",\"(\w+|)\",\"(\w+|)\""
    matches = re.findall(match, str)[0][group]
    if matches:
        print(matches)
    else:
         print(0)

def get_total():
    get_regex(0)

def get_day():
    get_regex(1)


def get_yesterday(yesterday):
    file =  os.path.expanduser("~/.cache/covid/covid19_2021_281.js");
    data  = open(file,'r')
    df = pd.read_csv(data)
    # yesterday = (date.today() -timedelta(days=1)).strftime("%-d") + '/' + (date.today() -timedelta(days=1)).strftime("%-m")
    df["Khánh Hòa"] = df["Khánh Hòa"].map('{:.0f}'.format)
    df1= df.loc[df['Ngày'] == yesterday, ['Khánh Hòa']]
    if df1.to_string(index=False,header=False) == "nan" :
        print(0)
    else:
        print(df1.to_string(index=False,header=False))
# Khanh Hoa
#Viet Nam
def get_viet_nam(value,date):
    file =  os.path.expanduser("~/.cache/covid/covid19_2021_by_day.js");
    data  = open(file,'r')
    df = pd.read_csv(data)
    # today = date.today().strftime("%-d") + '/' + date.today().strftime("%-m")
    df[value] = df[value].map('{:.0f}'.format)
    df1= df.loc[df['NGÀY'] == date, [value]]
    if df1.to_string(index=False,header=False) == "nan" :
        print(0)
    else:
        print(df1.to_string(index=False,header=False))

def get_viet_nam_all():
    get_viet_nam('total_cases_2020',TODAY)

def get_viet_nam_today():
    get_viet_nam('new_cases',TODAY)

def get_viet_nam_recovered_all():
    get_viet_nam('total_recovered_2020_25',TODAY)

def get_viet_nam_recovered():
    get_viet_nam('new_recovered',TODAY)

def get_viet_nam_deaths():
    get_viet_nam('total_deaths_2020',TODAY)

def get_viet_nam_treatment_all():
    get_viet_nam('total_active',TODAY)

def get_viet_nam_treatment():
    get_viet_nam('new_active',TODAY)
#yesterday
def get_viet_nam_yesterday():
    get_viet_nam('new_cases',YESTERDAY)
def get_viet_nam_recovered_yesterday():
    get_viet_nam('new_recovered',YESTERDAY)
def get_viet_nam_treatment_yesterday():
    get_viet_nam('new_active',YESTERDAY)

#End Viet Nam
parser = argparse.ArgumentParser()
#Khanh Hoa
parser.add_argument('--total' ,dest="flag_total", action='store_const'  ,const=True)
parser.add_argument('--day' ,dest="flag_day", action='store_const'  ,const=True)
parser.add_argument('--yesterday' ,dest="flag_yesterday", action='store_const'  ,const=True)
#Viet Nam
parser.add_argument('--vnall' ,dest="flag_vietnam_all", action='store_const'  ,const=True)
parser.add_argument('--vntoday' ,dest="flag_vietnam_today", action='store_const'  ,const=True)
parser.add_argument('--vnrecoveredall' ,dest="flag_vietnam_recovered_all", action='store_const'  ,const=True)
parser.add_argument('--vnrecovered' ,dest="flag_vietnam_recovered", action='store_const'  ,const=True)
parser.add_argument('--vndeaths' ,dest="flag_vietnam_deaths", action='store_const'  ,const=True)
parser.add_argument('--vntreatmentall' ,dest="flag_vietnam_treatment_all", action='store_const'  ,const=True)
parser.add_argument('--vntreatment' ,dest="flag_vietnam_treatment", action='store_const'  ,const=True)
#yesterday
parser.add_argument('--vnyesterday' ,dest="flag_vietnam_yesterday", action='store_const'  ,const=True)
parser.add_argument('--vnrecoveredyesterday' ,dest="flag_vietnam_recovered_yesterday", action='store_const'  ,const=True)
parser.add_argument('--vntreatmentyesterday' ,dest="flag_vietnam_treatment_yesterday", action='store_const'  ,const=True)

results = parser.parse_args()
if results.flag_total:
    get_total()
if results.flag_day:
    get_day()
if results.flag_yesterday:
    get_yesterday(YESTERDAY)
if results.flag_vietnam_all:
    get_viet_nam_all()
if results.flag_vietnam_today:
    get_viet_nam_today()
if results.flag_vietnam_recovered_all:
    get_viet_nam_recovered_all()
if results.flag_vietnam_recovered:
    get_viet_nam_recovered()
if results.flag_vietnam_deaths:
    get_viet_nam_deaths()
if results.flag_vietnam_treatment_all:
    get_viet_nam_treatment_all()
if results.flag_vietnam_treatment:
    get_viet_nam_treatment()
#yesterday
if results.flag_vietnam_yesterday:
    get_viet_nam_yesterday()
if results.flag_vietnam_recovered_yesterday:
    get_viet_nam_recovered_yesterday()
if results.flag_vietnam_treatment_yesterday:
    get_viet_nam_treatment_yesterday()
