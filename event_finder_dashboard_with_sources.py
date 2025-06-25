
import streamlit as st
import pandas as pd
from datetime import datetime

# Sample event data with new columns including source links
data = [
    {
        "Event Name": "MassBUYS Expo 2025",
        "Date": "2025-04-15",
        "Region": "Central MA",
        "Event Type": "Government Procurement",
        "Exhibitor Opportunities": "Available",
        "Address": "DCU Center, Worcester, MA",
        "Average Cost to be an Exhibitor": "$500",
        "Average Attendance & Demographics": "1,000+ attendees, public sector, vendors",
        "Source": "https://www.mass.gov/info-details/massbuys-expo-2025"
    },
    {
        "Event Name": "Swampscott Garden Art Walk",
        "Date": "2025-06-28",
        "Region": "North Shore",
        "Event Type": "Community Art",
        "Exhibitor Opportunities": "Sponsorships",
        "Address": "Downtown Swampscott, MA",
        "Average Cost to be an Exhibitor": "Donation-based",
        "Average Attendance & Demographics": "300+ attendees, families, artists",
        "Source": "https://www.swampscottma.gov/home/news/swampscott-garden-art-walk-2025-1"
    },
    {
        "Event Name": "Barnstable County Fair",
        "Date": "2025-07-21",
        "Region": "Cape Cod",
        "Event Type": "Agricultural Fair",
        "Exhibitor Opportunities": "Available",
        "Address": "Barnstable County Fairgrounds, Falmouth, MA",
        "Average Cost to be an Exhibitor": "$250",
        "Average Attendance & Demographics": "10,000+ attendees, families, youth, Latinx",
        "Source": "https://www.capecodfairgrounds.com/events/barnstable-county-fair/"
    }
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Convert date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Streamlit app layout
st.set_page_config(page_title="Massachusetts Event Finder", layout="wide")
st.title("📅 Massachusetts Event Finder Dashboard")

# Sidebar filters
st.sidebar.header("Filter Events")
regions = st.sidebar.multiselect("Select Region(s)", options=df["Region"].unique(), default=list(df["Region"].unique()))
event_types = st.sidebar.multiselect("Select Event Type(s)", options=df["Event Type"].unique(), default=list(df["Event Type"].unique()))
exhibitor_options = st.sidebar.multiselect("Exhibitor Opportunities", options=df["Exhibitor Opportunities"].unique(), default=list(df["Exhibitor Opportunities"].unique()))
start_date = st.sidebar.date_input("Start Date", value=datetime(2025, 1, 1))
end_date = st.sidebar.date_input("End Date", value=datetime(2025, 12, 31))

# Filter data
filtered_df = df[
    (df["Region"].isin(regions)) &
    (df["Event Type"].isin(event_types)) &
    (df["Exhibitor Opportunities"].isin(exhibitor_options)) &
    (df["Date"] >= pd.to_datetime(start_date)) &
    (df["Date"] <= pd.to_datetime(end_date))
]

# Convert source links to clickable markdown
def make_clickable(link):
    return f"[Link]({link})"

filtered_df["Source"] = filtered_df["Source"].apply(make_clickable)

# Display filtered table
st.markdown("### Filtered Events")
st.write(filtered_df.to_markdown(index=False), unsafe_allow_html=True)
