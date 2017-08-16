#!/usr/bin/env python

from StackList import StackList
from argparse import ArgumentParser
from maze import *


class AgentNavigator(Navigator):
    def __init__(self, maze):
        """ Constructor, calls Navigator constructor
        """
        Navigator.__init__(self, maze)
        self.stack = StackList()
        self.radar = None  # Stores current step rada
        self.dead_end = False  # True if the agent founded a dead end
        self.previous_movement = 'W'  # Previous movement of the agent
        self.inverse = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}  # Inverse movements

    def isCrossRoad(self):
        """ Checks if the agent is in a cross road
        :return: True if the agent is in a cross road
        """
        valors = self.radar.values() #coge los valores de radar
        if valors.count(True) >= 3: #si tiene mas de 2 opciones(3 o 4) igual a true es que esta en un encrucijada 
            return True
        else:
            return False

    def isDeadEnd(self):
        #mov = self.inverse[self.previous_movement] #guarda en 'mov' el ultimo movimiento invertido
        llista = self.radar.values()	#hace na lista con los valores actuales de radar
        if llista.count(True) == 1: #and self.radar[mov]: #si solo hay un movimiento posible y este movimeinto es el inverso al anteriormente hecho es que estas en un camino sin salida
            return True
        else:
            self.dead_end = False
            return False
            
    def nextAction(self):
        """ Choose the next agent's action
        :return: Action tuple
        """
        # Reloads radar information
        self.radar = self.maze.getAllowedMovements()
        # Checks if the agent is in a dead end
        if self.isDeadEnd():
            self.dead_end = True

        if self.isCrossRoad():
           if self.stack.length == 0:
               for i in self.radar:
                   if self.radar[i] == True and i != self.inverse[self.previous_movement]:
                       self.stack.push(i)
           self.previous_movement = self.stack.pop()
           print "stack eliminat", self.stack
           return ('move', self.previous_movement)
            
        else:
            if self.isDeadEnd():
                self.previous_movement = self.inverse[self.previous_movement]
                return ('move', self.previous_movement)
                
            posmovs = [k for k, v in self.radar.iteritems() if v == True]
            posmovs.remove(self.inverse[self.previous_movement])
            for j in posmovs:
                    self.previous_movement = j
            return ('move', self.previous_movement)
            
   
if __name__ == '__main__':
    parser = ArgumentParser(description='Maze solver')
    parser.add_argument('--interface', metavar='interface', default='gui', help='[gui|cmd]')
    args = parser.parse_args()

    # Creates the maze
    maze = Maze(simpleMazeStr)

    # Creates the agent that will solve the Maze
    if args.interface == 'gui':
        TkDrawer(maze).interactive(AgentNavigator(maze))
    elif args.interface == 'cmd':
        SimpleDrawer(maze).interactive(AgentNavigator(maze))
    else:
        print "Error unknown interface"

