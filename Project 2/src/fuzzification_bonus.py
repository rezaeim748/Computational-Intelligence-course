class d_C_fuzzy:
    
    def __init__(self):
        pass
    
    def close(self,x):
        if 0 <= x <50:
            return (50-x)/50
        else:
            return 0
        

    def moderate(self,x):
        if 40 <= x <=50:
            return (x-40)/10
        elif 50 < x <=100:
            return (100-x)/50
        else:
            return 0
        

    def far(self,x):
        if 90 <= x <=200:
            return (x-90)/110
        else:
            return 0
        

        
        
    def d_C_dic(self , x):
        
        return dict(close=self.close(x),moderate=self.moderate(x) ,far= self.far(x))









class output_fuzzy:
    
    def __init__(self):
        pass
    def o_low(x):
        if 0 <= x < 5:
            return (x)/5
        elif 5 <= x < 10:
            return (10-x)/5
        else:
            return 0


    def o_medium(x):
        if 0 <= x < 15:
            return (x)/15
        elif 15 <= x < 30:
            return (30-x)/15
        else:
            return 0


    def o_high(x):
        if 25 <= x < 30:
            return (x+10)/10
        elif 30 <= x < 90:
            return (90-x)/60
        else:
            return 0



    def output_dic(x):
        output = {
            'low': o_low(x),
            'medium': o_medium(x),
            'high': o_high(x)
        }
        return output


























