#!/usr/bin/python3
import os, re
from pick import Picker, pick
from collections import defaultdict

folder = input("Enter a folder to redate: ")
post_dates = []
post_dict = defaultdict(list)
for folderName, subfolders, filenames in os.walk(folder):
    print('Found {0} posts in '.format(len(filenames)) + folderName)
    for filename in filenames:
        filedate = filename[:10]
        post_dates += [filedate]
        post_dict[filedate] += [filename]

date_set = set(post_dates)
date_set = [x + " - " + ", ".join(post_dict[x]) for x in date_set]
more = True
msg=""
input("Beginning conversions...")
while more:
    dates_to_change = pick(sorted(list(date_set)), "{0}Space to select dates to modify (select none to quit)".format(msg), multi_select = True, min_selection_count=0)
    if len(dates_to_change) == 0:
        break
    for date in dates_to_change:
        valid = False
        olddate = date[0][:10]
        while not valid:
            new_date = input("Input new date for {0} in YYYY-MM-DD format: ".format(date[0]))
            if re.search(r'^\d\d\d\d\-\d\d-\d\d$', new_date):
                valid = True
            else:
                print("Date not valid")
        msg = "Changed all {0} posts to {1}\n".format(olddate, new_date)
        print(msg)
        
        for folderName, subfolders, filenames in os.walk(folder):
            for filename in filenames:
                filedate = filename[:10]
                if filedate == olddate:
                    oldpath = folderName + "/" + filename
                    newpath = folderName + "/{0}".format(new_date) + filename[10:]
                    os.rename(oldpath, newpath)
        date_set.remove(date[0])
