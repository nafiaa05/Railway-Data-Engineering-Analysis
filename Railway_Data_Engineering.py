import pandas as pd
import matplotlib.pyplot as plt

# ==========================
# Load Dataset
# ==========================

df = pd.read_csv("../Dataset/Railway_info.csv")

print("First 10 Rows:")
print(df.head(10))

print("\nDataset Information:")
df.info()

print("\nMissing Values:")
print(df.isnull().sum())

# ==========================
# Basic Statistics
# ==========================

total_trains = df["Train_No"].count()
print("\nTotal Number of Trains:", total_trains)

unique_source = df["Source_Station_Name"].nunique()
print("Unique Source Stations:", unique_source)

unique_destination = df["Destination_Station_Name"].nunique()
print("Unique Destination Stations:", unique_destination)

print("\nMost Common Source Station:")
print(df["Source_Station_Name"].value_counts().head(1))

print("\nMost Common Destination Station:")
print(df["Destination_Station_Name"].value_counts().head(1))

# ==========================
# Data Cleaning
# ==========================

df = df.dropna()

print("\nMissing values handled successfully.")

df["Source_Station_Name"] = df["Source_Station_Name"].str.upper()
df["Destination_Station_Name"] = df["Destination_Station_Name"].str.upper()

print("Station names converted to uppercase successfully.")

print("\nCleaned Dataset:")
print(df.head(10))

# ==========================
# Data Filtering
# ==========================

saturday_trains = df[df["days"] == "Saturday"]

print("\nNumber of Saturday Trains:", len(saturday_trains))
print(saturday_trains.head(10))

source_station_df = df[df["Source_Station_Name"] == "CST-MUMBAI"]

print("\nNumber of trains starting from CST-MUMBAI:", len(source_station_df))
print(source_station_df.head(10))

# ==========================
# Grouping and Aggregation
# ==========================

station_count = (
    df.groupby("Source_Station_Name")
      .size()
      .reset_index(name="Number_of_Trains")
)

print("\nNumber of Trains from Each Source Station:")
print(station_count.head(10))

average_trains = (
    df.groupby(["Source_Station_Name", "days"])
      .size()
      .groupby(level=0)
      .mean()
      .reset_index(name="Average_Trains_Per_Day")
)

print("\nAverage Trains Per Day:")
print(average_trains.head(10))

# ==========================
# Data Enrichment
# ==========================

def categorize_day(day):
    if day in ["Saturday", "Sunday"]:
        return "Weekend"
    return "Weekday"

df["Day_Category"] = df["days"].apply(categorize_day)

print("\nDay Category Count:")
print(df["Day_Category"].value_counts())

# ==========================
# Pattern Analysis
# ==========================

day_order = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

day_distribution = df["days"].value_counts().reindex(day_order)

print("\nDistribution of Train Journeys:")
print(day_distribution)

plt.figure(figsize=(8,5))

day_distribution.plot(
    kind="bar",
    color="orange",
    edgecolor="black"
)

plt.title("Distribution of Train Journeys Throughout the Week", fontsize=14, fontweight="bold")
plt.xlabel("Days")
plt.ylabel("Number of Trains")

plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()

# ==========================
# Top Source Stations
# ==========================

top_source = df["Source_Station_Name"].value_counts().head(10)

print("\nTop 10 Source Stations:")
print(top_source)

plt.figure(figsize=(10,5))

top_source.plot(
    kind="bar",
    color="purple",
    edgecolor="black"
)

plt.title("Top 10 Source Stations", fontsize=14, fontweight="bold")
plt.xlabel("Source Stations")
plt.ylabel("Number of Trains")

plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()

# ==========================
# Top Destination Stations
# ==========================

top_destination = df["Destination_Station_Name"].value_counts().head(10)

print("\nTop 10 Destination Stations:")
print(top_destination)

plt.figure(figsize=(10,5))

top_destination.plot(
    kind="bar",
    color="green",
    edgecolor="black"
)

plt.title("Top 10 Destination Stations", fontsize=14, fontweight="bold")
plt.xlabel("Destination Stations")
plt.ylabel("Number of Trains")

plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()

# ==========================
# Correlation and Insights
# ==========================

train_per_day = df["days"].value_counts().reindex(day_order)

print("\nNumber of Trains by Operating Day:")
print(train_per_day)

plt.figure(figsize=(8,5))

train_per_day.plot(
    kind="bar",
    color="hotpink",
    edgecolor="black"
)

plt.title("Number of Trains by Operating Day", fontsize=14, fontweight="bold")
plt.xlabel("Days")
plt.ylabel("Number of Trains")

plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()

# ==========================
# Project Completed
# ==========================

print("\n======================================")
print(" Railway Data Engineering Project")
print(" Successfully Completed")
print("======================================")