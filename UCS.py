from tkinter.constants import E, NONE
from typing import Match
import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import heapq
from pandas.core import indexing
from pandas.core.indexes.base import Index
import queue as Q
import collections

class CityNotFoundError(Exception):
    def __init__(self, targetcity):
        print("%s does not exist" % targetcity)


class FileNotFoundError(Exception):
    def __init__(self, filename):
        print("%s does not exist file" % filename)

def  uniform_cost_search(goal, start):
     
    
    global graph,cost,city1,cities
    answer = 10**8
 
    queue = []
 
    

    queue.append([0, start])
    visited = {}
 
    while (len(queue) > 0):

        queue = sorted(queue)

        p = queue[-1]
     

        del queue[-1]
 
        p[0] *= -1
    

     
        if (p[1] in goal):
 
            if (answer > p[0]):
                answer = p[0]
 
 
            queue = sorted(queue)
           
 
  

        if (p[1] not in visited):
            for i in range(len(graph[p[1]])):
                    queue.append( [(p[0] + cost[(p[1], graph[p[1]][i])])* -1, graph[p[1]][i]])

               

        # mark as visited
        visited[p[1]] = 1
    return answer

   
# main function
if __name__ == '__main__':
    while True:
        print("1) Choose csv File")
        print("2) Exit")
        choosenint = input()
        if(choosenint=="2"):
            exit()
        elif(choosenint=="1"):    
            win=Tk()
            win.attributes('-topmost',True)
            win.withdraw()
            filename = askopenfilename(filetypes=[("CSV files", ".csv")])
            print("%s Choosen File Path :"%filename)       
            citydata="" 
            if(filename!=""):
                citydata = pd.read_csv(filename,skiprows=1,header=None)
            
                city1,city2,cost1,cities,cost =[],[],[],[],{}

                for i in range(len(citydata)):
                        city1.append(citydata[0][i])
                        city2.append(citydata[1][i])
                        cost1.append(citydata[2][i])
                city1x=list(dict.fromkeys(city1))
                city2x=list(dict.fromkeys(city2))
                for i in city1x:
                        cities.append(i)
                for i in city2x:
                        cities.append(i)

                cities=list(dict.fromkeys(cities))
                graph=[[] for i in range(len(cities))]
                for i in range(len(city1)):
                        edge=cities.index(city1[i])
                        edge1=cities.index(city2[i])
                        graph[edge].append(edge1)
                        graph[edge1].append(edge)
                        cost[(edge, edge1)] = int(cost1[i])
                        cost[(edge1, edge)] = int(cost1[i])
                goal = []
                currentcity=input("Current City: ")
                targetcity=input("Target City: ")
                try:
                    goal.append(cities.index(targetcity))
                except Exception:
                    CityNotFoundError(targetcity)
                
                try:
                    cost = collections.OrderedDict(sorted(cost.items()))
                    cost=dict(cost)
                    answer = uniform_cost_search(goal,cities.index(currentcity))
                    if(answer!=10**8):
                        print("Minimum cost from", currentcity ,"to", targetcity, "is =" ,answer)
                except Exception:
                    CityNotFoundError(currentcity)
            else:
                FileNotFoundError(filename)


