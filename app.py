import streamlit as st

def main():
    st.set_page_config(page_title="AI Home Planner", layout="centered")
    
    st.title("🏗️ स्मार्ट होम डिज़ाइनर (Interactive)")
    st.write("कृपया अपने घर की जानकारी भरें, फिर 'नक्शा तैयार करें' पर क्लिक करें।")

    # --- इनपुट सेक्शन (एंट्री फॉर्म) ---
    with st.form("home_form"):
        st.header("📏 प्लॉट की माप (Feet में)")
        col1, col2 = st.columns(2)
        with col1:
            f = st.number_input("फ्रंट की चौड़ाई", min_value=10.0, value=35.0)
            l = st.number_input("बाईं साइड की लंबाई", min_value=10.0, value=32.0)
        with col2:
            b = st.number_input("पीछे की चौड़ाई", min_value=10.0, value=35.0)
            r = st.number_input("दाईं साइड की लंबाई", min_value=10.0, value=32.0)

        st.header("🏠 कमरों की ज़रूरत")
        c1, c2, c3 = st.columns(3)
        with c1:
            n_rooms = st.selectbox("बेडरूम", [1, 2, 3, 4, 5], index=1)
        with c2:
            n_baths = st.selectbox("बाथरूम", [1, 2, 3], index=0)
        with c3:
            has_store = st.radio("स्टोर रूम", ["हाँ", "नहीं"])

        st.header("🚪 अन्य जानकारी")
        entrance = st.selectbox("मेन एंट्रेंस किस दिशा में चाहिए?", ["North", "South", "East", "West"])
        
        # फॉर्म सबमिट बटन
        submitted = st.form_submit_button("नक्शा जनरेट करें")

    # --- नक्शा जनरेट करने का लॉजिक ---
    if submitted:
        st.success("जी! आपकी जानकारी के अनुसार नक्शा तैयार है।")
        
        sc = 12 # स्केल
        w, h = f * sc, l * sc
        
        # SVG मैप कोडिंग
        svg = f'<svg width="{w+60}" height="{h+100}" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff; border:4px solid #333;">'
        
        # प्लॉट बाउंड्री
        svg += f'<rect x="30" y="30" width="{w}" height="{h}" fill="white" stroke="black" stroke-width="3"/>'
        
        # कमरे बनाने का गणित
        room_w = w / 2
        room_h = h * 0.4
        
        # बेडरूम 1
        svg += f'<rect x="30" y="30" width="{room_w}" height="{room_h}" fill="#e3f2fd" stroke="black" stroke-width="2"/>'
        svg += f'<text x="40" y="60" font-weight="bold" font-size="14">Bedroom 1</text>'
        
        # बेडरूम 2 (अगर 2 या ज्यादा हों)
        if n_rooms >= 2:
            svg += f'<rect x="{30+room_w}" y="30" width="{room_w}" height="{room_h}" fill="#e3f2fd" stroke="black" stroke-width="2"/>'
            svg += f'<text x="{40+room_w}" y="60" font-weight="bold" font-size="14">Bedroom 2</text>'

        # किचन और बाथरूम (बीच की पट्टी)
        mid_y = 30 + room_h
        svg += f'<rect x="30" y="{mid_y}" width="{room_w/2}" height="{room_h/2}" fill="#fff3e0" stroke="black" stroke-width="2"/>'
        svg += f'<text x="35" y="{mid_y+25}" font-size="12">Kitchen</text>'
        
        svg += f'<rect x="{30+room_w/2}" y="{mid_y}" width="{room_w/2}" height="{room_h/2}" fill="#f3e5f5" stroke="black" stroke-width="2"/>'
        svg += f'<text x="{35+room_w/2}" y="{mid_y+25}" font-size="12">Bath</text>'

        if has_store == "हाँ":
            svg += f'<rect x="{30+room_w}" y="{mid_y}" width="{room_w/2}" height="{room_h/2}" fill="#f1f8e9" stroke="black" stroke-width="2"/>'
            svg += f'<text x="{35+room_w}" y="{mid_y+25}" font-size="12">Store</text>'

        # लिविंग हॉल (सामने का हिस्सा)
        svg += f'<text x="{w/2+30}" y="{h-20}" text-anchor="middle" font-weight="bold" font-size="18" fill="darkblue">LIVING AREA / HALL</text>'
        
        # गेट और दिशा
        svg += f'<line x1="{w/2}" y1="{h+30}" x2="{w/2+60}" y2="{h+30}" stroke="red" stroke-width="8"/>'
        svg += f'<text x="{w/2+30}" y="{h+50}" text-anchor="middle" font-size="12">Main Entrance: {entrance}</text>'
        
        svg += '</svg>'

        st.write("### आपका कस्टमाइज्ड 2D फ्लोर प्लान:")
        st.components.v1.html(svg, height=h+150)
        
        # सारांश
        st.info(f"प्लॉट साइज: {f}x{l} फीट | कुल एरिया: {f*l} Sq.Ft.")

if __name__ == "__main__":
    main()
