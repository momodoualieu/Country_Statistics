#****************************************
# Momodou Alieu Jallow
# 4/30/2018
#
# This program reads data from a file and 
# displays different statistics for 
# countries 
#****************************************

countries = open("/Users/mjallow/Documents/pythonHW9/world_countries.csv", "r")
country_stats = []

headings = countries.readline().strip().split(",")

line = countries.readline()
while line:
    line = line.strip()
    values = line.split(",") 
    country_stats.append(values)
    line = countries.readline() 

countries.close()

print("Countries with a population of over 400,000,000")
print()

for item in country_stats:
    if float(item[3]) > 400000000:
        print(item[0], float(item[3]))

print()
print("----------------------------------")

population_min = float(input("Enter population minimum: "))
print("Countries with a population over", population_min)

for item in country_stats:
    if float(item[3]) > population_min:
        print(item[0], float(item[3]))

print()
print("----------------------------------")

#get country length for formatting
countryLength = len(country_stats[0][0])
for item in country_stats:
        if len(item[0]) > countryLength:
                countryLength = len(item[0])

#get input from user 
col = int(input("Enter column[3-6]:"))

while col < 3 or col > 6:
    col = int(input("Enter column[3-6]: "))

#pass toPrint1 to input since input takes only one argument 
toPrint1 = "Enter " + headings[col] + " minimum: "
mini1 = int(input(toPrint1))
print("Countries with a", headings[col], "over", mini1)
for item in country_stats:
    if float(item[col]) > mini1:
        formattedString = '{:<{countryLength}}'.format(item[0], countryLength = countryLength)
        print(formattedString, float(item[col]))

print()
print("----------------------------------")

# get column name input from user
colName = input("Enter column name: ")
colNameIndex = headings.index(colName)

#pass toPrint2 to input since input takes only one argument 
toPrint2 = "Enter " + colName + " minimum: "
mini2 = float(input(toPrint2))
print("Countries with a", colName, "over", mini2)

for item in country_stats:
    if float(item[colNameIndex]) > mini2:
        formattedString = '{:<{countryLength}}'.format(item[0], countryLength = countryLength)
        print(formattedString, float(item[colNameIndex]))

print()
print("----------------------------------")

#dictionary that contains regions
regionDictionary = {"ASIA (EX. NEAR EAST)": 0, "EASTERN EUROPE": 0, "NORTHERN AFRICA": 0, "OCEANIA": 0, "WESTERN EUROPE": 0, "SUB-SAHARAN AFRICA": 0,
"LATIN AMER. & CARIB": 0, "C.W. OF IND. STATES": 0, "NEAR EAST": 0, "NORTHERN AMERICA": 0, "BALTICS": 0}

#Total population by region
#add to value when key is found
for item in country_stats:
        for k in regionDictionary:
                if item[2] == k:
                        regionDictionary[k] += int(item[3])
print("Total population by region:")

#get length for formatting
regionList = list(regionDictionary.keys())
regionLength = len(regionList[0])
for item in regionList[1:]:
        if len(item) > regionLength:
                regionLength = len(item)

#print region and total population
for k in regionDictionary:
        formattedString = '{:<{regionLength}}'.format(k, regionLength = regionLength)
        print(formattedString, regionDictionary[k])



                        








