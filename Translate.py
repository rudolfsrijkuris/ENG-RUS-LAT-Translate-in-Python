"""
	||||||       |||||||    ||||||||||||	 |||        |||		||||||||||||	|||      ||	||||||
	||    ||     ||   ||	||        ||	 || ||     || ||	||        ||	|| ||    ||	||    || 
	||     ||    |||||||	||        ||	 ||  ||   ||  ||	||        ||	|| ||    ||	||     ||
	||      ||          	||        ||	 ||   || ||   ||	||        ||	||  ||   || 	||      ||
	||       ||  |||||||	||        ||	 ||    ||     ||	||        ||	||  ||   || 	||       ||
	||      ||   ||   ||	||||||||||||	 ||           ||	||        ||	||   ||  ||	||      ||
	||     ||    ||   ||	||        ||	 ||           ||	||        ||	||   ||  || 	||     ||
	||    ||     ||   ||	||        ||	 ||           ||        ||        ||	||    || ||	||    ||
	||||||       |||||||	||        ||	 ||           ||	||||||||||||	||    |||||	||||||

				||        	||||||||	||||||||||||	|||      ||
				||		||    ||	||        || 	|| ||    ||
				||		||||||||	||        || 	|| ||    ||
				||        	        	||        ||	||  ||   || 
				||        	||||||||	||        ||	||  ||   ||
				||        	||    ||	||        ||	||   ||  || 
				||        	||    ||	||        ||	||   ||  || 
				||              ||    || 	||        ||	||    || ||
				||||||||||	||||||||	||||||||||||	||    |||||
    	>>> Developed by: 𝕯𝖎𝖆𝖒𝖔𝖓𝖉𝕷𝖎𝖔𝖓#7777					
	>>> © 𝕯𝖎𝖆𝖒𝖔𝖓𝖉𝕷𝖎𝖔𝖓 2020
"""

def task2():
    EngToLat = {'Hello':'Sveiks', 'my':'mans', 'friend':'draugs', 'from':'no', 'this':'šīs', 'country':'valsts'}
    EngToRus = {'Hello':'Привет', 'my':'мой', 'friend':'друг', 'from':'из', 'this':'етот', 'country':'страни'}
    LatToEng = {'Sveiks':'Hello', 'mans':'my', 'draugs':'friend', 'no':'from', 'šīs':'this', 'valsts':'country'}
    LatToRus = {'Sveiks':'Привет', 'mans':'мой', 'draugs':'друг', 'no':'из', 'šīs':'етот', 'valsts':'страни'}
    RusToLat = {'Привет':'Sveiks', 'мой':'mans', 'друг':'draugs', 'из':'no', 'етот':'šīs', 'страни':'valsts'}
    RusToEng = {'Привет':'Hello', 'мой':'my', 'друг':'friend', 'из':'from', 'етот':'this', 'страни':'country'}

    print('If you dont want translate from specified language then just type (No)')
    langEngLat = input('\033[92mTranslate from English(EngToLat) to Latvian?: \n')
    langEngRus = input('\033[92mTranslate from English(EngToRus) to Russian?: \n')
    langLatEng = input('\033[92mTranslate from Latvian(LatToEng) to English?: \n')
    langLatRus = input('\033[92mTranslate from Latvian(LatToRus) to Russian?: \n')
    langRusLat = input('\033[92mTranslate from Russian(RusToLat) to Latvian?: \n')
    langRusEng = input('\033[92mTranslate from Russian(RusToEng) to English?: \n')


    if langEngLat=='EngToLat':
        messageEngLat = input('\033[94mEnter (Hello my friend from this country) to translate to latvian: \n')
    
    elif langEngRus=='EngToRus':
        messageEngRus = input('\033[94mEnter (Hello my friend from this country) to translate to russian: \n')

    elif langLatEng=='LatToEng':
        messageLatEng = input('\033[94mRaksti (Sveiks mans draugs no šīs valsts), lai tulkotu angliski: \n')

    elif langLatRus=='LatToRus':
        messageLatRus = input('\033[94mRaksti (Sveiks mans draugs no šīs valsts), lai tulkotu krieviski: \n')

    elif langRusLat=='RusToLat':
        messageRusLat = input('\033[94mПыши (Привет мой друг из етот страни) штобы перевести в латышский язык: \n')

    elif langRusEng=='RusToEng':
        messageRusEng = input('\033[94mПыши (Привет мой друг из етот страни) штобы перевести в англиский язык: \n')

    elif langEngLat=='No' or langEngRus=='No' or langLatEng=='No' or langLatRus=='No' or langRusLat=='No' or langRusEng=='No':
        print('\033[91mYou desellected this language\n')

    else:
        print('\033[91mIncorrect syntax\n')
        
    # English to latvian
    if langEngLat=='EngToLat':
        for word in messageEngLat.split('/'):
            for character in word.strip().split():
                decode_dict = {v: k for k, v in LatToEng.items()}
            for word in messageEngLat.split(' '):
                for character in word.strip().split():
                    print('\033[93mEnglish -> Latvian: \n', decode_dict[character])
                    print(' ')
                    ' '.join(''.join(decode_dict[character] for character in word.strip().split())
                    for word in messageEngLat.split('/'))
    
    # English to russian
    if langEngRus=='EngToRus':
        for word in messageEngRus.split('/'):
            for character in word.strip().split():
                decode_dict = {v: k for k, v in RusToEng.items()}
            for word in messageEngRus.split(' '):
                for character in word.strip().split():
                    print('\033[93mEnglish -> Russian: \n', decode_dict[character])
                    print(' ')
                    ' '.join(''.join(decode_dict[character] for character in word.strip().split())
                    for word in messageEngRus.split('/'))

    #  Latvian to english
    if langLatEng=='LatToEng':
        for word in messageLatEng.split('/'):
            for character in word.strip().split():
                decode_dict = {v: k for k, v in EngToLat.items()}
            for word in messageLatEng.split('/'):
                for character in word.strip().split():
                    print('\033[93mLatvian -> English: \n', decode_dict[character])
                    print(' ')
                    ' '.join(''.join(decode_dict[character] for character in word.strip().split())
                    for word in messageLatEng.split('/'))
        
    #  Latvian to russian
    if langLatRus=='LatToRus':
        for word in messageLatRus.split('/'):
            for character in word.strip().split():
                decode_dict = {v: k for k, v in RusToLat.items()}
            for word in messageLatRus.split('/'):
                for character in word.strip().split():
                    print('\033[93mLatvian -> Russian: \n', decode_dict[character])
                    print(' ')
                    ' '.join(''.join(decode_dict[character] for character in word.strip().split())
                    for word in messageLatRus.split('/'))

    #  Russian to latvian
    if langRusLat=='RusToLat':
        for word in messageRusLat.split('/'):
            for character in word.strip().split():
                decode_dict = {v: k for k, v in LatToRus.items()}
            for word in messageRusLat.split('/'):
                for character in word.strip().split():
                    print('\033[93mRussian -> Latvian: \n', decode_dict[character])
                    print(' ')
                    ' '.join(''.join(decode_dict[character] for character in word.strip().split())
                    for word in messageRusLat.split('/'))

    #  Russian to english
    if langRusEng=='RusToEng':
        for word in messageRusEng.split('/'):
            for character in word.strip().split():
                decode_dict = {v: k for k, v in EngToRus.items()}
            for word in messageRusEng.split('/'):
                for character in word.strip().split():
                    print('\033[93mRussian -> English: \n', decode_dict[character])
                    print(' ')
                    ' '.join(''.join(decode_dict[character] for character in word.strip().split())
                    for word in messageRusEng.split('/'))
task2()
