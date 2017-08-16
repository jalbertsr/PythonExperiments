#!/usr/bin/env python

class Graph:
    def __init__(self,adjacent=[]):
        """
        Creates a Graph.
            :param adjacent: a list of tuples where the first element is a string 
        with a node name and the second a list of strings with all its neighbors.
        """
        self.adj=dict(adjacent)


    def getNodes(self):
        """
        Provides a list of strings with all the graph nodes.
        :return : A python array with all list nodes in ascending order
        """
        nodes=self.adj.keys()
        nodes.sort()
        return nodes

    def createFromBoolMatrix(self,mat):
        """
        Finds the shortest path bvetween two nodes.
        :param p1Label: a string with the node name to start the path
        :param p2Label: a string with the node name of the end of the path
        """
        def pos2name(y,x):
            """
            Auxiliary functions that return a unique node name for every point in the map
            :return :string
            """
            return 'p_'+str(x)+'_'+str(y)

        offset=[[0,1],[1,0],[0,-1],[-1,0]] #posiciones posibles

        for x in range(len(mat)): 
            for y in range(len(mat[x])): #recorremos matriz
                if mat[x][y] is True:
                    lstaux = []
                    for i in offset: #recorremos las posiciones del offset
                        if (0 <= (x+i[0]) < len(mat)) and (0 <= (y+i[1]) < len(mat[x])):#comprobamos cada posicion del offset con sus limites
                            if mat[x+i[0]][y+i[1]] is True:
                                lstaux.append(pos2name(y+i[1], x+i[0])) #agregamos a la lista

                    self.adj[pos2name(y,x)]=lstaux #actualizamos la lista


    def loadFromBoolMatrix(self,fname):
        """
        Loads a boolean matrix from a text file and uses it to populate the graph
            :param fname: the path to an existing text file containing a boolean matrix.
        """
        mat=[[col=='T' for col in line.strip()] for line in open(fname).read().split('\n') if len(line.strip())]
        self.createFromBoolMatrix(mat)


    def getBFS(self,p1Label,p2Label):
        """
        Finds the shortest path between two nodes if it exists.
        :param p1Label: a string with the node name to start the path
            :param p2Label: a string with the node name of the end of the path
        :return : A tuple with the legth of shortest as an integer and the 
            shortest path as a python array of strings. If there exists 
            no path, (-1,[]) is returned.
        """
        
        if self.adj.has_key(p1Label) is False and self.adj.has_key(p2Label) is False: #comprobamos si existe camino.
        	return (-1,[])
        lst=[]
        lst.append([1,[p1Label]]) 
        
        while (lst[0][1][-1] != p2Label): #miramos que el ultimo elemento de la sublista creada no coincida con el ultimo elemento del camino
        	lst_aux= self.adj[lst[0][1][-1]] #cogemos la lista de adyacencias
        	for k in lst_aux: #recorremos la lista de adyacencias
        		if k != lst[0][1][-1]:
        			lst.append([lst[0][0]+1,lst[0][1]+[k]]) #sumamos el numero de adyacentes y agregamos a la lista sus adyacentes
        	pos = lst[0][1][-1]
        	lst.pop(pos) #sacamos el primer elemento de la lista
        return lst[0] #retornamos el primer elemento de la lista

    def __repr__(self):
        """
        :return : A string containing a python expression that can build the graph.
        """
        adjList=self.adj.items()
        for a in adjList:
            a[1].sort()
        adjList.sort()
        return 'Graph('+str(adjList)+')'

    def __eq__(self, other):
        """
        :return : True if two graphs are exactly the same.
        """
        return repr(self)==repr(other)


