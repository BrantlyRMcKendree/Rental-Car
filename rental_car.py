import sys

#rentalCode as seen below is a variable.

rentalCode = input("(B)udget, (D)aily, or (W)eekly rental?\n")

if rentalCode == 'D' or rentalCode == 'd':
  (rentalPeriod) = input('Number of Days Rented:\n')
elif rentalCode == 'W' or rentalCode == 'w':
  (rentalPeriod) = input('Number of Weeks Rented:\n')
elif rentalCode == 'B' or rentalCode == 'b':
  (rentalPeriod) = input('Number of Days Rented:\n')

# Assigning Variable Values:
#   Below budgetCharge, dailyCharge, and weeklyCharge are being assigned a numerical value.
#   Also, directly above rentalPeriod is being assigned a string of text.   
  
budgetCharge = 40.00
dailyCharge = 60.00
weeklyCharge = 190.00

if rentalCode == 'D' or rentalCode == 'd':
  baseCharge = float(rentalPeriod) * dailyCharge

  
elif rentalCode == 'W' or rentalCode == 'w':
  baseCharge = float(rentalPeriod) * weeklyCharge

elif rentalCode == 'B' or rentalCode == 'b':
  baseCharge = float(rentalPeriod) * budgetCharge
  format(baseCharge,'.2f')

# Variables with Data-type appropriate operators
#   totalMiles below is a variable with data-type appropriate operators because it is
#   being assigned a value by operator the operator -. odoStart is being subtracted
#   from odoEnd. The data type is a number and the operator is subtraction.

odoStart = input("Starting Odometer Reading:\n")
odoEnd = input("Ending Odometer Reading:\n")
totalMiles = int(odoEnd) - int(odoStart)

# Changing Variable Values:
#   mileCharge is a variable that changes according to the conditional statements shown below.
#
# Branches:
#   The rentalCode variable below is being used in a branch of if and elif. 
#   if the rentalCode is B for budget then the program will execute that piece of the branch.
#   elif the rentalCode is D or W it will execute one of those pieces of the branch. 
#   else could be used last to blanket anything not covered in the branch. 
#   For example I could add else "Invalid entry" for anything beside the three 
#   identified by the branch below.

#

if rentalCode == 'B' or rentalCode == 'b':
  mileCharge = totalMiles * 0.25   
  
averageDayMiles = float(totalMiles)/float(rentalPeriod)
extraMiles = averageDayMiles - 100.00

if rentalCode == 'D' or rentalCode == 'd':
  if averageDayMiles < 100:
    mileCharge = 0.00
  elif averageDayMiles > 100:
    mileCharge = extraMiles * 0.25

averageWeekMiles = float(totalMiles)/float(rentalPeriod)

if rentalCode == 'W' or rentalCode == 'w':
  if averageWeekMiles < 900.00:
    mileCharge = 0.00
  elif averageWeekMiles > 900.00:
    mileCharge = float(rentalPeriod) * 100.00

    
amountDue = (mileCharge) + float(baseCharge) 
amountDue = ("{:.2f}".format(amountDue))   

print("Rental Summary")
print("Rental Code:" + rentalCode)
print("Rental Period:" + rentalPeriod)
print("Starting Odometer:" + odoStart)
print("Ending Odometer:" + odoEnd)
print("Miles Driven:" + str(totalMiles))
print("Amount Due:" + "$" + str(amountDue))
