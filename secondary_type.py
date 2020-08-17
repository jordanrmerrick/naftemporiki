from bs4 import BeautifulSoup
import requests
import csv
import re
import os
import datetime

class Naftemporiki:

    def __init__(self):
        self.st = []

    def generate_pages(self):
        print('STARTING PROCESS')
        urls_1, urls_2, urls_3, urls_4, urls_5, urls_6 = [], [], [], [], [], []

        urls = [urls_1, urls_2, urls_3, urls_4, urls_5, urls_6]

        # Test Case
        # urls_new = [urls_6]

        for i in range(1, 111):
            urls_1.append('https://www.naftemporiki.gr/search/?q=Νομου+Κατσελη&page={}'.format(i))
            urls_2.append('https://www.naftemporiki.gr/search/?q=Νόμος+Κατσέλη&page={}'.format(i))
            urls_3.append('https://www.naftemporiki.gr/search/?q=ν.+Κατσέλη&page={}'.format(i))
            urls_4.append('https://www.naftemporiki.gr/search/?q=3869/2010&page={}'.format(i))
            urls_5.append('https://www.naftemporiki.gr/search/?q=υπερχρεωμένα+νοικοκυριά&page={}'.format(i))
            urls_6.append('https://www.naftemporiki.gr/search/?q=grexit&page={}'.format(i))

        return urls

    def get_pages(self):
        urls = self.generate_pages()
        final_dates = []
        count = 0
        for url_list in urls:
            dates = []
            count1 = 0
            count += 1
            for page in url_list:
                print('\rList {}, url {}'.format(count, count1), end='')
                page = requests.get(page)
                soup = BeautifulSoup(page.text, 'html.parser')

                collection_date = soup.findAll(class_='topicDate')
                c = list(collection_date)

                dates.append(c)
                count1 += 1

            # class = topicDate
            final_dates.append(dates)

        return final_dates

    def output_to_csv(self):

        """
        final_dates is the input
        for each keyword there is a list
        [0]
            [0]
                [0]
                    str1
                    str2
                    str3
                [1]
                [2]
                [3]
            [1]
            [2]
            [3]
        [1]
        [2]
        [3]
        [4]

        I want this output in a CSV format so that each keyword outputs to a different csv
        :return:
        """
        lst = self.get_pages()
        # x[0][0]
        for x in range(len(lst)):
            titles = ['\"Νομου+Κατσελη\"', '\"Νόμος+Κατσέλη\"', '\"ν.+Κατσέλη\"', '\"3869_2010\"',
                      '\"υπερχρεωμένα+νοικοκυριά\"', '\"grexit\"']
            with open('./SecondaryOutput/output2_{}_{}.csv'.format(titles[x], datetime.datetime.now().strftime("%H:%M:%S")), 'w') as output_file:
                writer = csv.writer(output_file)
                writer.writerows(lst[x])

    # output_to_csv()


class Kathimerini:

    def __init__(self):
        self.setX = []

    def genPages(self):
        urls_1, urls_2, urls_3, urls_4, urls_5, urls_6 = [], [], [], [], [], []
        urls = [urls_1, urls_2, urls_3, urls_4, urls_5, urls_6]
        # url_test = [urls_1]

        for i in range(0, 600):
            urls_1.append("https://www.kathimerini.gr/search?q=Νομου+Κατσελη&t=0&page={}#searchFull".format(i))
            urls_2.append("https://www.kathimerini.gr/search?q=Νόμος+Κατσέλη&t=0&page={}#searchFull".format(i))
            urls_3.append("https://www.kathimerini.gr/search?q=ν.+Κατσέλη&t=0&page={}#searchFull".format(i))
            urls_4.append("https://www.kathimerini.gr/search?q=3869/2010&t=0&page={}#searchFull".format(i))
            urls_5.append("https://www.kathimerini.gr/search?q=υπερχρεωμένα+νοικοκυριά&t=0&page={}#searchFull".format(i))
            urls_6.append("https://www.kathimerini.gr/search?q=grexit&t=0&page={}#searchFull".format(i))

        return urls

    def parsePages(self):
        urls = self.genPages()

        dates = []
        keywords = ['Νομου Κατσελη', 'Νόμος Κατσέλη', 'ν. Κατσέλη', '3869/2010', 'υπερχρεωμένα νοικοκυριά', 'grexit']
        count = 0
        for urlList in urls:
            lst = []
            count1 = 0
            for url in urlList:
                print("\rKeyword: {} --- Page: {}".format(keywords[count], count1), end="")
                page = requests.get(url)
                soup = BeautifulSoup(page.text, 'html.parser')

                collection_date = soup.find_all("small")
                collection_date = list(collection_date)
                for date in collection_date:
                    getRegexed = re.match(r"<small>\[(.*)\]</small>", str(date))
                # StoL = ast.literal_eval(str(getRegexed.group(1)))
                    try:
                        lst.append(getRegexed.group(1))
                    except AttributeError:
                        pass

                count1 += 1

            count += 1
            dates.append(lst)

        return dates

    def reverseMonthDay(self):
        dates = self.parsePages()
        ret_dates = []
        for date_lst in dates:
            lst = []
            for date in date_lst:
                month = date[3:5]
                day = date[0:2]
                year = date[6:]
                lst.append("{}/{}/{}".format(month, day, year))

            ret_dates.append(lst)

        return ret_dates

    def countDates(self):
        dates = self.reverseMonthDay()
        counts = []
        for lst in dates:
            datelst = []
            st = set(lst)
            for date in st:
                x = lst.count(date)
                datelst.append([date, x])

            counts.append(datelst)

        return counts

    def OutputCSV(self):

        path = './Kathimerini_{}'.format(datetime.datetime.now())
        os.mkdir(path, mode=0o777)

        dates = self.countDates()

        for x in range(len(dates)):
            titles = ['\"Νομου+Κατσελη\"', '\"Νόμος+Κατσέλη\"', '\"ν.+Κατσέλη\"', '\"3869_2010\"',
                      '\"υπερχρεωμένα+νοικοκυριά\"', '\"grexit\"']

            with open('{}/outputKathimerini_{}.csv'.format(path, titles[x]), 'w') as output_file:
                writer = csv.writer(output_file)
                writer.writerows(dates[x])


