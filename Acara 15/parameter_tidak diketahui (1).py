def salam (*nama):
    i=0
    print ('Halo ', end='')
    while len (nama) > i:
        print (nama[i], end=',')
        i+=1    

salam ('Kaoruko','Subaru','Madoka') 
salam ('Kaoruko','Subaru','Madoka', 'Waguri') 