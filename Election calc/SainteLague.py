class SainteLague():
    # Q=V/(2*S+1)
    def formula(self,votes,seats_thus_far):
        quotient = votes / (2*seats_thus_far+1)
        return quotient