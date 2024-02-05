class FourPercent():
    def is_party_qualified_for_leveling_seats(self, party_votes, total_votes):
        if(party_votes/total_votes >= 0.04):
            return True
        else:
            return False
