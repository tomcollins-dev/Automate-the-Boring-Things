def date_detect(date):
    import re
    #Define acceptable date bounds
    vdates = {
        '01':31,'02':28,'03':31,'04':30,'05':31,'06':30,'07':31,'08':31,'09':30,'10':31,'11':30,'12':31
        }
    vdates_l = {
        '01':31,'02':29,'03':31,'04':30,'05':31,'06':30,'07':31,'08':31,'09':30,'10':31,'11':30,'12':31
        }

    #Define regex and search provided date for valid format
    date_regex = re.compile(r'(\d\d)/(\d\d)/(\d\d\d\d)')
    date_check = date_regex.search(date)

    if date_check is None:
        return False
    else:
        #Assign groups to variables representing dateparts
        dd,mm,yyyy = date_check.group(1),date_check.group(2),date_check.group(3)

        #Not a leap year
        if int(yyyy) % 4 != 0 or (int(yyyy) % 4 == 0 and int(yyyy) % 100 == 0 and int(yyyy) % 400 != 0):
            #Valid month
            if mm in vdates: 
                return int(dd) in range(vdates[mm])
            else:
                return False
        else:
            #Valid month
            if mm in vdates_l: 
                return int(dd) in range(vdates_l[mm]) 
            else:
                return False
