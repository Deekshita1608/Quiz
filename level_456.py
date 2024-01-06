import mysql.connector
demodb = mysql.connector.connect(host="localhost", user="root", passwd="udgam", database="kbc")
democursor=demodb.cursor( )

democursor.execute("CREATE TABLE if not exists level4 (sno int(3), question VARCHAR(1000),option1 VARCHAR(1000), option2 VARCHAR(1000), option3 VARCHAR(1000), option4 VARCHAR(1000), answer VARCHAR(1000),PRIMARY KEY(sno))")
query='INSERT IGNORE INTO level4 (sno,question,option1,option2,option3,option4,answer)VALUES(%s,%s,%s,%s,%s,%s,%s)'
values=[
    (1,'Which gods are jointly worshipped under the title \'Hari-Hara\'?','Shiva & Brahma', 'Brahma & Vishnu',' Vishnu & Shiva','Ganesh & Indra','Vishnu & Shiva'),
    (2,'Which boxer’s real name is Cassius Clay?','Mike Tyson',' Muhammad Ali','Sonny Liston',' Roberto Duran',' Muhammad Ali'),
    (3,'Gidda is a traditional folk dance form of which Indian state?',' Gujarat','Punjab','Orissa',' Kerala','Punjab'),
    (4,'Which layer of gas surrounds the Earth 30 kms above its surface?','Ozone',' Nitrogen','Carbon Dioxide','Oxygen','Ozone'),
    (5,'Which of these is not found in India in the wild?','Leopard','Tiger','Lion','Puma','Puma'),
    (6,'Which of these diseases is caused by a vitamin deficiency?',' Cholera','Plague',' Rickets','Typhoid',' Rickets'),
    (7,'Which comic character is known as \'The Ghost Who Walks\'?','Mandrake',' Flash Gordon','Phantom','Spiderman','Phantom'),
    (8,'The name of which state literally means \'The Land of Gems\'?','Nagaland','Manipur','Mizoram','Meghalaya','Manipur'),
    (9,'In the Mahabharata, what was the capital of the Kauravas?','Hastinapur',' Mathura','Indraprastha','Kaushambhi','Hastinapur'),
    (10,'Who played the title role of the cook in the film ‘Bawarchi’?','Rajesh Khanna','Sanjeev Kumar','Vinod Mehra','Dharmendra','Rajesh Khanna'),
     ]
democursor.executemany(query,values)
democursor.execute('commit')

import mysql.connector
demodb = mysql.connector.connect(host="localhost", user="root", passwd="udgam", database="kbc")
democursor=demodb.cursor( )
democursor.execute("CREATE TABLE if not exists level5 (sno int(3), question VARCHAR(1000),option1 VARCHAR(1000), option2 VARCHAR(1000), option3 VARCHAR(1000), option4 VARCHAR(1000), answer VARCHAR(1000),PRIMARY KEY(sno))")
query='INSERT IGNORE INTO level5 (sno,question,option1,option2,option3,option4,answer)VALUES(%s,%s,%s,%s,%s,%s,%s)'
values=[
    (1,'In which sport is the Rovers Cup awarded?','Tennis', 'Football','Golf','Hockey','Football'),
    (2,'Which leader was also called the ‘Fuehrer’?','Stalin', 'Hitler','Idi Amin','Mussolini','Hitler'),
    (3,'Which of these countries has not won the Football World Cup for men?','Argentina', 'England','France','Russia','Russia'),
    (4,'What are Shadaj, Madhyam, Pancham and Nishad names of?','Yogasanas', 'Musical Swaras','Dance Mudras','Mangoes','Musical Swaras'),
    (5,'From which language have the words almirah and peon entered Indian usage?','Persian', ' Arabic','French','Portuguese','Portuguese'),
    (6,'Which of these is the lightest chemical element?','Helium', ' Oxygen',' Hydrogen',' Nitrogen',' Hydrogen'),
    (7,'What is the atmospheric pressure in the hills in comparison to sea level?','Higher', 'Lower','Identical','Absent','Lower'),
    (8,'Which famous singer played the title role in the 1935 film \'Devdas\'?','Manna Dey', ' K L Saigal','Mukesh','C Ramachandran','K L Saigal'),
    (9,'A deficiency of which of the following vitamins causes night blindness?','Vitamin A', 'Vitamin B','Vitamin D','Vitamin C','Vitamin A'),
    (10,'What was the name given to the first cloned sheep?','Sally', 'Polly','Dolly','Molly','Dolly'),
    
    ]
democursor.executemany(query,values)
democursor.execute('commit')



democursor.execute("CREATE TABLE if not exists level6 (sno int(3), question VARCHAR(1000),option1 VARCHAR(1000), option2 VARCHAR(1000), option3 VARCHAR(1000), option4 VARCHAR(1000), answer VARCHAR(1000),PRIMARY KEY(sno))")
query='INSERT IGNORE INTO level6 (sno,question,option1,option2,option3,option4,answer)VALUES(%s,%s,%s,%s,%s,%s,%s)'
values=[
    (1,'Which of these sportspersons has not won an Olympic Gold medal?','Dipa Karmakar', 'Leander Paes','Abhinav Bindra','Karnam Malleswari','Dipa Karmakar'),
    (2,'Yehudi Menuhin was a world renowned exponent of which musical instrument?',' Sitar', 'Violin','Piano',' Guitar','Violin'),
    (3,'What are Kakori, Shashlik and Husseini types of?','Kebabs', 'Face Masks','Painting styles','Mountain Peaks','Kebabs'),
    (4,'Which of these countries has not had a Prime Minister of Indian origin?',' Fiji', 'Singapore','Mauritius','Guyana','Singapore'),
    (5,'What does the \'X\' stand for in the term X-ray?','Exact', 'Unknown','Electric','Ultraviolet','Unknown'),
    (6,'In which state is the famous battlefield of Plassey located?','Jharkhand', 'Bihar','West Bengal','Chhattisgarh','West Bengal'),
    (7,'To whom is the Sankatamochan temple in Varanasi dedicated?','Hanuman', 'Ganesha','Krishna','Rama','Hanuman'),
    (8,'Which title is usually held by the eldest son of the British monarch?','Duke of Edinburgh', 'Prince of Wales','Grand Prince','Duke of York','Prince of Wales'),
    (9,'Which Indian mammal is found in \'clouded\' and \'snow\' varieties?','Lion', 'Yak','Leopard','Deer','Leopard'),
    (10,'Who was the Indian Union Defence Minister during the Indo-Pak war of 1971?','Jagjivan Ram', 'Indira Gandhi','C Subramaniam','Y B Chavan','Jagjivan Ram'),
     
    
    
    ]
democursor.executemany(query,values)
democursor.execute('commit')
demodb.close()

