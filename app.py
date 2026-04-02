import streamlit as st
import pandas as pd
import pickle
import json
import os
import hashlib

st.set_page_config(page_title="NutriDex", page_icon="⚡", layout="centered")

# ========================
# USER DATABASE (JSON)
# ========================
USER_FILE = "users.json"

def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USER_FILE, 'w') as f:
        json.dump(users, f, indent=2)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# ========================
# LOAD DATA & MODEL
# ========================
@st.cache_data
def load_foods():
    return pd.read_csv('foods.csv')

@st.cache_resource
def load_model():
    with open('food_model.pkl', 'rb') as f:
        return pickle.load(f)

foods_df = load_foods()
model_data = load_model()

# ========================
# GBA POKEMON THEME CSS
# ========================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&family=Nunito:wght@400;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Nunito', sans-serif !important;
    background-color: #2860A8 !important;
    color: #1a1a2e !important;
}

.main {
    background: linear-gradient(180deg, #2860A8 0%, #3878C0 40%, #2860A8 100%) !important;
}

#MainMenu, footer, header {visibility: hidden;}
[data-testid="stToolbar"] { display: none !important; }
[data-testid="stDecoration"] { display: none !important; }

h1, h2, h3 {
    font-family: 'Press Start 2P', cursive !important;
    font-weight: 400 !important;
    color: #1a1a2e !important;
    font-size: 12px !important;
    letter-spacing: 0.5px;
}

/* ---- GBA DIALOG BOX ---- */
.gba-box {
    background: linear-gradient(180deg, #F8F8F0 0%, #E8E8E0 100%);
    border: 4px solid #1a1a2e;
    border-radius: 12px;
    padding: 20px 24px;
    margin: 10px 0;
    box-shadow: 4px 4px 0px #1a3a6e, inset 0 0 0 2px #c8c8b8;
    position: relative;
}

.gba-box h3 {
    color: #1a1a2e !important;
    margin-bottom: 12px;
}

/* ---- GBA HEADER BOX ---- */
.gba-header {
    background: linear-gradient(180deg, #E83030 0%, #C01818 100%);
    border: 4px solid #1a1a2e;
    border-radius: 14px;
    padding: 20px;
    text-align: center;
    box-shadow: 4px 4px 0px #1a3a6e, inset 0 0 0 2px #F85858;
    margin-bottom: 12px;
}

.gba-header .title {
    font-family: 'Press Start 2P', cursive;
    font-size: 22px;
    color: #FFD700;
    text-shadow: 2px 2px 0px #8B0000, -1px -1px 0px #FF6347;
    margin: 0;
}

.gba-header .sub {
    font-family: 'Press Start 2P', cursive;
    font-size: 8px;
    color: #FFE4B5;
    margin-top: 6px;
    letter-spacing: 1px;
}

/* ---- BUTTONS (A BUTTON STYLE) ---- */
.stButton > button {
    background: linear-gradient(180deg, #48B848 0%, #308030 100%) !important;
    color: white !important;
    border: 3px solid #1a1a2e !important;
    border-radius: 8px !important;
    font-family: 'Press Start 2P', cursive !important;
    font-size: 9px !important;
    padding: 10px 20px !important;
    box-shadow: 3px 3px 0px #1a3a6e !important;
    transition: all 0.1s !important;
    text-transform: uppercase !important;
}

.stButton > button:hover {
    background: linear-gradient(180deg, #58D058 0%, #48B848 100%) !important;
    transform: translate(1px, 1px) !important;
    box-shadow: 2px 2px 0px #1a3a6e !important;
}

.stButton > button:active {
    transform: translate(3px, 3px) !important;
    box-shadow: 0px 0px 0px #1a3a6e !important;
}

/* ---- INPUT FIELDS ---- */
.stTextInput input, .stNumberInput input {
    background: #F8F8F0 !important;
    color: #1a1a2e !important;
    border: 3px solid #1a1a2e !important;
    border-radius: 6px !important;
    font-family: 'Nunito', sans-serif !important;
    font-size: 14px !important;
    font-weight: 700 !important;
    box-shadow: 2px 2px 0px #8888a0 !important;
}

.stTextInput input:focus, .stNumberInput input:focus {
    border-color: #E83030 !important;
    box-shadow: 2px 2px 0px #E83030 !important;
}

.stNumberInput button {
    background: #48B848 !important;
    color: white !important;
    border: 2px solid #1a1a2e !important;
    border-radius: 4px !important;
}

/* ---- SELECT BOX ---- */
.stSelectbox > div > div {
    background: #F8F8F0 !important;
    border: 3px solid #1a1a2e !important;
    border-radius: 6px !important;
    color: #000000 !important;
    box-shadow: 2px 2px 0px #8888a0 !important;
}

.stSelectbox [data-baseweb="select"] > div {
    color: #000000 !important;
    font-weight: 700 !important;
}

.stSelectbox [data-baseweb="select"] span,
.stSelectbox [data-baseweb="select"] div,
.stSelectbox [data-baseweb="select"] p {
    color: #000000 !important;
}

[data-baseweb="popover"] {
    background: #F8F8F0 !important;
    border: 3px solid #1a1a2e !important;
    border-radius: 8px !important;
    box-shadow: 4px 4px 0px #1a3a6e !important;
}

[data-baseweb="menu"] { background: #F8F8F0 !important; }

[data-baseweb="menu"] li {
    background: #F8F8F0 !important;
    color: #1a1a2e !important;
    font-weight: 600 !important;
    border-bottom: 1px solid #d0d0c0 !important;
}

[data-baseweb="menu"] li:hover {
    background: #48B848 !important;
    color: white !important;
}

/* ---- LABELS ---- */
.stTextInput label, .stNumberInput label, .stSelectbox label, .stCheckbox label,
[data-testid="stWidgetLabel"] {
    font-family: 'Press Start 2P', cursive !important;
    font-size: 8px !important;
    color: #FFE4B5 !important;
    text-transform: uppercase !important;
    text-shadow: 1px 1px 0px rgba(0,0,0,0.5) !important;
}

/* removed - handled in main tab section below */

/* General text on blue background */
p, span, div {
    color: #F0F0F0;
}

/* Text inside gba-box should be dark */
.gba-box p, .gba-box span, .gba-box div,
.gba-box .stMarkdown p {
    color: #1a1a2e;
}

/* ---- STAT CARD ---- */
.stat-card {
    background: linear-gradient(180deg, #F8F8F0, #E0E0D8);
    border: 3px solid #1a1a2e;
    border-radius: 8px;
    padding: 14px;
    text-align: center;
    margin: 4px 0;
    box-shadow: 2px 2px 0px #8888a0;
}

.stat-card .label {
    font-family: 'Press Start 2P', cursive;
    font-size: 7px;
    color: #606070;
    text-transform: uppercase;
    margin-bottom: 4px;
}

.stat-card .value {
    font-family: 'Press Start 2P', cursive;
    font-size: 16px;
    color: #1a1a2e;
    font-weight: 400;
}

/* ---- HP BARS (GBA STYLE) ---- */
.hp-label {
    font-family: 'Press Start 2P', cursive;
    font-size: 9px;
    color: #FFFFFF;
    margin: 8px 0 2px 0;
}

.hp-container {
    background: #303030;
    border: 3px solid #1a1a2e;
    border-radius: 6px;
    height: 16px;
    width: 100%;
    overflow: hidden;
    box-shadow: inset 2px 2px 0px rgba(0,0,0,0.3);
}

.hp-fill {
    height: 16px;
    transition: width 0.5s ease;
    position: relative;
}

.hp-fill::after {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 6px;
    background: rgba(255,255,255,0.3);
}

/* ---- POKEMON SPRITE ---- */
.poke-sprite {
    text-align: center;
    margin: 8px 0;
}

.poke-sprite img {
    image-rendering: pixelated;
    filter: drop-shadow(2px 2px 0px #1a3a6e);
}

/* ---- FOOD ITEM ---- */
.food-row {
    background: #F0F0E8;
    border: 2px solid #b0b0a0;
    border-radius: 6px;
    padding: 8px 12px;
    margin: 4px 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-weight: 700;
    color: #1a1a2e;
}

.food-row span {
    color: #000000 !important;
}

.food-row:hover {
    border-color: #48B848;
    background: #E8F8E8;
}

.food-row .kcal {
    font-family: 'Press Start 2P', cursive;
    font-size: 8px;
    color: #E83030;
}

/* ---- BADGE ---- */
.gbadge {
    display: inline-block;
    border: 2px solid #1a1a2e;
    border-radius: 4px;
    padding: 2px 8px;
    font-family: 'Press Start 2P', cursive;
    font-size: 7px;
    margin: 2px;
}
.gbadge-red { background: #E83030; color: white; }
.gbadge-yellow { background: #F8D030; color: #1a1a2e; }
.gbadge-green { background: #48B848; color: white; }
.gbadge-blue { background: #5090D0; color: white; }

/* ---- SUGGESTION CARD ---- */
.sug-card {
    background: linear-gradient(180deg, #F8F8F0, #E8E8E0);
    border: 3px solid #48B848;
    border-radius: 8px;
    padding: 12px 16px;
    margin: 6px 0;
    box-shadow: 2px 2px 0px #8888a0;
}

.sug-card:hover {
    border-color: #E83030;
}

.sug-card div, .sug-card span, .sug-card p {
    color: #000000 !important;
}

/* ---- TABS ---- */
.stTabs [data-baseweb="tab-list"] {
    background: linear-gradient(180deg, #F8F8F0, #E0E0D8);
    border: 3px solid #1a1a2e;
    border-radius: 10px;
    padding: 4px;
    box-shadow: 3px 3px 0px #1a3a6e;
}

.stTabs [data-baseweb="tab"] {
    background: #1a1a2e !important;
    border-radius: 8px !important;
    color: #FFFFFF !important;
    font-family: 'Press Start 2P', cursive !important;
    font-size: 7px !important;
    padding: 10px 12px !important;
    border: 2px solid #1a1a2e !important;
}

.stTabs [data-baseweb="tab"]:hover {
    color: #FFD700 !important;
    background: #2a2a4e !important;
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(180deg, #E83030, #C01818) !important;
    color: #FFFFFF !important;
    border-color: #FFD700 !important;
    box-shadow: inset 0 0 0 1px #F85858 !important;
}

.stTabs [data-baseweb="tab-highlight"],
.stTabs [data-baseweb="tab-border"] { display: none !important; }

/* ---- CHECKBOX ---- */
.stCheckbox label span {
    color: #1a1a2e !important;
    font-weight: 700 !important;
}

/* ---- LOGIN BOX ---- */
.login-box {
    background: linear-gradient(180deg, #F8F8F0 0%, #E8E8E0 100%);
    border: 4px solid #1a1a2e;
    border-radius: 14px;
    padding: 30px;
    max-width: 400px;
    margin: 20px auto;
    box-shadow: 5px 5px 0px #1a3a6e, inset 0 0 0 2px #c8c8b8;
    text-align: center;
}

/* Arrow pointer for menu */
.arrow-item {
    font-family: 'Press Start 2P', cursive;
    font-size: 10px;
    color: #1a1a2e;
    padding: 6px 0;
}

.arrow-item::before {
    content: '▶ ';
    color: #E83030;
}
</style>
""", unsafe_allow_html=True)

# ========================
# SESSION STATE
# ========================
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = ""
if 'logged_foods' not in st.session_state:
    st.session_state.logged_foods = []
if 'todos' not in st.session_state:
    st.session_state.todos = []
if 'profile_done' not in st.session_state:
    st.session_state.profile_done = False

# ========================
# LOGIN / SIGNUP SCREEN
# ========================
if not st.session_state.logged_in:
    st.markdown("""
    <div class="poke-sprite">
        <img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png" width="130">
    </div>
    <div class="gba-header">
        <p class="title">NutriDex</p>
        <p class="sub">Gotta Track 'Em All!</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="gba-box">', unsafe_allow_html=True)
    st.markdown("### 🔐 Trainer Login")

    login_tab, signup_tab = st.tabs(["Login", "Sign Up"])

    with login_tab:
        login_user = st.text_input("Username", key="login_u")
        login_pass = st.text_input("Password", type="password", key="login_p")
        if st.button("⚡ Login"):
            users = load_users()
            if login_user in users and users[login_user]["password"] == hash_password(login_pass):
                st.session_state.logged_in = True
                st.session_state.username = login_user
                # Load saved profile if exists
                if "profile" in users[login_user]:
                    st.session_state.stats = users[login_user]["profile"]
                    st.session_state.profile_done = True
                st.rerun()
            else:
                st.error("Wrong username or password!")

    with signup_tab:
        new_user = st.text_input("Choose Username", key="signup_u")
        new_pass = st.text_input("Choose Password", type="password", key="signup_p")
        if st.button("📝 Sign Up"):
            users = load_users()
            if new_user in users:
                st.error("Username already taken!")
            elif len(new_user) < 3 or len(new_pass) < 3:
                st.error("Username and password must be at least 3 characters!")
            else:
                users[new_user] = {"password": hash_password(new_pass)}
                save_users(users)
                st.success(f"Account created! You can now login, {new_user}!")

    st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# ========================
# MAIN APP (AFTER LOGIN)
# ========================

# Header
st.markdown(f"""
<div class="gba-header">
    <img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png" 
         width="80" style="filter: drop-shadow(2px 2px 0px #8B0000);">
    <p class="title">NutriDex</p>
    <p class="sub">Trainer: {st.session_state.username}</p>
</div>
""", unsafe_allow_html=True)

# Logout button
if st.button("🚪 Logout"):
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.session_state.profile_done = False
    st.session_state.logged_foods = []
    st.session_state.todos = []
    st.rerun()

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["🧬 Profile", "🎒 Bag", "🤖 Suggest", "📋 Quests"])

# ========================
# TAB 1: PROFILE
# ========================
with tab1:
    st.markdown('<div class="gba-box">', unsafe_allow_html=True)
    st.markdown("### 🧬 Trainer Profile")

    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Name", value=st.session_state.username)
        age = st.number_input("Age", 10, 100, 20)
        height = st.number_input("Height (cm)", 100.0, 250.0, 170.0)
        goal = st.selectbox("Goal", ["Maintain Weight", "Lose Weight", "Gain Weight"])
    with col2:
        gender = st.selectbox("Gender", ["Male", "Female"])
        weight = st.number_input("Weight (kg)", 20.0, 200.0, 65.0)
        activity = st.selectbox("Activity", [
            "Sedentary (desk job)",
            "Lightly Active (1-3 days/week)",
            "Moderately Active (3-5 days/week)",
            "Very Active (6-7 days/week)"
        ])

    if st.button("⚡ Analyse Stats"):
        bmi = weight / ((height / 100) ** 2)

        if bmi < 18.5:
            category, bmi_color = "Underweight", "#5090D0"
        elif bmi < 25:
            category, bmi_color = "Normal", "#48B848"
        elif bmi < 30:
            category, bmi_color = "Overweight", "#F8D030"
        else:
            category, bmi_color = "Obese", "#E83030"

        bmr = (10 * weight + 6.25 * height - 5 * age + 5) if gender == "Male" else (10 * weight + 6.25 * height - 5 * age - 161)

        act_map = {
            "Sedentary (desk job)": 1.2,
            "Lightly Active (1-3 days/week)": 1.375,
            "Moderately Active (3-5 days/week)": 1.55,
            "Very Active (6-7 days/week)": 1.725
        }
        tdee = bmr * act_map[activity]

        if goal == "Lose Weight":
            cal_goal, ppk = tdee - 500, 2.2
        elif goal == "Gain Weight":
            cal_goal, ppk = tdee + 500, 2.0
        else:
            cal_goal, ppk = tdee, 1.6

        pro_g = ppk * weight
        fat_g = (cal_goal * 0.25) / 9
        carb_g = (cal_goal - (pro_g * 4) - (fat_g * 9)) / 4

        pro_pct = round((pro_g * 4 / cal_goal) * 100)
        carb_pct = round((carb_g * 4 / cal_goal) * 100)
        fat_pct = round((fat_g * 9 / cal_goal) * 100)

        st.session_state.stats = {
            "name": name, "weight": weight,
            "bmi": bmi, "category": category, "bmi_color": bmi_color,
            "calorie_goal": cal_goal,
            "protein_g": pro_g, "carbs_g": carb_g, "fat_g": fat_g,
            "protein_pct": pro_pct, "carbs_pct": carb_pct, "fat_pct": fat_pct
        }
        st.session_state.profile_done = True

        # Save profile to user file
        users = load_users()
        if st.session_state.username in users:
            users[st.session_state.username]["profile"] = st.session_state.stats
            save_users(users)

        # Pokemon based on BMI
        poke_map = {
            "Underweight": ("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/92.png", "Gastly"),
            "Normal": ("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png", "Pikachu"),
            "Overweight": ("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/143.png", "Snorlax"),
            "Obese": ("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/446.png", "Munchlax"),
        }
        pimg, pname = poke_map[category]

        st.markdown(f"""
        <div class="poke-sprite">
            <img src="{pimg}" width="120" style="filter: drop-shadow(3px 3px 0px #1a3a6e);">
            <p style="font-family:'Press Start 2P'; font-size:10px; color:{bmi_color}; margin-top:6px;">
                TYPE: {pname}
            </p>
        </div>
        """, unsafe_allow_html=True)

        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown(f'<div class="stat-card"><div class="label">BMI</div><div class="value">{bmi:.1f}</div></div>', unsafe_allow_html=True)
        with c2:
            st.markdown(f'<div class="stat-card"><div class="label">Status</div><div class="value" style="color:{bmi_color};font-size:10px;">{category}</div></div>', unsafe_allow_html=True)
        with c3:
            st.markdown(f'<div class="stat-card"><div class="label">Daily Kcal</div><div class="value">{cal_goal:.0f}</div></div>', unsafe_allow_html=True)

        st.markdown(f"""
        <div class="hp-label">🥩 PROTEIN — {pro_g:.0f}g <span class="gbadge gbadge-red">{pro_pct}%</span></div>
        <div class="hp-container"><div class="hp-fill" style="width:{pro_pct}%;background:linear-gradient(180deg,#F85858,#E83030);"></div></div>

        <div class="hp-label">🍚 CARBS — {carb_g:.0f}g <span class="gbadge gbadge-yellow">{carb_pct}%</span></div>
        <div class="hp-container"><div class="hp-fill" style="width:{carb_pct}%;background:linear-gradient(180deg,#F8E048,#F8D030);"></div></div>

        <div class="hp-label">🥑 FAT — {fat_g:.0f}g <span class="gbadge gbadge-green">{fat_pct}%</span></div>
        <div class="hp-container"><div class="hp-fill" style="width:{fat_pct}%;background:linear-gradient(180deg,#58D058,#48B848);"></div></div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ========================
# TAB 2: FOOD BAG
# ========================
with tab2:
    st.markdown("""
    <div class="poke-sprite">
        <img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/143.png" width="70">
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="gba-box">', unsafe_allow_html=True)
    st.markdown("### 🎒 Add Item")

    search_query = st.text_input("🔍 Type to search food", placeholder="e.g. chicken, rice, dosa...")

    if search_query:
        matches = foods_df[foods_df['name'].str.lower().str.contains(search_query.lower())]
        if len(matches) > 0:
            st.markdown(f'<p style="color:#FFD700;font-size:12px;">Found {len(matches)} results:</p>', unsafe_allow_html=True)
            for idx, fd in matches.head(10).iterrows():
                veg_icon = "🌿" if str(fd['veg']).lower() in ['true','1','yes'] else "🍗"
                col1, col2 = st.columns([4, 1])
                with col1:
                    st.markdown(f"""
                    <div class="food-row">
                        <span>{veg_icon} {fd['name']}</span>
                        <span class="kcal">{fd['calories']} KCAL | P:{fd['protein']}g | C:{fd['carbs']}g | F:{fd['fat']}g</span>
                    </div>
                    """, unsafe_allow_html=True)
                with col2:
                    if st.button("➕", key=f"add_{idx}"):
                        st.session_state.logged_foods.append(fd.to_dict())
                        st.rerun()
        else:
            st.warning("No foods found. Try a different search!")
    else:
        st.markdown('<p style="color:#A0C0E0;font-size:12px;">Start typing to see matching foods...</p>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # ---- MANUAL INPUT ----
    st.markdown('<div class="gba-box">', unsafe_allow_html=True)
    st.markdown("### ✏️ Add Custom Food")

    m_name = st.text_input("Food name", placeholder="e.g. Homemade Salad", key="manual_name")
    mc1, mc2, mc3, mc4 = st.columns(4)
    with mc1:
        m_cal = st.number_input("Calories", min_value=0, value=100, key="manual_cal")
    with mc2:
        m_pro = st.number_input("Protein (g)", min_value=0.0, value=0.0, key="manual_pro")
    with mc3:
        m_carb = st.number_input("Carbs (g)", min_value=0.0, value=0.0, key="manual_carb")
    with mc4:
        m_fat = st.number_input("Fat (g)", min_value=0.0, value=0.0, key="manual_fat")

    if st.button("✏️ Add Custom Food"):
        if m_name:
            custom_food = {
                'name': m_name,
                'calories': m_cal,
                'protein': m_pro,
                'carbs': m_carb,
                'fat': m_fat,
                'category': 'Custom',
                'veg': 'True'
            }
            st.session_state.logged_foods.append(custom_food)
            st.rerun()
        else:
            st.warning("Enter a food name!")

    st.markdown('</div>', unsafe_allow_html=True)

    if st.session_state.logged_foods:
        st.markdown('<div class="gba-box">', unsafe_allow_html=True)
        st.markdown("### 📦 Bag Contents")

        tot_cal = sum(f['calories'] for f in st.session_state.logged_foods)
        tot_p = sum(f['protein'] for f in st.session_state.logged_foods)
        tot_c = sum(f['carbs'] for f in st.session_state.logged_foods)
        tot_f = sum(f['fat'] for f in st.session_state.logged_foods)

        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.markdown(f'<div class="stat-card"><div class="label">KCAL</div><div class="value" style="font-size:14px;">{tot_cal:.0f}</div></div>', unsafe_allow_html=True)
        with c2:
            st.markdown(f'<div class="stat-card"><div class="label">PROTEIN</div><div class="value" style="font-size:14px;">{tot_p:.1f}g</div></div>', unsafe_allow_html=True)
        with c3:
            st.markdown(f'<div class="stat-card"><div class="label">CARBS</div><div class="value" style="font-size:14px;">{tot_c:.1f}g</div></div>', unsafe_allow_html=True)
        with c4:
            st.markdown(f'<div class="stat-card"><div class="label">FAT</div><div class="value" style="font-size:14px;">{tot_f:.1f}g</div></div>', unsafe_allow_html=True)

        if st.session_state.profile_done:
            rem = st.session_state.stats['calorie_goal'] - tot_cal
            col = "#48B848" if rem > 0 else "#E83030"
            st.markdown(f'<p style="text-align:center;font-family:\'Press Start 2P\';font-size:11px;color:{col};margin:10px 0;">{"▲" if rem > 0 else "▼"} {abs(rem):.0f} KCAL {"LEFT" if rem > 0 else "OVER"}</p>', unsafe_allow_html=True)

        for f in st.session_state.logged_foods:
            st.markdown(f'<div class="food-row"><span>{f["name"]}</span><span class="kcal">{f["calories"]} KCAL</span></div>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

        if st.button("🗑️ Empty Bag"):
            st.session_state.logged_foods = []
            st.rerun()

# ========================
# TAB 3: ML SUGGESTIONS
# ========================
with tab3:
    st.markdown("""
    <div class="poke-sprite">
        <img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/6.png" width="80">
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="gba-box">', unsafe_allow_html=True)
    st.markdown("### 🤖 Food Suggestions")
    st.write("KNN Machine Learning model finds foods matching your remaining daily macros.")

    if not st.session_state.profile_done:
        st.warning("Fill your Profile first! (Tab 1)")
    else:
        stats = st.session_state.stats
        eaten_cal = sum(f['calories'] for f in st.session_state.logged_foods)
        eaten_p = sum(f['protein'] for f in st.session_state.logged_foods)
        eaten_c = sum(f['carbs'] for f in st.session_state.logged_foods)
        eaten_f = sum(f['fat'] for f in st.session_state.logged_foods)

        rem_cal = max(0, stats['calorie_goal'] - eaten_cal)
        rem_p = max(0, stats['protein_g'] - eaten_p)
        rem_c = max(0, stats['carbs_g'] - eaten_c)
        rem_f = max(0, stats['fat_g'] - eaten_f)

        st.markdown(f"""
        <div class="stat-card" style="text-align:left;">
            <div class="label">REMAINING TARGETS</div>
            <div style="margin-top:6px;">
                <span class="gbadge gbadge-red">🔥 {rem_cal:.0f} kcal</span>
                <span class="gbadge gbadge-yellow">🥩 {rem_p:.0f}g P</span>
                <span class="gbadge gbadge-green">🍚 {rem_c:.0f}g C</span>
                <span class="gbadge gbadge-blue">🥑 {rem_f:.0f}g F</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        veg_only = st.checkbox("🌿 Vegetarian only")
        nonveg_only = st.checkbox("🍗 Non-Vegetarian only")
        no_fast_food = st.checkbox("🚫 Exclude fast food & sweets", value=True)

        if st.button("🔍 Find Suggestions"):
            import numpy as np
            import random

            scaler = model_data['scaler']
            knn_model = model_data['model']
            df = model_data['dataframe']

            target = np.array([[rem_cal, rem_p, rem_c, rem_f]])
            target_scaled = scaler.transform(target)
            distances, indices = knn_model.kneighbors(target_scaled, n_neighbors=min(50, len(df)))

            # Collect all valid matches first
            valid_matches = []
            excluded_cats = []
            if no_fast_food:
                excluded_cats = ['Fast Food', 'Sweets', 'Oils', 'Supplements']

            for idx in indices[0]:
                food = df.iloc[idx]
                is_veg = str(food['veg']).lower() in ['true', '1', 'yes']
                if veg_only and not is_veg:
                    continue
                if nonveg_only and is_veg:
                    continue
                if food['category'] in excluded_cats:
                    continue
                valid_matches.append(food)
                if len(valid_matches) >= 20:
                    break

            # Randomly pick 5 from top 20 for variety
            if len(valid_matches) > 5:
                results = random.sample(valid_matches, 5)
            else:
                results = valid_matches

            if results:
                st.markdown("---")
                st.markdown("#### 🎯 Suggested Combo")
                combo_cal = sum(f['calories'] for f in results)
                combo_p = sum(f['protein'] for f in results)
                combo_c = sum(f['carbs'] for f in results)
                combo_f = sum(f['fat'] for f in results)

                for food in results:
                    veg_badge = "🌿 VEG" if str(food['veg']).lower() in ['true','1','yes'] else "🍗 NON-VEG"
                    st.markdown(f"""
                    <div class="sug-card">
                        <div style="font-family:'Press Start 2P';font-size:9px;color:#1a1a2e;margin-bottom:6px;">{food['name']}</div>
                        <span class="gbadge gbadge-red">{food['calories']:.0f} kcal</span>
                        <span class="gbadge gbadge-yellow">P:{food['protein']:.1f}g</span>
                        <span class="gbadge gbadge-green">C:{food['carbs']:.1f}g</span>
                        <span class="gbadge gbadge-blue">F:{food['fat']:.1f}g</span>
                        <span style="font-size:11px;color:#606070;margin-left:6px;">{food['category']} • {veg_badge}</span>
                    </div>
                    """, unsafe_allow_html=True)

                st.markdown(f"""
                <div class="stat-card" style="text-align:left; margin-top:10px;">
                    <div class="label">COMBO TOTAL</div>
                    <div style="margin-top:6px;">
                        <span class="gbadge gbadge-red">🔥 {combo_cal:.0f} kcal</span>
                        <span class="gbadge gbadge-yellow">P:{combo_p:.1f}g</span>
                        <span class="gbadge gbadge-green">C:{combo_c:.1f}g</span>
                        <span class="gbadge gbadge-blue">F:{combo_f:.1f}g</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)

                st.markdown('<p style="font-size:12px;color:#FFD700;text-align:center;margin-top:8px;">💡 Hit Find again for a different combo!</p>', unsafe_allow_html=True)
            else:
                st.info("No matching foods found. Try changing filters!")

    st.markdown('</div>', unsafe_allow_html=True)

    # ---- PORTION CALCULATOR ----
    st.markdown('<div class="gba-box">', unsafe_allow_html=True)
    st.markdown("### 📐 Portion Calculator")
    st.write("Pick a food you already have, and we'll tell you how much to eat!")

    if st.session_state.profile_done:
        portion_food = st.selectbox("I have this food:", foods_df['name'].tolist(), key="portion_food")
        pf = foods_df[foods_df['name'] == portion_food].iloc[0]

        # Calculate how many servings to match remaining calories
        if pf['calories'] > 0:
            cal_servings = rem_cal / pf['calories']
            pro_from = pf['protein'] * cal_servings
            carb_from = pf['carbs'] * cal_servings
            fat_from = pf['fat'] * cal_servings

            # Per 100g reference (CSV values are per 100g or per piece)
            st.markdown(f"""
            <div class="sug-card">
                <div style="font-family:'Press Start 2P';font-size:9px;color:#1a1a2e;margin-bottom:10px;">📐 {pf['name']}</div>
                <p style="color:#1a1a2e;font-size:13px;margin:4px 0;">
                    <b>Per serving:</b> {pf['calories']} kcal | P:{pf['protein']}g | C:{pf['carbs']}g | F:{pf['fat']}g
                </p>
                <p style="color:#E83030;font-size:14px;font-weight:800;margin:8px 0;">
                    ▶ Eat <b>{cal_servings:.1f} servings</b> to fill your remaining {rem_cal:.0f} kcal
                </p>
                <p style="color:#1a1a2e;font-size:12px;margin:4px 0;">
                    That gives you: {pro_from:.1f}g protein | {carb_from:.1f}g carbs | {fat_from:.1f}g fat
                </p>
            </div>
            """, unsafe_allow_html=True)

            # Also show for protein target
            if pf['protein'] > 0:
                pro_servings = rem_p / pf['protein']
                st.markdown(f"""
                <div class="stat-card" style="text-align:left;">
                    <div class="label">TO HIT PROTEIN TARGET</div>
                    <p style="color:#1a1a2e;font-size:13px;margin:6px 0;">
                        Eat <b>{pro_servings:.1f} servings</b> for {rem_p:.0f}g protein ({pro_servings * pf['calories']:.0f} kcal)
                    </p>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.warning("Fill your Profile first! (Tab 1)")

    st.markdown('</div>', unsafe_allow_html=True)

# ========================
# TAB 4: TO-DO / QUESTS
# ========================
with tab4:
    st.markdown("""
    <div class="poke-sprite">
        <img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/448.png" width="70">
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="gba-box">', unsafe_allow_html=True)
    st.markdown("### 📋 Daily Quests")

    c1, c2 = st.columns([3, 1])
    with c1:
        new_todo = st.text_input("New quest", placeholder="e.g. Drink 2L water")
    with c2:
        st.write("")
        st.write("")
        if st.button("➕ Add"):
            if new_todo:
                st.session_state.todos.append({"task": new_todo, "done": False})
                st.rerun()

    if st.session_state.todos:
        for i, todo in enumerate(st.session_state.todos):
            c1, c2 = st.columns([5, 1])
            with c1:
                checked = st.checkbox(todo["task"], value=todo["done"], key=f"todo_{i}")
                st.session_state.todos[i]["done"] = checked
            with c2:
                if st.button("❌", key=f"del_{i}"):
                    st.session_state.todos.pop(i)
                    st.rerun()

        done = sum(1 for t in st.session_state.todos if t["done"])
        total = len(st.session_state.todos)
        pct = int((done / total) * 100) if total > 0 else 0

        st.markdown(f"""
        <div class="hp-label">QUEST PROGRESS: {done}/{total}</div>
        <div class="hp-container"><div class="hp-fill" style="width:{pct}%;background:linear-gradient(180deg,#58D058,#48B848);"></div></div>
        """, unsafe_allow_html=True)

        if st.button("🗑️ Clear Quests"):
            st.session_state.todos = []
            st.rerun()
    else:
        st.markdown('<p style="font-family:Press Start 2P;font-size:10px;color:#FFD700;text-align:center;">▶ No quests yet. Add one above!</p>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align:center; margin-top:20px;">
    <p style="font-family:'Press Start 2P'; font-size:7px; color:#A0C0E0;">NutriDex v1.0</p>
</div>
""", unsafe_allow_html=True)