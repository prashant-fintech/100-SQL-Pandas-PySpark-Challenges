# 📊 Classifying Ad Performance Based on Sales

## 📝 Problem Statement

Following a recent advertising campaign, the marketing department wishes to classify its efforts based on the **total number of units sold** for each product.

### 🎯 Task
You have been tasked with:
1. Calculating the **total number of units sold** for each product.
2. Categorizing **ad performance** based on the following criteria:

| Items Sold   | Ad Performance |
|-------------|---------------|
| 30+         | **Outstanding** |
| 20 - 29     | **Satisfactory** |
| 10 - 19     | **Unsatisfactory** |
| 1 - 9       | **Poor** |

### 📌 Expected Output
Your output should contain:
- **Product ID**
- **Total Units Sold** (sorted in **descending order**)
- **Categorized Ad Performance**
# 📊 Sample Dataset for Ad Performance Classification

## 📝 Dataset Structure

The dataset contains **sales transaction records**, including details such as user purchases, product IDs, quantities, and prices.

| Column Name   | Description |
|--------------|------------|
| `user_id`    | Unique identifier for the customer |
| `created_at` | Timestamp of the purchase |
| `product_id` | Unique identifier for the product |
| `quantity`   | Number of units purchased |
| `price`      | Price per unit of the product |

---

## 📋 Sample Data

```plaintext
user_id  | created_at           | product_id | quantity | price  
---------|----------------------|------------|----------|------
101      | 2023-06-01 08:30:00  | 501        | 4        | 50  
102      | 2023-06-02 14:20:00  | 507        | 2        | 120  
103      | 2023-06-03 17:45:00  | 509        | 6        | 89  
104      | 2023-06-04 12:15:00  | 515        | 3        | 220  
105      | 2023-06-05 09:50:00  | 503        | 5        | 75  
106      | 2023-06-06 10:30:00  | 512        | 2        | 150  
107      | 2023-06-07 15:10:00  | 514        | 7        | 99  
108      | 2023-06-08 11:40:00  | 505        | 3        | 135  
109      | 2023-06-09 13:00:00  | 510        | 4        | 180  
110      | 2023-06-10 16:25:00  | 508        | 1        | 260  
111      | 2023-06-11 07:50:00  | 506        | 3        | 95  
112      | 2023-06-12 20:05:00  | 501        | 2        | 50  
113      | 2023-06-13 09:30:00  | 511        | 5        | 200  
114      | 2023-06-14 21:15:00  | 516        | 6        | 80  
115      | 2023-06-15 18:00:00  | 507        | 2        | 120  
116      | 2023-06-16 08:45:00  | 509        | 4        | 89  
117      | 2023-06-17 12:10:00  | 515        | 3        | 220  
118      | 2023-06-18 19:30:00  | 503        | 7        | 75  
119      | 2023-06-19 14:50:00  | 512        | 2        | 150  
120      | 2023-06-20 10:20:00  | 514        | 5        | 99  

