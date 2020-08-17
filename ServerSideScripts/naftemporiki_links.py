from bs4 import BeautifulSoup
import requests
import re

econ_url = 'https://www.naftemporiki.gr/finance/economy?page='
politics_url = 'https://www.naftemporiki.gr/politics/headlines?page='
society_url = 'https://www.naftemporiki.gr/society/headlines?page='

links = []

# Function to initially scrape every article from each page of articles
# (Website -> Econ Section -> Pages 1-1000, Articles Scraped)
def get_econ_links(econ_urls_limiting):
    print('ECON LINKS BEGINNING CYCLE')

    # Local variables declared
    final_urls = []
    count = 1

    # Loop to go through each page and scrape the urls for each article
    for link in econ_urls_limiting:
        print('\rFETCHING ECON ARTICLE URLS... {}% DONE'.format(round(count/len(econ_urls_limiting)*100, 1)), end='')

        # Using GET method to import website info as text (html)
        page = requests.get(link)
        soup = BeautifulSoup(page.text, 'html.parser')
        count += 1

        # Each url is attached to the css class 'mainLink' and it used to scrape all info regarding urls
        collection_init = soup.findAll(class_='mainLink')

        for i in range(len(collection_init)):
            # Some unwanted data is included in the mainLink call, so I use regex here to find the specific url
            end_link = re.findall(r"<a class=\"mainLink\" href=\"(.*)\">", str(collection_init[i]))

            try:
                # end_link returns as a list, so we just format it with list[index 0]
                final_urls.append('https://www.naftemporiki.gr{}'.format(end_link[0]))
            # We can just ignore it if the index is beyond the scope, and move onto the next page number
            except IndexError:
                pass


    # Return all the article urls as a list
    print("")
    return final_urls


# The policy and society sections of Naftemporiki are formatted in the same way so I'm able to use a single function
def get_policy_links(policy_urls_limiting):
    print('P/S BEGINNING CYCLE')

    # Declaring local variables
    init_urls = []
    final_urls = []
    count = 1

    # Loop to find every url for every article within pages 1-1000
    for plink in policy_urls_limiting:
        if policy_urls_limiting == 'policy_urls':
            print('\rFETCHING POLICY ARTICLE URLS... {}% DONE'.format(round(count/len(policy_urls_limiting)*100, 1)), end='')
        else:
            print('\rFETCHING SOCIETY ARTICLE URLS... {}% DONE'.format(round(count/len(policy_urls_limiting)*100, 1)), end='')

        # Calling page information as plaintext/html
        page = requests.get(plink)
        soup = BeautifulSoup(page.text, 'html.parser')
        count += 1

        # Finding the website links via regex - all urls are under the css class 'summary'
        collection_init = soup.findAll(class_='summary')
        for i in range(len(collection_init)):
            end_link_1 = re.findall(r"<a href=\"(.*)\">", str(collection_init[i]))
            end_link_2 = re.findall(r"(.*)\">", str(end_link_1[0]))

            if end_link_2[0][1] == 's':
                # Sometimes end_link can return empty and calling its 0th index is outside the scope
                try:
                    final_urls.append('https://www.naftemporiki.gr{}'.format(end_link_2[0]))
                # We can just ignore this error and move onto the next article
                except IndexError:
                    pass

    # For some reason there is still a " at the end of each url and the above regex doesn't like to remove it
    # We just remove it in a separate loop, which is inefficient but it works
    #for item in range(len(init_urls)):
    #   link_final = re.findall(r"(.*)\">", init_urls[item])
    #   final_urls.append(link_final[0])

    # Returns all the urls as a list
    print("")
    return final_urls