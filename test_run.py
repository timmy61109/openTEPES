#%% libraries
import os
import time
import setuptools
import builtins
from   pyomo.environ import ConcreteModel
from openTEPES import InputData
from openTEPES import ModelFormulation
from openTEPES import ProblemSolving


StartTime = time.time()

builtins.CaseName = '9n'
builtins.SolvName = 'glpk'

# builtins.CaseName = '9n'                               # To select the case

#%% model declaration
builtins.mTEPES = ConcreteModel('Open Generation and Transmission Operation and Expansion Planning Model with RES and ESS (openTEPES) - Version 1.7.15 - September 4, 2020')

# import openTEPES_InputData
InputData(CaseName, mTEPES)

# import openTEPES_ModelFormulation
ModelFormulation(mTEPES)
mTEPES.write('openTEPES_'+CaseName+'.lp', io_options={'symbolic_solver_labels': True})  # create lp-format file

WritingLPFileTime = time.time() - StartTime
StartTime         = time.time()
print('Writing LP file                       ... ', round(WritingLPFileTime), 's')

# import openTEPES_ProblemSolving
ProblemSolving(mTEPES)

#     import openTEPES_OutputResults
#
#     TotalTime = time.time() - StartTime
#     print('Total time                            ... ', round(TotalTime), 's')