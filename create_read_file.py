try:
    with open("metal_music.txt", "w") as fileWrite:
        fileWrite.writelines(["\nHeavy metal is a genre of rock music that developed in the late 1960s and early 1970s.", "\nMetalcore is a fusion music genre that combines elements of heavy metal and hardcore punk.", "\nNu metal bands have drawn elements and influences from a variety of musical styles."])
        print("File successfully created.")

    with open("metal_music.txt", "r") as fileRead:
        data1 = fileRead.readlines()
        for line1 in data1:
            print(line1)

except Exception as e:
    print("Error: " +str(e))
