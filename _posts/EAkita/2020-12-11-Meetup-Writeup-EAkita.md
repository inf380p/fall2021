---
layout: post
author: EAkita
title: "Write-up for off-campus cultural immersion meetup experience"
---

**How did it go?** 
I initially signed up for 2; The Austin Python Meetup Monthly Meetup & Thinkful Webinar; Data Science Basics: Machine Learning. The second one was more interesting to me, however, I realized that there were only 2 other people signed up, and I wanted a more collaborative meetup with multiple views, so I went with the first (80 signed up, about 40 showed up). The entire meetup was interspersed with insightful discussions, with questions and answers. It was hosted online which ran from 7 pm to 9pm. Here is the link: https://meet.google.com/gqv-mynn-zeo  

There was a main talk - Web_scraping and Patent Analytics and a secondary talk “Who owns your code”. The main talk was given by Robert McKee,  is a licensed attorney with the USPTO, CA, and TX who now currently makes chatbots for the telecom industry, and the second talk was by D. C. Toedt III, an attorney in solo practice in Houston and an adjunct law professor at the University of Houston. 

The main presentation was mainly on tools, example code, deployment of AI models, and use cases of patent analytics. The second talk was on code ownership
It was really insightful, and there was some good information shared. There were lots of good questions and feedback as well. 

**What did you learn?** 

**Talk 1**

Robert recommended the book “Automate The boring Stuff with Python” which focused on knowledge such as  web scraping, automated, clean up of excel files. 
From his talk, the idea with patent analytics is basically to uncover new opportunities, and how to recognize a good idea and build a business around it. 

Robert discussed how patents are very expensive, and it’s important to know what you’re spending your money on and why. He exposed the audience to the patent analytics web data-  1.9TB worth of data, with applications going back to 1782. This is massive, free, public and data set of texts, images, and time series data. This data helps to do patent landscaping, or patents related to a particular topic, and you can find solutions on experienced patents that you can use. And on the lawyer’s side it helped him to predict patent outcomes. Essentially, if you can predict how your application will be viewed when sent, you can do a better job of writing the patent, which is extremely expensive. Software patents were apparently difficult, but AI patents were successful. He also mentioned people working on this stuff; Berkeley Fung engineering school, Google Global Patents, Carnegie Mellon
 
**Programmatic part for Patent Analytics** 
He used webscraping techniques in the beginning; going to the websites with program, using excel and charts. He currently uses SQL to go through millions of patent application to pull out in minutes
He uses different libraries but mostly “Pandas”. He advocated for deploying ones data with Streamlit, and not worry about HTML and other UI elements

**Data Collection of the Webscraping**: Install mechanicalsoup with pip; this tool turns the website into HTML code and CSS. However, this is messy, but mechanical soup makes it easy to pull out important information. eg. to get links on the page; browser.links() method to get all the links on the page.. This was good because the information was spread out on different places. A better way however is to use SQL query – going through 1.9 TB of data to collect names of companies, filing patent information. 
**Data Analysis**: Import pandas, excel maxes at 150000 rows, but pandas allows a few million

He discussed how to deply python training model using flask, heroku and streamlit.The main idea is basically to put code on Github, connect to streamlit, and that automatically creates the Patent application! He showed an example of an output of the model which displayed the rejection rate for the application process. This information essentionally helps to tailor the patent application writeup to improve the odds of success. 

**Talk 2**

D. C. Toedt III talked about '''Who "owns" what parts of your code, how much trouble can it get you into, and how can it make you money?'''
**Highlights**

* Two aspects of IP ownership: 
1. Right to use it (if no one owns it) 
2. Right to exclude it (stop others from using it, and license it)
 
* Code reviews can help document independent creation
* Documenting work on Github helps to track ownership
* When you start working on a project, check what the default IP is for that software and check everyone’s contracts
* Save all your emails for papertrail 

**Would you find value in this kind of event after class?** 
Yes, I think this event was very informative. Even though it was pretty general about software IP, there were portions where the main presentation discussed his code for analytics. It was great seeing how python is used in the real world to help in patent writing and generally to automate processes. 

**How was the experience different from your expectations?** 
No, I was looking for a very collaborative talk, which is what I experienced. I wasn’t sure about how much programming was going to be involved, or whether we were going to be asked to pair program. Even though there wasn’t any hands on programming, there was a good discussion on how code is used  in specific settings.

**Could you see yourself becomming a member of a professional community like this in the future?**
Yes, I see myself regularly attending these events to netowrk with other programmers and to expand my knowledge base. I realized that there are so many things that are discussed in these meetup events, and attending them is a great way to learn. Moving forward, this will become something I will occasionally attend. 
