from datetime import date, timedelta
from pprint import pprint
from sortedcontainers import SortedDict
import os, re, shutil, os
from pick import Picker, pick
###
# Defaults
###

use_defaults = True # Otherwise, prompt for inputs

default_start = date(2017,5,17)
default_end = date(2017,6,22)
default_dow_dict = {
    0 : { 
        "meets" : True,
        "name" : "Monday"
    },
    1 : {
        "meets" : True,
        "name" : "Tuesday"
    },
    2 : {
        "meets" : True,
        "name" : "Wedneday"
    }, 
    3 : {
        "meets" : True,
        "name" : "Thursday"
    },
    4 : {
        "meets" : False,
        "name" : "Friday"
    },
    5 : {
        "meets" : False,
        "name" : "Saturday"
    },
    6 : {
        "meets" : False,
        "name" : "Sunday"
    }
}
holiday_list = [
    {
        "date" : date(2017,5,29),
        "name" : "Memorial Day"
    },
    {
        "date" : date(2017,6,1),
        "name" : "No Class"
    }
    ]
unpublish_default = "y"

###
# Setup
###

default_year = None
no_choices =["n", "N" "no", "No"]
yes_choices = ["y", "Y", "yes", "Yes"]
allowed_choices =  no_choices + yes_choices
prior_month = None
dow = None
sessions = SortedDict({})
oldposts = SortedDict({})
num_sessions = 0

def get_valid_num(text, default = None):
    valid_num = False
    if default != None:
        text = text + " (Press enter for {0}) ".format(default)
    while not valid_num:
        try:
            num = input(text)
            if (default != None) and (num == ""):
                num = default
            elif type(num) != type(1):
                num = int(num)
            valid_num = True
        except ValueError:
            print("Please enter a valid number")
    return num
    
def get_date(text):
    global default_year, prior_month
    
    print("Now collecting " + text)
    # Get Year
    if default_year == None:
        choice = ""
        while choice not in allowed_choices:
            choice = input("Would you like to set a default year? (y/n) ")
        if choice in no_choices:
            default_year = False
        elif choice in yes_choices:
            year_set = False
            while not year_set:
                try:
                    default_year = get_valid_num("Enter default year: ", date.today().year)
                    if default_year // 2000 != 1:
                        raise ValueError
                    year = default_year
                    year_set = True
                except ValueError:
                    print("Please enter a valid 4 digit year")
                    default_year = None
                    continue
    elif default_year == False:
        year = get_valid_num("Enter year: ")
    else:
        year = default_year
        
    # Get month
    month = get_valid_num("Enter month: ", prior_month if prior_month else None)
    prior_month = month
    
    # Get day
    day = get_valid_num("Enter day: ")
    
    return date(year, month, day)

def get_dow():
    dowdict = {}
    for i, day in enumerate(["Monday", "Tuesday", "Wedneday", "Thursday", "Friday", "Saturday", "Sunday"]):
        answer = ""
        daydict = {}
        while answer not in allowed_choices:
            answer = input("Does your class meet {0}? ".format(day))
        daydict["meets"] = False if answer in no_choices else True
        daydict["name"] = day
        dowdict[i] = daydict.copy()
    return dowdict
        
def get_dates():
    global sessions, num_sessions
    
    print("Determining dates of new class...")
    # Start date
    if use_defaults:
        start_date = default_start
    else:
        start_date = get_date("Class Start Date")
    print(start_date)
    
    # End Date
    if use_defaults:
        end_date = default_end
    else:   
        end_date = get_date("Class End Date")
    
    # Days of week class meets
    if use_defaults:
        dow = default_dow_dict
    else:
        print("What days of the week does your class meet? ")
        dow = get_dow()
    
    # Build dict of all days
    delta = end_date - start_date
    for i in range(delta.days + 1):
        day_date = start_date + timedelta(days=i)
        meets = dow[day_date.weekday()]["meets"]
        if meets:
            num_sessions += 1
        sessions[str(day_date)] = { 
            "date" : day_date, 
            "meets" : meets,
            "holiday" : False,
            "nth_class" : num_sessions
        }
    pprint(sessions)
    
    # Subtract any holidays
    
    answer = ""
    holiday_index = 0
    while answer not in no_choices:
        print("Current Holidays:")
        for date in sessions:
            try:
                if sessions[date]["holiday"]:
                    print(date, sessions[date])
            except KeyError:
                pass
        if use_defaults and len(holiday_list) > holiday_index:
            answer = "y"
        elif use_defaults:
            answer = "n"
        else:
            answer = input("Any other holidays or days your class won't meet? ")
        if answer in yes_choices:
            # Collect holidays
            if use_defaults:
                holiday = holiday_list[holiday_index]["date"]
                holiday_name = holiday_list[holiday_index]["name"]
            else:
                holiday = get_date("Holiday")
                holiday_name = input("What is the name of the holiday? ")
            try:
                sessions[str(holiday)]["meets"] = False
                sessions[str(holiday)]["holiday"] = True
                sessions[str(holiday)]["holiday_name"] = holiday_name 
            except KeyError:
                print("Holiday not during class period.  Try Again.")
        holiday_index += 1
    
    print("Your final class schedule:")
    pprint(sessions)
    print("There are {0} sessions in your schedule".format(num_sessions))

output_dir = input("Select an output dir without slash (suggest using a new dir): ")

os.system("mkdir {0}".format(output_dir))

###
# Current Posts
###

# Get list of filenames as keys to dict of dicts
folder = input("Enter the folder where your posts are located (Usually _posts): ")
for folderName, subfolders, filenames in os.walk(folder):
    print('The current folder is ' + folderName)
    for filename in filenames:
        post_location = folderName + '/'+ filename
        post_date = filename[:10]
        print('Found post: ' + post_location)
        
        with open(post_location) as f:
            post_text = f.read()
            is_published = True if re.search(r'---.*?published\: false.*?---', post_text, flags=re.S) == None else False
            title_match = re.search(r'---.*?title\: (.*?)$.*?---', post_text, flags = re.S | re.M)
            if title_match == None:
                title = filename[:-3]
            else:
                title = title_match.group(1)
            
        oldposts[post_date] = { 
            "location" : post_location, 
            "suffix" : filename[10:],
            "is_published" : is_published,
            "post_text" : post_text,
            "title" : title,
            "date" : post_date,
            "selected" : False
        }

    print('')

get_dates()

###
# Conversion
###

answer = ""
while answer not in allowed_choices:
    if use_defaults:
        answer = unpublish_default
    else:
        answer = input("Un-publish all posts? ")
    if answer in yes_choices:
        unpublish = True
    elif answer in no_choices:
        unpublish = False

replacements = {}
default_title = input("Enter default title for post names")
for i, date in enumerate(sessions.keys()):
    session = sessions[date]
    if session["meets"]:
        try:
            options = [ "{0}: {1}".format(i["date"], i["title"]) for i in oldposts.values() if i["selected"] == False ]
            selections = pick(options, "Compiling {0}. {1} Sessions remain. {2} posts remain".format(date, num_sessions, len(options)), multi_select = True, min_selection_count=0)
        except ValueError:
            print("No more old posts to convert")
            break
        replacements[date] = []
        
        # Remove selections from old posts
        for selection in selections:
            replacements[date] += [selection[0]]
            oldposts[selection[0][:10]]["selected"] = True
        
        print(replacements[date])
        
        new_filename = str(date) + "-{1}-{0}.md".format(session["nth_class"], default_title)
        new_filepath = output_dir + "/" + new_filename
        with open(new_filepath, 'a+') as f:
            for i in selections:
                text = oldposts[i[0][:10]]["post_text"]
                if i[1] != 0:
                    # remove yaml header
                    text = re.sub(r'---.*?---', "", text, re.S | re.M)
                elif unpublish:
                    # make sure yaml header
                    text = re.sub(r'published\: true', 'published: false', text)
                    if not re.search(r'---.*?published: false.*?---', text, flags=re.S):
                        text = re.sub('(---.*?)(---)', '\g<1>published: false\n---', text, flags = re.S | re.M)
                f.write(text)
            print("Wrote {0}".format(new_filepath))
        num_sessions -= 1
    elif session["holiday"]:
        answer = ""
        while answer not in allowed_choices:
            answer = input("Make post for {0}? ".format(session["holiday_name"]))
            if answer in yes_choices:
                new_filepath = output_dir + "/" + str(date) + "-holiday-{0}.md".format(i + 1)
                with open(new_filepath,'w+') as f:
                    f.write("""---
author: elliott
title: {0}
---""".format(session["holiday_name"]))
        

