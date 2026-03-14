import streamlit as st

def main():
    st.set_page_config(page_title="AI Smart Architect", layout="wide")
    st.title("🏗️ स्मार्ट ऑटोमैटिक होम डिज़ाइनर")
    st.write("यह AI आपके प्लॉट साइज के हिसाब से कमरों को खुद व्यवस्थित (Arrange) करेगा।")

    # इनपुट - आपसे सवाल पूछना
    with st.sidebar:
        st.header("📐 प्लॉट की पैमाइश")
        f = st.number_input("फ्रंट (फीट)", value=35.0)
        s = st.number_input("साइड/गहराई (फीट)", value=32.0)
        
        st.header("🏠 आपकी ज़रूरतें")
        n_rooms = st.slider("कितने बेडरूम?", 1, 3, 2)
        has_store = st.checkbox("क्या स्टोर रूम चाहिए?", value=True)
        entrance = st.selectbox("मेन गेट की दिशा", ["North", "South", "East", "West"])

    if st.button("ऑटोमैटिक नक्शा तैयार करें"):
        # ड्राइंग की सेटिंग
        sc = 12  # Scale: 1ft = 12px
        w, h = f * sc, s * sc
        
        # दीवारों की मोटाई और कमरों की सेटिंग
        svg = f'<svg width="{w+60}" height="{h+60}" xmlns="http://www.w3.org/2000/svg" style="background:#f4f4f4; border:5px solid #333;">'
        
        # 1. मुख्य प्लॉट की बाउंड्री
        svg += f'<rect x="30" y="30" width="{w}" height="{h}" fill="white" stroke="#000" stroke-width="4"/>'

        # 2. ऑटोमैटिक रूम प्लेसमेंट लॉजिक (Grid System)
        # हम प्लॉट को पीछे (Back) और आगे (Front) के हिस्सों में बाँट रहे हैं
        r_w = (w / 2) - 10 # एक कमरे की चौड़ाई
        r_h = (h / 2) - 10 # एक कमरे की लंबाई

        # पीछे के दो बेडरूम (Back Side)
        # बेडरूम 1 (लेफ्ट कॉर्नर)
        svg += f'<rect x="30" y="30" width="{r_w}" height="{r_h}" fill="#d1e7dd" stroke="#000" stroke-width="2"/>'
        svg += f'<text x="40" y="60" font-weight="bold">Bedroom 1</text>'
        
        # बेडरूम 2 (राइट कॉर्नर)
        if n_rooms >= 2:
            svg += f'<rect x="{30+r_w}" y="30" width="{r_w}" height="{r_h}" fill="#d1e7dd" stroke="#000" stroke-width="2"/>'
            svg += f'<text x="{40+r_w}" y="60" font-weight="bold">Bedroom 2</text>'

        # 3. बाथरूम और स्टोर (बीच का हिस्सा)
        if has_store:
            svg += f'<rect x="30" y="{30+r_h}" width="{r_w/2}" height="{r_h/2}" fill="#fff3cd" stroke="#000" stroke-width="2"/>'
            svg += f'<text x="35" y="{50+r_h}" font-size="10">Store</text>'
            
        # बाथरूम
        svg += f'<rect x="{30 + r_w/2}" y="{30+r_h}" width="{r_w/2}" height="{r_h/2}" fill="#cfe2ff" stroke="#000" stroke-width="2"/>'
        svg += f'<text x="{35 + r_w/2}" y="{50+r_h}" font-size="10">Bath</text>'

        # 4. बड़ा हॉल और किचन (Front Side)
        svg += f'<rect x="{30 + r_w}" y="{30+r_h}" width="{r_w}" height="{r_h}" fill="#f8d7da" stroke="#000" stroke-width="2"/>'
        svg += f'<text x="{40 + r_w}" y="{60+r_h}" font-weight="bold">Kitchen/Dining</text>'

        # ड्राइंग हॉल (Center/Front)
        svg += f'<text x="{w/2}" y="{h}" font-size="20" font-weight="bold" fill="#084298">Living / Drawing Area</text>'
        
        # गेट मार्किंग
        svg += f'<circle cx="{w/2+30}" cy="{h+30}" r="10" fill="red"/>'
        svg += f'<text x="{w/2+45}" y="{h+35}" font-size="12">Main Entrance ({entrance})</text>'
        
        svg += '</svg>'

        st.write("### आपका ऑटो-जनरेटेड 2D प्लान:")
        st.components.v1.html(svg, height=h+100)
        
        st.warning("सूचना: यह एक AI प्रोटोटाइप है। दीवारों की सटीक मोटाई और पिलर के लिए इंजीनियर से सलाह लें।")

if __name__ == "__main__":
    main()
