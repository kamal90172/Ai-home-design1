import streamlit as st

st.set_page_config(page_title="Smart Home Design", layout="wide")

st.title("🏗️ Advanced Smart Home Planner")
st.write("अपने प्लॉट की डिटेल्स भरें और प्रोफेशनल नक्शा व बजट देखें।")

# Sidebar for inputs
st.sidebar.header("🏠 प्लॉट की जानकारी")
length = st.sidebar.number_input("प्लॉट की लंबाई (फीट में)", min_value=10, value=35)
width = st.sidebar.number_input("प्लॉट की चौड़ाई (फीट में)", min_value=10, value=30)
floors = st.sidebar.selectbox("कितने फ्लोर?", [1, 2, 3])

area = length * width

# Budget Calculation Logic
st.subheader("💰 निर्माण लागत का अनुमान (Estimated Budget)")
rate_per_sqft = 1600 # Average rate in Haryana/North India
total_cost = area * floors * rate_per_sqft

col1, col2, col3 = st.columns(3)
col1.metric("कुल एरिया", f"{area} Sq.Ft")
col2.metric("अनुमानित बजट", f"₹{total_cost:,}")
col3.metric("मैटेरियल क्वालिटी", "A-Grade")

# Simple 2D Map Visualization
st.subheader("🗺️ प्रस्तावित लेआउट (Provisional Map)")
# यहाँ हम एक बॉक्स बनाकर दिखा रहे हैं जो प्लॉट को दर्शाता है
st.markdown(f"""
<div style="border: 5px solid #4CAF50; width: {width*5}px; height: {length*5}px; background-color: #f1f1f1; display: flex; align-items: center; justify-content: center; border-radius: 10px;">
    <p style="text-align: center;"><b>{width}' x {length}' का प्लॉट</b><br>सामने का हिस्सा (Front)</p>
</div>
""", unsafe_allow_html=True)

st.info("नोट: यह एक ऑटो-जेनरेटेड अनुमान है। असली निर्माण से पहले इंजीनियर से सलाह लें।")
