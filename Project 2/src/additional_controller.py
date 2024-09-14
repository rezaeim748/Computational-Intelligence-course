import defuzzification_bonus
import inference_bonus

class FuzzyGasController:
    """
    # emtiazi todo
    write all the fuzzify,inference,defuzzify method in this class
    """

    def __init__(self):
        pass
        

    def decide(self, center_dist):
        """
        main method for doin all the phases and returning the final answer for gas
        """
        output=inference_bonus.rules(center_dist)
        
        #print("ouuuttttpuuuttt")
        #print(output)
        
        speed = defuzzification_bonus.defuzzification(output)



        return speed

        #return 30
    