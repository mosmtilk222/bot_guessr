# bot_guessr

![image](https://user-images.githubusercontent.com/53209906/167951345-26b8c6b9-2f38-4280-84f4-a2e1a273444a.png)

Script to guess as much citys as possible in https://iafisher.com/projects/cities/

This project uses cartesian product to find all the possible combinations of characters with given length, for example

Length of 3 

aaa, aab, aac ... aba ... baa ... zzz

The possibilitys in the cartesian product with 26 characters are

![image](https://user-images.githubusercontent.com/53209906/167965662-596bf6a3-d578-4e95-b637-2cffaa9bc2d3.png)

In my algorithm I just do the cartesian product of 3, 4, 5, 6, 7 so the possibilitys are

![image](https://user-images.githubusercontent.com/53209906/167966077-465f7d3d-c42c-44e7-b508-6046221027c3.png)

Then realized a lot of combinations had just consonants, then I added this:

![image](https://user-images.githubusercontent.com/53209906/167966366-1c80d07b-1097-4482-b102-5b6ebd1af58c.png)

To "ignore" words without vowels and save a lot of iterations, this code snippet gets worse when the length of the word is larger, but at the beginning when the length is 3 for example, it almost halve the possibilitys

---

## Important 
Due the complexity of the algorithm and how fast it scales in terms of memory and iterations it could cause performance issues

---

Then I use **selenium** to enter the page and submit the answers

# Results

I tested it once and performed better than I thought, **in a few hours guessed almost 2000 citys** all over the world

