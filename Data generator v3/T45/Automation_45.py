#!/usr/bin/env python3

import mhi.pscad
import time
import subprocess
import random
with mhi.pscad.application() as pscad:
    pscad = mhi.pscad.launch()
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
    
    t45 = pscad.project("T45")
    #pscad.load(r'T45.pscx')
    #
    #pscad.load('E:\Data generator v3\T45.pscx')
    for i in range(res,length,res) :   
        print("round "+str(i))
        random_integer = random.randint(5, 40)
        while random_integer in [30,31,32]:
            random_integer = random.randint(5, 40)
        t_l = i
        t45 = pscad.project("T45")
        #t45.parameters(creator="adarbandi,1397677439", time_duration="0.025", time_step="0.025", sample_step="1", chatter_threshold=".001", branch_threshold=".0005", StartType="0", PlotType="1", output_filename="$(Namespace).out", SnapType="0", SnapTime="0.3", snapshot_filename="$(Namespace).snp", MrunType="0", Mruns="1", Scenario="", Advanced="14335", Options="16", Build="18", Warn="0", Check="0", description="", revisor="vinur, 1705559842", startup_filename="", sparsity_threshold="200", )
        t4_5 = t45.component(1426503440)
        t45.navigate_to(t4_5)
        t45_1 = t45.component(1730758801)
        t45_1.parameters(Length=str(i/1000)+" [km]", )
        #t45_1.parameters(Name="T45_1", R="0.830042073324", Freq="50.0 [Hz]", X="1.71647621572", B="1.26961314344e-05", Length=str(i/1000)+" [km]", Dim="3", Mode="1", CoupleEnab="0", cct_overlayed="0", CoupleName="row", CoupleOffset="0.0 [m]", CoupleRef="0", ManEnab="0", tname="tandem_segment", sfault="0", linc="10.0 [km]", steps="3", DataFormat="0", VR="230.0 [kV]", MVA="100.0 [MVA]", r0mpu="dim (10,10)", r0m="dim (10,10)", xl0mpu="dim (10,10)", xl0m="dim (10,10)", xc0mpu="dim (10,10)", xc0m="dim (10,10)", bc0mpu="dim (10,10)", tt0m="dim (10,10)", zs0m="dim (10,10)", gen_cnst="1", const_path="C:\\Temp\\my_constants_file.tlo", Date="1705552228", )
        t45_2 = t45.component(837235280)
        t45_2.parameters(Length=str((length - i)/1000)+" [km]", )
        #t45_2.parameters(Name="T45_2", R="0.830042073324", Freq="50.0 [Hz]", X="1.71647621572", B="1.26961314344e-05", Length=str((length - i)/1000)+" [km]", Dim="3", Mode="1", CoupleEnab="0", cct_overlayed="0", CoupleName="row", CoupleOffset="0.0 [m]", CoupleRef="0", ManEnab="0", tname="tandem_segment", sfault="0", linc="10.0 [km]", steps="3", DataFormat="0", VR="230.0 [kV]", MVA="100.0 [MVA]", r0mpu="dim (10,10)", r0m="dim (10,10)", xl0mpu="dim (10,10)", xl0m="dim (10,10)", xc0mpu="dim (10,10)", xc0m="dim (10,10)", bc0mpu="dim (10,10)", tt0m="dim (10,10)", zs0m="dim (10,10)", gen_cnst="1", const_path="C:\\Temp\\my_constants_file.tlo", Date="1705552228", )
        obj = t45.component(1007846749)
        obj.parameters(Ipk=str(random_integer)+" [kA]", )
        t45.navigate_to()
        t45.save()
        t45.run()
        print("Sim done")
        subprocess.call(["python","OutFileToCSV_45.py"])


   

  
    

    
   