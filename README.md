# Demand Forecasting App

This is a **Demand Forecasting App** built with Streamlit. It forecasts product demand based on historical sales data, displays the top 10 products, and provides users with interactive tools to view demand trends and forecasts for specific stock codes.

## 🛠️ Features

- **Top 10 Products**: Displays a bar chart of the top 10 products based on sales quantity.
- **Interactive Stock Code Input**: Users can select a stock code to view detailed historical demand and future demand forecasts for the next 15 weeks.
- **Time Series Plot**: Combines actual historical demand and predicted future demand for selected products.
- **Error Histograms**: Separate histograms displaying error distributions for training and test datasets.

## 🚀 Live App

Check out the live app here: [Demand Forecasting App](https://demand-forecasting-app-dmgpaxd59vbr7bs6h7sdkg.streamlit.app/)

## 🖥️ How to Run Locally

### Prerequisites

- **Python 3.7 or higher**
- Install the required dependencies listed in `requirements.txt`.

### Steps to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Satyam0775/demand-forecasting-app.git

demand-forecasting-app/
├── app.py                # The main Streamlit app script
├── ProductInfo.csv       # Sample dataset used for forecasting
├── requirements.txt      # Python dependencies file
├── README.md             # Project documentation

⚙️ Technology Stack
Frontend: Streamlit
Backend: Python (Pandas, NumPy)
Visualization: Matplotlib
Data: CSV file containing historical sales data

✨ Features to Improve
Add more sophisticated models (e.g., ARIMA, LSTM) for demand forecasting.
Enhance visualizations with more interactive plots.
Enable CSV downloads for the forecasted data.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page if you have any suggestions or find bugs.

🧑‍💻 Author
Satyam - Satyam0775
