# ⚡ NutriDex — Pokémon-Style Calorie Tracker

> *Gotta Track 'Em All!*

**🔗 Live App:** [https://nutridex-calorie-calculator.streamlit.app/](https://nutridex-calorie-calculator.streamlit.app/)

NutriDex is a Pokémon GBA-themed calorie tracking web app built with **Streamlit** and a **K-Nearest Neighbors (KNN) Machine Learning model** that suggests Indian foods based on your daily macro needs.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red)
![ML](https://img.shields.io/badge/ML-KNN%20Model-green)
![Status](https://img.shields.io/badge/Status-Live-success)

---

## 🎮 Features

### 🧬 Trainer Profile
- Enter your age, height, weight, gender, activity level & goal
- Calculates **BMI**, **TDEE**, **daily calorie goal**
- Shows your **macro breakdown** (Protein, Carbs, Fat) with HP bars
- Assigns a **Pokémon** based on your BMI (Pikachu, Snorlax, Gastly, Munchlax)

### 🎒 Food Bag
- **Search** from 491 Indian foods with instant results
- **Manual input** — add custom foods with calories & macros
- Tracks daily totals and shows remaining calories

### 🤖 ML Food Suggestions
- Uses a **KNN (K-Nearest Neighbors)** model trained on the food dataset
- Suggests **food combos** that match your remaining daily macros
- **Random variety** — different suggestions every time you click
- Filters: Vegetarian / Non-Vegetarian / Exclude fast food
- **Portion Calculator** — tells you exactly how much of any food to eat

### 📋 Daily Quests
- To-do list for daily fitness habits
- Progress bar to track quest completion

### 🔐 Login System
- Create an account and login
- Profile data saved per user

---

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| **Python** | Core language |
| **Streamlit** | Web app framework |
| **Pandas** | Data processing |
| **scikit-learn** | KNN Machine Learning model |
| **Pickle** | Save/load trained ML model |

---

## 📂 Project Structure

```
calorie_app/
├── app.py              # Main Streamlit web app
├── data_prep.py        # ML model training script
├── food_model.pkl      # Trained KNN model (pickle file)
├── foods.csv           # Dataset of 491 Indian foods
├── requirements.txt    # Python dependencies
├── users.json          # User accounts (created at runtime)
└── README.md           # This file
```

---

## 🚀 How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/UDHAYA-UD/NutriDex.git
cd NutriDex

# 2. Install dependencies
pip install -r requirements.txt

# 3. Train the ML model (creates food_model.pkl)
python data_prep.py

# 4. Run the app
streamlit run app.py
```

---

## 🤖 Machine Learning Model

The app uses a **K-Nearest Neighbors (KNN)** algorithm to recommend foods:

1. **Training**: `data_prep.py` reads `foods.csv` and trains the model on 4 features — Calories, Protein, Carbs, Fat
2. **Scaling**: Uses `StandardScaler` to normalize the data
3. **Prediction**: Given your remaining daily macros, the model finds the closest matching foods using Euclidean distance
4. **Output**: Saved as `food_model.pkl` using Python's `pickle` library

---

## 📊 Dataset

- **491 Indian foods** covering: Grains, Protein, Dairy, Fruits, Vegetables, Meals, Snacks, Sweets, Drinks, Fast Food, Oils, Supplements
- Each food has: `name`, `calories`, `protein`, `carbs`, `fat`, `category`, `veg` (True/False)
- Source: Kaggle

---

## 🎨 Theme

Styled after **Pokémon GBA games** (FireRed/LeafGreen):
- Blue gradient background
- Light cream dialog boxes with pixel borders
- Press Start 2P pixel font for headings
- GBA-style HP bars, badges, and buttons
- Pokémon sprites from [PokeAPI](https://pokeapi.co/)

---

## 👨‍💻 Author

**UDHAYA**

---

*Made with ❤️ and Pokéballs*
