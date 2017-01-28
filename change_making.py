#!/usr/bin/env python

"""
@author: jalbert

The change-making problem addresses the following question:
how can a given amount of money be made with the least number of coins of given denominations? 
It is a knapsack type problem, and has applications wider than just currency.

We resolve this in three different ways, recursion, memoritzation and dynamic programming.
It also should be able to be resolved by intger programming, I'll work on it to bring it to you.
"""

class change_making:
    def __init__(self, coins=[]):
        """ Constructor
        :param coins: List of items. Each item is a money value avaliable to return.
        """
        self.coins = coins

    def solver(self, method, change):
        """ Input method to solve the change making problem
        :param method: Method used to compute the change making problem
        :param change: Total value to return
        :return: Numbe of coins used
        """
        print('Method: ' + method + ' for ' + str(change) + ' change')
        if method == 'recursive':
            sol = self.recursive(change)
        elif method == 'memorization':
            sol = self.memorization(change,[0]*(change+1))
        elif method == 'dynamic_programming':
            sol = self.dynamic_programming(change,[0]*(change+1))
        else:
            print('Unknown method')
        return sol

    def recursive(self,change):
        """ Return the minimum number of coins solving the change making problem
        :param change: Total value to return
        :return: Number of coins used.
        """
        result = change

        if change in self.coins: #check if the change is the same as one of our coins 
            return 1             #then we can return the singel coin
        elif change < 0:         #if the change is lower just return 0
            return 0
        else:
            for coin in self.coins:     
                if change >= coin:      
                    num_coins = self.recursive(change - coin) + 1   #recursive part
                if num_coins < result:      #number of coins is less than result  
                    result = num_coins      # entonces result es igual al numero de monedas

        return result                   

    def memorization(self, change, vChange):
        """ Memorization change making problem
        :param change: Total value to return
        :param vChange: Vector containing the value for each change
        :return: Number of coins used
        """
        """
        The memoritzation techinique works like recursion but instead of looking for the result in 
        the last call of the function, we keep all the results in a vector so when we need it we just have to go 
        and look the vector, making the recursion method more optimal.
        """
        result = change
        
        if vChange[change] == 0:

            if change in self.coins:        
                vChange[change] = 1         
                return 1                   
                
            elif vChange[change] > 0:       
                return vChange[change]      
    
            else:                           
                for coin in self.coins:     
                    if change >= coin:      
                        num_coins = self.memorization(change - coin, vChange) + 1 
                    if num_coins < result:  
                        result = num_coins  
                        vChange[change] = result    
        else:
            result = vChange[change]
        return result                   

    def dynamic_programming(self, change, minCoins):
        """ Solves the change making problem using dynamic programming
        :param change: Total value to return
        :param minCoins: Pre-computed change for each value. Initial value is a list of 0's
        :return: Number of coins used
        """

        for i in range(change + 1):  
            coinCount = i            
            for j in self.coins:     
                if j <= i:           
                    if coinCount >= minCoins[i - j] + 1:
                        coinCount = minCoins[i - j] + 1     # keep the varaible minCoin in the position  (i-j) +1 so we're taking the best result
            minCoins[i] = coinCount     # guardamos el valor de la variable coinCount dentro del vector minCoins que es el que guarda las monedas a devolver

        return minCoins[change]     #return the best value for the change inside minCoin vector which is going to be the best value at the same time.

if __name__ == '__main__':

    # Simple case
    vCoins1 = [1,3,10,15,25]
    vCoins2 = [1,13,14]
    change1 = 32
    change2 = 26

    # Create change making solver
    cm = change_making(vCoins1)
    cm2 = change_making(vCoins2)

    # Solve the problem using recursive solution
    print('=============================================================')
    sol = cm.solver('recursive',change1)
    print("Number of coins:" + str(sol) + " expected coins:4")
    
    print('=============================================================')
    sol = cm2.solver('recursive',change2)
    print("Number of coins:" + str(sol) + " expected coins:2")


    # Solve the problem using recursive solution
    print('=============================================================')
    sol = cm.solver('memorization',change1)
    print("Number of coins:" + str(sol) + " expected coins:4")
    
    print('=============================================================')
    sol = cm2.solver('memorization',change2)
    print("Number of coins:" + str(sol) + " expected coins:2")


    # Solve the problem using dynamic programming
    print('=============================================================')
    sol = cm.solver('dynamic_programming',change1)
    print("Number of coins:" + str(sol) + " expected coins:4")
    
    print('=============================================================')
    sol = cm2.solver('dynamic_programming',change2)
    print("Number of coins:" + str(sol) + " expected coins:2")
