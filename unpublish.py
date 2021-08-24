#!/usr/bin/python3
import os, re
folder = input("Enter a folder to unpublish: ")
for folderName, subfolders, filenames in os.walk(folder):
    print('The current folder is ' + folderName)
    for filename in filenames:
        post_location = folderName + '/'+ filename
        with open(post_location) as f:
            post_text = f.read()
        with open(post_location, 'w') as f:
            post_text = re.sub(r'published\: true', 'published: false', post_text)

            if re.search(r'---.*?published: false.*?---', post_text, flags=re.S) == None:
                print("Post has no published entry")
                post_text = re.sub(r'(---.*?)(---)', '\g<1>published: false\n---', post_text, flags=re.S)
                print("Writing:\n",post_text[:150])
            else:
                print("Post was published")
            f.write(post_text)
        print("Unpublished {0}".format(post_location))