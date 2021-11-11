import random

def explore():
    count = 0
    for i in range(100): #100 trials
        C1 = 9 #cafeteria 1 AVG Hapiness
        SD = 3 #cafeteria 1 St. Dev
        r1 = (random.normalvariate(C1, SD)) #random number generator based on AVG and st.Dev
        count = count + r1 #adding each random number to the total
    print("Cafeteria 1 Hapiness: ")
    print(count)

    count2 = 0
    for i in range(100):
        C2 = 7 #cafeteria 2 AVG Hapiness
        SD2 = 5 #cafeteria 2 St. Dev
        r2 = (random.normalvariate(C2, SD2)) #random number generator based on AVG and st.Dev
        count2 = count + r2
    print("Cafeteria 2 Hapiness: ")
    print(count2)

    count3 = 0

    for i in range(100):
        C3 = 11 #cafeteria 3 AVG Hapiness
        SD3 = 7 #cafeteria 3 St. Dev
        r3 = (random.normalvariate(C3, SD3)) #random number generator based on AVG and st.Dev
        count3 = count + r3
    print("Cafeteria 3 Hapiness: ")
    print(count3)

    sum = count + count2 + count3 #adding all of the total hapiness from 3 cafertias
    print("Sum: ")
    print(sum)
    return sum #returns total hapiness




explore()


def exploit():
    print("----------------------------")
    total = 0

    C1 = 9
    SD = 3
    r1 = (random.normalvariate(C1, SD))
    total = total + r1
    print(r1)

    C2 = 7
    SD2 = 5
    r2 = (random.normalvariate(C2, SD2))
    total = total + r2
    print(r2)

    C3 = 11
    SD3 = 7
    r3 = (random.normalvariate(C3, SD3))
    total = total + r3
                                                  
    r = max(r1, r2, r3)
    print(r3)
    print(r)

    if(r == r1):
        A = 9
        SD = 3

    if(r == r2):
        A = 7
        SD = 5
    if(r == r3):
        A = 11
        SD = 7
    
    for i in range(297):
        p = (random.normalvariate(A, SD))
        total = total + p
    print("Sum: ")
    print(total)



exploit()


def eGreedy(e: int) -> int:
    percent = e / 1  # e as a percentage
    day1Happiness = random.normalvariate(9, 3)  # first visit to cafeteria 1
    day2Happiness = random.normalvariate(7, 5)  # first visit to cafeteria 2
    day3Happiness = random.normalvariate(11, 7)  # first visit to cafeteria 3

    # happy(1-3) is the variable that tracks the total happiness for respective cafeteria
    happy1 = day1Happiness
    happy2 = day2Happiness
    happy3 = day3Happiness

    print("Starting Happiness Rating of Cafe (1-3):\t", happy1, happy2, happy3)
    day1, day2, day3 = 1, 1, 1

    # ignore h, v - just to check
    h = 0
    v = 0

    # for loop that checks rating for rest of the 297 days
    for i in range(297):
        # generates the random float between 0-1
        randomValue = random.random() * 100

        # this conditional statement checks if random percentage is -
        # less then e percentage and chooses a random cafeteria
        if randomValue < percent:
            # choses a random cafeteria (1-3)
            cafeteria = random.randint(1, 3)
            v += 1

        # this conditional statement checks for the best rated cafeteria and assigns cafeteria to the number
        else:

            if day1Happiness > day2Happiness and day1Happiness > day3Happiness:
                cafeteria = 1

            elif day2Happiness > day1Happiness and day2Happiness > day3Happiness:
                cafeteria = 2

            else:
                cafeteria = 3

            h += 1

        # This conditional statement checks cafeteria number and adds a day and rating
        if cafeteria == 1:
            happy1 += random.normalvariate(9, 3)
            day1 += 1

        elif cafeteria == 2:
            happy2 += random.normalvariate(7, 5)
            day2 += 1

        else:
            happy3 += random.normalvariate(11, 7)
            day3 += 1

        # averages rating for each cafe formula = (happiness/days)
        day1Happiness = happy1 / day1
        day2Happiness = happy2 / day2
        day3Happiness = happy3 / day3

    print("Picked cafe:", h, "  ||  ", "Random cafe:", v)
    print("Average Happiness Rating of Cafe (1-3): \t", day1Happiness, day2Happiness, day3Happiness)

    totalHappy = happy1 + happy2 + happy3
    print("\n\nTotal Happiness of 300 days:", totalHappy)

    return totalHappy


eGreedy(12)
