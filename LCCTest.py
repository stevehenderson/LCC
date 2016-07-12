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
import LCCModel 
import WBSRegressionModel
import log
import logging

#Setup logger
logger = log.setup_custom_logger('root', logging.ERROR)
logger.debug('Starting Test Run')

#Load LCC Model
myModel = LCCModel.LCCModel('TestModel')
myRegression = WBSRegressionModel.WBSRegressionModel('TestRegression', 'Turret')
myModel.loadLCCModel(".\\data\\lcc_wbs_models_all_phases.csv")

#Display it
print myModel.prettyPrint()

#
#Use the model to evaluate some mock models
#

#Test System 1, LCC from Excel: -2183971.177
testSystem1 = {'WEIGHT' : 10, 'CREW_CAPCITY' :2}
testSystem1LCC=myModel.evaluate(testSystem1)
print "testSystem1 value: {}".format(testSystem1LCC)

#Test System 2, LCC from Excel: 2649696.814
testSystem2 = {'WEIGHT' : 10987, 'ENGINE_POWER' : 654, 'WPN_CALIBER' : 57, 'CREW_CAPCITY' :1}
testSystem2LCC=myModel.evaluate(testSystem2)
print "testSystem2 value: {}".format(testSystem2LCC)


