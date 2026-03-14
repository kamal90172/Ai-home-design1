import streamlit as st

# ऐप का मुख्य टाइटल
st.set_page_config(page_title="Smart Home Designer", layout="wide")
st.title("🏗️ Smart Home Design & Budget Estimator")
st.write("अपने प्लॉट की डिटेल्स भरें और तुरंत नक्शा व बजट पाएं।")

# --- स्टेप 1: इनपुट सेक्शन ---
st.sidebar.header("🏠 प्लॉट और यूजर की पसंद")
length = st.sidebar.number_input("प्लॉट की लंबाई (फीट में)", value=35)
width = st.sidebar.number_input("प्लॉट की चौड़ाई (फीट में)", value=30)
direction = st.sidebar.selectbox("प्लॉट का मुख (Facing)", ["North", "South", "East", "West"])
vastu_on = st.sidebar.toggle("वास्तु शास्त्र (Vastu) लागू करें", value=True)

st.sidebar.divider()
floors = st.sidebar.multiselect("कितने फ्लोर बनाने हैं?", ["Ground Floor", "First Floor", "Second Floor"], default=["Ground Floor"])

# --- स्टेप 2: नक्शा और लेआउट लॉजिक ---
st.subheader("📋 आपके घर का प्रस्तावित लेआउट")

floor_data = {}
for floor in floors:
    with st.expander(f"📍 {floor} की सेटिंग्स", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            bhk = st.slider(f"{floor} में कमरों की संख्या (BHK)", 1, 5, 3)
        with col2:
            extras = st.multiselect(f"{floor} में अतिरिक्त क्या चाहिए?", ["Store Room", "Pooja Room", "Study Room", "Attached Bath"], key=floor)
        floor_data[floor] = {"BHK": bhk, "Extras": extras}

if st.button("नक्शा और खर्च कैलकुलेट करें"):
    st.divider()
    
    # लेआउट डिस्प्ले
    c1, c2 = st.columns(2)
    with c1:
        st.info(f"📐 प्लॉट एरिया: {length * width} Sq. Ft.")
        if vastu_on:
            st.success("✅ वास्तु के अनुसार: मुख्य दरवाजा उत्तर/पूर्व में, किचन दक्षिण-पूर्व में और बेडरूम दक्षिण-पश्चिम में रखें।")
        else:
            st.warning("⚠️ सामान्य लेआउट: बिना वास्तु के अधिकतम जगह का उपयोग किया गया है।")
    
    # --- स्टेप 3: बजट कैलकुलेटर ---
    with c2:
        total_sqft = length * width * len(floors)
        st.metric("कुल कंस्ट्रक्शन एरिया", f"{total_sqft} Sq. Ft.")

    st.subheader("💰 निर्माण सामग्री का अनुमानित खर्च")
    
    # कैलकुलेशन लॉजिक (बेसिक मानक)
    cement_bags = total_sqft * 0.45
    steel_kg = total_sqft * 4.5
    bricks = total_sqft * 22
    sand_cuft = total_sqft * 1.8
    
    # टेबल डिस्प्ले
    st.table({
        "सामग्री (Material)": ["सीमेंट (Cement)", "सरिया (Steel)", "ईंटें (Bricks)", "रेत (Sand/Bajri)"],
        "मात्रा (Quantity)": [f"{int(cement_bags)} बैग", f"{int(steel_kg)} किलो", f"{int(bricks)} पीस", f"{int(sand_cuft)} घन फीट"],
        "अनुमानित रेट (औसत)": ["₹400 /बैग", "₹70 /किलो", "₹8 /पीस", "₹60 /फीट"]
    })
    
    total_cost = (cement_bags * 400) + (steel_kg * 70) + (bricks * 8) + (sand_cuft * 60)
    st.error(f"### कुल अनुमानित बजट: ₹{int(total_cost):,}")
    st.caption("*यह खर्च केवल एक अनुमान है, लेबर और फिनिशिंग के हिसाब से बदल सकता है।")

