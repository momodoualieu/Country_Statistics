#*****************************************************
# Momodou Alieu Jallow
# 4/25/2019
#
# This program displays a ists of countries and their
# country flags in a sorted format
#*****************************************************

#Given a list of records, where each record is a list representing
#  a country name followed by the colors in it's flag
#Print the list of countries and colors in a table format.


countries = open("/Users/mjallow/Documents/pythonHW9/Flags.txt", "r")
country_flags = []
line = countries.readline()
while line:
    line = line.strip()
    values = line.split(",") 
    country_flags.append(values)
    line = countries.readline() 
    
countries.close()

#sorting by country
country_flags.sort()

#sorting flag colors
for item in country_flags:
    colorList = item[1:]
    
    #replace colors in order
    colorList.sort()
    for idx in range(1, len(item)):
        item[idx] = colorList[idx-1]


#get length of longest country name for spacing purposes 
#and column adjustment
#get initial longest name 
nameLength = len(country_flags[0][0])
for item in country_flags:
    if len(item[0]) > nameLength:
        nameLength = len(item[0])

#get color length for column adjustment
colorLength = len(country_flags[0][1])
for item in country_flags:
    for colors in item[1:]:
        if len(colors) > colorLength:
            colorLength = len(colors)


# Print the table
print("When colors and countries are sorted ")
print("--------------------------------------")
for item in country_flags:      

    # print all items in list with 3 spaces between each one
    #print('   '.join(item))
    # print country name, a tab, then all remaining items separated by commas
    for i in range(len(item)):
        if i == 0:
            formattedString = '{:<{nameLength}}'.format(item[0], nameLength = nameLength)
        else:
            formattedString = '{:<{colorLength}}'.format(item[i], colorLength = colorLength)
        print(formattedString, end=' ')
    print()
print()
print("--------------------------------------")

#*****************************************************
# print statistical information
#***************************************************

#countries with most and least colors 
#simply get length of lists
lengthforMost = len(country_flags[0])
countryMost = country_flags[0][0]
lengthforLeast = len(country_flags[0])
countryLeast = country_flags[0][0]

for item in country_flags:
    if len(item) > lengthforMost:
        lengthforMost = len(item)
        countryMost = item[0]
    if len(item) < lengthforLeast:
        lengthforLeast = len(item)
        countryLeast = item[0]

print("The country with most colors is: ", countryMost )
print("The country with least colors is: ", countryLeast )

#get all countries with most and least colors(equal number)
countriesWithLeast = []
countriesWithMost = []
for item in country_flags:
    if len(item) == lengthforLeast:
        countriesWithLeast.append(item[0])
    elif len(item) == lengthforMost:
        countriesWithMost.append(item[0])

print("The countries with the least flags are: ")
for item in countriesWithLeast:
    print(item)

print("The countries with the most flags are: ")
for item in countriesWithMost:
    print(item)

    
#statistical information for countries that contain color WHITE
coountriesWithWhite = []
for item in country_flags:
    for colors in item[1:]:
        if colors == 'White':
            coountriesWithWhite.append(item[0])

print("Number of countries with the color White in flag: ", len(coountriesWithWhite))

#one country with color white in flag
print("A country with color white in flag: ", coountriesWithWhite[2])

#All countries with color white 
print("All countries with color white in flag are as follows: ")
for item in coountriesWithWhite:
    print(item)

    


