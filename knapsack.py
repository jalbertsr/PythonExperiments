#!/usr/bin/env python

"""
If you dont put your personal data here, the submission will not be accepted
Group    : 511
Subgroup : 10
Name 1: Hanks Campana Cheel
NIU  1: 1368476
Name 2: Joan Albert Segura Rueda
NIU  2: 1395001
Remarks:
"""
class Knapsack:
    def __init__(self, max_weight=7, items=[]):
        """ Constructor
        :param max_weight: Max weight allowed in the knapsack
        :param items: List of items. Each item has a weight w, and a value v.
        """
        self.items = items
        self.max_weight = max_weight
        self.dp_dict = {}
        self.iterations = 0

    def solver(self, method='brute_force'):
        """ Input method to solve the knapsack problem
        :return: max_val and items
        """
        self.iterations = 0
        print('Method: ' + method)
        if method == 'brute_force':
            sol = self.brute_force()
        elif method == 'recursive':
            sol = self.recursive(len(self.items), self.max_weight)
            print('Iterations:' + str(self.iterations))
        elif method == 'dynamic_programming':
            sol = self.dynamic_programming(len(self.items), self.max_weight)
            print('Iterations:' + str(self.iterations))
        else:
            print('Unknown method')
        return sol

    def power_set(self):
        """ Creates all the possible combination of items
        :return: All the possible combination of items, including the empty case.
        """
        power_set = [[]]

        for i in range(1 << len(self.items)):
            s=[self.items[j] for j in range(len(self.items)) if (i & (1 << j))]#make a shift operation as a conditional
            power_set.append(s)
        power_set.remove([])
        return power_set

    def brute_force(self):
        """ Solves the knapsack problem using brute force
        :return: max_value and list of items
        """
        power_set = self.power_set()
        best_value = 0
        best_set = []
        best_weight = 0
        
        for item_set in power_set:
            set_weight = sum([x['w'] for x in item_set])#takes values form 'w', puts it in a list and sum it list by list
            set_value = sum([x['v'] for x in item_set])#same for 'v'
            if set_value > best_value and set_weight <= max_weight:
                best_value = set_value
                best_weight = set_weight
                best_set = item_set       
        
        return best_value, best_weight, best_set

    def recursive(self, n, max_weight):
        """ Recursive Knapsack
        :param n: Number of elements
        :param max_weight: Maximum weight allowed
        :return: max_valu
        """
        self.iterations += 1
        result = 0
        
        if n == 0 or max_weight == 0:
            return 0
        #If weight of the nth item is more than Knapsack of capacity
        #W, then this item cannot be included in the optimal solution
        if self.items[n-1]['w']> max_weight:
            result = self.recursive(n-1, max_weight)
        else:
            result = max((self.items[n-1]['v'] + self.recursive(n-1, max_weight-self.items[n-1]['w'])), self.recursive(n-1, max_weight))
        return result

    def dynamic_programming(self, n, max_weight):
        """ Solves the knapsack problem using dynamic programming
        :return: max_value
        """
        self.iterations += 1
        result = 0

        wt = [j['w'] for j in items] 
        val = [i['v'] for i in items]
        K = [[0 for x in range(max_weight+1)] for x in range(n+1)]         
        
        for i in range(n+1):
            for w in range(max_weight+1):
                if i==0 or w==0:
                    K[i][w] = 0
                elif wt[i-1] <= w:
                    K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
                else:
                    K[i][w] = K[i-1][w]
                    
        result = K[n][max_weight]
        
        return result       

if __name__ == '__main__':

    # Simple case
    items = [dict(id=0, w=4, v=12),
             dict(id=1, w=6, v=10),
             dict(id=2, w=5, v=8),
             dict(id=3, w=7, v=11),
             dict(id=4, w=3, v=14),
             dict(id=5, w=1, v=7),
             dict(id=6, w=6, v=9)]
    max_weight = 18

    # Create Knapsack solver
    knapsack = Knapsack(max_weight, items)

    # Solve the problem using brute force
    print('=============================================================')
    sol = knapsack.solver('brute_force')
    print("Max value:" + str(sol[0]) + " expected max_value:44")
    print("Total weight:" + str(sol[1]) + " expected weight:18")
    print("Selected items:")
    print(sol[2])

    # Solve the problem using recursive solution
    print('=============================================================')
    sol = knapsack.solver('recursive')
    print("Max value:" + str(sol) + " expected max_value:44")

    # Solve the problem using dynamic programming
    print('=============================================================')
    sol = knapsack.solver('dynamic_programming')
    print("Max value:" + str(sol) + " expected max_value:44")
