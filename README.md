🎵 Spotify Virality Prediction Engine
A Full-Stack Data Science & Engineering Case Study
🚀 Project Overview
This project is an end-to-end machine learning pipeline designed to predict the "Viral Probability" of music tracks using a dataset of 176,000+ songs. Beyond simple modeling, this project serves as a demonstration of high-level data engineering, database management, and resilient problem-solving in a hybrid-cloud environment.

🛠️ The Technical Stack
Language: Python 3.10+

Database: PostgreSQL (Relational storage & SQL-based feature engineering)

Libraries: Pandas, Scikit-Learn (RandomForest), SQLAlchemy, Imbalanced-Learn (SMOTE), Seaborn

Infrastructure: Google Colab, VS Code, ngrok (TCP Tunneling for database-to-cloud connection)

🧠 Key Technical Challenges & Solutions (The "Engineering Log")
A recruiter's favorite section. This highlights your resilience.

1. Relational Integrity & Database Recovery
Challenge: Encountered index corruption during the transition from raw CSV to PostgreSQL, resulting in "Zebra" indices (0, 1, 2...) overwriting the unique Spotify track_id.

Solution: Built a standalone Python-driven Recovery Script using SQLAlchemy to drop the corrupted schema and re-map the 22-character Spotify hashes, ensuring 100% relational integrity between the track and audio_features tables.

2. Handling Class Imbalance
Challenge: Viral tracks represent less than 5% of the dataset, creating a significant bias in standard classification models.

Solution: Implemented SMOTE (Synthetic Minority Over-sampling Technique) to balance the training set, allowing the Random Forest model to identify the subtle audio "signatures" of viral hits without overfitting.

3. Hybrid-Cloud Infrastructure Pivot
Challenge: Local visualization tools (Power BI) were too rigid for the desired custom aesthetics, but cloud environments (Google Colab) could not natively access the local PostgreSQL database.

Solution: Architected a Secure TCP Tunnel using ngrok. When network latency persisted, I pivoted to a Static Data Snapshot (CSV) strategy to ensure project delivery, demonstrating the ability to choose reliability over architectural complexity when meeting deadlines.

📊 Data Insights: The "Viral Signature"
The model identified several key "green flags" for track virality:

The Energy-Danceability Sweet Spot: Viral tracks consistently cluster in high-energy (0.7+) and high-danceability (0.6+) quadrants.

Valence as a Predictor: Positive musical "mood" (Valence) showed a stronger correlation with virality than tempo or loudness.

🎯 How to Run
Clone the Repo: git clone https://github.com/your-username/spotify-viral-prediction.git

Restore Database: Run db_recovery.py to initialize the PostgreSQL schema.

Train Model: Open the Jupyter Notebook to run the Random Forest pipeline.

Visualize: Run the Seaborn script to generate the virality insights report.
