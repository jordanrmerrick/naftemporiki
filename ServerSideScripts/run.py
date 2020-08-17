import secondary_type as st
import datetime

# TODO:
#   Change static class list to dynamic using sys, inspect, etc.
#   Allow for multiple entries, not just a single or all.

def userInput():
    while True:
        inpt = input("Please select the websites you would like to scan. If you would like to select multiple websites,"
                     "separate them with a comma. If you would like to scan all websites, select that option."
                     "\nPOSSIBLE OPTIONS:\n1. Naftemporiki (Enter 'Na')\n2. Kathimerini (Enter 'Ka')\n3. All\n--> ")

        """
        if ',' in inpt:
            inpt.replace(" ", "")
            for i in range(len(inpt)):
                if inpt[i] == ',':
                    if i == len(inpt) - 1:
                        continue
                    x = inpt[:i]
                    y = int[i + 1:]
                    
                    if x.lower == 'ka':
                        ka = st.Kathimerini()
                        print('Starting Process... ')
                        ka.OutputCSV()
                    elif x.lower == 'na':
                        na = st.Naftemporiki()
                        print('Starting Process... ')
                        na.output_to_csv()
                        
                    if y.lower == 'ka':
                        ka = st.Kathimerini()
                        print('Starting Process... ')
                        ka.OutputCSV()
                    elif y.lower == 'na':
                        na = st.Naftemporiki()
                        print('Starting Process... ')
                        na.output_to_csv()
                    else:
                        continue    
                    return False
        """

        if inpt.lower() == 'na':
            na = st.Naftemporiki()
            print('Starting Process... ')
            na.output_to_csv()
            print("Ended process at {}".format(datetime.datetime.now()))
            return False

        elif inpt.lower() == 'ka':
            ka = st.Kathimerini()
            print('Starting Process... ')
            ka.OutputCSV()
            print("Ended process at {}".format(datetime.datetime.now()))
            return False

        elif inpt.lower() == 'all':
            na = st.Naftemporiki()
            ka = st.Kathimerini()
            print('Starting Process... ')
            na.output_to_csv()
            ka.OutputCSV()
            print("Ended process at {}".format(datetime.datetime.now()))
            return False

        else:
            continue

userInput()
