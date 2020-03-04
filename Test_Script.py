import glob
import os
import pandas as pd
import csv
import sys

# What I'm trying to do here is to take a given value, and if it's a certain value, write it somewhere. Irrelevant what value it is. For now for PED only.
cwd = os.getcwd()  # gets current directory
os.chdir(cwd)  # directory to files
cwd_list = os.listdir(".")
file = cwd_list[0]  # set up specific file



TTC = "PedestrianDetection.s_Ped_00_TTC_withA"
Timestamp = "PedestrianDetection.s_Ped_Image_Number"
CB_Early="PedestrianDetection.s_Ped_00_AccBrakeX"
Class="PedestrianDetection.s_Ped_00_Class"

xl = pd.read_csv(file, usecols=[TTC, Timestamp,CB_Early,Class])  # imports only these columns
xl_2 = pd.DataFrame({'Timestamp':[],'TTC':[],'CB_Early':[],'Class':[]},index=[])  # Creates dataframe
x = -1 #to ensure x starts at 0
l = 0



for row in xl.iterrows():  # for each in each item
    x = x + 1
    FrameID=xl.iloc[x][0] #sets up values
    CB_Early=xl.iloc[x][-1]
    TTC=xl.iloc[x][-2]
    Class=xl.iloc[x][-3]
    
    if CB_Early == 0.5:
        l = l + 1
        temp=xl_2.loc[l,:]=[FrameID,TTC,CB_Early,Class] 
        xl_2.append(temp) #adds a new row
        #print(FrameID)

xl_3 = pd.DataFrame({'Frame Start':[],'Frame End':[],'Class':[],'Lenght':[]},index=[])
#print(xl_2['TTC'].count())

x=-1
for row in xl_2.iterrows():
    x = x + 1
    current_frame=xl_2.iloc[x][0]
    next_frame = xl_2.iloc[x+1][0]
    first_frame=0
    last_frame=0
    count=0
    obj_type=xl.iloc[x][-3]
    
    if x+2< xl_2['TTC'].count():
        if current_frame == next_frame -1:
            count=count+1
        if xl_2.iloc[x-1][0] != current_frame:
            first_frame=current_frame            

        else:
            last_frame=current_frame

    print("first frm: ", first_frame, "last frm: ", last_frame)

    temp_2=xl_3.loc[l,:]=[first_frame,last_frame,obj_type,count]
    xl_3.append(temp_2)
    #print(temp_2)
#print(xl_3)
    

#print(xl_2)
#xl_2.to_excel(r'C:\Users\wj8wfy\Desktop\Script_test\deets.xlsx') #exports to excel
