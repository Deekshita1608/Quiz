import mysql.connector
demodb = mysql.connector.connect(host="localhost", user="root", passwd="udgam", database="kbc")
democursor=demodb.cursor( )
democursor.execute("CREATE TABLE if not exists level1 (sno int(3), question VARCHAR(1000),option1 VARCHAR(1000), option2 VARCHAR(1000), option3 VARCHAR(1000), option4 VARCHAR(1000), answer VARCHAR(1000), PRIMARY KEY(sno))")
query='INSERT IGNORE INTO level1(sno,question,option1,option2,option3,option4,answer)VALUES(%s,%s,%s,%s,%s,%s,%s)'
values=[
    (1,'Who is your paternal grandfather\'s daughter-in-law?','Your mother', 'Your sister','Your niece','Your daughter','your mother'),
    (2,'Which city is the destination of the letter with PIN code 400001?','Kolkata','New Delhi','Mumbai','Chennai','mumbai'),
    (3,'What colour would you get if you mixed blue with red?','Green','Yellow','Purple','Black','purple'),
    (4,'What do the letters HB on a pencil stand for?','Hard bound','Hard black','Hot burnt','Hand Block','hard black'),
    (5,'In which of these cities could you spend an evening at a beach?','Cherrapunji','Chittor','Chennai','Chandigarh','chennai'),
    (6,'With reference to cricket, what does the "L" in "LBW" stand for?','Low','Leg','Line','Leap','leg'),
    (7,'Who played Anarkali in the film \'Mughal-e-Azam\'?','Meena Kumari','Madhubala','Nutan','Nargis','Madhubala'),
    (8,'According to the zodiac, which of the following is the birth sign of Jesus Christ?','Aquarius','Capricorn','Sagittarus','Scorpio','Capricorn'),
    (9,'Which of the following is the name given to a doctor who treats ailments of the eye?','Nephrologist','Gastroentrologist','Ophthalmologist','Virologist','Ophthalmologist'),
    (10,'Which century would the year 1650 be in?','16th','17th','15th','50th','17th')
    ]
democursor.executemany(query,values)
democursor.execute('commit')

democursor.execute("CREATE TABLE if not exists level2 (sno int(3), question VARCHAR(1000),option1 VARCHAR(1000), option2 VARCHAR(1000), option3 VARCHAR(1000), option4 VARCHAR(1000), answer VARCHAR(1000), PRIMARY KEY(sno))")
query='INSERT IGNORE INTO level2(sno,question,option1,option2,option3,option4,answer)VALUES(%s,%s,%s,%s,%s,%s,%s)'
values=[
    (1,'In the Ramayana, who among the following was not a daughter-in-law of Dasharatha?','Urmila','Shrutakirthi','Mandvi','Madri','Madri'),
    (2,'Which of the following characters from the Mahabharata was given the name\'Pitamah\'?','Pandu','Bhishma','Krishna','Arjuna','Bhishma'),
    (3,'In tennis, what is numeric value of the first point won by a player?','25','5','10','15','15'),
    (4,'Which community\'s New year Day is called \'Navroz\'?','Sikh','Parsi','Christian','Muslim','Parsi'),
    (5,'Which of the following regions is not named in the Indian national Anthem?','Punjab','Himachal','Gujarat','Delhi','Delhi'),
    (6,'In which of the following water bodies are the Lakshadweep Islands located?','Arabian Sea','Bay of Bengal','Indian Ocean','Gulf of Kutch','Arabian Sea'),
    (7,'Which of these is a helicopter used by the Indian Airforce?','Chakra','Cheetah','Chandra','Chakravyuha','Cheetah'),
    (8,'If an object absorbs all light, what would it look like?','White','Black','Transparent','Transluscent','Black'),
    (9,'Eskimos are natives of which region?','Arctic','Antarctic','Estonia','Eskomia','Arctic'),
    (10,'Which of these was the precursor of the Devanagri script?','Sharada','Pali','Newari','Siddhamatrika','Siddhamatrika')
    ]

democursor.executemany(query,values)
democursor.execute('commit')

democursor.execute("CREATE TABLE if not exists level3 (sno int(3), question VARCHAR(1000),option1 VARCHAR(1000), option2 VARCHAR(1000), option3 VARCHAR(1000), option4 VARCHAR(1000), answer VARCHAR(1000), PRIMARY KEY(sno))")
query='INSERT IGNORE INTO level3(sno,question,option1,option2,option3,option4,answer)VALUES(%s,%s,%s,%s,%s,%s,%s)'
values=[
    (1,'Who invented the oral Polio vaccine(OPV)?','Ronald Ross','Louis Pasteur','Frances Crick','Albert Sabin','Albert Sabin'),
    (2,'Which was the first country to make Christianity the official religion?','Italy','England','Greece','Armania','Armania'),
    (3,'Who was the first Chief Justice of the Supreme Court of India?','Mehr Chand Khanna','K. John Mathew','H.J. Kania','K.N. Wanchoo','H.J. Kania'),
    (4,'Which of these cricketers played Test Cricket for both India and Pakistan?','Dilawar Hussain','Amir Elahi','Jahangir Khan','Nasim-Ul-Ghani','Amir Elahi'),
    (5,'Which two places were connected by India\'s first electric train?','Bombay-Thane','Howrah-Hooghly','Delhi-Agra','Bombay VT-Kurla','Bombay VT-Kurla'),
    (6,'Which was the first Hindi film to use playback singing?','Dhoop Chhaon','Alam Ara','Noor Jahan','Bees Sal Baad','Dhoop Chhaon'),
    (7,'Who played the title role in the 1945 film \'Meera\'?','Kanan Devi','M S Subbulakshmi','Sulochana','Devika Rani','M S Subbulakshmi'),
    (8,'Who was independent India\'s first Union Defence Minister?','Sardar Baldev Singh','Jagjivan Ram','Rafi Ahmed Kidwai','Rajkumari Amrit Kaur','Sardar Baldev Singh'),
    (9,'Which branch of Ayurveda deals with mental disorders?','Kaayachikitsa','Bhutavidya','Vaajikarna','Rasaayana','Bhutavidya'),
    (10,'Which character from Harry Potter said the famous dialogue \'If you don\'t mind, I am now going to bed, before the two of you come up with another clever idea that could get us killed or worse, expelled\'','Albus Dumbledore','Collin Creevey','Hermione Granger','Ron weasley','Hermione Granger'),
    ]

democursor.executemany(query,values)
democursor.execute('commit')
demodb.close()
