# Brooklyn Bridge Pedestrian Counts Analysis
[View Interactive dashboard](https://lookerstudio.google.com/u/0/reporting/d457aff5-89a6-49b7-aa19-12d3232ce37c/page/ILUhD)

## A. Dataset Detail
- Source: [NYC Open Data](https://data.cityofnewyork.us/Transportation/Brooklyn-Bridge-Automated-Pedestrian-Counts-Demons/6fi9-q3ta)
- Last updated: May 9, 2022
- Data provider: Department of Transportation (DOT)
- See raw data at [raw_data.csv](https://github.com/dbdesign-students-fall2023/3-spreadsheet-analysis-khanh-quynh/blob/main/data/raw_data.csv)

| hour_beginning        | location        | Pedestrians | Towards Manhattan | Towards Brooklyn | weather_summary        | temperature | precipitation | lat            | long             | events        | Location1                       |
|-----------------------|-----------------|-------------|-------------------|------------------|------------------------|-------------|---------------|----------------|------------------|---------------|----------------------------------|
| 04/30/2019 12:00:00 AM | Brooklyn Bridge | 3           | 3                 | 0                |                      |             |               | 40.7081639691 | -73.9995087015  |               | (40.7081639691088, -73.9995087014816) |
| 12/31/2019 10:00:00 PM | Brooklyn Bridge | 10          | 9                 | 1                | cloudy               | 42          | 0.0005        | 40.7081639691 | -73.9995087015  |               | (40.7081639691088, -73.9995087014816) |
| 12/31/2019 11:00:00 PM | Brooklyn Bridge | 2           | 0                 | 2                | cloudy               | 42          | 0.0004        | 40.7081639691 | -73.9995087015  |               | (40.7081639691088, -73.9995087014816) |
| 12/31/2019 09:00:00 PM | Brooklyn Bridge | 12          | 0                 | 12               | cloudy               | 42          | 0.0036        | 40.7081639691 | -73.9995087015  |               | (40.7081639691088, -73.9995087014816) |
| 04/01/2019 03:00:00 AM | Brooklyn Bridge | 1           | 0                 | 1                | clear-night          | 36          | 0             | 40.7081639691 | -73.9995087015  |               | (40.7081639691088, -73.9995087014816) |

- Description:
| Column Name         | Description                                       | Type         |
|---------------------|---------------------------------------------------|--------------|
| hour_beginning      | Date and time of hourly count                     | Date & Time  |
| location            | Name of site where count was obtained             | Plain Text   |
| Pedestrians         | Total count (sum of directions)                   | Number       |
| Towards Manhattan   | Pedestrians crossing towards Manhattan            | Number       |
| Towards Brooklyn    | Pedestrian crossing towards Brooklyn              | Number       |
| weather_summary     | Overall daily weather (cloudy, clear, rain, etc.) | Plain Text   |
| temperature         | Hourly temperature, in Fahrenheit degrees         | Number       |
| precipitation       | Hourly precipitation, in inches                   | Number       |
| lat                 | Latitude                                          | Number       |
| long                | Longitude                                         | Number       |
| events              | Holidays                                          | Plain Text   |
| Location1           |                                                   | Location     |


- Sample rows of *cleaned* dataset, see full at [clean_data.csv](https://github.com/dbdesign-students-fall2023/3-spreadsheet-analysis-khanh-quynh/blob/main/data/clean_data.csv)
|  year  |  season  |      time      |  total_pedestrian  |  to_manhattan  |  to_brooklyn  |    weather     |       event        
|-------|----------|----------------|---------------------|---------------|---------------|----------------|--------------------
|  2019 |  Spring  |  12:00:00 AM  |         3           |       3       |       0       |                |                    
|  2019 |  Winter  |  10:00:00 PM  |        10           |       9       |       1       |     cloudy     |                    
|  2019 |  Winter  |  11:00:00 PM  |         2           |       0       |       2       |     cloudy     |                    
|  2019 |  Winter  |  09:00:00 PM  |        12           |       0       |      12       |     cloudy     |                    
|  2019 |  Spring  |  03:00:00 AM  |         1           |       0       |       1       |   clear night  |                    
|  2019 |  Winter  |  02:00:00 PM  |       3171          |     1685      |     1486      |    clear day   |   Christmas Day     |        

## B. Analysis
#### 1. 
- This shows the number of pedestrians counted in both directions and each direction. On average, 687 people cross Brooklyn Bridge in an hour with the maximum amount of 4000 people per hour. If we compare the amount of people going to Manhattan or to Brooklyn using the bridge per hour, on average, it seems that more people are heading to Brooklyn. And this trend stays the same when exploring different periods of a day.
| Variable            | Description                                        | Average | Maximum | Minimum | Median 
|---------------------|----------------------------------------------------|---------|---------|---------|--------
| total_pedestrian    | Num of Pedestrians per hour                        | 687     | 4,330    | 0       | 227    
| to_manhattan (MH)   | Num of Pedestrians crossing to MH per hour         | 335     | 3,657    | 0       | 112    
| to_brooklyn (BK)    | Num of Pedestrians crossing to BK per hour         | 352     | 2,872    | 0       | 111    

- Assumption: morning 5AM - 12PM, afternoon 12PM - 5PM, evening 5PM - 9PM, night 9PM - 5AM.
- On average, most people go to Brooklyn Bridge in the afternoon from 12PM to 5PM, and more are recorded to be crossing to Brooklyn. The site is the least crowded during night after 9PM with an hourly count of only roughly 60 people, 14 times less than that of the peak period.
- Here is a sample of Excel function to calculate aggregate statistics with conditions `=ROUND(AVERAGEIFS($E$2:$E$16058, $C$2:$C$16058, ">=5:00:00 AM", $C$2:$C$16058, "<12:00:00 PM"),0)`
| Period      | AVG Num of Pedestrians crossing to MH per hour | AVG Num of Pedestrians crossing to BK per hour|
|-------------|-----------------------------------------------|-----------------------------------------------|
| Morning     | 278                                           | 251                                           |
| Afternoon   | 814                                           | 935                                           |
| Evening     | 453                                           | 456                                           |
| Night       | 64                                            | 62                                            |

- From 2017 to 2019, the number of pedestrians on Brooklyn Bridge increased continuously at rate approximately 100% each year. No data was collected during Covid-19 pandemic, but from this dataset, we can say that there is an upward trend in number of people visiting Brooklyn Bridge or using it for daily purposes. 
|  Year  | Total Pedestrians crossing Brooklyn Bridge per hour |
|--------|-----------------------------------------------------|
|  2017  | 1,481,746                                           |
|  2018  | 3,539,946                                           |
|  2019  | 6,011,174                                           |

- I was interested to see if holidays would make a difference on the amount of pedestrians on Brooklyn Bridge, and it appears that Brooklyn Bridge is more crowded during holiday seasons. Even though the total number of pedestrians of 2 cases below are not that far off each other (holiday: 5.3M, non-holiday: 5.6M), day with events only account for much fewer records, yet they can still bring the number up to almost as high as normal days. With such few occurrences and high number of pedestrians recorded, we can say that Brooklyn Bridge can be a potential tourism or hang-out spot for everyone.  
|          | Total Pedestrians crossing Brooklyn Bridge per hour |
|----------|-----------------------------------------------------|
| Holiday  | 5,375,441                                           |
| Non-holiday | 5,657,425                                        |

- `time `: analyzing the same pattern as above, this pivot table looks closer into which hour people are most likely to traverse Brooklyn Bridge. 2-3PM are at the top of the chart, while 3-4AM does not sound that attractive to any Brooklyn Bridge enthusiasts. However, at any point, fewer people are traversing from Brooklyn to Manhattan than the vice versa. We can explain thhis as following: Manhattan is more packed with tourists or people in general who would love to use the Brooklyn Bridge as a great route to get to and visit Brooklyn. Since lots of fun and hustle happen across Manhattan from downtown FiDi to Uptown Central Park, tourists might choose Manhattan as their accomocation and then go visit Brooklyn during the day. So, the number of people heading to Brooklyn is consistently higher than the number of people heading to Manhattan. 
|   Time    | AVG Num of Pedestrians | AVG Pedestrians to Manhattan | AVG Pedestrians to Brooklyn |
|-----------|------------------------|-----------------------------|-----------------------------|
| 3:00:00 PM| 1,838                  | 861                         | 977                         |
| 2:00:00 PM| 1,784                  | 820                         | 964                         |
| 4:00:00 PM| 1,753                  | 822                         | 932                         |
| 2:00:00 AM| 6                      | 3                           | 3                           |
| 3:00:00 AM| 3                      | 2                           | 2                           |
| 4:00:00 AM| 3                      | 1                           | 1                           |

- `season`: this pivot table is more self-explanatory. Summer, so far, is everyone's favorite time to go out and enjoy the sun, as a third of total pedestrians going to Brooklyn Bridge is going there during the summer. It is not surprising to see a surge in the number of people walking across Brooklyn Bridge starting May until late August. Winter's wind is least favored, which is reflected well in how fewer pedestrians choose to go up to the bridge.
|  Season  | AVG Num of Pedestrians | AVG Pedestrians to Manhattan | AVG Pedestrians to Brooklyn |
|----------|------------------------|-----------------------------|-----------------------------|
|  Summer  | 892                    | 438                         | 454                         |
|  Spring  | 748                    | 357                         | 392                         |
|   Fall   | 705                    | 343                         | 362                         |
|  Winter  | 435                    | 218                         | 217                         |

- `weather`: Even though this is closely related to the `season`, weather conditions can have interesting impact on people's decision to go to Brooklyn Bridge or not. We can imagine how a clear or slightly cloudy day appear to be a great chance to hop on a Brooklyn Bridge walk, but how about rainy days versus clear night? On average, in an hour, more people tend to show up on the bridge if it is rainy or foggy than if it is a beautiful night. Up to this point, we can see that time is period of a day (timestamp) plays a huge role in people's decision to go to the Brooklyn Bridge. It might be that even if the weather is not exactly dry and comfortable, a night walk on the Brooklyn Bridge is not a universal hangout idea.
|   Weather Conditions     | AVG Num of Pedestrians |
|--------------------------|------------------------|
| partly cloudy day       | 1,422                   |
| clear day               | 1,387                   |
| wind                    | 668                    |
| cloudy                  | 542                    |
| rain                    | 256                    |
| fog                     | 234                    |
| snow                    | 195                    |
| sleet                   | 118                    |
| clear night             | 103                    |
| partly cloudy night     | 94                     |

- Holiday: Based on this [statistics](https://www.statista.com/statistics/1277607/most-popular-holidays-in-the-united-states/) of the US' favorite holidays, we will continue the analysis. In descending order, favorite holidays considered are Thanksgiving, Memorial Day, Christmas Day, Veterans Day, and Mother's/ Father's Day, and we will check the number of pedestrians on those specific events. We will have to take a leap of faith to make any statement about this result. It seems like Brooklyn Bridge is not always a destination for people to spend their favorite holidays for several reasons. For example, although Thanksgiving is the most loved holdiday, the holiday itself it more about reunion and family time and gathering. Therefore, it will make more sense if a family stay at home with one another and not dragging everyone around New York City from Manhattan to Brooklyn. Less popular holidays, on average, do have fewer pedestrians on the bridge. Another reason could be that, since we are comparing to the Americans' favorite holiday and come across a huge gap, this can suggest that the large number of people coming to Brooklyn Bridge might be foreign visitors. These are just observations and speculations, but there is too little information to make this a sound statement.
| Holidays                          | AVG Num of Pedestrians |
|-----------------------------------|------------------------|
| Easter Sunday                     | 1,322                  |
| Memorial Day                      | 1,314                  |
| Father's Day                      | 931                    |
| New Year's Day                    | 845                    |
| Christmas Day                     | 832                    |
| New Year's Eve                    | 827                    |
| Cinco de Mayo                     | 808                    |
| Independence Day                  | 750                    |
| St. Patrick's Day                 | 747                    |
| Black Friday                      | 724                    |
| Christmas Eve                     | 706                    |
| Columbus Day (regional holiday)   | 694                    |
| (blank)                           | 687                    |
| Veterans Day                      | 632                    |
| Easter Monday                     | 582                    |
| Tax Day                           | 568                    |
| Halloween                         | 566                    |
| Thanksgiving Day                  | 565                    |
| Daylight Saving Time ends         | 549                    |
| Presidents' Day (regional holiday)| 536                    |
| Labor Day                         | 514                    |
| Daylight Saving Time starts       | 505                    |
| Valentine's Day                   | 451                    |
| Veterans Day observed             | 421                    |
| Mother's Day                      | 335                    |
| Martin Luther King Jr. Day        | 195                    |
