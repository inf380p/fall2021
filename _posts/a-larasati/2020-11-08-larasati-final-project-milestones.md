---
layout: post
author: a-larasati
title: "Final Project Milestones"
---
I've always enjoyed travelling, and although the current world circumstances has all but struck that opportunity out for the next forseeable future, I thought it would be interesting to look at some commercial flight data. I don't quite know yet what kind of flight data I want to look at or conduct data analysis on, but I know that there are some basic information that the dataset should have, specifically the general airport traffic and information on the airport itself.

I managed to find some airport traffic data through the (US FAA)[https://www.faa.gov/airports/planning_capacity/passenger_allcargo_stats/passenger/] site, specifically relating to enplanement, which the FAA has defined as airline passengers; the data from 2019 seemed the most relevant at the moment. I also found some data from the US Bureau of Transportation Statistics regarding (airline on-time statistics)[https://www.transtats.bts.gov/OT_Delay/OT_DelayCause1.asp?pn=1]. For the time being, I think sticking with data from 2019 would be a good starting point just to make sure things are actually working. I might need to find monthly data of airport traffic to have a better "comparison" between airprot traffic and on-time data. It would be interesting to also find weather data to see how that affects traffic and on-time information. For now, I'm keeping the milestones very broad as I haven't quite narrowed down the specifics of what I want to do with this information. Ultimately, I think I want to get this program to at least give me a snapshot information on the activity of a given airport.

- [x] Get air traffic & on-time data for 2019
  - [x] Find the data
  - [x] Clean the data
- [] Program should be able to read the data (either in .txt or .csv format)
- [] Program should be able to take user inputs
  - [] Determine what kind of user inputs
  - [] Determine what kind of data analysis (in general) program should be able to do
- [] Program should be able to return statistics depending on the input
- [] Program should include a "Help" function
  - [] Determine what should go in the function
 
Some stretch goals that would be an interesting addition to the program:
- [] Find national weather data for 2019 (note: might need to find weather data from/around the airports itself)
- [] Find more specific air travel data (international vs. domestic arrival/departure)
- [] Program might be able to identify/compare data from international & domestic flights for a given airport
- [] Program might be able to identify if a given airport is an airline hub
- [] Find "historical" data (the past ~5-10 years) so program might be able to compute different changes over time
