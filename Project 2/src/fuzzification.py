class d_R_fuzzy:
    
    def __init__(self):
        pass
    
    def close_R(self,x):
        if 0 <= x <50:
            return (50-x)/50
        else:
            return 0
        

    def moderate_R(self,x):
        if 35 <= x <=50:
            return (x-35)/15
        elif 50 < x <=65:
            return (65-x)/15
        else:
            return 0
        

    def far_R(self,x):
        if 50 <= x <=100:
            return (x-50)/100
        else:
            return 0
        

        
        
    def d_R_dic(self , x):
        
        return dict(close_R=self.close_R(x),moderate_R=self.moderate_R(x) ,far_R= self.far_R(x))






class d_L_fuzzy:
    
    def __init__(self):
        pass
    
    def close_L(self,x):
        if 0 <= x <50:
            return (50-x)/50
        else:
            return 0
        

    def moderate_L(self,x):
        if 35 <= x <=50:
            return (x-35)/15
        elif 50 < x <=65:
            return (65-x)/15
        else:
            return 0
        

    def far_L(self,x):
        if 50 <= x <=100:
            return (x-50)/100
        else:
            return 0
        

        
        
    def d_L_dic(self , x):
        
        return dict(close_L=self.close_L(x),moderate_L=self.moderate_L(x) ,far_L= self.far_L(x))





class output_fuzzy:
    
    def __init__(self):
        pass
    def o_high_right(x):
        if -50 <= x < -20:
            return (x+50)/30
        elif -20 <= x < -5:
            return (-5-x)/15
        else:
            return 0


    def o_low_right(x):
        if -20 <= x < -10:
            return (x+20)/10
        elif -10 <= x < 0:
            return (-x)/10
        else:
            return 0


    def o_nothing(x):
        if -10 <= x < 0:
            return (x+10)/10
        elif 0 <= x < 10:
            return (10-x)/10
        else:
            return 0


    def o_low_left(x):
        if 0 <= x < 10:
            return (x)/10
        elif 10 <= x < 20:
            return (20-x)/10
        else:
            return 0


    def o_high_left(x):
        if 5 <= x < 20:
            return (x-5)/15
        elif 20 <= x < 50:
            return (50-x)/30
        else:
            return 0


    def output_dic(x):
        output = {
            'high_right': o_high_right(x),
            'low_right': o_low_right(x),
            'nothing': o_nothing(x),
            'low_left': o_low_left(x),
            'high_left': o_high_left(x)
        }
        return output


























