import turtle

def get_user_input():
    print("--- AI होम डिज़ाइन असिस्टेंट में आपका स्वागत है ---")
    
    # प्लॉट की माप
    dimensions = {
        "front": float(input("प्लॉट का फ्रंट (Feet): ")),
        "back": float(input("प्लॉट का पिछला हिस्सा (Feet): ")),
        "left": float(input("बाईं दिशा की लंबाई (Feet): ")),
        "right": float(input("दाईं दिशा की लंबाई (Feet): "))
    }
    
    # ग्राउंड फ्लोर की ज़रूरतें
    print("\n--- ग्राउंड फ्लोर की जानकारी ---")
    g_floor = {
        "rooms": int(input("कितने बेडरूम चाहिए? ")),
        "bathrooms": int(input("कितने बाथरूम चाहिए? ")),
        "store": int(input("कितने स्टोर रूम चाहिए? ")),
        "entrance": input("मेन एंट्रेंस किस दिशा में चाहिए (North/South/East/West)? ")
    }
    
    # फर्स्ट फ्लोर की ज़रूरतें
    print("\n--- फर्स्ट फ्लोर की जानकारी ---")
    f_floor = {
        "rooms": int(input("कितने बेडरूम चाहिए? ")),
        "balcony": input("क्या बालकनी चाहिए? (Yes/No): ")
    }

    return dimensions, g_floor, f_floor

def draw_2d_map(dims):
    # यह फंक्शन स्क्रीन पर एक बेसिक 2D आउटलाइन ड्रा करेगा
    screen = turtle.Screen()
    screen.title("आपका 2D होम प्लान")
    t = turtle.Turtle()
    
    scale = 5  # 1 foot = 5 pixels
    
    t.penup()
    t.goto(-100, 0)
    t.pendown()
    
    # चारों दिशाओं को ड्रा करना
    t.forward(dims['front'] * scale) # Front
    t.left(90)
    t.forward(dims['left'] * scale)  # Left
    t.left(90)
    t.forward(dims['back'] * scale)  # Back
    t.left(90)
    t.forward(dims['right'] * scale) # Right
    
    t.write("आपका प्लॉट एरिया", align="center")
    print("\n[सफलता] आपका 2D मैप जनरेट हो गया है।")
    turtle.done()

# प्रोग्राम शुरू करें
if __name__ == "__main__":
    plot_dims, ground, first = get_user_input()
    
    print("\n--- डिज़ाइन सारांश ---")
    print(f"कुल एरिया: {plot_dims['front'] * plot_dims['left']} Sq. Ft. लगभग")
    print(f"ग्राउंड फ्लोर: {ground['rooms']} BHK + {ground['store']} स्टोर")
    print(f"एंट्रेंस: {ground['entrance']} की तरफ")
    
    # मैप ड्रा करने के लिए
    draw_2d_map(plot_dims)
