# Unique Password Generator
### Generates unique password according to user character requirement and adheres to certain laws

#### Requirements
1. Password must be at least 4 characters long.
2. Password must have one capital letter (A - Z), one small letter (a - z), one number (0-9) and one special character ('!', '@', '#', '$', '%', '&', '?').

#### Process:
1. Create the character list in a two-dimensional list.
2. Create an empty array.
3. Generate four random characters that adheres to the limitations provided above.
4. Check how many characters are remaining - if none, move to shuffling.
5. If more characters remain, pick random characters from the entire list.
6. Shuffle the entire list 10 times so that it's even more random. The shuffling process includes generating two random index integers and swap those two index values. [Users can check how the pre-shuffled list looked like by including `print(genPass)` right before the shuffle loop.]
7. Join the list items so that it's a complete password string.
8. Return the string.
