
# **EASY** 4 Line Java/Python3 Solution | 1ms Runtime & 39.79 mb Memory


Aug 12, 2023 - Java - Python3

# Intuition

First thought is to do an easy divide of two numbers, this works  **99%**  of the time except with one case  (−2147483648/−1), for this case we will have to  **cheese🧀**  it a bit with a if statement (it's not  cheating, its a  **feature**  ;) ).

# Approach

To make this simple we will approch this in steps:
1.  Create a variable that holds the  **answer**.
2.  Let the answer = the quotient of  **dividend**  and  **divisor**.
3.  Create a if statement to check for the case of  **(-2147483648/-1)**  to equal the expect answer of  2147483647.
4.  Return  **answer**  variable.

**Note**: make sure youre variables are coming out as integers, this problem request that you round the number / no trailing decimals.

# Complexity

-   **Java**  Time complexity: 1ms
-   **Java**  Space complexity: 39.79 mb

----------

-   **Python3**  Time complexity: 46ms
-   **Python3**  Space complexity: 16.26 mb

----------

# Java Code

```cpp
class Solution {
    public int divide(int dividend, int divisor) {
        int answer;
        answer = dividend / divisor;
        if(dividend == -2147483648 && divisor == -1){ return 2147483647;}
        return answer;
    }
}
```

# Python3 Code

```java
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        answer = 0
        answer = int(dividend / divisor)
        if dividend == -2147483648 and divisor == -1: return 2147483647
        return answer
```