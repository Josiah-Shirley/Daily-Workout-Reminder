import random
from datetime import date


class Coach:
    def __init__(self, exercise):
        self.exercise = exercise
        self.difficulty = 2

    def giveWorkout(self):
        workout = ""
        if len(self.exercise) == 4:
            for lift in self.exercise:
                workout += str(1 * self.difficulty) + " Sets of " + str(
                    2 * self.difficulty) + " Reps of " + lift + ". " + "\n"
        else:
            workout = "Run " + str(0.2 * self.difficulty) + " miles." + "\n" + "Climb " + str(
                5 * self.difficulty) + " flights of stairs on the stair climber." + "\n" + "Do " + str(
                2 * self.difficulty) + " miles on the bike." + "\n"
        return workout


def main():
    legDay = ["Barbell Squat", "Shoulder Shrugs", "Leg Curls", "Leg Push-downs"]
    chestDay = ["Bench Press", "Dumbbell Fly's", "Dips", "Cable Crossover"]
    armDay = ["Barbell Curls", "EZ Barbell Curl", "Skull Crushers", "Close Grip Bench Press"]
    backDay = ["Dead-lift", "Lat Pull Downs", "Overhead Press", "Pull Ups"]
    cardioDay = ["Run", "Stair Climber", "Bike"]
    liftCombinations = [legDay, chestDay, armDay, backDay, cardioDay]
    today = date.today()
    dayOfWeek = today.weekday()
    # The following block within the if statement should only be executed on Monday mornings
    # which is a '0' in date.today()
    if dayOfWeek == 2:
        random.shuffle(liftCombinations)
        scheduleFile = open("ww.txt", "w")
        for lift in liftCombinations:
            coach = Coach(lift)
            workout = coach.giveWorkout()
            scheduleFile.write(str(workout) + " <><><> " + "\n")
        scheduleFile.close()
    # The following block within the if statement should only be executed on weekdays
    # which is '0' through '4' in date.today()
    isWeekday = False
    if dayOfWeek < 5:
        isWeekday = True
    if isWeekday:
        scheduleFile = open("ww.txt", "r")
        schedule = scheduleFile.read()
        scheduleList = schedule.split("<><><>")
        todaysWorkout = scheduleList[dayOfWeek]
        print(todaysWorkout)
        scheduleFile.close()
        # TODO: Send today's workout as an email to myself


main()
