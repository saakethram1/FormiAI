# Nearest Moustache Property API

This project is a backend API built with **FastAPI** to help tele-callers quickly find Moustache properties within a **50km radius** of any city, state, or area in India. It integrates a fast LLM using **Groq** to smartly extract locations from natural-language queries and uses Redis to cache results for fast responses.

---

## 🚀 Features
- Accepts free-form location queries like: _"Near Goa or Mount Abu"_
- Uses LLM (`llama3-8b-8192` on Groq) to extract relevant places
- Geocodes locations and finds all nearby properties from CSV
- Responds under 2 seconds using Redis caching
- Clean FastAPI backend with `/nearest-properties` and `/start` routes
