from bs4 import BeautifulSoup
import in_links as il
import requests
import csv
import datetime

# In
in_policy_urls = []
in_econ_urls = []
in_world_urls = []
in_greece_urls = []

for j in range(1, 751):
    print('GENERATING IN PAGE URLS... {}/{}'.format(j, 751))
    in_policy_urls.append('https://www.in.gr/politics/page/{}'.format(j))
    in_econ_urls.append('https://www.in.gr/economy/page/{}'.format(j))
    in_world_urls.append('https://www.in.gr/world/page/{}'.format(j))
    in_greece_urls.append('https://www.in.gr/greece/page/{}'.format(j))

in_policy_urls_test = in_policy_urls[:30]
in_econ_urls_test = in_econ_urls[:30]
in_world_urls_test = in_world_urls[:30]
in_greece_urls_test = in_greece_urls[:30]

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
        name_short = 'το'
        name_long = 'Νόμος Κατσέλη'

        for url in range(len(self.el)):
            'class_ = main-content pos-rel article-wrapper'
            print('SEARCHING ARTICLE {} OF {}'.format(url, len(self.el)))
            page = requests.get(self.el[url])
            soup = BeautifulSoup(page.text, 'html.parser')

            collection_init = soup.find(class_='main-content pos-rel article-wrapper')
            print(collection_init)
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
        name_short = 'το'
        name_long = 'Νόμος Κατσέλη'

        for url in range(len(self.pl)):
            'class_ = main-content pos-rel article-wrapper'
            print('SEARCHING ARTICLE {} OF {}'.format(url, len(self.pl)))
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
        name_short = 'το'
        name_long = 'Νόμος Κατσέλη'

        for url in range(len(self.wl)):
            'class_ = main-content pos-rel article-wrapper'
            print('SEARCHING ARTICLE {} OF {}'.format(url, len(self.wl)))
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
        name_short = 'το'
        name_long = 'Νόμος Κατσέλη'

        for url in range(len(self.gl)):
            'class_ = main-content pos-rel article-wrapper'
            print('SEARCHING ARTICLE {} OF {}'.format(url, len(self.gl)))
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
        outfile = open('./output_{}.csv'.format(datetime.datetime), 'w')
        writer = csv.writer(outfile)
        writer.writerow(['Κατσελη Count', 'Νόμος Κατσέλη Count'])
        writer.writerows([self.find_econ_names(), self.find_policy_names(), self.find_world_names(),
                          self.find_greece_names()])


in_initialize = In(il.get_article_urls(in_econ_urls_test), il.get_article_urls(in_policy_urls_test),
                   il.get_article_urls(in_world_urls_test), il.get_article_urls(in_greece_urls_test))

in_initialize.output_to_csv()


dct = {
'Πέμπτη, 31 Οκτωβρίου 2019': 17,
'Τετάρτη, 30 Οκτωβρίου 2019': 28,
'Τρίτη, 29 Οκτωβρίου 2019': 22,
'Δευτέρα, 28 Οκτωβρίου 2019': 12,
'Κυριακή, 27 Οκτωβρίου 2019': 5,
'Σάββατο, 26 Οκτωβρίου 2019': 4,
'Παρασκευή, 25 Οκτωβρίου 2019': 4,
'Πέμπτη, 24 Οκτωβρίου 2019': 3
 }

