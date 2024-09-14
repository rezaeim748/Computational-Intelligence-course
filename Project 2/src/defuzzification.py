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
    array4=[]
    array5=[]
    n=0
    dn=0
    center = 0
    #فعال بودن 
    if(output_['outputroll_high_right']>0):
        array1=high_right_def(output_['outputroll_high_right'])
        n+=array1[0]
        dn+=array1[1]
        print(array1)
    if(output_['outputroll_low_right']>0):
        array2=low_right_def(output_['outputroll_low_right'])
        n+=array2[0]
        dn+=array2[1]
        print(array2)
    if(output_['outputroll_nothing']>0):
        array3=nothing_def(output_['outputroll_nothing'])
        n+=array3[0]
        dn+=array3[1]
        print(array3)
    if(output_['outputroll_low_left']>0):
        array4=low_left_def(output_['outputroll_low_left'])
        n+=array4[0]
        dn+=array4[1]
        print(array4)
    if(output_['outputroll_high_left']>0):
        array5=high_left_def(output_['outputroll_high_left'])
        n+=array5[0]
        dn+=array5[1]
        print(array5)
        center += 4
        
    center += n/dn
    #print(center)
    #print(n)
    #print(dn)
    
    return center


def high_right_def(value):
    #y=ax+b
    a1=1/30   #(1 - 0) / (30-0)
    b1= 50/30
    a2= -1/15 
    b2= -5/15
    
    #if value is 1 and all dagram compute for defuzzy
    if(value==1):
        n1,dn1=mohasebeantegral(-50, -20, a1, b1)
        n2,dn2=mohasebeantegral(-20, -5, a2, b2)
        return (n1+n2),(dn1+dn2)
       
    else:
        n1,dn1=mohasebeantegral(-50, (value-b1)/a1 , a1, b1)
        n2,dn2=mohasebeantegral((value-b2)/a2 , -5 , a2, b2)
        n3,dn3=mohasebeantegral((value-b1)/a1 ,(value-b2)/a2 , 0 , value)
        return (n1+n2+n3),(dn1+dn2+dn3)

def low_right_def(value):
    #y=ax+b
    a1=1/10   
    b1= 2
    a2= -1/10
    b2= 0
    
    #if value is 1 and all dagram compute for defuzzy
    if(value==1):
        n1,dn1=mohasebeantegral(-20, -10, a1, b1)
        n2,dn2=mohasebeantegral(-10, 0, a2, b2)
        return (n1+n2),(dn1+dn2)
       
    else:
        n1,dn1=mohasebeantegral(-20, (value-b1)/a1 , a1, b1)
        n2,dn2=mohasebeantegral((value-b2)/a2 , 0 , a2, b2)
        n3,dn3=mohasebeantegral((value-b1)/a1 ,(value-b2)/a2 , 0 , value)
        return (n1+n2+n3),(dn1+dn2+dn3)

def nothing_def(value):
    #y=ax+b
    a1=1/10   
    b1= 1
    a2= -1/10
    b2= 1
    
    #if value is 1 and all dagram compute for defuzzy
    if(value==1):
        n1,dn1=mohasebeantegral(-10, 0, a1, b1)
        n2,dn2=mohasebeantegral(0, 10, a2, b2)
        return (n1+n2),(dn1+dn2)
       
    else:
        n1,dn1=mohasebeantegral(-10, (value-b1)/a1 , a1, b1)
        n2,dn2=mohasebeantegral((value-b2)/a2 , 10 , a2, b2)
        n3,dn3=mohasebeantegral((value-b1)/a1 ,(value-b2)/a2 , 0 , value)
        return (n1+n2+n3),(dn1+dn2+dn3)


def low_left_def(value):
    #y=ax+b
    a1=1/10   
    b1= 0
    a2= -1/10
    b2= 2
    
    #if value is 1 and all dagram compute for defuzzy
    if(value==1):
        n1,dn1=mohasebeantegral(0, 10, a1, b1)
        n2,dn2=mohasebeantegral(10, 20, a2, b2)
        return (n1+n2),(dn1+dn2)
       
    else:
        n1,dn1=mohasebeantegral(0, (value-b1)/a1 , a1, b1)
        n2,dn2=mohasebeantegral((value-b2)/a2 , 20 , a2, b2)
        n3,dn3=mohasebeantegral((value-b1)/a1 ,(value-b2)/a2 , 0 , value)
        return (n1+n2+n3),(dn1+dn2+dn3)


def high_left_def(value):
    #y=ax+b
    a1=1/15  
    b1= -5/15
    a2= -1/30
    b2= 50/30
    
    #if value is 1 and all dagram compute for defuzzy
    if(value==1):
        n1,dn1=mohasebeantegral(5, 20, a1, b1)
        n2,dn2=mohasebeantegral(20, 50, a2, b2)
        return (n1+n2),(dn1+dn2)
       
    else:
        n1,dn1=mohasebeantegral(5, (value-b1)/a1 , a1, b1)
        n2,dn2=mohasebeantegral((value-b2)/a2 , 50 , a2, b2)
        n3,dn3=mohasebeantegral((value-b1)/a1 ,(value-b2)/a2 , 0 , value)
        return (n1+n2+n3),(dn1+dn2+dn3)


def defuzzification(output_):
    center=center_(output_)
    return center












