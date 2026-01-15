import pandas as pd
import folium
from folium.plugins import HeatMap, MarkerCluster

# Load data
df = pd.read_csv("Crime_Data_2023_-_Part_1_Offenses_(With_Lat_&_Long_Info).csv")
df = df.dropna(subset=['Latitude', 'Longitude'])

# Map center (Syracuse area)
m = folium.Map(location=[43.0481, -76.1474], zoom_start=12)

# Add heatmap
heat_data = df[['Latitude', 'Longitude']].values.tolist()
HeatMap(heat_data, radius=10).add_to(m)

# Save HTML map
m.save("syracuse_crime_heatmap.html")

# MarkerCluster
mc = MarkerCluster()
for idx, row in df.iterrows():
    mc.add_child(folium.Marker(location=[row['Latitude'], row['Longitude']],
                               popup=row.get("CODE_DEFINED", "Crime Event")))
m2 = folium.Map(location=[43.0481, -76.1474], zoom_start=12)
mc.add_to(m2)
m2.save("syracuse_crime_cluster_map.html")