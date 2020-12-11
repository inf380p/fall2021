---
layout: post
author: spaceranger-23
title: "Final Project: Cyber Threat Intelligence Program"
---


# Code
<iframe src="https://trinket.io/embed/python3/3895e2a303" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>




# Reflection 

Topic: Data Analysis Project on Cyber Threat Intelligence (CTI)
Planning Phase:
 
## Background 
Building a CTI (Cyber Threat Intelligence) program was my goal at the beginning of this Python class. A reason I have this goal is due to my previous course work in cyber and information security. During the Spring 2020 semester, I enrolled in a cybersecurity course called “Network Security and Incident Response,” which was part of the University of Texas law school. This course allows students to understand and receive hands-on experience of how to conduct cyber investigations. The class learned how to perform incident response, study cyber frameworks, and use multiple security tools to investigate compromised network traffic or hardware.
For example, I was able to analyze a PCAP (application for capturing network traffic) to determine IOCs (indicators of compromise), understand the source and destination IP (Internet protocol) address, and the overall objective of the adversary. This information helped me understand the 5 W’s (Who, What, When, Where, and Why) of why illicit cyber actors target a particular computer system or infrastructure. Although this experience enables me to gain experience in conducting cyber investigations, I have always wondered how cyber organizations build programs to capture this technical data. After reviewing several websites on what CTI is and making a Python program, I knew this idea was the challenge for me. Below are several websites that help tailor my thinking on the construction of this program:

1. https://www.recordedfuture.com/threat-intelligence-feeds/
2. https://searchsecurity.techtarget.com/feature/An-introduction-to-threat-intelligence-services-in-the-enterprise
3. https://www.crowdstrike.com/epp-101/threat-intelligence/
4. GitHub - AlienVault-OTX/OTX-Python-SDK: The Python SDK for AlienVault OTX
5. Cyber Threat Intelligence Technical Committee (oasis-open.github.io)

## Strategies 
To complete this project by December 12, 2020, I created several strategies that would lead me to victory. First, I decided that I would commit four days a week to work on the project. Monday, Tuesday, and Saturday are days designated to solely working the CTI project. Thursdays are days that I reach out to my Python community to troubleshoot existing errors. Secondly, I dedicated one 4-hour block to work on the CTI project. I would set a timer for 25 minutes to write code and 5 minutes to rest. After two hours of writing code, I would take a 30-minute break and then continue writing code for the reaming time I have left. Third, if I become overwhelmed with writing code, I will stop for the day and reflect on the errors to prepare for troubleshooting day. Last, I wrote on a sticky note to remind that writing this program will probably be the most challenging homework assignment I ever took on. NEVER GIVE UP!

## Outline
Step 1: Scrape the website for data – find cyber news websites that generates a lot of news stores and data. 
Step 2: Extract keywords (cyber-attacks) – think about cyber terms that appears a lot in new stories.
Step 3: Save a data to a file – save the data to CSV file with the number of how my cyber attacks the program found a day.
Step 4: Load the data – load the data back into the program to for visualization. 
Step 5: Import data into graphic – use Matplotlib to graph your data.

## Step 1: Web Scraping a Website
Scraping a website for data is challenging. When I first wrote my first initial draft on what types of information I would like to collect, my thought process was extensive. For example, my initial outline consists of typing code that could extract data from multiple cybersecurity news sites. This will allow users of the program to understand the types of cyberattacks that are occurring on a daily-week basis.
After speaking with a few classmates and friends with programming experience, their response was to narrow the number of websites and cyber key terms. They believed I was trying to do a little too much with creating a data analysis program. Base on the advice I received from my Python community, I begin to research a website that will fit my, and the programs need.
My goal was to explore the types of cyber-attacks APT (Advanced Persistent Threats) 28 conducts. However, APT 28 has several nicknames that associate with the organization. According to INTSIGHTs threat intelligence report on Russian cyber groups, APT goes by Tsar Team, Sofacy Group, Pawn Storm, Sednit, and STRONTIUM. Another name that is not included in the intelligence report but commonly known in the global security community is Fancy Bear. Overall, researching APTs for this cyber project would have overcomplicated the issues that I am already facing with this project's development. Therefore, I decided to only look for keywords such as Malware, Phishing, and DDoS at this time

1. http://wow.intsights.com/rs/071-ZWD-900/images/RussianAPTs.pdf

As I was researching a website to scrape, another issue came to mind. The first website that I choose to scrape is Cyberscoop.com. This website is highly informative when it comes to publishing cyber news. However, the website does not generate a lot of new stories for the program to be useful. On average, Cyberscoop.com publish anywhere from 2 to 5 articles a day. Because of this issue, I had to go with another website to scrape.
The next website that I thought would be beneficial is Twitter.com. Twitter generates millions of posts every day, which would be great to conduct cyber analysis. However, to scrape the website, a user will have to sign up for a developer's account to use Twitter API (application programming interface). After signing up for a Twitter account, it took several days for me to gain approval. Because of the time it took to gain access to the website; I decided it would be best to look for another website.  
The website that would meet the needs of my CTI project is Cyware.com. Cyware.com is a Twitter-like website that continually updates with cyber news in almost real-time. On average, the website generates roughly 13 to 15 news articles daily. This is more what Cyberscoop.com publishes and less than Twitter. Cyware.com is an excellent website to stay up to date on the latest news.
1. https://cyware.com/cyber-security-news-articles

## Step 2: Extracting Cyber Keywords
Extracting cyber keywords from Cyware.com was a bit challenging. To extract keywords, I had to access Google Chrome developers' tools to find the div that associates with each of the news threads' titles and bodies. This part of the extracting phase took a while due to being a couple of dozen divs. After finding the correct div, I extracted the title and body of the paragraph, making it easier to find keywords. Also, I was able to do a rough count of how many times I identified a cyber word before writing out the code.

## Step 3: Save Data to a File
Save the data to a CSV (comma-separated values) file was the most challenging challenge compared to the other steps. I refer to YouTube videos and research Python articles to understand the errors I was experiencing. At first, I attempt to create several columns with the labels of Date (column A), DDoS (column B), Malware (column C), and Phishing (column D). In return, columns A-D appeared in the Excel file; however, the labels all appeared in column A. After trying various codes and watching multiple videos, this is one of the first problems that I had to ask for help on my troubleshooting day.

## Step 4: Load the Data
Loading the data back into the program was just as difficult as step 3. I attempt to call the same function I was using in step 3 and would receive multiple errors. Again, I had to use my troubleshooting day to understand why I could not bypass the step. I could not return the data because I did not need to use the function in step 3 to call the function in step 4.

## Step 5: Import Data Into a Visual Graph
Importing the data was the most exciting step with the development of this project. I did not know before starting this CTI project that Python can create graphs/visualizations of the data that I collected. I imported Matplotlib and followed the steps in the book “Automate the Boring Stuff with Python” to plot the data. Doing this step increasing my curiosity on other things I can use Python before. Importing the data was the most exciting step with the development of this project. Doing this step increasing my curiosity on other things I can use Python for.

## Controlling Emotions and Asking For Help
One of the biggest challenges with this entire Python project is my controlling emotions and asking for help. There were days I became frustrated because I kept on receiving errors and did not know what to do to solve the issue. For a moment, I almost wanted to switch to another project, but the sticky note that I created from the beginning continues to remind me never to give up.
Furthermore, if it were not for having a Python community, I would not achieve what I have done with this project. I am a person that does not like to ask for help and will repeatedly try to solve issues until I find a solution. However, the lesson learned from this project is that people in this world want to help and want you to be successful. Without them, none of this would be possible this semester.

