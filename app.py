# -------------------------------------------
# 📦 Imports
# -------------------------------------------
import streamlit as st
from src.core.planner import TravelPlanner
from dotenv import load_dotenv
import base64

# -------------------------------------------
# 🔐 Load Environment Variables
# -------------------------------------------
load_dotenv()

# -------------------------------------------
# 🌐 Page Configuration
# -------------------------------------------
st.set_page_config(
    page_title="TripWise",
    page_icon="🧳",
    layout="centered",
)


# -------------------------------------------
# 🎨 Custom Styling
# -------------------------------------------
def add_custom_background():
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),
                        url("https://images.unsplash.com/photo-1507525428034-b723cf961d3e");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            font-family: 'Segoe UI', sans-serif;
            color: white !important;
        }

        .glass-card {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            padding: 2rem;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            margin-bottom: 2rem;
            color: #f1f1f1 !important;
        }

        h1, h2, h3, h4, p, label {
            color: #ffffff !important;
            text-shadow: 1px 1px 2px #000000cc;
        }

        .stTextInput > div > div > input,
        .stTextArea > div > textarea {
            background-color: #ffffffdd !important;
            color: #000000 !important;
            border-radius: 8px !important;
        }

        .stButton > button {
            background-color: #ff914d !important;
            color: #ffffff !important;
            font-weight: bold;
            border-radius: 10px;
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.3);
            text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
            box-shadow: 1px 1px 5px #00000055;
            padding: 0.5rem 1rem;
        }

        .stDownloadButton > button {
            background-color: #0077b6 !important;
            color: white !important;
            border-radius: 8px;
            font-weight: bold;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


add_custom_background()

st.markdown(
    '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
    unsafe_allow_html=True,
)

# -------------------------------------------
# 🧳 App Header
# -------------------------------------------
st.markdown("<h1 style='text-align: center;'>🧳 TripWise</h1>", unsafe_allow_html=True)
st.markdown(
    "<h3 style='text-align: center;'>Your Personalized AI Travel Companion</h3>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align: center;'>Plan a <strong>custom itinerary</strong> based on your travel destination and interests. Powered by AI!</p>",
    unsafe_allow_html=True,
)

# -------------------------------------------
# 🔁 Session State Defaults
# -------------------------------------------
for key in ["last_city", "last_interests", "last_itinerary"]:
    if key not in st.session_state:
        st.session_state[key] = ""

# -------------------------------------------
# ✍️ Input Form
# -------------------------------------------
st.markdown('<div class="glass-card">', unsafe_allow_html=True)

with st.form("planner_form"):
    st.markdown("#### 📋 Tell us your travel preferences")

    city = st.text_input(
        "📍 Destination City",
        value=st.session_state.last_city,
        placeholder="e.g., Goa, Varanasi, Rajasthan",
    )

    interests = st.text_input(
        "✨ Interests ",
        value=st.session_state.last_interests,
        placeholder="e.g., temples, food, beaches, heritage",
    )

    submitted = st.form_submit_button("🚀 Generate My Itinerary")

st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------------
# 🛠️ Itinerary Generation Logic
# -------------------------------------------
if submitted:
    if city.strip() and interests.strip():
        with st.spinner("🗺️ Creating your itinerary..."):
            try:
                cleaned_city = city.strip()
                cleaned_interests_list = [
                    i.strip() for i in interests.split(",") if i.strip()
                ]
                cleaned_interests_str = ", ".join(cleaned_interests_list)

                st.session_state.last_city = cleaned_city
                st.session_state.last_interests = cleaned_interests_str

                planner = TravelPlanner()
                planner.set_city(cleaned_city)
                planner.set_interests(
                    cleaned_interests_str
                )  # ✅ Fixed: pass string not list

                itinerary = planner.create_itinerary()
                st.session_state.last_itinerary = itinerary

                # -------------------------
                # ✅ Output Itinerary
                # -------------------------
                st.success("✅ Here’s your custom itinerary!")
                st.markdown('<div class="glass-card">', unsafe_allow_html=True)
                st.markdown("#### 📝 AI-Curated Travel Plan")

                if "Option" in itinerary:
                    options = itinerary.strip().split("Option")
                    for option in options:
                        if option.strip():
                            title, *content = option.strip().split("\n", 1)
                            with st.expander(f"🧭 Option {title.strip()}"):
                                st.markdown("\n".join(content) if content else "")
                else:
                    st.markdown(itinerary)

                st.markdown("</div>", unsafe_allow_html=True)

                # Google Maps Button
                query = "+".join([cleaned_city] + cleaned_interests_list)
                maps_url = f"https://www.google.com/maps/search/{query}"
                st.markdown(
                    f"[🌐 Explore on Google Maps]({maps_url})",
                    unsafe_allow_html=True,
                )

            except Exception as e:
                st.error(f"🚫 Error generating itinerary:\n\n{e}")
    else:
        st.warning(
            "⚠️ Please enter both the destination city and at least one interest."
        )

# -------------------------------------------
# 📥 Download + Reset
# -------------------------------------------
if st.session_state.last_itinerary:
    st.markdown("---")
    st.download_button(
        label="📥 Download Itinerary (.txt)",
        data=st.session_state.last_itinerary,
        file_name=f"{st.session_state.last_city.lower().replace(' ', '_')}_itinerary.txt",
        mime="text/plain",
        use_container_width=True,
    )
    if st.button("🔄 Generate Another Plan"):
        st.session_state.last_itinerary = ""

# -------------------------------------------
# 🧾 Footer
# -------------------------------------------
st.markdown(
    "<hr><p style='text-align: center;'>🧠 Powered by AI · Built with ❤️ using Streamlit</p>",
    unsafe_allow_html=True,
)
