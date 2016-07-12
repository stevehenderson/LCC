
"""
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
"""
import WBSRegressionModel
import Includes as inc
import logging


class LCCModel:
	'''
	 An LCCModel is a complete Life Cycle Cost model

	 It contains the underlying work breakdown structure (WBS) and regression
	 models required to evaluate life cycle costs for a system.
	 
	 Typical use cases:
	 
	 1. Load an existing LCCModel (from a csv file)
	 2. Evaluate LCCModel given a certain system and its attributes
	 
	 OR, Once a model is created and fit

	 1. Create a new LCCModel
	 2. Fit LCCModel to data (TO BE DEVELOPED)
	 3. Save LCCModel
	 4. Evaluate LCCModel given a certain system and its attributes
	
	'''
	
	def __init__(self, name):
		'''
		
		Creates a new LCCModel.
		
		@param self: ionstance variable
		@prama name: the name of the cost mode ("basic", "M1A1", etc)
		
		'''
		self.name = name
		
		#A dictionary speficying the wbs regression models for a lifecycle
		self.wbsRegressionModels= {}	
						
		#A logger used to help debug the code 
		self.logger = logging.getLogger('root')
				
	
	def evaluate(self, ivalues):
		'''
		
		Evauates an LCC given some independent variable values (model attributes)
	
		This will aggregate the individual regression models for each LCC Phase, for
		each WBS element.
	
		@param ivalues:  A dictionary of modelAttributes (see includes.py) that define the 
		independent variables in the model
	 
		@return The total LCC value given those values
		
		'''
		result=0;
		for key in self.wbsRegressionModels:
			nextValue = self.wbsRegressionModels[key].evaluate(ivalues)
			self.logger.debug("{} regression model contribution: {} ".format(key,nextValue))
			result=result+nextValue
			
		return result;
		
	def fitLCCModel(dataFilePath):
		'''
		(NOT IMPLMENETED)  Fit an LCC model given a data file
		
		'''
		self.logger.debug("TODO: model fit to data in file %s..ensure you call saveLCCModel! %s" % modelFilePath)
	
	
	def loadLCCModel(self, modelFilePath):
		'''
		
		Loads an LCCModel from disk.  This is represented as a CSV that defines a sparse matrix of regression models.
		
		@param modelFilePath:  The CSV containing the LCC model to load
				
		There is one row/rregression model for each combination of LCC phase, and WBS level
		
		There are K LCC phases, These correcpond to LCC_PHASES in includes.py
		
		There are N factors, or independent variables, called model attributes.  These correcpond to MODEL_ATTRIBUTES in includes.py
		
		There are M WBS levels that correspond to WBS_ELEMENTS in includes.py 
		
		In general this will look like:
		
		PHASE_0, WBS_0, R2, INTERCEPT, R2,INTERCEPT, Factor_1_Coeff,Factor_1_PValue, Factor_2_Coeff,Factor_2P_Value,..., Factor_N_Coeff,Factor_N_PValue
		PHASE_0, WBS_1, R2, INTERCEPT, R2,INTERCEPT, Factor_1_Coeff,Factor_1_PValue, Factor_2_Coeff,Factor_2P_Value,..., Factor_N_Coeff,Factor_N_PValue
		.
		.
		PHASE_K, WBS_M, R2, INTERCEPT, R2,INTERCEPT, Factor1Coeff,Factor1PValue, Factor2Coeff,Factor2PValue,..., FactorNCoeff,FactorNPValue
		.
		
		
		The following is an extract of an actual file:
		
		CC_PHASE,WBS_ID,R2,INTERCEPT,WEIGHT,WEIGHT-P,WHEELBASE,WHEELBASE-P,ENGINE_POWER,ENGINE_POWER_P,WPN_CALIBER,WPN_CALIBER_P,CREW_CAPACITY,CREW_CAPACITY_P,TRACK_TIRE,TRACK_TIRE_P
		RESEARCH & DEVELOPMENT,WBS_VEHILCE_ASSEMBLED,0.0781,27905.9554,,,,,154.1194,0.0988,,,,,,
		RESEARCH & DEVELOPMENT,WBS_HULL_FRAME,0.1318,27915.2634,,,,,,,871.1196,0.032,,,,
		.
		.
		.
		PROCUREMENT,WBS_VEHILCE_ASSEMBLED,0.0781,27905.9554,,,,,154.1194,0.0988,,,,,,
		PROCUREMENT,WBS_HULL_FRAME,0.1318,27915.2634,,,,,,,871.1196,0.032,,,,
		
		'''
		modelCount=0
		with open(modelFilePath, mode='r', buffering=1) as csvfile:
			#skip header
			next(csvfile)
			for row in csvfile:
				#Pull off LCC_PHASE
				model = row.split(",")
				lccPhase = model[0]				
				nextRegression = WBSRegressionModel.WBSRegressionModel('UnnamedRegression', 'UnnamedWBS')
				nextRegression.loadFromCSVString( ','.join(model[1:]))
				nextRegression.name=nextRegression.wbsId+"_COST_MODEL"
				modelCount=modelCount+1
				self.wbsRegressionModels[(lccPhase,nextRegression.wbsId)]=nextRegression				
			
		self.logger.debug("LCC Model loaded {} regression cost models from {}".format(modelCount,modelFilePath))
	
	def prettyPrint(self):
		'''
		
		Provides a prettier string representation for the model		
		
		'''
		sb=[]
		sb.append("LCCModel {}\n".format(self.name))
		modelCounter=0
		for phase in inc.LCC_PHASE:
			sb.append("Regression models in Phase: {}".format(phase))
			for key in inc.WBS_ELEMENTS:
				try:
					sb.append(self.wbsRegressionModels[(phase,key)].prettyPrint())
					modelCounter=modelCounter+1					
				except KeyError:
					self.logger.debug("No entry for key {},{}".format(phase,key))
			
			if modelCounter == 0:	
				sb.append("\n(NONE)")			
			
			sb.append("\n\n")			
		return ''.join(sb)	
	
	
	#
	# loadLCCModel:  Load an LCCModel from disk.  This will include
	# 					its fitted WBS regression equations (if present)
	#
	# modelFilePath:  Path for the model file
	#		
	def saveLCCModel(self, modelFilePath):
		logger.debug("TODO: model saved to %s" % modelFilePath)
	
		
	#
	# returns a string representation of object
	def __repr__(self):
		return "< name:%s \n attributes: %s \n wbsRegressionModels:%s >" % (self.name,inc.MODEL_ATTRIBUTES, self.wbsRegressionModels)
		#return "< name:%s >" % (self.name)
