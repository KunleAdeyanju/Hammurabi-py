import os
import random
import math

class Hammurabi:
    def __init__(self):
        self.rand = random.Random()

    def main(self):
        self.playGame()

    def playGame(self):
        # declare local variables here: grain, population, etc.
        # statements go after the declarations
        population = 100    # number of people at the start
        bushels = 2800      # number of bushels of grain in storage
        land = 1000         # acres of land
        land_value = 19     # land value bushels/acre
        year = 1
        deaths = 0
        immigrants = 0
        harvet = 0
        harvet_per_acre = 0
        rats = 0
        bushels_rats_ate = 0

        king_dead = False   # if true end the game
        finish_game = True  # turns false when youu hit year 10

        
        while not king_dead and finish_game:
            print(f"""
            O great Hammurabi!
            You are in year {year} of your ten year rule.
            In the previous year {deaths} people starved to death.
            In the previous year {immigrants} poeple entered the kingdom.
            The poplulation is now {population}.
            We harvested {harvet} bushels at {harvet_per_acre} per acre.
            Rats destroyed {bushels_rats_ate}, leaving {bushels} bushels in storage.
            The city owns {land} acres of land.
            Land is currently worth {land_value} bushels per acre
            """)

            land_decision = True # trigger to move on from buy or sell condition
            buy_or_sell = input("Do you want to buy or sell land\n").lower()
            while land_decision:
                if buy_or_sell == 'buy':
                    land_bought = Hammurabi.askHowManyAcresToBuy(land_value,bushels)
                    bushels = bushels - (land_bought*land_value)
                    land = land_bought + land
                    land_decision = False
                elif buy_or_sell == 'sell':
                    land_sold = Hammurabi.askHowManyAcresToSell(land)
                    land = land - land_sold
                    bushels = bushels + (land_sold*land_value)
                    land_decision = False
                else:
                    buy_or_sell = input("You daft?? Do you want to buy or sell land choose one\n").lower()

            grain_to_feed = Hammurabi.askHowMuchGrainToFeedPeople(bushels)
            bushels = bushels - grain_to_feed

            acers_planted = Hammurabi.askHowManyAcresToPlant(land, population, bushels)
            harvest_collected = Hammurabi.harvest(acers_planted)
            bushels = bushels + harvest_collected

            starvation_deaths = Hammurabi.starvationDeaths(population,grain_to_feed)
            population = population - starvation_deaths
            print(f"{starvation_deaths} people have died due to starvation, {population} people remain")
            
            if starvation_deaths > 0:
                uprising_happening = Hammurabi.uprising(population, starvation_deaths)
                if uprising_happening:
                        print(f"You Starved too many people, they revolted")
                        king_dead = Hammurabi.game_over(year, population, land)
                        

            plague_death = Hammurabi.plagueDeaths(population)
            population = population - plague_death
            print(f"The plague ushered {plague_death} people to the after life, you have {population} citizens\n")
            
            
            
            input("Press enter to continue....")

            """
                Last part of the code
            """
            year+=1

            if year == 11:
                print("You served your full term as king impressive, here are your ending stats\n")
                print(f"""
                O great Hammurabi!
                You are in year {year} of your ten year rule.
                In the previous year {deaths} people starved to death.
                In the previous year {immigrants} poeple entered the kingdom.
                The poplulation is now {population}.
                We harvested {harvet} bushels at {harvet_per_acre} per acre.
                Rats destroyed {bushels_rats_ate}, leaving {bushels} bushels in storage.
                The city owns {land} acres of land.
                Land is currently worth {land_value} bushels per acre
                """)
                finish_game = False
    

                


    
    

    # other methods go here

    def askHowManyAcresToBuy(price, bushels):
        land_bought = input("How many acres of land do you want to buy?\n")
        while (int(land_bought)*price) > bushels:
            print(f"Jedi mind tricks don't work, I can see how much you have the most you can buy is {math.floor(bushels/price)} acres")
            land_bought = input("How many acres of land do you want to buy?\n")
        return int (land_bought)
    
    def askHowManyAcresToSell(acres_owned):
        land_sold = input("How many acres of land do you want to sell?\n")
        while int (land_sold) > acres_owned:
            print(f"Imaginary land doesn't count, you only have {acres_owned} acres")
            land_sold = input("How many acres of land do you want to sell?\n")
        return int (land_sold)
    
    def askHowMuchGrainToFeedPeople(bushels):
        how_much_feed = input("How many bushels do you wish to feed your people?\n")
        while int(how_much_feed) > bushels:
            print(f"Why oh why must you test me? You have {bushels} bushels")
            how_much_feed = input("How many bushels do you wish to feed your people?\n")
        return int(how_much_feed)
    
    def askHowManyAcresToPlant(acers_owned, population, bushels):
        how_much_to_plant = input("How many acres do you want to plant grain?\n")
        while (int (how_much_to_plant) > acers_owned or 
        math.floor(int (how_much_to_plant)/population) > 20 or
        math.floor(int (how_much_to_plant)/bushels) > 2
        ):
            if int (how_much_to_plant) > acers_owned:
                print(f"Aim for the bushes doesn't me the starts, you only have {acers_owned} acers")
            elif math.floor(int (how_much_to_plant)/population) > 20:
                print(f"Look again, you don't have the manpower, only {population} citizens remain, you can plant upto {population*20} acers")
            elif math.floor(int (how_much_to_plant)/bushels) > 2:
                print(f"Check your coffers lad, you can plan {bushels*2} acers")
            how_much_to_plant = input("How many acres do you want to plant grain?\n")
        return int (how_much_to_plant)

    def plagueDeaths(population):
        if random.randint(0,99) < 15:
            return math.floor(population/2)
        else:
            return int (population)
    
    def starvationDeaths(population, bushelsFedToPeople):
        if math.floor(bushelsFedToPeople/population) < 20:
            return int (20 - bushelsFedToPeople/population)
        else:
            return int (0)
    
    def uprising(population, howManyPeopleStarved):
        return int ((howManyPeopleStarved/population)*100 > 45)
    
    def game_over(year, population, land):
        print(f"""
            O great Hammurabi!
            Your reign ended early in year {year} of your ten year rule.
            Your poplulation ended at {population} citizens.
            Your city owned {land} acres of land.
            """)
    
    def harvest(acres):
        bushels_per_acre = random.randint(1,6)
        print(f"Your harvet yeilded {bushels_per_acre} bushels per acre for a total of {bushels_per_acre * acres} acres")
        return int (bushels_per_acre * acres)
        


        


if __name__ == "__main__":
    hammurabi = Hammurabi()
    hammurabi.main()
