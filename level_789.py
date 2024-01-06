import mysql.connector
demodb = mysql.connector.connect(host="localhost", user="root", passwd="udgam", database="kbc")
democursor=demodb.cursor( )
democursor.execute("CREATE TABLE if not exists level7 (sno int(3), question VARCHAR(1000),option1 VARCHAR(1000), option2 VARCHAR(1000), option3 VARCHAR(1000), option4 VARCHAR(1000), answer VARCHAR(1000),PRIMARY KEY(sno))")
query='INSERT IGNORE INTO level7 (sno,question,option1,option2,option3,option4,answer)VALUES(%s,%s,%s,%s,%s,%s,%s)'
values=[
    (1,'According to Norse Mythology, which one of the following is the parent of Your-moon-gaan-dar, the Midgard Serpent?','Hel', 'Loki','Fenrir','Sleipnir', 'Loki'),
    (2,'According to Hindu Mythology, who currently holds the title of \'Indra\'?','Manojav','Purandar','Sushaanti','Suchi','Purandar'),
    (3,'Which of the following is not one of the Twelve Olympians in Greek Mythology?','Hermes','Aphrodite','Persephone','Hephaestus','Persephone'),
    (4,'In Christian Mythology, which character cursed a fig tree?','Isaac','Abraham','Moses','Jesus','Jesus'),
    (5,'What does Idun, the Norse Goddess responsible for Immortality, give to the gods to stay young?','Water from the Fountain of Youth','Golden Apples of Youth','Blood of the goats sacrificed by humans in name of Bragi','Potion of Youth','Golden Apples of Youth'),
    (6,'Which of the following characters in Hindu mythology did not have exactly one hundred brothers?','Gandhari','Duhshala','Duryodhan','Vahvashin','Duhshala'),
    (7,'According to Abrahamic Mythology, who is Cain’s fraternal twin and later wife after he kills her first husband, Abel?','Azura','Awan','Luluwa','Leah','Luluwa'),
    (8,'In the Rig Veda, who steals the hidden, divine fire from Surya and brings it to Earth?','Matarisvan','Meghanada','Danu','Dasksha','Matarisvan'),
    (9,'In Irish folklore, what is the usual occupation of a leprechaun?','Carpenter','Shoemaker','Thief','Blacksmith','Shoemaker'),
    (10,'According to Christian Mythology, which of the following was created from the rib of Adam?','Eve','Lilith','Sarah','Rebecca','Eve'),
    ]
democursor.executemany(query,values)
democursor.execute('commit')

democursor.execute("CREATE TABLE if not exists level8 (sno int(3), question VARCHAR(1000),option1 VARCHAR(1000), option2 VARCHAR(1000), option3 VARCHAR(1000), option4 VARCHAR(1000), answer VARCHAR(1000),PRIMARY KEY(sno))")
query='INSERT IGNORE INTO level8 (sno,question,option1,option2,option3,option4,answer)VALUES(%s,%s,%s,%s,%s,%s,%s)'
values=[
    (1,'Between 1834-1836, two brothers scammed the Paris Stock Exchange with government-owned semaphore telegraphs. What were their names?','Pierre & Francois Blanc','Claude & Joseph Blanc','Claude & Pierre Blanc','Francois and Joseph Blanc','Francois and Joseph Blanc'),
    (2,'Troilokya, the serial-killer and con-woman operating in the 1880’s Colonial Bengal, killed five women form what walk of life?','Maids','Prostitutes','English Missionary teachers','Members of Bhartiya Muslim Mahila Anjuman','Prostitutes'),
    (3,'Which German King tricked his entire population into eating potatoes when they were clearly against it by pretend-treating his potato garden as an important, protected land?','Arnulf the Bad','Charles the Fat','Fredrick the Great','Stephen','Fredrick the Great'),
    (4,'Where was the world’s first fingerprinting bureau established?','Paris','Calcutta','London','California','Calcutta'),
    (5,'Which baby is officially considered to be India’s one billionth child?','Asha Acharya','Astha Arora','Akanksha Anand','Anoushka Ahuja','Astha Arora'),
    (6,'Who was the first to climb the highest peak on each of all the seven continents?','Daniel Johnson','Richard Bass','Phil Hartman','Reinhold Messner','Richard Bass'),
    (7,'Which actor captained England in his only appearance in a Test cricket?','William Holden','C Aubrey Smith','Alan Ladd','W C Fields','C Aubrey Smith'),
    (8,'Lyricist Sampooran Singh Karla is better known by what name?','Gulzar','Jagjit Singh','Pankaj Udhas','Bhupinder Singh','Gulzar'),
    (9,'Which was the first Indian film to get a ‘Restricted for Adults’ certification?','Satyam Shivam Sundaram','Mera Naam Joker','Hanste Aansoo','Gumnaam','Hanste Aansoo'),
    (10,'Where did the Great Fire of London of 1666 start?','Meux Brewery','Thomas Farriner\'s bakery','Purity Distilling Company','Brick House Bakery','Thomas Farriner\'s bakery'),
    ]
democursor.executemany(query,values)
democursor.execute('commit')

democursor.execute("CREATE TABLE if not exists Level9 (sno int(3), question VARCHAR(1000),option1 VARCHAR(1000), option2 VARCHAR(1000), option3 VARCHAR(1000), option4 VARCHAR(1000), answer VARCHAR(1000),PRIMARY KEY(sno))")
query='INSERT IGNORE INTO Level9 (sno,question,option1,option2,option3,option4,answer)VALUES(%s,%s,%s,%s,%s,%s,%s)'
values=[
    (1,'On what fictional island is the first Jurassic Park novel set?','Isla Sorna','Isla Nubular','Isla Moos','Isla Muerta','Isla Nubular'),
    (2,'In the novel Dracula by Bram Stoker, what is the name of the ship that brings Dracula to England?','The Pequod','The Gloria Scott','The Demeter','The Nautilus','The Demeter'),
    (3,'In One Thousand and One Nights, who is Scheherazade’s husband who does not kill her for 1001 nights so that he could listen to her stories?','Shah Zaman','Jafar','Duban','Shahryar','Shahryar'),
    (4,'In what year did Sikkim become a part of India?','Nineteen-sixty-three','Nineteen-sixty-five','Nineteen-seventy-three','Nineteen-seventy-five','Nineteen-seventy-five'),
    (5,'Which district of Assam became part of Pakistan after the 1947 plebiscite?','Tinsukia','Sylhet','Nalbari','Lohit','Sylhet'),
    (6,'Who was independent India’s first ambassador to the USSR?','Vijayalakshmi Pandit','Sarojini Naidu','S. Radhakrishnan','Acharya Kripalani','Vijayalakshmi Pandit'),
    (7,'Who is the primary antagonist of the third Panchatantra book, the Kakolukiyam (On War and Peace)?','The Crow King','The Lion King','The Owl King','The Brahmin','The Owl King'),
    (8,'In the comic book series, the Adventures of Tintin, Thomson and Thompson\'s only discernible difference is:','the style of their walking sticks','the shape of their moustaches','the size of their bowler hats','the shape of their eyebrows','the shape of their moustaches'),
    (9,'In Disney’s Donald Duck shared Universe, what is Gizmoduck’s catchphrase?','Bless me bagpipes','Oh, phooey!','Blathering blatherskite','Let’s get dangerous!','Blathering blatherskite'),  
    (10,'What moisturizer is derived from sheep\'s wool?','Malana Oil','Lanolin Oil','Idukki Oil','Cashmere Oil','Lanolin Oil'),
    ]
democursor.executemany(query,values)
democursor.execute('commit')
demodb.close()
