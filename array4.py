import pandas as pd

users = {
    "player": ["lebron", "curry", "curry", "tatum", "ginobilli", "campazzo", "tatum","ginobilli", "curry", "lebrom", "lebron" ],
    "team": ["lakers", "miami", "clippers", "boston", "lakers", "miami", "clippers", "boston", "miami", "boston", "miami" ]
}

frame = pd.DataFrame(users)
frame["country"] = ["argentina", "brasil", "argentina", "chile", "uruguay", "argentina", "brasil", "peru", "argentina", "chile", "uruguay"]
print(frame)