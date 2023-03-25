from datetime import datetime, timedelta
import os
import pandas as pd

def get_all_days_current_week():
    now = datetime.now()
    week = []

    sunday = now - timedelta(days = now.weekday())
    for i in range(7):
        current_day = sunday + timedelta(days=i)
        week.append(current_day.strftime('%Y-%m-%d'))
    
    return week

def get_monday_sunday_current_week():
    now = datetime.now()

    monday = now - timedelta(days = now.weekday())
    sunday = now - timedelta(days = now.weekday()) + timedelta(days=6)

    return monday.strftime('%Y-%m-%d'), sunday.strftime('%Y-%m-%d')

def find_files_of_current_week(path):
    matching_files = []
    filenames_date_search = get_all_days_current_week()
    filenames_list = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and 'week' not in f.lower()]

    for filename in filenames_list:
        with open(path + '/' + filename, "r", encoding="utf-8") as f:
            contents = f.read()
            for search_filename_string in filenames_date_search:
                if search_filename_string in contents:
                    matching_files.append(filename)

    return matching_files

def join_files_current_week(list_files, path):
    combined_df = pd.DataFrame()

    combined_df = pd.concat([pd.read_csv(path + '/' + filename) for filename in list_files], ignore_index=True)

    monday, sunday = get_monday_sunday_current_week()
    weekly_csv_file = './data/weeks/week-' + monday + '_' + sunday + '-eurovision-odds.csv'
    combined_df.to_csv(weekly_csv_file, index=False, mode='w')