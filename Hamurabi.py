import random

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

            # land_business = input("How many acres of land do you want to buy/negative if you want to sell\n")
            land_bought = Hammurabi.askHowManyAcresToBuy(land_value,bushels)
            bushels = bushels - (land_bought*land_value)
            land = land_bought + land

            year+=1

            if year == 4:
                finish_game = False

                


    
    

    # other methods go here

    def askHowManyAcresToBuy(price, bushels):
        land_bought = input("How many acres of land do you want to buy?\n")
        while (int(land_bought)*price) > bushels:
            print("Jedi mind tricks don't work, I can see how much you have")
            land_bought = input("How many acres of land do you want to buy?\n")
        
        return int (land_bought)
    
    def askHowManyAcresToSell(acres_owned):
        land_sold = input("How many acres of land do you want to sell?\n")
        while int (land_sold) > acres_owned:
            print(f"Imaginary land doesn't count, you only have {acres_owned} acres")
            land_bought = input("How many acres of land do you want to buy?\n")
        
        return int (land_bought)
    


if __name__ == "__main__":
    hammurabi = Hammurabi()
    hammurabi.main()
