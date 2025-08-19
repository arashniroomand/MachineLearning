### **Coefficient of Determination (R²) - Explanation with Example**

The **Coefficient of Determination (R²)** is a statistical measure that indicates how well a regression model explains and predicts the outcomes of a dependent variable based on the independent variables. It ranges from **0 to 1** (or **0% to 100%**) and represents the proportion of variance in the dependent variable that is predictable from the independent variables.

- **R² = 0** → The model explains none of the variability.
- **R² = 1** → The model explains all the variability.
- **Higher R²** → Better the model fits the data.

---

### **Formula:**
\( R² = 1 - \frac{SS_{res}}{SS_{tot}} \)
where:
- \(SS_{res}\) = Sum of Squares of Residuals (errors)
- \(SS_{tot}\) = Total Sum of Squares (variance in data)

---

### **Example: Predicting House Prices**
Suppose we want to predict house prices based on their size (in square feet). We collect data and fit a linear regression model:

| House Size (sq. ft) | Actual Price ($) | Predicted Price ($) |
|---------------------|------------------|---------------------|
| 1000                | 200,000          | 210,000             |
| 1500                | 250,000          | 260,000             |
| 2000                | 300,000          | 310,000             |
| 2500                | 350,000          | 360,000             |

#### **Step 1: Calculate Residuals (Errors)**
\[
SS_{res} = \sum (Actual - Predicted)^2 = (200k-210k)^2 + (250k-260k)^2 + (300k-310k)^2 + (350k-360k)^2 = 400,000
\]

#### **Step 2: Calculate Total Sum of Squares**
First, find the **mean** of actual prices:
\[
\bar{Y} = \frac{200k + 250k + 300k + 350k}{4} = 275,000
\]
Now compute:
\[
SS_{tot} = \sum (Actual - Mean)^2 = (200k-275k)^2 + (250k-275k)^2 + (300k-275k)^2 + (350k-275k)^2 = 1,250,000
\]

#### **Step 3: Compute R²**
\[
R² = 1 - \frac{SS_{res}}{SS_{tot}} = 1 - \frac{400,000}{1,250,000} = 1 - 0.32 = 0.68
\]

#### **Interpretation:**
- **R² = 0.68 (or 68%)** → **68% of the variation in house prices** is explained by the house size.
- The remaining **32%** is due to other factors (e.g., location, age, etc.).

---

### **Key Takeaways:**
✅ **Higher R² = Better Fit** (but beware of overfitting!)  
✅ **Used in Regression Models** (Linear, Multiple, Polynomial)  
✅ **Does Not Imply Causation** (only correlation)  

### **What is a "Satisfactory" R² (Coefficient of Determination) Score?**

There is **no universal threshold** for a "good" R² value because its acceptability depends on:
- **The field of study** (social sciences vs. physics vs. finance)
- **The complexity of the problem** (some phenomena are inherently noisy)
- **The purpose of the model** (prediction vs. explanation)

However, here are **general guidelines**:

| **R² Range**       | **Interpretation**                                                                 |
|---------------------|-----------------------------------------------------------------------------------|
| **0 - 0.3**         | Very weak explanation (may not be useful)                                         |
| **0.3 - 0.5**       | Weak but acceptable in social sciences (human behavior is hard to predict)        |
| **0.5 - 0.7**       | Moderate (decent for many real-world models)                                      |
| **0.7 - 0.9**       | Strong (good for engineering, physics, or controlled experiments)                |
| **0.9 - 1.0**       | Very strong (but may indicate overfitting or artificial data)                    |

---

### **Key Considerations:**
1. **Field-Specific Norms:**
   - **Social Sciences (Psychology, Economics):** R² of **0.2 - 0.5** may be acceptable because human behavior is complex.
   - **Physical Sciences (Physics, Chemistry):** R² **> 0.8** is often expected due to precise measurements.
   - **Machine Learning/Finance:** Depends on the problem—sometimes even **R² = 0.1** can be profitable if the effect is consistent.

2. **Adjusted R² for Multiple Regression:**
   - If you add more variables, R² **always increases**, even if the new variables are useless.  
   - **Use Adjusted R²** instead, which penalizes unnecessary predictors.

3. **Overfitting Risk:**
   - An R² **too close to 1.0** (e.g., 0.99) may mean the model is memorizing noise rather than learning patterns.

4. **Compare to Baseline:**
   - If a simple model (e.g., mean prediction) gives R² = 0, your model should do significantly better.

---

### **Example: Is R² = 0.6 Good?**
- **In psychology?** → **Yes!** (Explaining 60% of human behavior is impressive.)  
- **In a physics lab?** → **No!** (Experiments should explain >90% of variability.)  

---

### **When to Worry:**
⚠️ **R² < 0.1** → The model is barely better than guessing the mean.  
⚠️ **R² > 0.95** → Check for data leakage or overfitting.  

Would you like help interpreting R² for your specific use case? 😊