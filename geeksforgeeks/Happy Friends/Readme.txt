You and your friends decide to dine at a restaurant. The menu offers N dishes with varying prices, and interestingly, each dish is disliked by exactly one of your friends.

Find the minimum amount you need to spend such that all of the friends have something to eat considering that a dish can be shared among multiple people, and any friend who dislikes a dish will not consume it.

In case, it is not possible return "-1", where the prices of the dishes are represented in array prices and the array dislike represents that the i-th dish is disliked by friend dislike[i].

Example 1:

Input:
N = 5
prices[] = {10, 8, 5, 12, 8}
dislike[] = {1, 1, 3, 2, 4}
Output: 13
Explanation: Choose dishes no. 3 and 5 by spending 5 and 8 coins respectively.

Example 2:

Input:
N = 2
prices[] = {10, 9}
dislike[] = {1, 1}
Output: -1
Explanation: You cannot choose any combination of dishes as friend 1 dislikes them all.

Your Task:

This is a function problem. The input is already taken care of by the driver code. You only need to complete the function MinCost() that takes a number of dishes (n), prices of each dish ( prices[] ) and the friend that dislikes each dish (dislike[]). Return the minimum amount you need to spend or return "-1" if it is not possible. The driver code takes care of the printing.

Constraints:

1 <= n <= 10^5

1 <= price[i] <= 10^5

1<= dislike[i] <= n


