from bs4 import BeautifulSoup
import naftemporiki_links as nl
import in_links as il
import requests
import csv
import datetime
import re
from collections import Counter

print("Version 0.8.2")

econ_url = 'https://www.naftemporiki.gr/finance/economy?page='
politics_url = 'https://www.naftemporiki.gr/politics/headlines?page='
society_url = 'https://www.naftemporiki.gr/society/headlines?page='

kwords = ['Κατσελη', 'Νόμος Κατσέλη', 'κατσελη', 'νόμος κατσελη']

# Naftemporiki
na_econ_urls = []
na_policy_urls = []
na_society_urls = []

# In
in_policy_urls = []
in_econ_urls = []
in_world_urls = []
in_greece_urls = []

# Generates urls for each page within each section of the newspaper (naftemporiki.gr)

# Generates urls for each page within each section of the newspaper (in.gr)


# Class object defining Naftemporiki web-scraping
class Naftemporiki:

    # declaring variables for the class (list of econ urls, list of policy urls, list of society urls)
    def __init__(self, el, pl, sl):
        self.el = el
        self.pl = pl
        self.sl = sl

    # The structure of the econ section of the website is different from the rest, and it needs its own
    # function to find information in the econ articles
    def find_econ_names(self):

        print('\nScraping text and dates from economic articles - Part 1/3.')

        #Local variables
        text_list, date_list = [], []

        # Takes each page of articles (self.el) and searches them for
        for url in range(len(self.el)):
            print('\rSEARCHING ECON ARTICLES... {}% DONE'.format(round(url/len(self.el)*100, 1)), end='')
            page = requests.get(self.el[url])
            soup = BeautifulSoup(page.text, 'html.parser')

            # Finds everything under the span title and with the id spBody, which in this case is
            # the main text of the article
            collection_init = soup.find("span", {'id': 'spBody'})
            collection_date = soup.find(class_='Date')

            cd_final = re.findall(r"<div class=\"Date\" id=\"CPMain_sDate\">(.*) \d\d:\d\d</div>", str(collection_date))
            try:
                date_list.append(str(cd_final[0]))
                text_list.append(str(collection_init))
            except IndexError:
                pass

        return [text_list, date_list]

    def find_policy_names(self):

        print('\nScraping text and dates from policy articles - Part 2/3.')

        # Variable declarations
        text_list, date_list = [], []

        # This will cycle through each article within the list of pages in the policy section of Naftemporiki
        for url in range(len(self.pl)):
            print('\rSEARCHING POLICY ARTICLES... {}% DONE'.format(round(url/len(self.pl)*100, 1)), end='')

            # The get request and html parsing is handled internally by BeautifulSoup
            page = requests.get(self.pl[url])
            soup = BeautifulSoup(page.text, 'html.parser')

            # Finds everything under the span title and with the id spBody, which in this case is
            # the main text of the article
            collection_init = soup.find("span", {'id': 'spBody'})
            collection_date = soup.find(class_='Date')

            cd_final = re.findall(r"<div class=\"Date\" id=\"leftPHArea_sDate\">(.*) \d\d:\d\d</div>", str(collection_date))

            try:
                date_list.append(str(cd_final[0]))
                text_list.append(str(collection_init))
            except IndexError:
                pass

        return [text_list, date_list]

    def find_society_names(self):

        print('\nScraping text and dates from society articles - Part 3/3.')

        # Variable declarations
        text_list, date_list = [], []

        # This will cycle through each article within the list of pages in the policy section of Naftemporiki
        for url in range(len(self.sl)):
            print('\rSEARCHING SOCIETY ARTICLES... {}% DONE'.format(round(url/len(self.sl)*100, 1)), end='')

            # The get request and html parsing is handled internally by BeautifulSoup
            page = requests.get(self.sl[url])
            soup = BeautifulSoup(page.text, 'html.parser')

            # Finds everything under the span title and with the id spBody, which in this case is
            # the main text of the article
            collection_init = soup.find("span", {'id': 'spBody'})
            collection_date = soup.find(class_='Date')

            cd_final = re.findall(r"<div class=\"Date\" id=\"leftPHArea_sDate\">(.*) \d\d:\d\d</div>", str(collection_date))

            try:
                date_list.append(str(cd_final[0]))
                text_list.append(str(collection_init))
            except IndexError:
                pass
            # Since we're returning how many times each keyword is said through the sum of all the articles,
            # this is just a basic counting mechanism

        return [text_list, date_list]

    def check_for_keywords(self):
        e = self.find_econ_names()
        p = self.find_policy_names()
        s = self.find_society_names()

        text_list = [e[0], p[0], s[0]]
        date_list = [e[1], p[1], s[1]]
        final_list = []
        k_words = ['Κατσελη', 'Νόμος Κατσέλη', 'κατσελη', 'νόμος κατσελη', 'τσ']

        for i in range(len(k_words)):
            for j in range(len(text_list)):
                for k in range(len(text_list[j])):
                    if k_words[i] in text_list[j][k]:
                        final_list.append(date_list[j][k])

        return final_list

    def count_dates(self):

        keyword = self.check_for_keywords()
        cnt = Counter()

        for i in keyword:
            cnt[i] += 1

        return dict(cnt)

    def output_raw_print(self):
        print(self.count_dates())
        print("\n\n\n\n")

    def output_to_csv(self):
        print('ATTEMPTING CSV EXPORT')
        values = []

        cd = self.count_dates()
        for key, value in cd.items():
            temp = [key, value]
            values.append(temp)

        # Generates an empty csv with the name output_{} where {} is the current time in Hour:Minute:Second
        with open('./naftemporiki_output_{}.csv'.format(datetime.datetime.now().strftime("%H:%M:%S")), 'w') as output_file:
            writer = csv.writer(output_file)
            writer.writerows(values)


    def output_to_csv_false(self):
        print('FAKE PRINT. . . FINISHING UP')
        print('{} \n {} \n {} \n'.format(self.find_econ_names(), self.find_policy_names(), self.find_society_names()))


class In:

    def __init__(self, el, pl, wl, gl):
        self.el = el
        self.pl = pl
        self.wl = wl
        self.gl = gl

    def find_econ_names(self):
        print('ECON MAIN CYCLE')
        count_list = []
        count_short = 0
        count_long = 0
        name_short = 'grexit'
        name_long = 'Grexit'

        for url in range(len(self.el)):
            'class_ = main-content pos-rel article-wrapper'
            print('SEARCHING ARTICLE {} OF {}... {}% DONE'.format(url, len(self.el), round(url/len(self.el)*100, 2)))
            page = requests.get(self.el[url])
            soup = BeautifulSoup(page.text, 'html.parser')

            collection_init = soup.find(class_='main-content pos-rel article-wrapper')
            if name_short in str(collection_init):
                count_short += 1

            if name_long in str(collection_init):
                count_long += 1

        count_list.append(count_long)
        count_list.append(count_short)

        return count_list

    def find_policy_names(self):
        print('POLICY MAIN CYCLE')
        count_list = []
        count_short = 0
        count_long = 0
        name_short = 'grexit'
        name_long = 'Grexit'

        for url in range(len(self.pl)):
            'class_ = main-content pos-rel article-wrapper'
            print('SEARCHING ARTICLE {} OF {}... {} PERCENT DONE'.format(url, len(self.pl), round(url/len(self.pl)*100, 2)))
            page = requests.get(self.pl[url])
            soup = BeautifulSoup(page.text, 'html.parser')

            collection_init = soup.find(class_='main-content pos-rel article-wrapper')
            if name_short in str(collection_init):
                count_short += 1

            if name_long in str(collection_init):
                count_long += 1

        count_list.append(count_long)
        count_list.append(count_short)

        return count_list

    def find_world_names(self):
        print('GREECE MAIN CYCLE')
        count_list = []
        count_short = 0
        count_long = 0
        name_short = 'grexit'
        name_long = 'Grexit'

        for url in range(len(self.wl)):
            'class_ = main-content pos-rel article-wrapper'
            print('SEARCHING ARTICLE {} OF {}... {}% DONE'.format(url, len(self.wl), round(url/len(self.wl)*100, 2)))
            page = requests.get(self.wl[url])
            soup = BeautifulSoup(page.text, 'html.parser')

            collection_init = soup.find(class_='main-content pos-rel article-wrapper')
            if name_short in str(collection_init):
                count_short += 1

            if name_long in str(collection_init):
                count_long += 1

        count_list.append(count_long)
        count_list.append(count_short)

        return count_list

    def find_greece_names(self):
        print('GREECE MAIN CYCLE')
        count_list = []
        count_short = 0
        count_long = 0
        name_short = 'grexit'
        name_long = 'Grexit'

        for url in range(len(self.gl)):
            'class_ = main-content pos-rel article-wrapper'
            print('SEARCHING ARTICLE {} OF {}... {}% DONE'.format(url, len(self.gl), round(url/len(self.gl)*100, 2)))
            page = requests.get(self.gl[url])
            soup = BeautifulSoup(page.text, 'html.parser')

            collection_init = soup.find(class_='main-content pos-rel article-wrapper')
            if name_short in str(collection_init):
                count_short += 1

            if name_long in str(collection_init):
                count_long += 1

        count_list.append(count_long)
        count_list.append(count_short)

        return count_list

    def output_to_csv(self):
        print('ATTEMPTING TO OUTPUT TO CSV')
        outfile = open('./in_output_{}.csv'.format(datetime.datetime.now().strftime("%H:%M:%S")), 'w')
        writer = csv.writer(outfile)
        writer.writerow(['Κατσελη Count', 'Νόμος Κατσέλη Count'])
        writer.writerows([self.find_econ_names(), self.find_policy_names(), self.find_world_names(),
                          self.find_greece_names()])

        # This will text the 'to' number (in this case, mine) when the csv has been generated
        # client = Client('AC8cf8e53f8fb8cb971bfda5d8fc9ec7dc', '50e4ac6af374d85538be724a70230c2c')
        # client.messages.create(to='+13123510150', from_="+12512659046",
                               # body='Your script has finished running!')

    def output_to_csv_false(self):
        print('FAKE PRINT. . . FINISHING UP')


# Variable calling the Naftemporiki class and declaring its variables

# Variable calling the In class and declaring its variables
def user_input_website():
    while True:
        news_site = input("Please enter either Na or In: ")
        page_count = input("How many pages do you want to scan?: ")

        page_count = int(page_count)

        if news_site.lower() == "na":

            for i in range(1, page_count + 1):
                na_econ_urls.append(econ_url + '{}'.format(i))
                na_policy_urls.append(politics_url + '{}'.format(i))
                na_society_urls.append(society_url + '{}'.format(i))
                if i == page_count:
                    print('Successfully generated {} urls.'.format(page_count))

            na_initialize = Naftemporiki(nl.get_econ_links(na_econ_urls), nl.get_policy_links(na_policy_urls),
                                         nl.get_policy_links(na_society_urls))

            na_initialize.output_to_csv()
            return False

        elif news_site.lower() == 'in':

            for j in range(1, page_count + 1):
                in_policy_urls.append('https://www.in.gr/politics/page/{}'.format(j))
                in_econ_urls.append('https://www.in.gr/economy/page/{}'.format(j))
                in_world_urls.append('https://www.in.gr/world/page/{}'.format(j))
                in_greece_urls.append('https://www.in.gr/greece/page/{}'.format(j))
                if j == page_count:
                    print('Successfully generated {} urls.'.format(page_count))

            in_initialize = In(il.get_article_urls(in_econ_urls), il.get_article_urls(in_policy_urls),
                               il.get_article_urls(in_world_urls), il.get_article_urls(in_greece_urls))

            in_initialize.output_to_csv()
            return False

        else:
            print("Please try again")


user_input_website()