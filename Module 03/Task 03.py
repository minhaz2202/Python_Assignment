# Hemoglobin level checker
gender = input ("Enter biological gender (male/female): ")
hemoglobin = int(input("Enter hemoglobin value (g/L): "))

if gender == "female":
    if hemoglobin < 117:
        print ("hemoglobin value is low.")
    elif hemoglobin > 155:
        print("hemoglobin value is high.")
    else :
        print("hemoglobin value is normal.")

elif gender == "male":
    if hemoglobin < 134:
        print ("hemoglobin value is low.")
    elif hemoglobin > 167:
        print("hemoglobin value is high.")
    else:
        print("hemoglobin value is normal.")

else:
    print("Error: Invalid gender entered.")
    exit()
