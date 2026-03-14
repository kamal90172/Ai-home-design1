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
