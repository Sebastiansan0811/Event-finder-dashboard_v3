
import streamlit as st
import pandas as pd
from datetime import date

# Sample data for demonstration
data = [
    {
        "Event Name": "MassBUYS Expo 2025",
        "Date": "2025-04-10",
        "Region": "Central MA",
        "Event Type": "Government Procurement",
        "Exhibitor Opportunities": "Available",
        "Address": "DCU Center, Worcester, MA",
        "Avg Exhibitor Cost": "$500",
        "Avg Attendance & Demographics": "1,200 attendees; public sector, nonprofits"
    },
    {
        "Event Name": "Swampscott Garden Art Walk",
        "Date": "2025-06-28",
        "Region": "North Shore",
        "Event Type": "Community Art",
        "Exhibitor Opportunities": "Sponsorships",
        "Address": "Downtown Swampscott, MA",
        "Avg Exhibitor Cost": "Donation-based",
        "Avg Attendance & Demographics": "300 attendees; families, local artists"
    },
    {
        "Event Name": "Massachusetts Agricultural Fair",
        "Date": "2025-09-15",
        "Region": "Western MA",
        "Event Type": "Agriculture & Community",
        "Exhibitor Opportunities": "Available",
        "Address": "Franklin County Fairgrounds, Greenfield, MA",
        "Avg Exhibitor Cost": "$150",
        "Avg Attendance & Demographics": "5,000 attendees; youth, farmers, Latinx"
    }
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Streamlit App
st.set_page_config(page_title="Massachusetts Event Finder", layout="wide")
st.title("📅 Massachusetts Event Finder Dashboard")

# Sidebar Filters
st.sidebar.header("Filter Events")

regions = st.sidebar.multiselect("Select Region(s):", options=df["Region"].unique(), default=df["Region"].unique())
event_types = st.sidebar.text_input("Event Type Keyword:")
exhibitor_filter = st.sidebar.selectbox("Exhibitor Opportunities:", options=["All", "Available", "Sponsorships", "Not Available"])
start_date = st.sidebar.date_input("Start Date", value=date(2025, 1, 1))
end_date = st.sidebar.date_input("End Date", value=date(2025, 12, 31))

# Filter Logic
filtered_df = df[
    df["Region"].isin(regions) &
    df["Date"].between(str(start_date), str(end_date))
]

if event_types:
    filtered_df = filtered_df[filtered_df["Event Type"].str.contains(event_types, case=False)]

if exhibitor_filter != "All":
    filtered_df = filtered_df[filtered_df["Exhibitor Opportunities"] == exhibitor_filter]

# Display Table
st.subheader("🎪 Upcoming Events")
st.dataframe(filtered_df.reset_index(drop=True), use_container_width=True)
