class SainteLagueMod():
    # Q=V/(2*S+1), if S==0 -> Q=V/(1.4)
    def formula(self,votes,seats_thus_far):
        if(seats_thus_far == 0)
            quotient = votes/1.4
        else 
            quotient = votes / (2*seats_thus_far+1)

        return quotient

