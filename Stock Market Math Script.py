#Start Stock Price
print ('Enter Start Price of Stock')
StartP = float(input())
#Previous Week's price
print ("Enter Previous Week's Price")
LastWeekP = float(input())
#Current stock price
print ("Enter Current Stock Value/Close Value")
CurrentP = float(input())
#Number of shares value
print ("Enter the number of shares bought")
Shares = int(input()) 
#Is this a gain or loss? Boolean
Gain = bool(True)

#Current Value of stocks
Current_Value = CurrentP * Shares 

#Last Weeks Value of stocks
LastWeek_Value = LastWeekP * Shares

#Start Value
Start_Value = StartP * Shares

#you might need to create and check function that checks current value and last week value to dettermin if it's week loss or gain.

#Weekly Difference Calculation
WeeklyDif = Current_Value - LastWeek_Value

if Current_Value > LastWeek_Value: #gain
    WeeklyDif = Current_Value - LastWeek_Value
else:
    Gain = False
    WeeklyDif = LastWeek_Value - Current_Value

if Start_Value > Current_Value:
    GainStart = bool(False)
else:
    GainStart = bool(True)

#Difference From Start
if GainStart == False: #when loss
    Start_Diff = Start_Value - Current_Value
else: #when gain
    Start_Diff = Current_Value - Start_Value
    
# % Increase or Decrease
In_or_Dec_Percent = ((Start_Diff/Start_Value) * 100)

#printing here

print("""
Results:
(Remember to round up to dollars and cents)

""")

#Weekly gain/loss
print("Total Value is: $" + str(Current_Value))
if Gain == True:
    print("Weekly Gain is: $" + str(WeeklyDif))
    print ("Weekly Loss is: XXX")

if Gain == False:
    print("Weekly Gain is: XXX")
    print("Weekly Loss is: $" + str(WeeklyDif))

#Weekly difference
print("Weekly Difference from start is: " + str(Start_Diff))

#Percent Increase
if GainStart == True:
    print("Percent increase is: " + str(In_or_Dec_Percent))
    print("Percent decrease is: XXX")

if GainStart == False:
    print("Percent increase is: XXX")
    print("Percent decrease is: " + str(In_or_Dec_Percent))

