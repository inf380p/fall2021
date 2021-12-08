---
layout: post
author: sj-roh
title: "SJ's Meetup Writeup"
---

## Meetup Writeup

On Tuesday, November 16, 2021, I attended “An Evening of Python Coding” at the Austin Python Meetup group virtually through Jitsi Meet. 
The meeting turned out to be super interesting, and I was very glad that I attended specifically on this occasion. The meeting lasted around an hour and a half, 
and we had a guest speaker: James Lamb, a Machine Learning Engineer from SpotHero, come in to introduce a new and popular Python data science library: LightGBM 
(Light Gradient Boosted Machine) to us. He gave us a presentation on what LightGBM is, its purpose, and different use-case scenarios, followed by 30 minutes of 
Q&A time. I thought it was super interesting and it was nice to hear somebody so well-versed in the data science field take us through the library. Although it 
was definitely difficult to understand fully, James was nice enough to start off with the basics, then work his way into the fine details of LightGBM’s features.

I learned a decent amount from this meetup. I learned that LightGBM is a gradient boosting machine, a framework used for supervised machine learning, when truth 
labels are known. I learned that gradient boosting can be done with decision trees where it creates a sequence of rules for the machine to run through. LightGBM’s 
tree gradient boosting machine’s algorithm picks the rules that best explains the observations, a type of automatic feature selection. Lightgbm figures out the 
observations that are not well explained and that do not contribute to finding the target, or classification. It does not use randomness in this decision-making 
process, as opposed to random forests which utilize feature randomness. I remembered learning about hyperparameter tuning in Dr. Gurari’s Intro to Machine Learning 
course last spring, so I asked if Lightgbm has a specific way it tunes hyperparameters if the prediction scores are low. He answered that LightGBM does not try to 
tune hyperparameters, rather, it iteratively creates sets of rules and descriptions explaining training data. It is good to tune hyperparameters yourself by 
training a model with specific parameters. Also, it can pick out the features that are going to break these set rules, and subsequently will throw these features 
away. Lastly, I learned that LightGBM is fast in its training speed because it buckets continuous features into discrete bins in histograms, resulting in lower 
memory usage as well.

I would find value in this kind of event after class if data science-related topics are the focus. However, I would not find value if it was otherwise because of 
the general way the class is structured, as well as the environment. I did not find the structure of the meeting to be entirely organized, as the leader of the 
group would excessively cater to specific members of the meeting if they looked like they were more advanced in programming or data science. As far as the 
environment goes, I think it was alright but it definitely could have been more welcoming and inclusive. There was in particular, one person who you could tell, 
acted like he knew a lot more than he really did about machine learning. And actually, a huge lesson I learned from this meeting was, it’s always better to be 
humble. Seeing this guy go on and on just trying to sound like he knew so much opened my eyes. I thought to myself, “dang, I’ve done this. I’ve for sure done 
this. I need to watch the way I act from now on.” We were there to learn and learn from this expert in the field, but half of the time, the guest speaker 
listened to this one guy speak. I thought the leader should have done a much better job of organizing the meeting and navigating the general vibe of the meeting, 
especially with an industry expert taking time out of his day to present to us. The leader catered to the one guy previously mentioned, and asked him to talk 
about his start-up company during the Q&A session with the guest speaker literally having to watch someone give a pitch to the whole group for 15 or so minutes. 
You could tell by the end of meeting, the speaker was worn out listening to pitches and gave off an energy of “does anyone have more questions about LightGBM? 
The reason why I’m here?” Generally speaking, however, I 100% do find value in this kind of event. It was beneficial learning practical tools from a knowledgeable
industry expert from the field that I eventually want to enter. 

The experience was different from my expectations in the sense that I was expecting one leader to give a demo, and us to break off into groups to work on example 
problems. I was not expecting a guest speaker whatsoever, nor a presentation on a machine learning library. This was a pleasant surprise. I was excited to learn 
about a new and popular library from an industry expert who has had years of experience working for companies ranging from start-ups to corporate companies, who 
also currently teaches an R programming course at Marquette University. It was great to learn from someone who has experience teaching students especially, as 
you could tell he had a certain way of teaching applicable to a classroom setting.

I could see myself becoming a member of a professional community like this in the future under humble leadership, a welcoming environment of all levels, and if 
it is data science-focused. I want to eventually enter into this field, and do see value in learning new libraries, methods, models, and trends workers in the 
industry are following. Learning from guest speakers like James is something that I would always be open to doing, and if the professional community exploited 
opportunities like this, I would be happy to join as an official member. I just had a negative reaction to one person in the meeting, but acknowledge the fact 
that not everyone is like this, and that I shouldn't be so critical of that person. I've done it and still catch myself doing it today, so I must be understanding 
of people and not base my decisions solely on one experience. I shouldn't take things so personally, and certainly, one experience does not define a programming 
meetup group. Everyone else in the meeting room seemed kind and friendly. There were also many messages of encouragement in the chatroom!

Sorry for my passive-aggressive piece, there were stretches where I got pretty frustrated during the meeting lol. 
