'''
Given a number n. Print Butterfly Pattern with n lines. 

Examples:

Input: n = 4
Output:
*     * 
**   ** 
*** *** 
******* 
*** *** 
**   ** 
*     * 
Input: n = 5 
Output: 
*       * 
**     ** 
***   *** 
**** **** 
********* 
**** **** 
***   *** 
**     ** 
*       *
Constraints:
1 ≤ n ≤ 100
'''


# code here
n = int(input())

for i in range(1,n+1):
    if i == n:
        print("*"*(2*n-1))
    else:
        star = "*"*i
        space = " "*(2*(n-i)-1)
        row = star + space + star 
        print(row) 

for i in range(1,n):
    star = "*"*(n-i)
    space = " "*(2*i-1)
    row = star + space + star 
    print(row)
