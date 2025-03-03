def writesome(list_of_elements):
    with open("c:/Users/kadae/Desktop/python/all_labs_pp2/lab6/examples/example.txt", '+a') as f:
        text = "\n"
        for i in list_of_elements:
            text+=str(i)+' '
        f.write(text)
        f.close()
    
 

writesome([12345, 56789, 90987654, "dfghjkl","efrgf",34,34])