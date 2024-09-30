import streamlit as st

# Sample data for demonstration purposes
startups = [
    {"name": "Startup A", "industry": "Tech", "location": "San Francisco"},
    {"name": "Startup B", "industry": "Health", "location": "New York"},
    {"name": "Startup C", "industry": "Finance", "location": "London"},
]

def main():
    st.title("Y Combinator Startups Directory")
    
    # Sidebar filters
    industry_filter = st.sidebar.selectbox("Select Industry", ["All"] + list(set([s["industry"] for s in startups])))
    location_filter = st.sidebar.selectbox("Select Location", ["All"] + list(set([s["location"] for s in startups])))

    # Filter startups based on user selection
    filtered_startups = [
        s for s in startups
        if (industry_filter == "All" or s["industry"] == industry_filter) and
           (location_filter == "All" or s["location"] == location_filter)
    ]

    # Display the filtered startups
    for startup in filtered_startups:
        st.write(f"**{startup['name']}**")
        st.write(f"Industry: {startup['industry']}")
        st.write(f"Location: {startup['location']}")
        st.write("---")

if __name__ == "__main__":
    main()
