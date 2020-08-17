## Version History

#### 0.8.2
- Changed `output_to_csv` function so that the dictionary returned by `count_dates` is reformatted as a list and 
written to a csv file. This was done because `DictWriter` was not interpreting the dictionary correctly.

#### 0.8.1
- Removed redundant calling of every function within the Naftemporiki class, effectively cutting runtime in half.

#### 0.8.0
This was a complete rework of how articles are found, scraped, analyzed, collated, and otherwise processed.

Initially, there was a major flaw within naftemporiki_links where the wrong function was called from BeautifulSoup.
"find" was used instead of "findAll" such that `find(class_='mainlink'` returned only the first article on each page,
 while `findAll(class_='mainlink')` returned every article on the page. This alone resolved a lot of issues, 
 and explained why I was getting results where nothing was being returned.
 
 Despite this glaring issue being fixed, it exposed a number of other issues within the code. It was difficult to read
 and, while well commented, was needlessly compact and hard to follow.
 
 - the `find` function in nafteporiki_links was replaced by `findAll` to return all articles instead of the first
 on each page.
    - Runtime has been multiplied by ~30, and takes close to 10 minutes per 100 pages scraped (33 from each section).
    
 - `find_econ_names`, `find_policy_names`, and `find_society_names` have been changed to return a list of plaintext
 from each article and a list of dates for each article in the form `[[text_list], [date_list]]`.
 
 - Checking for the keywords has been changed to its own function (`check_for_keywords`) which takes the input from
  each `find_x_names` function and checks each article plaintext for the keywords. This is done via a triple-nested
  loop which is horribly efficient, but works well enough and will be optimized in the near future.
  
 - A new function has been created (`count_dates`) to collate the times the keywords have been mentioned by date with
  a daily frequency.
  
 - `output_to_csv` is still used, now it just outputs the dict in the form of `date: count` in rows.
 
#### 0.7.4
 - Implemented a text feature in `output_to_csv` where I will receive a text everytime the script finished running.
 This has no meaningful effect on runtime, however it does require another library (`twilio.rest`). 
 
 - Dynamic keyword entry is now possible, since the keywords are no longer hardcoded into the functions.
 
