class SainteLague():
    # Q=V/(2*S+1)
    def formula(self,votes,seats_thus_far):
        divisor = 2*seats_thus_far+1
        quotient = votes/divisor
        return quotient