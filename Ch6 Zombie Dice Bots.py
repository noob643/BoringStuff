 # A bot that, after the first roll, randomly decides if it will continue or stop:
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if random.randint(0,1) == 0:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break
                

 # A bot that stops rolling after it has rolled two brains:
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if brains <= 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break
 

 # A bot that stops rolling after it has rolled two shotguns:
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            
            if diceRollResults['shotgun'] < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break
                
                
 # A bot that initially decides it’ll roll the dice one to four times, but will stop early if it rolls two shotguns:
        brains = 0
        z = 0
        t = random.randint(1,4)
        while diceRollResults is not None and z in range(0,t):
            brains += diceRollResults['brains']
            z += 1
            if diceRollResults['shotgun'] < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break
                
                
