---
layout: post
author: benderliz
title: "Liz's Meetup Writeup"
---

# Introduction
On October 13th, I attended a virtual meet-up with the Austin Python Monthly Meet-up group. Most of their meetings, including this one, are posted on YouTube [here.](https://www.youtube.com/channel/UCMYbTawA7NcTLOYOxg1WOoA.) Generally, the meeting attendance was more than I expected-- about 20-25 folks-- and it seemed that about 15 of those people were regular attendees, based on their participation and familiarity with each other. 

After some catching up that involved sharing intriguing book and article recommendations ([for example](https://www.quantamagazine.org/how-wavelets-allow-researchers-to-transform-and-understand-data-20211013/)), the meeting began by thanking the sponsor, Capital Factory, which I think is the coworking space where the group used to meet pre-pandemic. Subsequently, the host made several announcements, such as that US Bank is hiring and that a FAST API developers meeting Py Data Global conference were on the horizon.
Then, the bulk of the meeting was spent on two mini-lectures by people who seemed like they were regulars as well. 

# First Presentation: “Viruses! Small and dangerous; How can a knowledge graph help us?” by Dr. Gunnar Kleeman
Dr. Gunnar Kleemann, a molecular biologist by training and data scientist, delivered the first talk. A man of seemingly many talents, Kleemann works as the CEO of Austin Capital Data (ACD), which uses data science to produce knowledge graphs, making meaning out of scientific data. Specifically, they use Python and Vaticle (typeDB) Knowledge Graphs to organize and develop deep tech data streams. The startup has worked on some interesting projects, including pancreatic cancer graphs and a flavor profiler to recommend new cocktails. 

In his talk, titled, “Viruses! Small and dangerous; How can a knowledge graph help us?”, Kleeman discussed a current ACD project that is looking at mapping different strains of coronavirus to the specific proteins they act upon in the human body. In doing so, there is a hope that we can more fully “cure”, or mitigate, coronaviruses, which the firm purports are likely to only continue emerging and reproducing in coming years (in part due to the warming global temperatures). The team gathers “bio-COVID data” from several databases (including CORD-NER, Uniprot, Coronaviruses database, DGldb, Human Proteins Atlas, Reactome, DisGeNet, SemMed) as well as other virus-related data. A specific type of virus, called a string virus (viruses.string-db.org), is of importance to the firm. 

Once the data is compiled, the team downloads a tsv file, parses it, and stuffs it into a database (which I believe is the Biograkn knowledge graph semantic database, but there was a lot going on, so I may have captured this incorrectly) using an API (I think) which uses GQL (again, I think!). They use Python for the parsing of the data, which he showed us a couple instances of, and it looked not totally unfamiliar to me, which was cool. Around this time, he showed the use of the .session, .transaction, and .commit methods, saying, “Each transaction is a read or a write.” I believe this was referring to the integration between Python and GQL. 

At this point in the presentation, aside from the interesting implications of using Python and data science concepts in general for a field as significant as virology, what I found most valuable was to see what Python usage looks like “in the wild”. As you can infer, I was both in awe of and perplexed by the technical connections between Python programs and other things in the DS ecosystem-- like Biograkn, GQL, APIs, etc. It was hard to follow in the moment, but I think I would pick it up after more exposure. I find this aspect of Python intimidating but also cool because it means there are endless applications of this language.

Ultimately, the knowledge graphs resulted in several viral-to-protein connections which could be further analyzed, e.g. there were 99 proteins that had “private” (only one) connections with a virus (out of 7 viruses); and two of the viruses (MHV and IBV) were highly connected to proteins generally. Kleemann concluded by saying that, “There is a wealth of data points out there, but it is a matter of having people who can work with the data and visualize it and turn it into something useful.” I found this statement to summarize nicely why learning programming and DS is so valuable in our data-soaked world.

# Second Presentation: 8 Rules of Fast Code by Dillon Niederhut
The second presentation, by Dillon Niederhut, felt a little more directly tied to our coursework. Niederhut presented “The Eight Rules of Fast Code” because he believes fast code is important for several reasons:
Shorter iteration cycles
Lower AWS costs
Reduced task switching
People are impatient
His rule of thumb for whether code is fast is “The Coffee Rule”: if he can run to the kitchen and grab coffee and come back and the code is still running, that’s too slow.

I took some pretty detailed notes on these rules, but I’ve truncated them for this post.

__Dillon’s 8 Rules of Fast Code:__

- #1 Do not change the code. 
    - There is a strong inverse relationship between code that is fast vs. readable/reusable/extensible/clean
- #2 Do not change the code!
    - Same reasoning…
    - He showed a tree traversal example using tuples and numba.
- #3 Find the bottleneck.
  - 80/20 rule is more often, in the case of Python, the 95/5 rule; 5% of the code is causing it to slow down, not 20%.
  - Run code through profiler to find bottleneck. He recommends several profilers to do so.
- #4 Don’t run the code.
  - The fastest code is code that is never executed. *[Note: I found this rule to be in explicit conflict with our class’ “Run” principle!]*
- #5 Look at asymptotic complexity.
  - Sets are lists with distinct values
  - Operations on lists take longer than on even equivalent sets, which matters as data structures get larger.
  - Don’t mix data structures and functions from different libraries.
  - He recommends the article “The Case for Learned Index Structures”.
- #6 Rewrite the code in a different language. 
  - Python’s weakness, according to Dillon, is that it is bad at math compared to other languages.
  - This would, of course, be a challenge for me and probably most of my classmates at this point.
- #7 Run the code in parallel.
  - It’s useful to have an escape hatch; run the code in cereal to have option
- #8 GoTo line 3

# Final Thoughts
Attending this Python meeting was enlightening and enjoyable. In the first presentation, I saw an example of how Python fits into the greater tech environment, yet outside of a purely tech discipline (bioinformatics). In the second, I learned some more direct Python advice, which contextualized some of the material we’ve learned in class, as well as showed that I have so much further to go in being Pythonic. There were a lot of mathematical principles discussed, which always makes me nervous, as I haven’t taken a math course in about 10 years. I do not want this to keep me from delving further into programming, though. If anything, I think I would appreciate the emphasis on *applied* math. 

Culturally, I thought this group was friendly, funny, and, of course, wicked smart. I noticed the professional diversity of this group, as well as some (albeit not a lot of) ethnic diversity. There were also some people who seemed to be from different countries. There were about 3 women present, which made me wonder if women tend to go to PyLadies in place of this group, there really are that few women in the community, or they are not interested. Regardless, I think the group could benefit from more ethnic and gender representation. Still, I could see myself attending these meetings, even as a beginner, just to learn. I think it would honestly take me years, though, to feel comfortable contributing any sort of work or insights to this advanced group.
