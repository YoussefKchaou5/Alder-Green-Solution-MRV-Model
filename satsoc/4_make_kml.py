import pandas as pd
import simplekml
import os
folder_path = r"C:\Users\Youss\satsoc\locations data"

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    df = pd.read_csv(file_path)
    lats = list(df["Y"])
    longs = list(df["X"])
    coordinates = []

    for i in range(len(lats)):
        coordinates.append((lats[i], longs[i]))

    min_lat, min_lon = min(coordinates, key=lambda x: x[0])[0], min(coordinates, key=lambda x: x[1])[1]
    max_lat, max_lon = max(coordinates, key=lambda x: x[0])[0], max(coordinates, key=lambda x: x[1])[1]

    kml = simplekml.Kml()
    polygon = kml.newpolygon(name="Bounding Rectangle",
                            outerboundaryis=[(min_lon, min_lat), (max_lon, min_lat), (max_lon, max_lat),
                                            (min_lon, max_lat), (min_lon, min_lat)])
   
    kml.save(fr"C:\Users\Youss\satsoc\kml\kml{filename}.kml")
    print(f"{filename}.kml is saved")