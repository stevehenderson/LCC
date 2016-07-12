
#http://www.statmethods.net/stats/regression.html

library(MASS)
library(leaps)
library(car)

#Change this for you computer!
setwd('F:\\dev\\lcc\\R-models')
uber<-read.csv('uber.csv')

#Examine structure
str(uber)

#How many rows
nrow(uber)

#Rows by system
summary(uber$PROGRAM_NAME)

#Rows by life cycle phase
summary(uber$LIFE_CYCLE_PHASE)



###################################################################################
#WBS_TURRET_ASSEMBLY
###################################################################################

###########################
# ORDINARY
###########################
wbsModel<- lm(WBS_TURRET_ASSEMBLY~GW+WIDTH+ENGINE_PWR_HP+WPN_CALIBER_MM+TRACK_TIRE, data=uber)
summary(wbsModel)

############################
# STEPWISE
############################
#See:http://www.statmethods.net/stats/regression.html
#TODO:  ADD CREW CAPACITY--Make DICHATOMOUS
wbsModel.step<- stepAIC(wbsModel, direction="both")
#wbsModel.step$anova
summary(wbsModel.step)

###################################################################################
#WBS_HULL_FRAME
###################################################################################

###########################
# ORDINARY
###########################
wbsModel<- lm(WBS_HULL_FRAME~GW+WIDTH+ENGINE_PWR_HP+WPN_CALIBER_MM+TRACK_TIRE, data=uber)
summary(wbsModel)

############################
# STEPWISE
############################
#See:http://www.statmethods.net/stats/regression.html
#TODO:  ADD CREW CAPACITY--Make DICHATOMOUS
wbsModel.step<- stepAIC(wbsModel, direction="both")
summary(wbsModel.step)

###################################################################################
#WBS_SUSPENSION
###################################################################################

###########################
# ORDINARY
###########################
wbsModel<- lm(WBS_SUSPENSION~GW+WIDTH+ENGINE_PWR_HP+WPN_CALIBER_MM+TRACK_TIRE, data=uber)
summary(wbsModel)

############################
# STEPWISE
############################
#See:http://www.statmethods.net/stats/regression.html
#TODO:  ADD CREW CAPACITY--Make DICHATOMOUS
wbsModel.step<- stepAIC(wbsModel, direction="both")
summary(wbsModel.step)

###################################################################################
#WBS_SUSPENSION
###################################################################################

###########################
# ORDINARY
###########################
wbsModel<- lm(WBS_SUSPENSION~GW+WIDTH+ENGINE_PWR_HP+WPN_CALIBER_MM+TRACK_TIRE, data=uber)
summary(wbsModel)

############################
# STEPWISE
############################
#See:http://www.statmethods.net/stats/regression.html
#TODO:  ADD CREW CAPACITY--Make DICHATOMOUS
wbsModel.step<- stepAIC(wbsModel, direction="both")
summary(wbsModel.step)

###################################################################################
#WBS_POWER_PACKAGE_TRAIN
###################################################################################

###########################
# ORDINARY
###########################
wbsModel<- lm(WBS_POWER_PACKAGE_TRAIN~GW+WIDTH+ENGINE_PWR_HP+WPN_CALIBER_MM+TRACK_TIRE, data=uber)
summary(wbsModel)

############################
# STEPWISE
############################
#See:http://www.statmethods.net/stats/regression.html
#TODO:  ADD CREW CAPACITY--Make DICHATOMOUS
wbsModel.step<- stepAIC(wbsModel, direction="both")
summary(wbsModel.step)

###################################################################################
#WBS_AUXILIARY_AUTOMOTIVE
###################################################################################

###########################
# ORDINARY
###########################
wbsModel<- lm(WBS_AUXILIARY_AUTOMOTIVE~GW+WIDTH+ENGINE_PWR_HP+WPN_CALIBER_MM+TRACK_TIRE, data=uber)
summary(wbsModel)

############################
# STEPWISE
############################
#See:http://www.statmethods.net/stats/regression.html
#TODO:  ADD CREW CAPACITY--Make DICHATOMOUS
wbsModel.step<- stepAIC(wbsModel, direction="both")
summary(wbsModel.step)

###################################################################################
#WBS_FIRE_CONTROL
###################################################################################

###########################
# ORDINARY
###########################
wbsModel<- lm(WBS_FIRE_CONTROL~GW+WIDTH+ENGINE_PWR_HP+WPN_CALIBER_MM+TRACK_TIRE, data=uber)
summary(wbsModel)

############################
# STEPWISE
############################
#See:http://www.statmethods.net/stats/regression.html
#TODO:  ADD CREW CAPACITY--Make DICHATOMOUS
wbsModel.step<- stepAIC(wbsModel, direction="both")
summary(wbsModel.step)



