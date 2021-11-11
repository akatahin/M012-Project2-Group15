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

def eGreedy(e: int):
    pass

# • You will visit one of the cafeterias each day for 300 days.
# • There are three cafeterias: C1, C2, and C3
# • The cafeterias have happiness values that are normally distributed
# with the following mean and standard deviation values:
# o C1: average happiness = 9, standard deviation = 3
# o C2: average happiness = 7, standard deviation = 5
# o C3: average happiness = 11, standard deviation = 7

# Returns the total happiness where the first three days
# each cafeteria is used.
import random
def eGreedy(e: int) -> int:
    totalHappy = 0
    percent = e / 100  # e as a percentage
    print(percent)
    day1Happiness = random.normalvariate(9, 3)  # first visit to caf 1
    day2Happiness = random.normalvariate(7, 5)  # first visit to caf 2
    day3Happiness = random.normalvariate(11, 7)  # first visit to caf 3

# hap(1-3) is the variable that tracks the total hap for respective caf
    hap1 = day1Happiness
    hap2 = day2Happiness
    hap3 = day3Happiness
    print(hap1, hap2, hap3)

# next three if/elif/else statments establish the best caf after first three days
    if day1Happiness > day2Happiness and day1Happiness > day3Happiness:
        bestCafeteria = "Cafeteria 1"
        best = day1Happiness
    elif day2Happiness > day1Happiness and day2Happiness > day3Happiness:
        bestCafeteria = "Cafeteria 2"
        best = day2Happiness
    else:
        bestCafeteria = "Cafeteria 3"
        best = day3Happiness
    print(bestCafeteria, totalHappy)
    totalHappy += best
    print(bestCafeteria, totalHappy)

    for i in range(297):
        r = random.random() # generates the random number between 0-1
        print(r)
        if r < percent:  # this if statement is for when you are picking a random caf
            caf = random.randint(1, 3)
            if caf == 1:
                c1Hap = random.normalvariate(9, 3)
                totalHappy = totalHappy + c1Hap
                hap1 = hap1 + c1Hap
            elif caf == 2:
                c2Hap = random.normalvariate(7, 5)
                totalHappy = totalHappy + c2Hap
                hap2 = hap2 + c2Hap
            elif caf == 3:
                c3Hap = random.normalvariate(11, 7)
                totalHappy = totalHappy + c3Hap
                hap3 = hap3 + c3Hap
        else:  # this else is running the best caf when r > percent (e%)
            if bestCaf == "c1":
                c1Hap = random.normalvariate(9, 3)
                totalHappy = totalHappy + c1Hap
                hap1 += c1Hap
            elif bestCaf == "c2":
                c2Hap = random.normalvariate(7, 5)
                totalHappy = totalHappy + c2Hap
                hap2 += c2Hap
            elif bestCaf == "c3":
                c3Hap = random.normalvariate(11, 7)
                totalHappy = totalHappy + c3Hap
                hap3 += c3Hap
        if hap1 > hap2 and hap1 > hap3:  # next three if statements resets what the best caf is after each run of the for loop
            bestCaf = "c1"
        elif hap2 > hap1 and hap2 > hap3:
            bestCaf = "c2"
        elif hap3 > hap2 and hap3 > hap1:
            bestCaf = "c3"
    return totalHappy


print(eGreedy(12))  # runs eGreedy with 12 percent greedy

