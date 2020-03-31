import pymysql.cursors

#This connects us to the database
connection = pymysql.connect (host = "localhost",
                                    user = "root",
                                    password = "",
                                    db = "corona_virus",
                                    charset = "utf8mb4",
                                    cursorclass = pymysql.cursors.DictCursor) 


def create_tables():

    with connection.cursor() as cursor:
        table_for_countries = "create table if not exists countries (id int primary key not null auto_increment, name varchar(100), longitude float, latitude float)"
        cursor.execute(table_for_countries)

        table_for_deaths = "create table if not exists deaths (id int primary key not null auto_increment, country_id int(100), foreign key(country_id) references countries(id), deaths int, date_of_death date)"
        cursor.execute(table_for_deaths)

        connection.commit()




#Enters the selected countries into the database
def write_countries(name, longitude, latitude):

    with connection.cursor() as cursor:
        enter_country = f"insert into countries (name, longitude, latitude) values ('{name}', '{longitude}', '{latitude}')"
        cursor.execute(enter_country)

        connection.commit()


#Enters the deaths in selected countries into the database
def write_deaths(country_id, deaths, date_of_death):

    with connection.cursor() as cursor:
        enter_death = f"insert into deaths (country_id, deaths, date_of_death) values ('{country_id}', '{deaths}', '{date_of_death}')"

        cursor.execute(enter_death)

        connection.commit()


#Gets any one country from the database
def check_country(name):

    with connection.cursor() as cursor:
        get_country = f"select * from countries where name = '{name}'"
        cursor.execute(get_country)

        response = cursor.fetchall()
        return response
        


#This function formats the date in the csv file into sql format of year, month and day
def date_format(date):
	
	month, day, year = date.split("/")      #spliting the dates in the csv file into a list eg 1/20/20 now becomes [1, 20, 20]
	
	#using a - to separate the list([1, 20, 20]), flipping the list while concatenating +20 to the year(20) to have ([2020-1-20])
	changed_date = "-".join([year.replace('\n','')+'20', month, day])
	
	return changed_date


#write_countries("Turkey", 38.9637,35.2433)
create_tables()


