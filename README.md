# Contest_Sol
ICPC(The International Collegiate Programming Contest) Regionals and Finals

            20th South African Regional International Collegiate Programming Contest
                          20 October 2018
                  Problem D — Red Balloon Power2 Game
                          Problem Description
## Description.
Alice and Bob have developed a simple game to both pass the time and practice their arithmetic skills.
The game works as follows: 
• Alice and Bob decide upon a number. 
• Alice always takes the ﬁrst turn, after which they alternate. 
• The player whose turn it is performs one of two actions, depending on the current value of number at that time.
            - If the number is a power of two, the number is divided by two.
            – If the number is not a power of two, the largest power of two less than the number is subtracted from the number. 
• This process repeats until there is a winner. 
• The winner of the game is whoever reduces the number to 1. Your task is to determine, for a given number, who the winner of the game is.

### * Input
Input consists of an arbitrary number of test cases, but no more than 10 000. Each test case consists of a single number N, where ```1 < N < 263```, the start number as selected by Alice and Bob. Use “long long” in C/C++ and “long” in Java.

#### Input is terminated by -1 on it’s own line.

### * Output
For each test case, output the name of the winner, either “Alice” or “Bob”.

--------------------
```
Sample input
10 
4251 
4 
12413211 
-1
````
---------------------
```
Sample output
Bob
Alice
Bob 
Alice
```
---------------------

Time limit
1 second
