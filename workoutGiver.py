import random
import daytime

class Exercise:
    def __init__(self, lifts, cardio):
        self.lifts = lifts
        self.cardio = cardio
    
    def getLifts(self):
        return self.lifts
    
    def getCardio(self):
        return self.cardio
    
    def addLift(self, newLift):
        self.lifts.append(newLift)

    def setCardio(self, newCardio):
        self.cardio = newCardio

class Coach:
    def __init__(self, exercise):
        self.exercise = exercise
        self.difficulty = 2
    
    def giveWorkout(self):
        print("Hello")
        workout = {}
        if len(self.exercise.lifts) >= 4:
            for lift in self.exercise.lifts:
                workout[lift] = str(1*self.difficulty) + " Sets of " + str(2*self.difficulty) + " Reps of " + lift + "."
        else:
            for lift in self.exercise.lifts:
                workout = "Run " + str(0.2*self.difficulty) + " miles, climb " + str(5*self.difficulty) + " flights of stairs on the stair climber, and do " + str(2*self.difficulty) + " miles on the bike."
        print(workout)

def main():
    legDay = ["Barbell Squat", "Shoulder Shrugs", "Leg Curls", "Leg Pushdowns"]
    chestDay = ["Bench Press", "Dumbell Flys", "Dips", "Cable Crossover"]
    armDay = ["Barbell Curls", "EZ Barbell Curl", "Skull Crushers", "Close Grip Bench Press"]
    backDay = ["Deadlift", "Lat Pull Downs", "Overhead Press", "Pull Ups"]
    cardioDay = ["Run", "Stair Climber", "Bike"]
    liftCombinations = [legDay, chestDay, armDay, backDay, cardioDay]
    
    cardio = "Treadmill"
    exercise = Exercise(lifts, cardio)
    coach = Coach(exercise)
    coach.giveWorkout()

main()