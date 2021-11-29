---
layout: post
author: itohosagie
title: Meet-up Write-up: Workshop on Spatial Data in SQL Server
---

# Meet-up Write-up: Workshop on Spatial Data in SQL Server

### First Impression
Going into the meet-up, I expected for the material to be way over my head, despite my interest in the topic. Even a quick glance at the roster initially intimidated me because it seemed as though I would be the only student and likely the attendee most inexperienced at SQL at that. Looking back, I realize that I lacked confidence going into this space and carried this false perception that the content would surpass my level of understanding. 

For context, I have very little prior experience using SQL, but what drew me to the meet-up I’d selected was the focus on the use of spatial data within SQL Server, which combined two interests of mine: SQL and maps. Whereas I anticipated the meeting to be directed toward experienced SQL users, the host, Doug Sartoni, was very thorough and intentional with the material, walking us through the basics of encountering spatial data as well as real-world scenarios where this would be applicable. 

### Learnings
One personal takeaway from this experience was that the intention of these meet-ups are not necessarily to create a divide between less and more experienced programmers, but to create a space for learning and exploring various tools in new ways. I was surprised by the fact that the coordinator covered basic aspects of working with spatial data, like the type of file (`.shp, .geojson, .kml, .wkt`) one would expect to use and even importing the file into the SQL server. He even took the time to read aloud lines of code to help explain what exactly was being executed in his queries. Receiving this information helped me to feel as though this was an inclusive space where the more knowledgeable party had a genuine interest in sharing the techniques they’ve learned. 

In addition, a couple technical takeaways I got from the meet-up were potential project ideas for the future, as well as the importance of paying attention to detail in not just the code, but also in the map projections utilized for visualization. One note that Sartoni gave while working through a demo was the “right-hand” rule, which referred to the orientation of polygons based on the spatial data. Unlike other programs, SQL Server is “left-handed”, in which it defines the polygons counter-clockwise. To counter this Sartoni suggested that we start with a small plug of QGIS (an open-source mapping application) to alter the format of the data from one instance to another. He also encouraged us to be mindful of the effects of different map projects based on the area we may intend to depict. 

### Looking Forward
Overall, I thought it was pretty cool to see how spatial data could be utilized within SQL and greatly appreciated the thorough introduction Sartoni gave for merging these two things into one workshop. I’m not too sure how the information from this meet-up would apply following this course, but I would like to still learn more about the use of spatial data within SQL Server, which could be done by joining an interest group or maybe even reaching out to Sartoni for assistance in the future. 

