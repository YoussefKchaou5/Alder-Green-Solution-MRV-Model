import pandas as pd

complete_df = pd.read_csv("complete.csv")
flatland_df = complete_df[(complete_df["sample_depth_min"] == 0)].drop(columns="sample_depth_min")
flatland_df.to_csv("flatland.csv", index=False)