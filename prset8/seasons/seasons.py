from datetime import date
import sys, inflect,re

def main():
    print(getMinutes(input("Enter your date of birth : ").strip()))

def getMinutes(dt):

    d = checkDob(dt).split('-')

    engine = inflect.engine()

    today = date.today()
    dob = date(int(d[0]),int(d[1]),int(d[2]))
    minutes = ((today - dob).days)*24*60

    words = engine.number_to_words(minutes).replace(' and', '').strip().capitalize()
    return(words + ' minutes')


def checkDob(dob):

    if re.match('[0-9]{4}-[0-9]{2}-[0-9]{2}',dob) and int(dob.split('-')[1]) < 12 and int(dob.split('-')[1]) < 31:
        return dob
    else:
        sys.exit('Invalid Date use YYYY-MM-DD')



if __name__ == "__main__":
    main()
