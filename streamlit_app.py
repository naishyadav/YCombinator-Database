import streamlit as st
from PIL import Image

# Sample data for demonstration purposes
startups = [
    {"name": "Startup A", "industry": "Tech", "location": "San Francisco", "logo": "https://via.placeholder.com/150"},
    {"name": "Startup B", "industry": "Health", "location": "New York", "logo": "https://via.placeholder.com/150"},
    {"name": "Startup C", "industry": "Finance", "location": "London", "logo": "https://via.placeholder.com/150"},
]

def main():
    # Custom CSS for styling
    st.markdown("""
        <style>
        .startup-card {
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            padding: 20px;
            margin-bottom: 20px;
            background-color: #f9f9f9;
        }
        .startup-logo {
            width: 100%;
            border-radius: 10px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("🚀 Y Combinator Startups Directory")
    
    # Sidebar filters
    industry_filter = st.sidebar.selectbox("Select Industry", ["All"] + list(set([s["industry"] for s in startups])))
    location_filter = st.sidebar.selectbox("Select Location", ["All"] + list(set([s["location"] for s in startups])))

    # Filter startups based on user selection
    filtered_startups = [
        s for s in startups
        if (industry_filter == "All" or s["industry"] == industry_filter) and
           (location_filter == "All" or s["location"] == location_filter)
    ]

    # Display the filtered startups in a more interactive way
    for startup in filtered_startups:
        with st.container():
            col1, col2 = st.columns([1, 3])
            with col1:
                st.image(startup["logo"], use_column_width=True, caption=startup["name"], output_format="auto")
            with col2:
                st.markdown(f"<div class='startup-card'><h3>{startup['name']}</h3>", unsafe_allow_html=True)
                st.write(f"**Industry:** {startup['industry']}")
                st.write(f"**Location:** {startup['location']}")
                st.markdown("</div>", unsafe_allow_html=True)
                with st.expander("More Info"):
                    st.write("Additional details about the startup can go here.")

if __name__ == "__main__":
    main()
