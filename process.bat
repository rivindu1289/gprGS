rscript.exe sigProc.R "2014_04_25_frenke/rawGPR/LINE04.DT1" procOut1.txt
call conda activate capstone
python python\plotgpr.py
call conda deactivate