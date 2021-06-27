import pandas as pd

data = {
    "player" : ["Curry", "Le Bron", "Campazo", "Ginobilli"],
    "minutes_season" : ["436", "235", "810", "960"],
    "faults_season" : ["36", "21", "55", "76"],
}
frame = pd.DataFrame(data)
frame["score"] = [34, 56, 89, 123]
print(frame)