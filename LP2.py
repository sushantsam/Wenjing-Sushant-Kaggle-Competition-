#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 14:16:06 2021

@author: sushantsamvarghese
"""
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


#pyomo solve abstract1.py abstract1.dat --solver=glpk