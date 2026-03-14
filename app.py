import streamlit as st

def main():
    st.title("🏡 AI इंटरैक्टिव होम डिज़ाइन")
    st.write("अपने घर की जानकारी भरें और अपना 2D मैप देखें।")

    # 1. चारों दिशाओं की माप
    st.header("1. प्लॉट की माप (फीट में)")
    col1, col2 = st.columns(2)
    with col1:
        front = st.number_input("फ्रेंट (Front)", min_value=1.0, value=30.0)
        left = st.number_input("बाईं साइड (Left)", min_value=1.0, value=50.0)
    with col2:
        back = st.number_input("पीछे का हिस्सा (Back)", min_value=1.0, value=30.0)
        right = st.number_input("दाईं साइड (Right)", min_value=1.0, value=50.0)

    # 2. कस्टमाइजेशन (सवालात)
    st.header("2. फ्लोर कस्टमाइजेशन")
    
    tab1, tab2 = st.tabs(["ग्राउंड फ्लोर", "फर्स्ट फ्लोर"])
    
    with tab1:
        g_rooms = st.slider("कितने बेडरूम चाहिए?", 1, 5, 2)
        g_bath = st.slider("कितने बाथरूम चाहिए?", 1, 4, 1)
        g_store = st.selectbox("कितने स्टोर रूम?", [0, 1, 2])
        entrance = st.selectbox("मेन एंट्रेंस की दिशा", ["उत्तर (North)", "दक्षिण (South)", "पूर्व (East)", "पश्चिम (West)"])

    with tab2:
        f_rooms = st.slider("फर्स्ट फ्लोर पर बेडरूम?", 0, 5, 1)
        balcony = st.radio("क्या बालकनी चाहिए?", ["हाँ", "नहीं"])

    # 3. 2D मैप जनरेट करना (SVG का उपयोग करके)
    if st.button("अपना होम डिज़ाइन जनरेट करें"):
        st.success("डिज़ाइन तैयार है!")
        
        # स्केल सेट करना (1 फीट = 5 पिक्सल)
        w = front * 5
        h = left * 5
        
        # एक साधारण नक्शा दिखाना (SVG तकनीक)
        svg_code = f"""
        <svg width="{w+40}" height="{h+40}" style="border:2px solid black; background: #f9f9f9;">
            <rect x="20" y="20" width="{w}" height="{h}" fill="none" stroke="blue" stroke-width="3" />
            <text x="{w/2}" y="15" fill="black" font-size="12">Front: {front} ft</text>
            <text x="0" y="{h/2}" fill="black" font-size="12" transform="rotate(-90 10,{h/2})">Side: {left} ft</text>
            <text x="{w/4}" y="{h/2}" fill="gray" font-size="14">AI Plan: {g_rooms}BHK + {g_store} Store</text>
        </svg>
        """
        st.write("### आपका 2D मैप लेआउट:")
        st.components.v1.html(svg_code, height=h+100)

        # सारांश
        st.info(f"नोट: आपकी मुख्य एंट्री {entrance} की दिशा में रखी गई है।")

if __name__ == "__main__":
    main()

import streamlit as st

def main():
    st.set_page_config(page_title="Advanced AI Architect", layout="wide")
    st.title("🏡 एडवांस ऑटोमैटिक होम डिज़ाइनर")

    # 1. इनपुट सेक्शन
    with st.sidebar:
        st.header("📏 प्लॉट की जानकारी")
        front = st.number_input("फ्रेंट (Front in ft)", value=35.0)
        side = st.number_input("गहराई (Side in ft)", value=32.0)
        
        st.header("🛏️ ज़रूरतें")
        rooms = st.slider("बेडरूम की संख्या", 1, 4, 3)
        bathrooms = st.slider("बाथरूम की संख्या", 1, 3, 1)
        store = st.checkbox("स्टोर रूम चाहिए?", value=True)
        entrance = st.selectbox("मेन गेट", ["North", "South", "East", "West"])

    # 2. नक्शा बनाने का लॉजिक (SVG)
    if st.button("सटीक 2D नक्शा जनरेट करें"):
        scale = 10 # 1 ft = 10 pixels
        w, h = front * scale, side * scale
        
        # कमरों का साइज (एक औसत साइज)
        room_w, room_h = (front/2.5) * scale, (side/2.5) * scale
        
        svg = f"""
        <svg width="{w+50}" height="{h+50}" style="background:#ffffff; border:3px solid #333;">
            <rect x="25" y="25" width="{w}" height="{h}" fill="none" stroke="black" stroke-width="5" />
            
            <rect x="25" y="25" width="{room_w}" height="{room_h}" fill="#e3f2fd" stroke="black" stroke-width="2" />
            <text x="{30}" y="{50}" font-family="Arial" font-size="12">Master Bedroom</text>
            
            <rect x="{25 + room_w}" y="25" width="{room_w}" height="{room_h}" fill="#f1f8e9" stroke="black" stroke-width="2" />
            <text x="{30 + room_w}" y="{50}" font-family="Arial" font-size="12">Bedroom 2</text>
        """
        
        # स्टोर रूम का लॉजिक
        if store:
            svg += f"""
            <rect x="25" y="{25 + room_h}" width="{room_w/2}" height="{room_h/2}" fill="#fff3e0" stroke="black" stroke-width="2" />
            <text x="30" y="{45 + room_h}" font-family="Arial" font-size="10">Store</text>
            """
            
        # बाथरूम का लॉजिक
        svg += f"""
        <rect x="{25 + room_w/2}" y="{25 + room_h}" width="{room_w/2}" height="{room_h/2}" fill="#f3e5f5" stroke="black" stroke-width="2" />
        <text x="{30 + room_w/2}" y="{45 + room_h}" font-family="Arial" font-size="10">Bath</text>
        """

        # हॉल/लिविंग एरिया
        svg += f"""
        <text x="{w/2}" y="{h-30}" font-family="Arial" font-size="16" font-weight="bold" fill="darkblue">Drawing/Living Area</text>
        <text x="{w/2}" y="{h+10}" font-family="Arial" font-size="12">Main Entrance: {entrance}</text>
        </svg>
        """

        st.write("### आपका कस्टमाइज्ड फ्लोर प्लान:")
        st.components.v1.html(svg, height=h+100)
        st.info("यह एक ऑटो-जनरेटेड लेआउट है। इसमें आप कमरों की जगह को अपने हिसाब से कोडिंग में बदल सकते हैं।")

if __name__ == "__main__":
    main()
