import csv
import matplotlib.pyplot as plt
import pandas as pd
import os
import time
from tabulate import TableFormat, tabulate



#The following function is to clean the shell
def clean():
    if os.name=="nt":
        os.system("cls")
        
    else:
        os.system("clear")





def readFiles():

    #reads the CSV for lotto
    thisFolder=os.path.dirname(os.path.abspath(__file__))
    lottoCSVFile=os.path.join(thisFolder,"lotto-draw-history.csv")

    lottoCSV=open(lottoCSVFile,'r')
    lottoDictReader=csv.DictReader(lottoCSV)
    lottoList=[]

    #creating list of dicts 
    for row in lottoDictReader:
        lottoList.append(row)
    
    return lottoList


#function for representing data as probabilities
def dispProb(data,count):
    
    sortedDics=dict(sorted(data.items(),key=lambda item:item[1]))
    topNumbers=[]
    probabilities=[]
    
    i=-1
    while i>=-6:
        topNumbers.append(list(sortedDics)[i])
        i-=1
            
          
    for number in topNumbers:

        probability=str(round(((sortedDics[number])/count)*100,2))+ ' %'
        probabilities.append(probability)

    probDic={
        'Number':topNumbers,
        'Possibility':probabilities
    }  
        
    df = pd.DataFrame(probDic, index=['Most Probable Num 1', 'Most Probable Num 2', 'Most Probable Num 3','Most Probable Num 4', 'Most Probable Num 5', 'Most Probable Num 6'])

    print(df)
    print('\n \n')

#function for representing presense of each number as a bar graph and a table
def graphs(numbers):

    tableData=[["Numbers", "Counts"]]
    for number in numbers:
        data=[]
        data.append(number)
        data.append(numbers[number])
        tableData.append(data)

    
    print(tabulate(tableData , tablefmt='fancy_grid'))

    numList=list(numbers)
    counts=list(numbers.values())

    plt.bar(numList,counts)
    plt.xlabel('Numbers')
    plt.ylabel('Count')
    plt.title('Numbers Count')

    plt.show()


def main():
    clean()
    #Welcome message
    error=False
    print("\n")
    print ("Welcome to Lotto and Eurro Millionair lottery numbers likelyhood checker")
    print("\n")
    print("Please be aware you have to update the CSV files in the path to get better likelyhood \n")

    
    #Asking user how likelyhood should be calculated
    print("Select a time period \n")
    print("* 1 - likelyhood from last 3 months data")
    print("* 2 - likelyhood from last 6 months data")
    print("* 3 - likelyhood from this year data")
    print("* 4 - likelyhood from all previous data since 2018 \n")

    dateChoice=input("Please type your choice number here and press enter: ").strip()
    clean()

    #defining balls
    numbers={}
    for i in range(1,60):
        numbers[f"{i}"]=0
    
    Rawdata=readFiles()
    dataCount=0


    for ball in Rawdata:

        for i in range(1,7):
            #counting the presences of each number depending on the user's selection
            for number in numbers:
                if dateChoice=="1":
                    if int(ball[f'Ball {i}'].strip()) == int(number) and ball["YYYY"]=="2021" and ball["MMM"] in ["Jul","Jun","May"] :
                        numbers[number]+=1

                elif dateChoice=="2":
                    if int(ball[f'Ball {i}'].strip()) == int(number) and ball["YYYY"]=="2021" and ball["MMM"] in ["Jul","Jun","May","Apr","Mar","Feb"] :
                        numbers[number]+=1

                elif dateChoice=="3":
                    if int(ball[f'Ball {i}'].strip()) == int(number) and ball["YYYY"]=="2021":
                        numbers[number]+=1
                elif dateChoice=="4":
                    if int(ball[f'Ball {i}'].strip()) == int(number):
                        numbers[number]+=1
                else:
                    print("Invalid input! please try again...")
                    time.sleep(2)
                    error=True
                    break
            if error:
                break
        if error:
            break
    if error:
        exit()

    #calculating total counts depending on user's selection
    if dateChoice=="1":
        for ball in Rawdata:
            if ball["YYYY"]=="2021" and ball["MMM"] in ["Jul","Jun","May"]:
                dataCount+=1
    elif dateChoice=="2":
        for ball in Rawdata:
            if ball["YYYY"]=="2021" and ball["MMM"] in ["Jul","Jun","May","Apr","Mar","Feb"]:
                dataCount+=1
        
    elif dateChoice=="3":
        for ball in Rawdata:
            if ball["YYYY"]=="2021":
                dataCount+=1
    else:
        for ball in Rawdata:
            dataCount+=1
    
    #Asking user how results should be presented
    print("Please select an option.(Type the option number and press enter) \n")
    print(" 1 - See number counts and most probable numbers.")
    print(" 2 - Enter a set of numbers and see the probability of getting them as the winning numbers. \n")
    userChoice=input("Please enter your choice here: ").strip()
    clean()


    if userChoice=="1":       
        dispProb(numbers,dataCount)
        

    else:
        graphs(numbers)

    

if __name__=='__main__':
    main()
else:
    print("Sorry! something went wrong ")

    


