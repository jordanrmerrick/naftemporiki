# Webscraping
## Fall 2019 Research Assistant

## Summary
I'm working as a research assistant at American University this semester and this is a project I've been working on.

The purpose of this project is to find a number keywords in hundreds of thousands of articles  throughout a number of websites.
From there I need to count how many articles each of the keywords appeared in, and the date of each relevant
article.

## Dependencies

#### Native Libraries
- csv
- datetime
- re
- collections

#### Custom Libraries
- naftemporiki_links
- in_links


#### External Libraries
- requests
- bs4
- twilio.rest

## Usage
The usage of this program is very simple. Just run main.py and you will be prompted
with an input option to enter which news website you want to get the output of.

## Future Plans
 - Build in more websites. This should be relatively simple and will be started on Oct. 22 after my midterm exams.

 - Automate the output so that every website is scraped by running main.py.

 - Build in parallel processing - the processes being run are not computationally complex or intensive, but
take a long time due to how much information is pulled from websites and how long
that takes. Parallel processing would allow the requests to be pulled in unison
while still not reaching the limit of processing power.

 - Update version history.
 
 - Change nested loop in `check_for_keywords` to increase efficiency.