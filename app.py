import streamlit as st

def main():
    st.set_page_config(page_title="Pro AI Architect", layout="centered")
    st.title("🏗️ एडवांस्ड AI होम डिज़ाइनर")
    st.write("यह सिस्टम कमरों के बीच गैलरी और सही एडजस्टमेंट के साथ नक्शा बनाएगा।")

    # एंट्री फॉर्म
    with st.form("pro_form"):
        col1, col2 = st.columns(2)
        with col1:
            f = st.number_input("फ्रंट (चौड़ाई)", value=35.0)
            l = st.number_input("लंबाई (Side)", value=32.0)
        with col2:
            n_rooms = st.selectbox("बेडरूम", [1, 2, 3])
            has_store = st.radio("स्टोर रूम", ["हाँ", "नहीं"], horizontal=True)
            
        entrance = st.selectbox("मेन गेट की दिशा", ["North", "South", "East", "West"])
        submitted = st.form_submit_button("नक्शा एडजस्ट करके जनरेट करें")

    if submitted:
        st.success("जी! कमरों को सही जगह पर एडजस्ट कर दिया गया है।")
        
        sc = 15  # स्केल थोड़ा बड़ा किया
        w, h = f * sc, l * sc
        
        # SVG शुरू
        svg = f'<svg width="{w+100}" height="{h+150}" viewBox="0 0 {w+100} {h+150}" xmlns="http://www.w3.org/2000/svg">'
        # बैकग्राउंड और बाउंड्री
        svg += f'<rect x="20" y="20" width="{w}" height="{h}" fill="#fafafa" stroke="#333" stroke-width="6"/>'
        
        # --- लॉजिक: प्लॉट को 3 हिस्सों में बांटना (पीछे, बीच, आगे) ---
        back_h = h * 0.4  # पीछे के बेडरूम के लिए 40% जगह
        mid_h = h * 0.2   # बीच में बाथरूम, स्टोर और पैसेज के लिए 20% जगह
        front_h = h * 0.4 # आगे हॉल और किचन के लिए 40% जगह

        # 1. बेडरूम्स (पीछे की तरफ)
        r_w = (w / n_rooms) if n_rooms > 0 else w
        for i in range(n_rooms):
            color = "#e3f2fd" if i%2==0 else "#e1f5fe"
            svg += f'<rect x="{20 + (i*r_w)}" y="20" width="{r_w}" height="{back_h}" fill="{color}" stroke="#333" stroke-width="2"/>'
            svg += f'<text x="{30 + (i*r_w)}" y="50" font-family="Arial" font-size="12" font-weight="bold">Bedroom {i+1}</text>'

        # 2. पैसेज और यूटिलिटी (बीच की पट्टी)
        # बाथरूम (लेफ्ट में)
        svg += f'<rect x="20" y="{20+back_h}" width="{w*0.2}" height="{mid_h}" fill="#f3e5f5" stroke="#333" stroke-width="2"/>'
        svg += f'<text x="25" y="{45+back_h}" font-size="10">Bath</text>'
        
        # पैसेज (चलने का रास्ता - बीच में)
        svg += f'<rect x="{20 + w*0.2}" y="{20+back_h}" width="{w*0.6}" height="{mid_h}" fill="#fffde7" stroke="none"/>'
        svg += f'<text x="{20 + w*0.4}" y="{45+back_h}" font-size="10" fill="#999">PASSAGE</text>'

        # स्टोर (राइट में)
        if has_store == "हाँ":
            svg += f'<rect x="{20 + w*0.8}" y="{20+back_h}" width="{w*0.2}" height="{mid_h}" fill="#fff3e0" stroke="#333" stroke-width="2"/>'
            svg += f'<text x="{25 + w*0.8}" y="{45+back_h}" font-size="10">Store</text>'

        # 3. किचन और ड्राइंग हॉल (आगे की तरफ)
        # किचन (एक कोने में)
        k_w = w * 0.3
        svg += f'<rect x="20" y="{20+back_h+mid_h}" width="{k_w}" height="{front_h}" fill="#f1f8e9" stroke="#333" stroke-width="2"/>'
        svg += f'<text x="30" y="{50+back_h+mid_h}" font-weight="bold" font-size="12">Kitchen</text>'
        
        # लिविंग हॉल (बचा हुआ हिस्सा)
        svg += f'<rect x="{20+k_w}" y="{20+back_h+mid_h}" width="{w-k_w}" height="{front_h}" fill="white" stroke="#333" stroke-width="2"/>'
        svg += f'<text x="{40+k_w}" y="{60+back_h+mid_h}" font-weight="bold" font-size="16" fill="#1a237e">DRAWING HALL</text>'

        # एंट्रेंस गेट
        gate_x = 20 + (w/2)
        svg += f'<rect x="{gate_x-20}" y="{h+15}" width="40" height="10" fill="red"/>'
        svg += f'<text x="{gate_x-40}" y="{h+40}" font-size="12" font-weight="bold">MAIN GATE ({entrance})</text>'
        
        svg += '</svg>'

        st.write("### व्यवस्थित फ्लोर प्लान (Adjusted Layout):")
        st.components.v1.html(svg, height=h+200)
        st.info(f"साइज: {f}x{l} फीट | बेडरूम के पीछे से किचन तक का सही तालमेल बनाया गया है।")

if __name__ == "__main__":
    main()
