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
