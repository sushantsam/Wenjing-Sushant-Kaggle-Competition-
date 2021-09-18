#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 14:27:32 2021

@author: sushantsamvarghese
"""

import pyomo.environ as pe 
#import pyomo.opt as po

from pyomo.opt import SolverFactory

solver =SolverFactory('cplex')

model=pe.ConcreteModel()

model.x1 = pe.Var(domain=pe.Binary)

model.x2 = pe.Var(domain=pe.Binary)
model.x3 = pe.Var(domain=pe.Binary)
model.x4 = pe.Var(domain=pe.Binary)
model.x5 = pe.Var(domain=pe.Binary)

obj_expr = 3 * model.x1 

model.obj = pe.Objective(sense=pe.maximize, expr = obj_expr)

con_expr = 3 * model.x1 + 3 * model.x1 + 3 * model.x1 + 3 * model.x1 + 3 * model.x1 <= 20

model.con = pe.Constraint(expr=con_expr)

result=solver.solve(model)

