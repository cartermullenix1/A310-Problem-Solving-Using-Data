The first thing I had to fix was the change us the order of my import of random from choice.
I spelled flip wrong in the intial commit but it was spelled correctly on my page so that it my bad.
I next had to move my defined varables into the for loop and create an initial condition of if scount == 0 to start the loop of checking if a_flip == previous.
Next I got rid of previous because I this variable was not contributing to my goal and just overcomplicated my code.
I next needed to put the assignment of a_flip to choice of 'H' or 'T' into the for loop so that it would be reassigned each time.
I created an elif statement to check if the previous flip was the same as the current flip, if it was to add one to the scount, and if not it resets the scount to 1 (because the current flip is the start of the new streak).
Next within that if elif statement I placed my the if num_s == 6 from my original code and replaced num_s with scount.
In that if statement I returned if the scount == 6 and if not I set the previous to a_flip. In my code I used an extra variable that overcomplicated it and didn't do what I was supposed to.
I added an else statement to the first if statement that if a_flip != previous it resets the scount to 1 and makes a_flip the new previous.
I also changed the return statement to return 0 instead of scount because I was returning the wrong thing.
I next added a n variable at the top and assigned it 75 and assigned trials to 100.
I then added a for loop to run the function 100 times and added sum + flip(n) to a variable called assigned sum = 0 before the loop.
I then added a print statement to divide the sum by the number of trials to get how many times the streak of 6 was flipped in a randomly generated list of heads and tails in a given number of flips, n and trials.

I believe that I had to change alot of things to get it to work but I think I had a little bit of an idea of what is going on.