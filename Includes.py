'''
MIT License

Copyright (c) 2016 Steven J. Henderson 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

'''

THIS FILE CONTAINS GLOBAL PRIMITIVES USED THROUGHOUT ALL CLASSES

'''

'''
LIFE CYCLE PHASES -- These are the main phases of the Life Cycle Cost Model
                     that are modeled.  Each phases has its own set of regression models
                     for every WBS element.
'''
LCC_PHASE = ['RESEARCH & DEVELOPMENT','PROCUREMENT','OPERATIONS & MAINTENANCE']


'''
MODEL ATTRIBUTES -- These are the main attributes of the regression model.
They represent the independent variables or factors in the WBS regression models.
They are case sensitive, and MUST match the column names in any of the data files
'''
MODEL_ATTRIBUTES = ['WEIGHT','WHEELBASE','ENGINE_POWER','WPN_CALIBER','CREW_CAPCITY','TRACK_TIRE']

'''
WORK BREAKDOWN STRUCTURE (WBS) ELEMENTS.  These are the individual parts of a WBS structure
An LCC model will include a regresison model for each of these lines
'''
WBS_ELEMENTS = ['WBS_VEHILCE_ASSEMBLED','WBS_HULL_FRAME','WBS_TURRET_ASSEMBLY','WBS_SUSPENSION',
               'WBS_VEHICLE','WBS_POWER_PACKAGE_TRAIN','WBS_AUXILIARY_AUTOMOTIVE','WBS_FIRE_CONTROL',
               'WBS_ARMAMENT','WBS_AUTOMATIC_AMMO_HANDLING','WBS_NAVIGATION','WBS_SPECIAL_EQUIP',
               'WBS_COMMUNICATIONS','WBS_SYSTEM_TEST_EVAL','WBS_TRAINING','WBS_DATA',
               'WBS_COMMON_SUPPORT_EQUIP','WBS_OPERATIONAL_SITE_ACTIVATION','WBS_INDUSTRIAL_FACILIITIES']




