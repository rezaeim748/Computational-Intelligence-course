from scipy.integrate import quad as q

def mohasebeantegral(mini , maxi ,a , b):
    step=0.0001
    i=mini
    n1=0
    nn1=0.0
    while i<maxi:
        n1+=(i*(a*i+b))*step
        nn1+=(a*i+b)*step
        i+=step
    return n1,nn1

def center_(output_):
    array1=[]
    array2=[]
    array3=[]
    n=0
    dn=0
    center = 30
    #فعال بودن 
    h = 0
    print(output_)
    if(output_['outputspeed_high']>0):
        array1=high_def(output_['outputspeed_high'])
        n+=array1[0]
        dn+=array1[1]
        #print("/////////////////////////")
        print(array1)
        h = 1
    if(output_['outputspeed_medium']>0):
        array2=medium_def(output_['outputspeed_medium'])
        n+=array2[0]
        dn+=array2[1]
        #print("/////////////////////////")
        print(array2)
        h = 1
    if(output_['outputspeed_low']>0):
        array3=low_def(output_['outputspeed_low'])
        n+=array3[0]
        dn+=array3[1]
        #print("/////////////////////////")
        print(array3)
        h = 1
    
    if (h != 0):
        center = 20 + n/dn
    
    
    #print(center)
    #print(n)
    #print(dn)
    
    return center


def high_def(value):
    #y=ax+b
    a1=1/5   #(1 - 0) / (30-0)
    b1= 0
    a2= -1/5 
    b2= 2
    
    #if value is 1 and all dagram compute for defuzzy
    if(value==1):
        n1,dn1=mohasebeantegral(0, 5, a1, b1)
        n2,dn2=mohasebeantegral(5, 10, a2, b2)
        return (n1+n2),(dn1+dn2)
       
    else:
        n1,dn1=mohasebeantegral(0, (value-b1)/a1 , a1, b1)
        n2,dn2=mohasebeantegral((value-b2)/a2 , 10 , a2, b2)
        n3,dn3=mohasebeantegral((value-b1)/a1 ,(value-b2)/a2 , 0 , value)
        return (n1+n2+n3),(dn1+dn2+dn3)

def medium_def(value):
    #y=ax+b
    a1=1/15  
    b1= 0
    a2= -1/15
    b2= 2
    
    #if value is 1 and all dagram compute for defuzzy
    if(value==1):
        n1,dn1=mohasebeantegral(0, 15, a1, b1)
        n2,dn2=mohasebeantegral(15, 30, a2, b2)
        return (n1+n2),(dn1+dn2)
       
    else:
        n1,dn1=mohasebeantegral(0, (value-b1)/a1 , a1, b1)
        n2,dn2=mohasebeantegral((value-b2)/a2 , 30 , a2, b2)
        n3,dn3=mohasebeantegral((value-b1)/a1 ,(value-b2)/a2 , 0 , value)
        return (n1+n2+n3),(dn1+dn2+dn3)

def low_def(value):
    #y=ax+b
    a1=1/5   
    b1= -5
    a2= -1/60
    b2= 3/2
    
    #if value is 1 and all dagram compute for defuzzy
    if(value==1):
        n1,dn1=mohasebeantegral(25, 30, a1, b1)
        n2,dn2=mohasebeantegral(30, 90, a2, b2)
        return (n1+n2),(dn1+dn2)
       
    else:
        n1,dn1=mohasebeantegral(25, (value-b1)/a1 , a1, b1)
        n2,dn2=mohasebeantegral((value-b2)/a2 , 90 , a2, b2)
        n3,dn3=mohasebeantegral((value-b1)/a1 ,(value-b2)/a2 , 0 , value)
        return (n1+n2+n3),(dn1+dn2+dn3)




def defuzzification(output_):
    center=center_(output_)
    return center












