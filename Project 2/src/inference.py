import fuzzification

def rules(d_R, d_L): 
    high_right = []
    low_right = []
    nothing = []
    low_left = []
    high_left= []


    high_right.append(min(fuzzification.d_R_fuzzy().d_R_dic(d_R)['far_R'], fuzzification.d_L_fuzzy().d_L_dic(d_L)['close_L']))
    low_right.append(min(fuzzification.d_R_fuzzy().d_R_dic(d_R)['moderate_R'], fuzzification.d_L_fuzzy().d_L_dic(d_L)['close_L']))
    nothing.append(min(fuzzification.d_R_fuzzy().d_R_dic(d_R)['moderate_R'], fuzzification.d_L_fuzzy().d_L_dic(d_L)['moderate_L']))
    low_left.append(min(fuzzification.d_R_fuzzy().d_R_dic(d_R)['close_R'], fuzzification.d_L_fuzzy().d_L_dic(d_L)['moderate_L']))
    high_left.append(min(fuzzification.d_R_fuzzy().d_R_dic(d_R)['close_R'], fuzzification.d_L_fuzzy().d_L_dic(d_L)['far_L']))


    output=dict(
        outputroll_high_right=max(high_right),
        outputroll_low_right=max(low_right),
        outputroll_nothing=max(nothing),
        outputroll_low_left=max(low_left),
        outputroll_high_left=max(high_left)
    )
    return output







       