# Dice-roll-sim


**description:** Just a very basic dice rolling simulator. once the code is run it prints out 1 side of six-sided dice. The design of the dice when might be a bit off when it's printing 3 or 5 but it's the best I could come up with for now.


**dice_roller() -** This function uses the randint() function from the random module to generate a random integer between 1 and 6. Then returns the generated integer.


**dice_designer(number) -** This function takes an integer parameter 'number' and uses it to generate a pattern of red dots (🔴). It starts by setting a variable n equal to the input parameter, and then repeatedly yields a string containing two dice emojis_(to simulate a row in a dice)_ while n is greater than or equal to 2. and the final yield statement is there to catch any remainder in the case of n being an odd number
