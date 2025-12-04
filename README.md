# Financial Calculator

A simple Python toolkit for common financial calculations, including:

- Bond price (with or without coupons)
- Duration of a single bond or an entire portfolio
- Monthly mortgage payment and total interest paid

This project is designed as an educational tool for practicing Python applied to finance.

---

## 📌 Features

### **1. Bond Price Calculation**
Supports:
- Zero-coupon bonds  
- Coupon bonds with customizable:
  - Yield to Maturity (YTM)
  - Coupon rate
  - Maturity
  - Number of coupon payments per year  

The formula discounts each cash flow individually.

---

### **2. Portfolio Duration**
You can calculate:
- The duration of a single bond  
- The duration of a portfolio composed of multiple bonds  

Portfolio duration is computed as the weighted average:

\[
D_{port} = \sum_{i=1}^{n} w_i \cdot D_i
\]

Where:

\[
w_i = \frac{P_i}{\sum P_i}
\]

---

### **3. Mortgage Payment**
Computes:
- Monthly payment  
- Total interest paid  

Using the standard amortization formula:

\[
R = C \cdot \frac{i(1+i)^n}{(1+i)^n - 1}
\]

---

## 🚀 How to Run the Program

1. Make sure you have **Python 3** installed.  
2. Download or clone this repository.  
3. Run the script:


