import smsutils.xmlcleaner as cleaner
import smsutils.stats as stats
import csv

# Removes the MMS entries from the log
# cleaner.remove_non_sms('data/sms.xml', 'data/newoutput.xml')

myStats = stats.Stats('data/clean.xml')
contacts_dict = myStats.contact_stats()
with open('data/contact_stats.csv', 'w', encoding='utf8', newline='') as f:
    w = csv.writer(f)
    for contact in contacts_dict:
        w.writerow([contact, contacts_dict[contact]])




# for contact in c_dict:
#     print(contact + " : " + str(c_dict[contact]))