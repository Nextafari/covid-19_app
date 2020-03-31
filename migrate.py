from sql_with_python import *

file = open("time_series_covid19_deaths_global.csv")


choice_countries = ["Turkey", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom"]
heading = file.readlines(1)      #prints out everything on line 1 of the csv file in this case the headers for each column


for line in file.readlines():           #Using a for loop to read the lines of the csv file
	
	line_data = line.split(",")     #Using dot split method to convert the strings into a list item so it could worked on
	
	#print(line_data[1])            #prints all the data with an index of 1 in the csv file which is the country name

	country_name = line_data[1]
   
	if country_name in choice_countries:     #If country(line_data[1]) is equal to Turkey	
		country_exists = check_country(country_name)

		#print(country_exists)

		if country_exists:	
			for data in list(zip(line_data, heading[0].split(",")))[4:]:

 				print(date_format(data[1]), data[1])	
				#write_deaths(country_exists[0]['id'], data[0], date_format(data[1]))
				
		
		#else:	
			#longitude = line_data[2]	
			#latitude = 	line_data[3]
			#write_countries(country_name, longitude, latitude)



