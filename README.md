# 🎬 Movie Recommender System (Streamlit App)

This project is a **content-based movie recommendation system** built using **Python and Streamlit**.  
It recommends similar movies based on textual similarity and displays **real-time movie posters** using the **TMDB API**.

---

## 📌 Overview

Given a selected movie, the system suggests **top 5 similar movies** using:
- NLP-based feature extraction
- Cosine similarity
- Precomputed similarity matrix
- Live poster fetching from TMDB

The application provides an **interactive and visually appealing UI** built with Streamlit.

---

## ✨ Features

- 🎥 Content-based movie recommendations
- 🧠 NLP-based similarity using cosine similarity
- 📊 Precomputed similarity matrix for fast results
- 🖼️ Live movie posters fetched from TMDB API
- 🎨 Custom background & UI styling with CSS
- ⚡ Fast and interactive Streamlit interface

---

## 🛠️ Tech Stack

| Category | Technology |
|--------|-----------|
| Language | Python |
| Web App | Streamlit |
| ML / NLP | Scikit-learn |
| Data Handling | Pandas, Pickle |
| API | TMDB API |
| Similarity | Cosine Similarity |

---

## 📂 Project Structure

```text
Movie-Recommender-Streamlit/
│── app.py                  # Streamlit application
│── movies_dict.pkl         # Serialized movie metadata
│── similarity.pkl          # Precomputed similarity matrix
│── README.md
```

---

## ⚙️ How It Works
1. Load preprocessed movie data and similarity matrix
2. User selects a movie from the dropdown
3. The system finds the most similar movies using cosine similarity
4. Movie posters are fetched dynamically using the TMDB API
5. Results are displayed in a clean, responsive UI

---

## 🚀 How to Run Locally
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Naman-27072004/movie-recommendation-system.git
cd movie-recommender-streamlit
```
### 2️⃣ Install Dependencies
```bash
pip install streamlit pandas scikit-learn request
```
### 3️⃣ Run the App
```bash
streamlit run app.py
```
The app will open in your browser at:
```bash
http://localhost:8501
```

---

## 🧪 Example Output
- Select a movie from the dropdown
- Click “Show Recommendation”
- Get 5 similar movies with posters displayed

---

## ⚠️ Notes
- TMDB API key is required for fetching posters
- If the API fails, a placeholder image is shown
- This is a content-based recommender, not collaborative filtering

---

## 🔮 Future Improvements
- Add search functionality
- Use TF-IDF for better text representation
- Deploy on Streamlit Cloud
- Add user ratings & collaborative filtering
- Improve recommendation ranking logic

---

## 🧾 License
This project is licensed under the MIT License.

---

## 📬 Author
- Naman Gupta
- MCA @ JIMS Rohini
- Full-Stack Developer | AI & ML Enthusiast

