---
layout: post
author: scyrill
title: "Stephanie's Meetup Writeup"
---

# Reflection
For my coding/tech meetup, I attended the PyLadies London meeting led by Marco Gorelli. The main topic of the meetup was contributing to Pandas and it was open to everyone, regardless of level of experience using Pandas. This was perfect for me because I never heard of Pandas before, so it was interesting to learn more about it. I was nervous pretty early on because though it said that you didn’t need to have prior experience to participate, the people in the meeting were clearly experienced in using the platform as they were breezing through the Pandas set up list. However as the meeting went on, it wasn’t as bad as I thought it would be. 

When the meeting started, Marco introduced himself and the tasks that we would do during the session. At the beginning, he shared links that we’d be using, and the first of these was a Google Sheet. The Google Sheet contained the names of the participants and goals that we would reach during our sprint, which would enable us to set up Pandas on our devices and begin working on tasks in Visual Studio Code. I liked and disliked this at the same time because it meant that I couldn’t just watch, but that I had to actually participate. At first I didn’t take this seriously because I thought I could just do the bare minimum and if I got lost, it would be fine and I could just watch. We spent the first hour setting up, which included importing the GitHub library to Terminal and going to Github to fork pandas-dev/pandas and clone the fork. This was easy for me because we have been using GitHub in class, so I knew how to do this, but I ran into trouble after this. The next step was to set pandas-dev/pandas as upstream. I didn’t really know what this meant, but when watching Marco, it seemed to include writing ‘https://github.com/scyrill/pandas.git’ followed by ‘pandas-dev/pandas.git’ into Terminal. With the way it looked on Marco’s screen, it seemed like ‘git’ was already included in Terminal, so when I tried it, I was confused as to why I kept receiving error messages. I didn’t know how to fix this because I was new to Pandas, didn’t know how to connect GitHub to my Terminal, and I haven’t used Terminal in years. In short, I had no idea what I was doing. Instead of asking for help though, I thought that since I was lost, this was a good stopping point for me and I could just watch what would happen as Marco shared his screen. However, I found out that this was not going to be the case and that we would not move on until everyone was on the same page. 

If I or others fell behind, Marco would ask where we were at and help out. He noticed pretty quickly that there were a couple of people who hadn’t checked off the tasks, while everyone else was moving towards the end of the task list. In response, he checked in periodically to see how things were going and how he could help, which was nice because it made it feel like we were all in it together, and that he wasn’t just going to continue when there were people lagging behind. Turns out that my issue had been that though I had technically followed the steps correctly, I never downloaded the Pandas package to even call it, so Marco sent the link to do so, but it took a long time before it was fully installed, and once it finally ran, I ran into another error. Because I seemed to keep getting errors and everyone was moving on, Marco put me and some other attendees in a breakout room with Richard so that we could receive direct help with achieving the tasks and ask questions if needed. In the breakout room, I received direct help from Richard, a PyLadies helper, who was very helpful and excited to walk me through what was going wrong in my downloading process and finding the Pandas and Anaconda files in my computer. He taught me how to import and clone Pandas on my computer: 

stephaniecyrill@Stephanies-MacBook-Pro ~ % git clone https://github.com/scyrill/pandas.git  
Cloning into 'pandas'...
remote: Enumerating objects: 292289, done.
remote: Total 292289 (delta 0), reused 0 (delta 0), pack-reused 292289
Receiving objects: 100% (292289/292289), 237.17 MiB | 34.05 MiB/s, done.
Resolving deltas: 100% (244501/244501), done.
stephaniecyrill@Stephanies-MacBook-Pro ~ % cd pandas-dev 
cd: no such file or directory: pandas-dev

When I ran into another error, he showed me how to basically traceback to find where Pandas was on my computer to make sure it actually downloaded and called Pandas again. 

stephaniecyrill@Stephanies-MacBook-Pro ~ % cd pandas
stephaniecyrill@Stephanies-MacBook-Pro pandas % ls
AUTHORS.md		MANIFEST.in		asv_bench		doc			pyproject.toml		setup.py		versioneer.py
Dockerfile		Makefile		azure-pipelines.yml	environment.yml		requirements-dev.txt	test_fast.bat		web
LICENSE			README.md		ci			flake8			scripts			test_fast.sh
LICENSES		RELEASE.md		codecov.yml		pandas			setup.cfg		typings

Upon finding that Pandas had downloaded, I could see the directory and now the next step was getting Anaconda to run on my computer. I didn’t know what Anaconda was or how to get it because I just thought I needed to download the Pandas package, but with Richard’s help, I downloaded the Anaconda package and saw how I could use Terminal to search files on my computer, which was a new experience for me. I used commands like ‘echo $ PATH’ to locate what bin my downloads were in and ‘which conda’ to find and activate the Anaconda environment on my computer. After this, I moved onto the next steps, which were downloading the C compiler and creating a pandas-dev conda environment, which was possible after the previous step. I created the pandas-dev conda environment by using the command ‘conda activate pandas-dev’. I was immediately surprised by how after this step, things started flowing in quickly, creating the environment and this was really cool to watch! I will admit though that I didn’t really know what was happening, as things were flowing in fast, but it was definitely something that made me curious about using Terminal and creating environments in the future, if that was even possible. After this, I was ready to begin working on tasks, but unfortunately, the set up process took so long for me that we ran out of time and I didn’t get to deep dive into it, but in the future, I could see myself wanting to attempt to do tasks in the Visual Studio Code queue. 

Because of this, I got to see all the steps in using the terminal to install packages, search for sources in my computer and get to a point of writing python in the terminal. I also got to learn how to create a Pandas, Anaconda, and commit environment using Terminal, which was new to me like everything else was in this meetup. Considering this, this meetup was a good experience for someone like me to get acquainted with other coding packages like Pandas and using Anaconda. It really helped that Marco was pretty understanding and patient and that Richard, who helped me get everything set up, was very helpful and willing to hand hold me through the process and was excited to do it, even though it was 4AM CST. Despite my initial want to just watch and not engage, I was glad that I received this direct help from the leaders of the group because it showed me there were people in the tech industry who genuinely wanted to teach and help everyone learn, instead of just breezing through material and assuming that everyone there should “just get it.” Experiencing this kind of environment in comparison to the articles we read in class made me less worried about entering the tech industry because there are people like this there too. 


# Links Sent Throughout the Session: 
https://docs.google.com/spreadsheets/d/1k3KTsL6x57K_qUFp9IqUI2_YQgyXKZ2gGgON6vTnbOE/edit#gid=0
https://gitter.im/pandas-dev/pyladies-sprint-apr-2021
https://pandas.pydata.org/docs/development/contributing.html#contributing-your-changes-to-pandas
https://pandas.pydata.org/pandas-docs/stable/development/contributing_codebase.html#pre-commit
https://pandas.pydata.org/docs/development/contributing_environment.html#installing-a-c-compiler
https://docs.Anaconda.com/anaconda/install/mac-os/
https://code.visualstudio.com/docs/?dv=osx
