import csv
import time 
import os
DataSet = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
file_path1 = 'T45.gf46\T45_01.out'
file_path2 = 'T45.gf46\T45_02.out'
def assign_data_to_read():

    num = 0
    with open("loc.txt", "r+") as file1:
    # Reading from a file
        num = int(file1.read())
    column_order = ['time', 'I4:1', 'I4:2', 'I4:3', 'E4:1', 'E4:2', 'E4:3'
                    , 'I7:1', 'I7:2', 'I7:3', 'E7:1', 'E7:2', 'E7:3', 
                    'I9:1', 'I9:2', 'I9:3', 'E9:1', 'E9:2', 'E9:3']  # Define the column names as desired
    ######################################################################
    seconds = time.time()

    file_name1 = "L_4_5_"+str(num*100)+"_1"+".csv"
    ############################################################3
    with open(file_name1, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(column_order)
        for i in range(0, len(DataSet[0])):
            #print("Completed  " + str(i*100/1000002)+"%")
            writer.writerow([ DataSet[0][i],DataSet[1][i],DataSet[2][i],DataSet[3][i],DataSet[4][i],DataSet[5][i],DataSet[6][i],DataSet[7][i],DataSet[8][i],DataSet[9][i],DataSet[10][i],DataSet[11][i],DataSet[12][i],DataSet[13][i],DataSet[14][i],DataSet[15][i],DataSet[16][i],DataSet[17][i],DataSet[18][i]])


    with open("loc.txt", "w") as file1:
    # Writing data to a file
        file1.write(str(num+1))
        
        file1.close()  # to change file access modes

def readGeneratedData():
    ignoredDataCount = 0
    
    

    with open(file_path1, 'r') as file:
        count = 0
        print(file)
        for line in file:
            # Split each line into a list of values, assuming space-separated columns
            if count > 0:
                #print("scsc"+line)
                values = line.strip().split()
                # Append the first and second values to the data list
                #if len(values) == 9 :
                #print(values)
                float_array = [float(element) for element in values]
                #print(len(float_array))
                for i in range(0,11):
                    DataSet[i].append(float_array[i])
                    # count +=1
                    # if count > 1000:
                    #     break
                #else:
                #    ignoredDataCount+=1
            else:
                count += 1
    print("File 1 done ")
    with open(file_path2, 'r') as file:
        count = 0
        for line in file:
            # Split each line into a list of values, assuming space-separated columns
            if count > 0 :
                values = line.strip().split()
                #print(values)
                # Append the first and second values to the data list
                #if len(values) == 9 :
                float_array = [float(element) for element in values]
                for i in range(11,19):
                    DataSet[i].append(float_array[i-10])
                    # count +=1
                    # if count > 1000:
                    #     break
                #else:
                #    ignoredDataCount+=1
            else:
                count += 1
    print("File 2 done ")
    return 0

readGeneratedData()
print(len(DataSet[0]))
assign_data_to_read()
if os.path.exists(file_path1):
  os.remove(file_path1)
else:
  print("The file does not exist")

if os.path.exists(file_path2):
  os.remove(file_path2)
else:
  print("The file does not exist")
