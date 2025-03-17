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

        king_alive = True
        finish_game = True

        
        while king_alive and finish_game:
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
            
            plague_death = Hammurabi.plagueDeaths(population)
            population = population - plague_death
            print(f"The plague ushered {plague_death} people to the after life, you have {population} citizens\n")


            """
                Last part of the code
            """
            year+=1

            if year == 4:
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
            return population/2
        else:
            return population
    
    def starvationDeaths(population, bushelsFedToPeople):
        if math.floor(bushelsFedToPeople/population) < 20:
            return 20 - bushelsFedToPeople/population
        else:
            return 0
        


        


if __name__ == "__main__":
    hammurabi = Hammurabi()
    hammurabi.main()
