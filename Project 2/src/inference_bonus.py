import fuzzification_bonus

def rules(d): 
    high = []
    medium = []
    low = []
    


    high.append(fuzzification_bonus.d_C_fuzzy().d_C_dic(d)['far'])
    medium.append(fuzzification_bonus.d_C_fuzzy().d_C_dic(d)['moderate'])
    low.append(fuzzification_bonus.d_C_fuzzy().d_C_dic(d)['close'])
    


    output=dict(
        outputspeed_high=max(high),
        outputspeed_medium=max(medium),
        outputspeed_low=max(low)
        #high = high,
        #low = low,
        #medium=medium
    )
    return output







       