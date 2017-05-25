import csv
import numpy as np
import matplotlib.pyplot as plt

crime_statistics = {}
crimes_per_year = {'2011' : 0, '2012' : 0, '2013' : 0, '2014' : 0, 'Recent' : 0}

most_crime_year = '2011'
crimes_number = 0
most_common_crime = ''
most_common_crime_number = 0
rarest_crime = ''
rarest_crime_number = 2000000000


with open('crime_incident_data_2011.csv', 'r') as userFile:
    crimes_per_year['2011'] = 0
    userFileReader = csv.reader(userFile)

    for line in userFileReader:
        if str(line[3]) == 'Major Offense Type':
            continue
        elif str(line[3]) in crime_statistics:
            crime_statistics[str(line[3])] = crime_statistics[str(line[3])] + 1
            crimes_per_year['2011'] = crimes_per_year['2011'] + 1
        else:
            crime_statistics[str(line[3])] = 1
            crimes_per_year['2011'] = crimes_per_year['2011'] + 1


with open('crime_incident_data_2012.csv', 'r') as userFile:
    crimes_per_year['2012'] = 0
    userFileReader = csv.reader(userFile)

    for line in userFileReader:
        if str(line[3]) == 'Major Offense Type':
            continue
        elif str(line[3]) in crime_statistics:
            crime_statistics[str(line[3])] = crime_statistics[str(line[3])] + 1
            crimes_per_year['2012'] = crimes_per_year['2012'] + 1
        else:
            crime_statistics[str(line[3])] = 1
            crimes_per_year['2012'] = crimes_per_year['2012'] + 1

with open('crime_incident_data_2013.csv', 'r') as userFile:
    crimes_per_year['2013'] = 0
    userFileReader = csv.reader(userFile)

    for line in userFileReader:
        if str(line[3]) == 'Major Offense Type':
            continue
        elif str(line[3]) in crime_statistics:
            crime_statistics[str(line[3])] = crime_statistics[str(line[3])] + 1
            crimes_per_year['2013'] = crimes_per_year['2013'] + 1
        else:
            crime_statistics[str(line[3])] = 1
            crimes_per_year['2013'] = crimes_per_year['2013'] + 1

with open('crime_incident_data_2014.csv', 'r') as userFile:
    crimes_per_year['2014'] = 0
    userFileReader = csv.reader(userFile)

    for line in userFileReader:
        if str(line[3]) == 'Major Offense Type':
            continue
        elif str(line[3]) in crime_statistics:
            crime_statistics[str(line[3])] = crime_statistics[str(line[3])] + 1
            crimes_per_year['2014'] = crimes_per_year['2014'] + 1
        else:
            crime_statistics[str(line[3])] = 1
            crimes_per_year['2014'] = crimes_per_year['2014'] + 1

with open('crime_incident_data_recent.csv', 'r') as userFile:
    crimes_per_year['Recent'] = 0
    userFileReader = csv.reader(userFile)
    for line in userFileReader:
        if str(line[3]) == 'Major Offense Type':
            continue
        elif str(line[3]) in crime_statistics:
            crime_statistics[str(line[3])] = crime_statistics[str(line[3])] + 1
            crimes_per_year['Recent'] = crimes_per_year['Recent'] + 1
        else:
            crime_statistics[str(line[3])] = 1

for key in crime_statistics:
    if crime_statistics[key] > most_common_crime_number:
        most_common_crime = key
        most_common_crime_number = crime_statistics[key]
    if crime_statistics[key] < rarest_crime_number:
        rarest_crime = key
        rarest_crime_number = crime_statistics[key]
for key in crimes_per_year:
    if crimes_per_year[key] > crimes_number:
        most_crime_year = key
        crimes_number = crimes_per_year[key]


print(most_crime_year + ' crime was the most abundant with ' + str(crimes_number) + ' occurences.')
print(most_common_crime + ' was the most common crime over the years with ' + str(most_common_crime_number) + ' occurences.')
print(rarest_crime + ' was the rarest crime over the years with ' + str(rarest_crime_number) + ' occurences.')

temp_list = []
labels = []
for key in crime_statistics:
    labels.append(key)
    temp_list.append(0.1)


explode = tuple(temp_list)

sizes = []
for key in crime_statistics:
    sizes.append(crime_statistics[key])




fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
