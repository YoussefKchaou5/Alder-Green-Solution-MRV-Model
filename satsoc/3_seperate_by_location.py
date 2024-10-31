import pandas as pd

complete_df = pd.read_csv("flatland.csv")
for site, site_df in complete_df.groupby("site"):
    # Keep only the required columns for each site's DataFrame
    site_df_filtered = site_df[["location_id", "X", "Y", "SOCc"]]
    
    # Step 3: Save the DataFrame as a CSV file named after the site
    filename = fr"C:\Users\Youss\satsoc\locations data\{site}_data.csv"
    site_df_filtered.to_csv(filename, index=False)

    print(f"Saved {filename}")
