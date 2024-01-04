# Quick test to see if the data processing works since we don't have participant data yet

subjectid = ["1", "2", "3", "4", "5", "6", "7"]
dyadid = ["1", "1", "NA", "2", "2", "3", "3"]
paired = ["TRUE", "TRUE", "FALSE", "TRUE", "TRUE", "TRUE", "TRUE"]
condition = ["control", "control", "control", "intervention", "intervention", "intervention", "intervention"]
finished_demographics = ["True", "True", "True", "True", "True", "True", "False"]

for i in range (len(subjectIDs)):
    print(f"https://richmond.ca1.qualtrics.com/jfe/form/SV_5dOVnvtOliEnQCW?subjectid={subjectid[i]}&dyad_ID={dyadid[i]}&paired={paired[i]}&condition={condition[i]}&finished_demographics={finished_demographics[i]}")