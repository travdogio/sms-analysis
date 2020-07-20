import smsutils.xmlcleaner as cleaner
import smsutils.stats as stats

# Removes the MMS entries from the log
# cleaner.remove_non_sms('data/sms.xml', 'data/newoutput.xml')

myStats = stats.Stats('data/clean.xml')
print(myStats.message_count(''))
