# Unique Password Generator
### Generates unique password according to user character requirement and adheres to certain laws

#### Update 1: Removed list of characters and instead ASCII table for efficiency and readability.

#### Requirements
1. Password must be at least 4 characters long.
2. Password must have one capital letter (A - Z), one small letter (a - z), one number (0-9) and one special character.

#### Process:
1. Create an empty array.
2. Generate four random characters using ASCII character table that adheres to the limitations provided above.
3. Check how many characters are remaining - if none, move to shuffling.
4. If more characters remain, pick random characters from the entire list.
5. Shuffle the entire list 10 times so that it's even more random. The shuffling process includes generating two random index integers and swap those two index values. [Users can check how the pre-shuffled list looked like by including `print(genPass)` right before the shuffle loop.]
6. Join the list items so that it's a complete password string.
7. Return the string.
