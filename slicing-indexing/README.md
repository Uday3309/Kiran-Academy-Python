| **Positive Index** | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Character | k | i | r | a | n | | a | c | a | d | e | m | y |
| **Negative Index** | -13 | -12 | -11 | -10 | -9 | -8 | -7 | -6 | -5 | -4 | -3 | -2 | -1 |


## Slicing Scenarios
1. Positive Step Size (Forward)
Explores how increasing the step size "skips" characters while moving from left to right.

- Key Logic: name[start:stop:positive_step]

- Examples: name[0::1], name[1::2], name[2::3]

2. Negative Step Size (Backward)
Navigate the string in reverse. Note how the start must be "after" the stop for results to appear.

- Key Logic: name[start:stop:negative_step]

- Examples: name[-4:-12:-1], name[-1:-8:-2]

3. Start Negative, End Positive
Using a negative index to define the starting point but moving forward toward a positive index.

- Example: name[-12:-8:1] (Results in "iran")

4. Start Positive, End Negative
Starting from a forward-counting index and moving backward to a negative-counting index.

- Example: name[10:6:-1] (Results in "edac")

5. Start Negative, End Negative
Moving strictly within the "backward-counting" zone of the string.

- Example: name[-9::-1] (Reverses "kiran")

6. Start Positive, End Positive
Traditional slicing using standard index positions.

- Example: name[6:13:3] (Grabs every 3rd character starting from 'a')