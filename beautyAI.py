import streamlit as st
from google import genai
from google.genai import types
import random

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="GlowGenius AI",
    page_icon="💄",
    layout="wide"
)

# ==================================================
# HIDDEN API KEY
# ==================================================

api_key = "AQ.Ab8RN6JMNaezG6qR-ANjAD4_XxVu4wK_LNJAtdAqbk4mUI0bbQ"

# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown("""
<style>

.stApp{
background: linear-gradient(
135deg,
#ff9a9e,
#fad0c4,
#fbc2eb,
#a18cd1
);
background-size:400% 400%;
animation:gradient 12s ease infinite;
}

@keyframes gradient{
0%{background-position:0% 50%;}
50%{background-position:100% 50%;}
100%{background-position:0% 50%;}
}

.main-title{
text-align:center;
font-size:55px;
font-weight:bold;
color:white;
}

.subtitle{
text-align:center;
font-size:20px;
color:white;
margin-bottom:25px;
}

.glass-card{
background: rgba(255,255,255,0.20);
backdrop-filter: blur(15px);
-webkit-backdrop-filter: blur(15px);
border-radius:20px;
padding:20px;
border:1px solid rgba(255,255,255,0.25);
box-shadow:0 8px 32px rgba(0,0,0,0.15);
margin-bottom:20px;
}

.result-card{
background:white;
border-radius:20px;
padding:25px;
box-shadow:0px 6px 18px rgba(0,0,0,0.15);
}

.stButton button{
width:100%;
background:linear-gradient(
90deg,
#ff4f9a,
#6a5cff
);
color:white;
font-size:18px;
font-weight:bold;
border-radius:12px;
padding:12px;
border:none;
}

.footer{
text-align:center;
color:white;
font-weight:bold;
margin-top:40px;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# HEADER
# ==================================================

st.markdown("""
<div class="main-title">
✨ GlowGenius AI
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="subtitle">
Your Personal AI Beauty Advisor 💄
</div>
""", unsafe_allow_html=True)

# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.title("🌸 Beauty Dashboard")

    st.markdown("""
    ### Services

    ✅ Personalized Skincare

    ✅ Makeup Recommendations

    ✅ Beauty Routines

    ✅ Ingredient Education

    ✅ Haircare Guide

    ✅ Product Suggestions
    """)

    st.divider()

    st.subheader("🔥 Trending Ingredients")

    st.markdown("""
    • Niacinamide

    • Vitamin C

    • Retinol

    • Salicylic Acid

    • Hyaluronic Acid
    """)

    st.divider()

    beauty_tips = [
        "Apply sunscreen daily.",
        "Hydration improves skin health.",
        "Patch-test new products.",
        "Avoid over-exfoliation.",
        "Clean makeup brushes regularly."
    ]

    st.subheader("💡 Daily Beauty Tip")
    st.success(random.choice(beauty_tips))

# ==================================================
# SCORE
# ==================================================

st.metric("✨ Beauty Readiness Score", "92%")

# ==================================================
# PROFILE BUILDER
# ==================================================

st.markdown("""
<div class="glass-card">
<h3>💎 Beauty Profile Builder</h3>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:

    skin_type = st.selectbox(
        "Skin Type",
        [
            "Oily",
            "Dry",
            "Combination",
            "Sensitive",
            "Normal"
        ]
    )

    age_group = st.selectbox(
        "Age Group",
        [
            "Teen",
            "20-30",
            "30-40",
            "40+"
        ]
    )

with col2:

    concern = st.selectbox(
        "Primary Concern",
        [
            "Acne",
            "Pigmentation",
            "Dark Spots",
            "Dryness",
            "Anti Aging",
            "Dull Skin"
        ]
    )

    budget = st.selectbox(
        "Budget",
        [
            "Budget Friendly",
            "Mid Range",
            "Luxury"
        ]
    )

brands = st.multiselect(
    "Preferred Brands",
    [
        "Cetaphil",
        "CeraVe",
        "The Ordinary",
        "Neutrogena",
        "La Roche Posay",
        "Minimalist",
        "Nykaa",
        "Maybelline",
        "Loreal"
    ]
)

# ==================================================
# PROFILE SUMMARY
# ==================================================

st.markdown(f"""
<div class="glass-card">
<h3>✨ Profile Summary</h3>

<b>Skin Type:</b> {skin_type}<br>
<b>Concern:</b> {concern}<br>
<b>Age Group:</b> {age_group}<br>
<b>Budget:</b> {budget}
</div>
""", unsafe_allow_html=True)

# ==================================================
# SUGGESTED QUESTIONS
# ==================================================

st.subheader("💬 Popular Questions")

popular_question = st.radio(
    "",
    [
        "Routine for oily acne prone skin",
        "Best serum for pigmentation",
        "How to remove dark spots",
        "Beginner makeup kit",
        "Products for sensitive skin"
    ]
)

# ==================================================
# USER QUESTION
# ==================================================

user_question = st.text_area(
    "Ask a Beauty Question",
    value=popular_question,
    height=150
)

# ==================================================
# SYSTEM PROMPT
# ==================================================

system_instruction = """
You are GlowGenius AI.

You ONLY answer questions related to:

- Skincare
- Makeup
- Haircare
- Cosmetics
- Beauty Products
- Beauty Routines
- Beauty Ingredients

If a user asks anything unrelated, respond:

'I am GlowGenius AI and can only assist with beauty, skincare, makeup, haircare, ingredients, and cosmetic recommendations.'

Always provide:

✨ Beauty Profile

🌞 Morning Routine

🌙 Night Routine

💄 Product Recommendations

🧪 Ingredient Explanation

💎 Beauty Tips
"""

# ==================================================
# PROMPT
# ==================================================

beauty_prompt = f"""

Skin Type: {skin_type}

Age Group: {age_group}

Concern: {concern}

Budget: {budget}

Preferred Brands: {brands}

Question:

{user_question}

"""

# ==================================================
# GENERATE
# ==================================================

if st.button("✨ Generate Beauty Advice"):

    try:

        client = genai.Client(api_key=api_key)

        with st.spinner("Creating personalized recommendations..."):

            response = client.models.generate_content(
                model="gemini-flash-lite-latest",
                contents=beauty_prompt,
                config=types.GenerateContentConfig(
                    system_instruction=system_instruction
                )
            )

        st.markdown(
            f"""
            <div class="result-card">
            <h2>💖 Personalized Beauty Plan</h2>
            <hr>
            {response.text}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.success("Beauty plan generated successfully!")

    except Exception as e:
        st.error(f"Error: {e}")

# ==================================================
# FAQ SECTION
# ==================================================

st.divider()

st.subheader("❓ Beauty FAQs")

with st.expander("Which ingredient helps acne?"):
    st.write("✅ Salicylic Acid")

with st.expander("Which ingredient helps pigmentation?"):
    st.write("✅ Vitamin C")

with st.expander("Which ingredient helps hydration?"):
    st.write("✅ Hyaluronic Acid")

with st.expander("Which ingredient helps anti-aging?"):
    st.write("✅ Retinol")

with st.expander("Do oily skin types need moisturizer?"):
    st.write("✅ Yes. Use an oil-free gel moisturizer.")

# ==================================================
# QUICK GUIDE
# ==================================================

st.subheader("📌 Ingredient Guide")

c1, c2, c3 = st.columns(3)

with c1:
    st.info("""
🧴 Niacinamide

• Oil Control

• Acne Marks

• Barrier Repair
""")

with c2:
    st.info("""
🍊 Vitamin C

• Brightening

• Glow

• Dark Spots
""")

with c3:
    st.info("""
💧 Hyaluronic Acid

• Hydration

• Plumping

• Smooth Skin
""")

# ==================================================
# FOOTER
# ==================================================

st.markdown("""
<div class="footer">
💖 Powered by Gemini AI | GlowGenius AI
</div>
""", unsafe_allow_html=True
)