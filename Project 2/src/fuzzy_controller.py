import fuzzification
import defuzzification
import inference



class FuzzyController:
    """
    #todo
    write all the fuzzify,inference,defuzzify method in this class
    """

    def __init__(self):
        pass


    def decide(self, left_dist,right_dist):
        """
        main method for doin all the phases and returning the final answer for rotation
        """

        output=inference.rules(right_dist, left_dist)
        
        #print("ouuuttttpuuuttt")
        #print(output)
        
        rotation = defuzzification.defuzzification(output)
        
        return rotation

        
    