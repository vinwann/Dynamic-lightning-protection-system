#!/usr/bin/env python3

import mhi.pscad
import time
import subprocess
import random
with mhi.pscad.application() as pscad:
    import csv
    import os
                 
    with open("loc.txt", "w") as file1:
    # Writing data to a file
        file1.write(str(1))                     
    length= 10000
    res = 100              
    tr_names = ["7_8","8_9","4_5","5_7","4_6","6_9"]
    seed = 31
    random.seed(seed)
    #pscad.load(r'T46.pscx')
    for i in range(res,length,res) :   
        print("round "+str(i))
        t_l = i
        random_integer = random.randint(5, 40)
        while random_integer in [30,31,32]:
            random_integer = random.randint(5, 40)
        t46 = pscad.project("T46")
        t4_6 = t46.component(1036163106)
        t46.navigate_to(t4_6)
        t46_1 = t46.component(1196769153)
        t46_1.parameters(Length=str(i/1000)+" [km]", )
        #t46_1.parameters(Name="T46_1", R="0.830042073324", Freq="50.0 [Hz]", X="1.71647621572", B="1.26961314344e-05", Length=str(i/1000)+" [km]", Dim="3", Mode="1", CoupleEnab="0", cct_overlayed="0", CoupleName="row", CoupleOffset="0.0 [m]", CoupleRef="0", ManEnab="0", tname="tandem_segment", sfault="0", linc="10.0 [km]", steps="3", DataFormat="0", VR="230.0 [kV]", MVA="100.0 [MVA]", r0mpu="dim (10,10)", r0m="dim (10,10)", xl0mpu="dim (10,10)", xl0m="dim (10,10)", xc0mpu="dim (10,10)", xc0m="dim (10,10)", bc0mpu="dim (10,10)", tt0m="dim (10,10)", zs0m="dim (10,10)", gen_cnst="1", const_path="C:\\Temp\\my_constants_file.tlo", Date="1705552228", )
        t46_2 = t46.component(1709921185)
        t46_2.parameters(Length=str((length - i)/1000) +" [km]", )
        #t46_2.parameters(Name="T46_2", R="0.830042073324", Freq="50.0 [Hz]", X="1.71647621572", B="1.26961314344e-05", Length=str((length - i)/1000) +" [km]", Dim="3", Mode="1", CoupleEnab="0", cct_overlayed="0", CoupleName="row", CoupleOffset="0.0 [m]", CoupleRef="0", ManEnab="0", tname="tandem_segment", sfault="0", linc="10.0 [km]", steps="3", DataFormat="0", VR="230.0 [kV]", MVA="100.0 [MVA]", r0mpu="dim (10,10)", r0m="dim (10,10)", xl0mpu="dim (10,10)", xl0m="dim (10,10)", xc0mpu="dim (10,10)", xc0m="dim (10,10)", bc0mpu="dim (10,10)", tt0m="dim (10,10)", zs0m="dim (10,10)", gen_cnst="1", const_path="C:\\Temp\\my_constants_file.tlo", Date="1705552228", )
        obj = t46.component(128950166)
        obj.parameters(Ipk=str(random_integer)+" [kA]", )
        t46.navigate_to()
        t46.save()
        t46.run()
        print("Sim done")
        subprocess.call(["python","OutFileToCSV_46.py"])

        
        

   
    
