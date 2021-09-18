#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 14:03:36 2021

@author: sushantsamvarghese
"""

#Import the LP solver from ORtools

from ortools.linear_solver import pywraplp

#Declare the solver:
solver = pywraplp.Solver_CreateSolver('GLOP')

#Create a variable x: lower bound, upper bound, assign to the string object x
x = solver.NumVar(0,10,'x')

y = solver.NumVar(0,10,'y')

#Add the equations to the solver object
solver.Add(-x+2*y<=8)
solver.Add(2*x+y<=14)
solver.Add(2*x-y<=10)

#Create the objective function:
solver.Maximize(x+y)

#Solve the problem and assign it to the results
results = solver.Solve()

#Check if the solution is optimal:
if results==pywraplp.Solver.OPTIMAL: print("Optimal Solution Found")

#Print the results:
print('x:',x.solution_value())
print('y:',y.solution_value())