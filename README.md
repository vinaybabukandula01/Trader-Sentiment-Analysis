# Trader Sentiment Analysis

## Objective

Analyze the relationship between **Bitcoin market sentiment (Fear vs Greed)** and **trader behavior and performance** on the Hyperliquid platform.
The goal is to identify patterns that can help inform **smarter trading strategies**.

---

## Datasets

This project uses two datasets provided in the assignment.

### 1. Bitcoin Market Sentiment (Fear / Greed)

Contains daily sentiment classification of the Bitcoin market.

Columns include:

* Date
* Classification (Fear / Greed)

Dataset Link:
https://drive.google.com/file/d/1PgQC0tO8XN-wqkNyghWc_-mnrYv_nhSf/view

---

### 2. Historical Trader Data (Hyperliquid)

Contains detailed trading activity including:

* account
* symbol
* execution price
* size
* side (Long / Short)
* timestamp
* closedPnL
* leverage
* event

Dataset Link:
https://drive.google.com/file/d/1IAfLZwu6rJzyWKgBToqwSmmVYU6VbjVs/view

---

## Methodology

### 1. Data Cleaning

* Loaded both datasets using **Pandas**
* Checked for missing values and duplicates
* Converted timestamps to proper datetime format
* Extracted **daily date values**

### 2. Data Alignment

Trader data and sentiment data were merged using the **date column** to align trading activity with market sentiment.

### 3. Feature Engineering

Key metrics created for analysis:

* **Daily PnL per trader**
* **Win rate**
* **Average trade size**
* **Leverage distribution**
* **Number of trades per day**
* **Long vs Short trade ratio**

---

## Analysis

The analysis focused on understanding how **market sentiment affects trader behavior**.

Key questions explored:

* Does trading performance differ between **Fear vs Greed** days?
* Do traders change behavior based on sentiment?
* How do leverage, trade frequency, and position size change with sentiment?

Charts and visualizations were created to support the findings.

---

## Trader Segmentation

Traders were grouped into behavioral segments such as:

* **High vs Low leverage traders**
* **Frequent vs Infrequent traders**
* **Consistent winners vs inconsistent traders**

This segmentation helped reveal different trading patterns across sentiment conditions.

---

## Key Insights

### Insight 1

Trader profitability tends to improve during **Greed sentiment periods**, suggesting that bullish markets may support more profitable trading opportunities.

### Insight 2

Trading activity increases during **Fear sentiment**, indicating that traders react more aggressively during volatile or uncertain market conditions.

### Insight 3

Position sizes tend to increase during **Greed periods**, reflecting increased risk appetite when the market outlook is positive.

---

## Strategy Recommendations

Based on the analysis, the following strategy ideas were proposed:

### Strategy 1

During **Fear sentiment**, traders should consider **reducing leverage and position size** to minimize exposure to volatility.

### Strategy 2

During **Greed sentiment**, experienced or high-performing traders may benefit from **increasing position sizes**, as bullish trends may improve trade outcomes.

---

## Project Structure

```
Trader-Sentiment-Analysis
│
├── analysis.ipynb      # Data analysis notebook
├── app.py              # Streamlit dashboard (optional)
└── README.md           # Project documentation
```

---

## Tools & Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Streamlit (optional dashboard)

---

## Conclusion

This project demonstrates how **market sentiment influences trader behavior and performance**.
Understanding these patterns can help traders adjust strategies based on **market psychology**, potentially improving risk management and profitability.

---

## Author

Kandula Vinay Babu
