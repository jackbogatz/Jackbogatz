import pandas as pd
import matplotlib.pyplot as plt
import csv

"""
You should have created as many csv files for as many tests as you
did, but if you did not and have all the data under 1 csv file, then
create as many as csv files for as many many tests as you did and put
the data in them because that's how this code is set up. I have already 
prepared 5 test runs, so if there are more, then add more with the format
below. 

There might be some data above the headings, so if there is, then erase 
them

"""

# Previous tests
January_Test = pd.read_csv("January 21 Thrust CharacterizationTest.csv")
Febuary_11_Test =pd.read_csv("Febuary 12 Thrust CharacterizationTest.csv")
Feb_19_E11J = pd.read_csv("Febuary 19  E11J Test.csv")
Feb_19_E6_1 = pd.read_csv("Febuary 19 E6  Test Old Case.csv")
Feb_19_E11J_2 = pd.read_csv("Febuary 19 E11J Test2 New Case.csv")
Feb_19_F12J_1 = pd.read_csv("Febuary 19 F12J Test New Case.csv")
Feb_19_F12J_2 = pd.read_csv("Febuary 19 F12J Test2 New Case.csv")


#Graph to show what a F11J Engine Thrust vs TIme graph should look like
D12 = pd.read_csv("D12 Manufactorer Thrust vs Time.csv")
#D12.plot(x = 'Time')
#plt.legend(['D12'])
#plt.xlabel("Time (S)")
#plt.ylabel("Thrust (N)")
#plt.title("Thrust vs Tine")


#Graph to show what a F11J Engine Thrust vs TIme graph should look like
F12J = pd.read_csv("F11J Thrust vs Time.csv")
#F12J.plot(x = 'Time')
#plt.legend(['F12J'])
#plt.xlabel("Time (S)")
#plt.ylabel("Thrust (N)")
#plt.title("Thrust vs Tine")

# Graph to show what a E11J Motor Thrust vs Time graph should look like
E11J = pd.read_csv("E11J Manufactorer Thrust vs Time.csv")
#E11J.plot(x = 'Time')
#plt.legend(['E11J'])
#plt.xlabel("Time (S)")
#plt.ylabel("Thrust (N)")
#plt.title("Thrust vs Tine")

E6 = pd.read_csv("E6 Maufactorer Thrust Data.csv")
#E6.plot(x = 'Time')
#plt.legend(['E6'])
#plt.xlabel("Time (S)")
#plt.ylabel("Thrust (N)")
#plt.title("Thrust vs Tine")



# Graph that shows our first motor test 
"""  E old case """
test1 = pd.read_csv("Test1.csv")
test1.iloc[:,0] = test1.iloc[:,0] -107.110
#test1.plot(x = 'Time', y = ['Thrust'])
#plt.legend(['test1'])
#plt.xlabel("Time (S)")
#plt.ylabel("Thrust (N)")
#plt.title("Thrust vs Tine")


# Graph that shows our second motor test 
"""  E6  """
test2 = pd.read_csv("Test2.csv")
test2.iloc[:,0] = test2.iloc[:,0] - 11.815
#test2.plot(x = 'Time', y = ['Thrust'])
#plt.legend(['test2'])
#plt.xlabel("Time (S)")
#plt.ylabel("Thrust (N)")
#plt.title("Thrust vs Tine")


# Graph that shows our third motor test 
""" E new case """
test3 = pd.read_csv("Test3.csv")
test3.iloc[:,0] = test3.iloc[:,0] - 39.287
#test3.plot(x = 'Time', y = ['Thrust'])
#plt.legend(['test3'])
#plt.xlabel("Time (S)")
#plt.ylabel("Thrust (N)")
#plt.title("Thrust vs Tine")


# Graph that shows our fourth motor test 
"""  F12 new case  """
test4 = pd.read_csv("Test4.csv")
test4.iloc[:,0] = test4.iloc[:,0] - 25.492
#test4.plot(x = 'Time', y = ['Thrust'])
#plt.legend(['test4'])
#plt.xlabel("Time (S)")
#plt.ylabel("Thrust (N)")
#plt.title("Thrust vs Tine")

# Graph that shows our fifth motor test 
"""  F12 new case """
test5 = pd.read_csv("Test5.csv")
test5.iloc[:,0] = test5.iloc[:,0] - 17.649
#test5.plot(x = 'Time', y = ['Thrust'])
#plt.legend(['test5'])
#plt.xlabel("Time (S)")
#plt.ylabel("Thrust (N)")
#plt.title("Thrust vs Tine")


# Graph that shows our sixth motor test 
#test6 = pd.read_csv("Test6.csv")
#test6.iloc[:,0] = test6.iloc[:,0] - 152.833
#test6.plot(x = 'Time', y = ['Thrust'])
#plt.legend(['test6'])
#plt.xlabel("Time (S)")
#plt.ylabel("Thrust (N)")
#plt.title("Thrust vs Tine")


"""
UNCOMMENT ALL THE CODE BELOW
TO DISPLAY ALL THE GRAPHS ON A SINGLE GRAPH

"""
#plt.plot(January_Test['Time'], January_Test['Thrust'], label = 'January_Test')
#lt.plot(Febuary_11_Test['Time'], Febuary_11_Test['Thrust'], label = 'Febuary 11 Test')
#plt.plot(Feb_19_E11J['Time'], Feb_19_E11J['Thrust'], label = 'Febuary 19 E11J Test' )
#plt.plot(Feb_19_E6_1['Time'], Feb_19_E6_1['Thrust'], label = 'Febuary 19 E6')
#plt.plot(Feb_19_E11J_2['Time'], Feb_19_E11J_2['Thrust'], label = 'Febuary 19 E11J Test2')
plt.plot(Feb_19_F12J_1['Time'], Feb_19_F12J_1['Thrust'], label = 'Febuary 19 F12J Test1')
plt.plot(Feb_19_F12J_2['Time'], Feb_19_F12J_2['Thrust'], label = 'Febuary 19 F12J Test2')

#plt.plot(D12['TIme'], D12['Thrust'],label = 'D12')
#plt.plot(F12J['Time'], F12J['Thrust'],label = 'F12J')   
#plt.plot(E11J['Time'], E11J['Thrust'],label = 'E11J')
#plt.plot(E6['Time'], E6['Thrust'], label = 'E6')

#plt.plot(test1['Time'], test1['Thrust'], label = 'test1')
#plt.plot(test2['Time'], test2['Thrust'], label = 'test2')
#plt.plot(test3['Time'], test3['Thrust'], label = 'test3')
#plt.plot(test4['Time'], test4['Thrust'], label = 'test4')
#plt.plot(test5['Time'], test5['Thrust'], label = 'test5')
#plt.plot(test6['Time'], test6['Thrust'], label = 'test6')

plt.xlabel("Time (S)")
plt.ylabel("Thrust (N)")
plt.title("Thrust vs Tine")
plt.legend()
plt.show()

# Converts the data to a csv file where time starts at 0
#test1.to_csv("RevisedTimeTest1.csv", index = False)
    
