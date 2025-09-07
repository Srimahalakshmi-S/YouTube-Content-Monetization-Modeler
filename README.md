# YouTube-Content-Monetization-Modeler

💡 Problem Statement

YouTube creators and media companies need to forecast revenue for content strategy, ad planning, and income estimation. This project predicts ad revenue using video performance and contextual features.

🛠 Key Features

Revenue Prediction: Input video metrics to get estimated ad revenue.

Feature Engineering: Engagement rate, watch time ratio, views per minute.

Interactive Visuals: Input summary and bar chart of key metrics.

Preprocessing & Modeling: Handles missing values, categorical encoding, and applies the best regression model.

📊 Tech Stack

Python, Pandas, Numpy

Scikit-learn (Linear Regression, Random Forest, Gradient Boosting)

Streamlit (Web App)

Matplotlib / Seaborn for visualizations

📈 Business Use Cases

Content Strategy Optimization – Identify high-return content.

Revenue Forecasting – Predict expected income.

Creator Support Tools – Analytics for YouTubers.

Ad Campaign Planning – Forecast ROI based on content metrics.

📂 Dataset

Format: CSV (~122k rows)

Target: ad_revenue_usd

Key Features: views, likes, comments, watch_time_minutes, video_length_minutes, subscribers, category, device, country

⚡ How to Run

Clone the repository:

git clone <repo_link>


Install dependencies:

pip install -r requirements.txt


Run the Streamlit app:

streamlit run app.py

📈 Evaluation Metrics

R² Score

RMSE

MAE

Visual insights and model explanation
