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
import Includes as inc
import logging

class WBSRegressionModel:
	'''
	This WBSRegression class models a basic Work Breakdown Structure (WBS) regression model.
	
	
	To use this class, you must first instantiate it, then load it using a CSV string that
	contains the R2, intercept, coefficients, and the p-valeus for each coefficient.
	
	'''	
	def __init__(self, name, wbs_id):
		'''
		Creates a -I{WBSRegressionModel} given a name and WBS id.
		
		@param name: A name to help remember the model i.e. "Army Life Cycle Costing Model"
		@param wbs_id:  The ID number for the WBS model.  This should match one of the values in Include.py
		
		
		'''
		self.name = name
		self.wbsId = wbs_id
		self.R2 = -1		
		self.intercept = 0
		self.attributeCoeff = {}
		self.attributeSignificance = {}
		self.logger = logging.getLogger('root')

		#make a coeeficient array for the attributes.  Initialize as zero
		for attribute in inc.MODEL_ATTRIBUTES:
			self.attributeCoeff[attribute] = 0
			self.attributeSignificance[attribute] = 0

	
	def fitWBSRegressionModel(self, dataFilePath):
		'''
		(UNIMPLMENTED)
		Fits a regresssion model to some data. (
		
		@param dataFilePath:  Path to a matrix of WBSRegression data.  This should
		                      include look like this:
				      
		                      WBS_CODE WBS_ITEM COST A1 A2 A3 ... An
	                              where A1..An are the attributes defined in WBSRegressionAttributes
	 
	
		'''
		print "TODO: model fit to data in file %s..ensure you call saveWBSRegressionModel! %s" % modelFilePath
	
	def evaluate(self, ivalues):
		'''
		
		Evaluates a regression model given some independent variable values (model attributes) 
		
		@param  ivalues: a dictionary of (key, value) pairs where key is one of the indenpendent
		                 variables names in Includes.py and value is the variable's value
				 
		@return:  The value of the dependent model given those values
		
		
		'''
		result=self.intercept;
		for attribute in inc.MODEL_ATTRIBUTES:
			if ivalues.has_key(attribute):
				nextCoeff=0.0;
				nextCoeffS = self.attributeCoeff[attribute];
				try:
					nextCoeff=float(nextCoeffS);
				except ValueError:
					nextCoeff=0;	
							
				nextIVValue = ivalues[attribute];
				result=result+nextCoeff*nextIVValue;		
		return result;
	
	def loadFromCSVString(self, csvString):
		'''

		Load the WBSRegressionModel from a CSV string. 
		
		@param:	A CSV string representation of the regression model.
		
		This CSV string is formatted as follows:
		
		R2,INTERCEPT, Factor1Coeff,Factor1PValue, Factor2Coeff,Factor2PValue,..., FactorNCoeff,FactorNPValue
						
		'''
		model = csvString.split(",")
		if len(model) >= 2*len(inc.MODEL_ATTRIBUTES)+3 :		                     
			self.wbsId=model[0]
			self.R2 = model[1]
			try:
				self.intercept = float(model[2])
			except ValueError:
				self.intercept=0;				
			i=3
			for attribute in inc.MODEL_ATTRIBUTES:
				self.attributeCoeff[attribute] = model[i]
				self.attributeSignificance[attribute] = model[i+1]
				i=i+2
			self.logger.debug("Regression model {} loaded".format(self.wbsId))
		else:
			self.logger.error("***ERROR: Model CSV does not contain the right number of elements. ")
			self.logger.error("**Got:" + csvString + "Expecting:**")
			sb=[]
			sb.append("\tWBS,R2,INTERCEPT")
			for attribute in inc.MODEL_ATTRIBUTES:
				sb.append(",{}_Coeff,".format(attribute))
				sb.append("{}_PValue".format(attribute)	)			
			self.logger.error(''.join(sb))
	
	def prettyPrint(self):
		'''
		Prints a nice representation of the regression model.
		
		@return:  A nice, readable, multi-line representation of the regression model
		
		'''
		sb=[]
		sb.append("\n\n\t---------------------------------------------------")
		sb.append("\n\tWBS_ID: {}\n".format(self.wbsId))
		sb.append("\tR2: {}\n\n".format(self.R2))
		sb.append("\tY= {} ".format(self.intercept))
		for attribute in inc.MODEL_ATTRIBUTES:
			if self.attributeCoeff[attribute] <> '':			
				sb.append("+ {} * {}".format(self.attributeCoeff[attribute],attribute))
		sb.append("\n\n\tCoeff Significance:\n")
		for attribute in inc.MODEL_ATTRIBUTES:
			if self.attributeCoeff[attribute] <> '':			
				sb.append("\t\t{} : {}".format(attribute,self.attributeSignificance[attribute]))
		
		return ''.join(sb)

	def toCSVString(self):
		'''
		
		Returns a csv string representation of the regression model.
		
		return:  A csv sstring representation of the WBSregressionModel.  Format is:
		
		R2,INTERCEPT, Factor1Coeff,Factor1PValue, Factor2Coeff,Factor2PValue,..., FactorNCoeff,FactorNPValue
		
		'''
		sb=[]
		sb.append("{},{}".format(self.R2, self.intercept))
		for attribute in inc.modelAttributes:
			sb.append(",{},".format(self.attributeCoeff[attribute]	))
			sb.append("{}".format(self.attributeSignificance[attribute] )	)
		return ''.join(sb)
	

	def __repr__(self):	
		'''
		return:  a string representation of object.  For a cleaner view, use prettyprint()
		'''
		sb=[]
		sb.append("name:%s \nWBS ID: %s \nR2:%s \nIntercept: %s \nAttributes:\n" % (self.name,self.wbsId, self.R2, self.intercept))
		for attribute in inc.modelAttributes:
			sb.append("\t{}:".format(attribute))
			sb.append(" {}".format(self.attributeCoeff[attribute]))
			sb.append(', p=')
			sb.append("{}\n".format(self.attributeSignificance[attribute]))
		return ''.join(sb)
    