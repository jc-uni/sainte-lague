from SainteLague import SainteLague
from SainteLagueMod import SainteLagueMod
from ElectoralThreshold import FourPercent


# This code does not take electoral districts into account
def main():
    # SL = SainteLague()
    SLM = SainteLagueMod()
    LS = FourPercent() #Levelling Seats

    # name:[total votes, seats granted, quotient]
    voting_result_2021 = {"r": [140931, 0, 0], "sv": [228063, 0, 0], "ap": [783394, 0, 0], "sp": [402961, 0, 0], "mdg": [117647, 0, 0], "krf": [113344, 0, 0], "v": [137433, 0, 0], "h": [607316, 0, 0], "frp": [346474, 0, 0], "pf": [4950, 0, 0], "lib": [4520, 0, 0], "fnb": [3435, 0, 0], "a": [2489, 0, 0], "pp": [2308, 0, 0], "nkp": [301, 0, 0], "fi": [275, 0, 0], "kp": [171, 0, 0], "gp": [199, 0, 0], "rn": [97, 0, 0], "dik": [34068, 0, 0], "pep": [19006, 0, 0], "pdk": [10448, 0, 0], "ion": [10031, 0, 0], "ps": [7836, 0, 0], "hp": [6490, 0, 0]}
    
    sum_votes = count_total_votes(voting_result_2021) + 19103 #blanks
    print("A total of " , sum_votes, " votes in 2021")

    for i in range(150):
        voting_result_2021 = SLM.voting_round(voting_result_2021)
    
    print("Election result before levelling seats")
    for party in voting_result_2021:
        print(party,": ",voting_result_2021[party][1]," seats")

    print("Election result after levelling seats")

    # Only a select group qualifies for levelling seats. In this group, seats are distributed as per first round.
    parties_qualified_for_levelling_seats = {}
    for party in voting_result_2021:
        if LS.is_party_qualified_for_leveling_seats(voting_result_2021[party][0],sum_votes):
            parties_qualified_for_levelling_seats.update({party: voting_result_2021[party]})
     
    for x in range(19):
        parties_qualified_for_levelling_seats = SLM.voting_round(parties_qualified_for_levelling_seats)
    
    voting_result_2021.update(parties_qualified_for_levelling_seats)
    for party in voting_result_2021:
        print(party,": ",voting_result_2021[party][1]," seats")


def count_total_votes(votes):
    total_votes = 0

    for element in votes:
        total_votes += votes[element][0]

    return total_votes    
        

if __name__ == "__main__":
    main()