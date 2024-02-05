class SainteLagueMod():
    # Q=V/(2*S+1), if S==0 -> Q=V/(1.4)
    def formula(self,votes,seats_thus_far):
        if(seats_thus_far == 0):
            quotient = votes/1.4
        else: 
            quotient = votes / (2*seats_thus_far+1)

        return quotient

    def voting_round(self, voting_result):
        for party in voting_result:
            voting_result[party][2] = self.formula(voting_result[party][0],voting_result[party][1])
            # print(party, ": ",voting_result[party][2])
        
        voting_result = self.grant_seat(voting_result)
        return voting_result
    
    def grant_seat(self,voting_result):
        party_with_largest_quotient = list(voting_result.keys())[0] # the var needs to be a valid assignment before for loop
        # print("start: ",party_with_largest_quotient)

        for party in voting_result:
            # print(party)
            if voting_result[party][2] > voting_result[party_with_largest_quotient][2]:
                party_with_largest_quotient = party
        
        # print("end result: ",party_with_largest_quotient)
        voting_result[party_with_largest_quotient][1] += 1
        return voting_result