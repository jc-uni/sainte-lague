from SainteLague import SainteLague

def main():
    SL = SainteLague()


    voting_result_2021 = {"r": 140931, "sv": 228063, "ap": 783394, "sp": 402961, "mdg": 117647, "krf": 113344, "v": 137433, "h": 607316, "frp": 346474, "p": 4950}

    print(voting_result_2021)

    for element in voting_result_2021.values():
        print(SL.formula(element,0))
        

if __name__ == "__main__":
    main()