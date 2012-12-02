city = raw_input("Where do you think you're going?")
def planeRideCost(city):
    #this creates a dictionary where we have mapped values to variables
    citymap = {"Charlotte":183,
               "Tampa":220,
               "Pittsburgh":222,
               "Los Angeles":475}
    #need the if statement to confirm the variable is in the dictionary
    if city in citymap:
        return citymap[city]
    else:
        return "Not a city"
print planeRideCost(city)
