
# WAP to take input string and perform below scenarios
Python Slicing Challenge: "kiran academy"
Objective: Master the art of string slicing using the variable name = "kiran academy". Complete the following 30 scenarios to test your understanding of indices and steps.

1. Positive Start + Positive Stop
Extract substrings using only forward-counting indices (0 to 9).

Example: name[0:5] → "hello"

name[0:6]

name[3:8]

name[5:10]

name[2:4]

name[0:9]

2. Positive Start + Negative Stop
Mix forward-counting starts with backward-counting stops.

Example: name[0:-5] → "hello"

name[0:-6]

name[1:-1]

name[5:-2]

name[2:-4]

name[4:-1]

3. Negative Start + Negative Stop
Navigate the string using only backward-counting indices (-10 to -1).

Example: name[-5:-1] → "worl"

name[-6:-1]

name[-10:-5]

name[-4:-2]

name[-8:-3]

name[-9:-1]

4. Negative Start + Positive Stop
- Start from the end and try to reach a forward index.

- Note: Watch out for empty results if your step direction doesn't match your index direction!

    - name[-2:1]
    - name[-5:10]
    - name[-10:5]
    - name[-8:6]
    - name[-1:5]

5. Varying Positive Step Sizes (Forward)
- Explore how increasing the step size "skips" characters.

    - name[::1] (Step of 1)
    - name[::2] (Step of 2 - Skip 1)
    - name[::3] (Step of 3 - Skip 2)
    - name[::4] (Step of 4 - Skip 3)
    - name[::5] (Step of 5 - Skip 4)

6. Varying Negative Step Sizes (Backward)
- Reverse and skip characters using negative increments.

    - name[::-1] (Standard reverse)
    - name[::-2] (Reverse skip 1)
    - name[::-3] (Reverse skip 2)
    - name[::-4] (Reverse skip 3)
    - name[::-5] (Reverse skip 4)
