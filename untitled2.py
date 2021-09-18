#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 12:50:38 2021

@author: sushantsamvarghese
"""



from pyomo.environ import *
model = ConcreteModel()
model.x_1 = Var(within=NonNegativeReals)
model.x_2 = Var(within=NonNegativeReals)
model.obj = Objective(expr=model.x_1 + 2*model.x_2)
model.con1 = Constraint(expr=3*model.x_1 + 4*model.x_2 >= 1)
model.con2 = Constraint(expr=2*model.x_1 + 5*model.x_2 >= 2)



#%%

from pyomo.environ import *
import mydata
model = ConcreteModel()
model.x = Var(mydata.N, within=NonNegativeReals)
def obj_rule(model):
    return sum(mydata.c[i]*model.x[i] for i in mydata.N)
model.obj = Objective(rule=obj_rule)
def con_rule(model, m):
    return sum(mydata.a[m,i]*model.x[i] for i in mydata.N) \
               >= mydata.b[m]
model.con = Constraint(mydata.M, rule=con_rule)


#%%


from pyomo.environ import *
model = AbstractModel()
model.N = Set()
model.M = Set()
model.c = Param(model.N)
model.a = Param(model.M, model.N)
model.b = Param(model.M)
model.x = Var(model.N, within=NonNegativeReals)
def obj_rule(model):
    return sum(model.c[i]*model.x[i] for i in model.N)
model.obj = Objective(rule=obj_rule)
def con_rule(model, m):
    return sum(model.a[m,i]*model.x[i] for i in model.N) \
               >= model.b[m]
model.con = Constraint(model.M, rule=con_rule)