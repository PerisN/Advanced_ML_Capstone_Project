# Electricity Theft Detection.

## 1. Project Overview

Electricity theft is a major challenge for electricity distribution companies because it contributes to commercial energy losses, revenue losses, infrastructure damage and risks to public safety.

Traditional approaches to detecting electricity theft can involve inspections, investigations and analysis of meter readings. However, the increasing availability of smart-meter and electricity-consumption data creates an opportunity to use machine learning to automatically identify unusual consumption patterns.

This project investigates how machine learning and deep learning techniques can be used to analyse electricity-consumption patterns and classify consumption sequences as normal or associated with electricity theft.

The project is structured around two main objectives:

1. **Discover and visualize electricity-consumption patterns using dimensionality reduction and clustering.**
2. **Use time-series classification to determine whether consumption patterns are associated with normal consumption or electricity theft.**

> **Important dataset note:** Although the problem is motivated by the Kenyan electricity sector, this project does not use Kenyan electricity-consumption data. The study uses the publicly available TDD2022 electricity theft detection dataset, which was developed from Open Energy Data Initiative (OEDI) consumption data. The dataset contains synthetic theft scenarios designed for benchmarking electricity-theft detection methods.

---

# 2. Problem Statement

Electricity theft and other forms of non-technical electricity losses present challenges for electricity distribution systems in Kenya. Such losses can reduce utility revenue, affect the efficiency of electricity distribution, contribute to infrastructure problems and create safety risks.

According to EPRA (Energy and Petroleum Regulatory Authority), Kenya's average system losses were 23.36% during the 2024/2025 financial year, exceeding the allowable system-loss benchmark of 17.5%. EPRA identifies commercial losses as including electricity supplied through illegal connections, meter tampering and unmetered energy.

Kenya Power has also reported cases involving illegal electricity connections. For example, in 2025, an investigation into illegal connections in Meru County found an underground network supplying multiple borehole pumps. Kenya Power reported that the illegal connections contributed to transformer failures and estimated revenue losses of KSh 90.7 million over four years in that particular case.

The identification of electricity theft can be difficult because abnormal consumption may not always be obvious from individual meter readings. Theft can also occur through different manipulation patterns, meaning that consumption data may contain different patterns associated with normal and abnormal electricity use.

Therefore, this project investigates electricity-consumption patterns using clustering and dimensionality reduction and uses time-series classification to determine whether consumption sequences are associated with normal consumption or electricity theft. The TDD2022 benchmark dataset provides a controlled experimental environment for this investigation.

---

# 3. Research Aim

The main aim of this project is:

> **To investigate electricity-consumption patterns using dimensionality reduction and clustering and to classify electricity-consumption sequences as normal or associated with electricity theft using time-series classification.**

---

# 4. Research Questions

### Main Research Question

**How effectively can dimensionality reduction, clustering and time-series classification be used to analyse electricity-consumption patterns and identify electricity theft?**

### Specific Research Questions

1. **What consumption patterns distinguish normal electricity usage from electricity theft?**

2. **Do electricity-consumption patterns naturally form different groups, and do some of these groups correspond to abnormal or theft-related patterns?**

3. **How effectively can clustering techniques identify different electricity-consumption patterns?**

4. **How can dimensionality-reduction techniques help visualize the structure of electricity-consumption data?**

5. **How effectively can time-series classification models classify electricity-consumption sequences as Normal or Theft?**

6. **Which temporal patterns are associated with correct and incorrect electricity-theft classifications?**

---

# 5. Dataset

This project uses the **TDD2022 Electricity Theft Detection Dataset** :https://data.mendeley.com/datasets/c3c7329tjj/1

TDD2022 was developed from electricity-consumption data obtained from the Open Energy Data Initiative (OEDI). The dataset contains approximately **560,640 observations**, representing **16 different consumer types** and seven classes: normal consumption and six different theft types.

The data contains hourly energy-consumption measurements over a one-year period.

The seven target classes are:

- Normal
- Theft 1
- Theft 2
- Theft 3
- Theft 4
- Theft 5
- Theft 6

For the main time-series classification task, the theft categories will initially be combined into a single **Theft** class.

Therefore, the classification task will initially consist of:

- Normal
- Theft

The different theft categories can later be investigated if the initial classification task is successful.

### Dataset characteristics

| Characteristic | Description |
|---|---|
| Dataset | TDD2022 |
| Source | Open Energy Data Initiative (OEDI) |
| Approx. observations | 560,640 |
| Consumer types | 16 |
| Time resolution | Hourly |
| Time period | One year |
| Original target classes | 7 |
| Classification task | Normal vs Theft |
| Theft labels | Synthetic/controlled scenarios |

---

# 6. Project Methodology

The project follows two main objectives.

### Objective 1: Discover and visualize electricity-consumption patterns

**Raw electricity data**

↓

**Data cleaning and preprocessing**

↓

**Exploratory Data Analysis**

↓

**Feature engineering**

↓

**Dimensionality reduction**

↓

**Clustering**

↓

**Cluster interpretation**

### Objective 2: Classify electricity-consumption sequences

**Chronological electricity data**

↓

**Time-series feature engineering / sequence creation**

↓

**Training and testing split**

↓

**Logistic Regression + Random Forest baselines**

↓

**LSTM time-series model**

↓

**Model evaluation**

↓

**Error analysis**

---

# 7. Data Preprocessing

The preprocessing stage will prepare the electricity-consumption data for analysis and modelling.

This will include:

- Checking for missing values
- Removing or handling invalid observations
- Checking for duplicate records
- Examining class distributions
- Identifying numerical and categorical variables
- Scaling numerical variables where appropriate
- Organising observations chronologically for time-series modelling
- Creating suitable input sequences for the LSTM model

Special attention will be given to preventing **data leakage**.

Because the dataset contains repeated hourly observations from consumption profiles, individual rows will not be randomly split between training and testing. An appropriate **time-aware and/or consumer-aware splitting strategy** will be used so that highly related observations do not appear in both training and testing sets.

---

# 8. Exploratory Data Analysis

Exploratory analysis will be used to understand electricity-consumption behaviour before modelling.

The analysis will investigate:

- Distribution of electricity consumption
- Consumption patterns across consumer types
- Normal versus theft consumption
- Distribution of the target classes
- Correlations between consumption variables
- Hourly consumption patterns
- Differences between normal and theft consumption
- Outliers and unusual consumption patterns

Visualisations will include consumption distributions, correlation plots, time-series plots and class-distribution charts.

---

# 9. Dimensionality Reduction

Dimensionality-reduction techniques will be used to help visualize the structure of electricity-consumption data.

### PCA

PCA will be used to reduce the feature space to two or three dimensions and visualize whether different consumption patterns form distinguishable groups.

The PCA representation can be visualized using:

- Cluster assignments
- Normal/theft labels for interpretation
- Consumer types where appropriate

### t-SNE

t-SNE may also be used as an additional visualization technique.

It will remain an **optional visualization technique** rather than becoming another major modelling component.

The purpose of PCA and t-SNE is primarily **visual exploration**, rather than prediction.

---

# 10. Clustering

Clustering will be used as an **unsupervised exploration component**.

The theft labels will not be provided to the clustering algorithms when fitting the models.

The purpose is to investigate:

> **Do electricity-consumption patterns naturally form different groups, and do some of these groups correspond to abnormal or theft-related patterns?**

Meaningful consumption-profile features will be created, such as:

- Average consumption
- Peak consumption
- Consumption variability
- Daytime versus nighttime consumption
- Weekday versus weekend consumption
- Daily consumption summaries
- Other relevant consumption-pattern features

The project will investigate:

### K-Means Clustering

K-Means will group electricity-consumption patterns based on their similarity.

### DBSCAN

DBSCAN will investigate whether electricity-consumption patterns form dense groups and whether unusual observations can be identified as noise.

After clustering, the known theft labels may be used for interpretation and evaluation.

The analysis will investigate:

- What proportion of each cluster consists of normal observations?
- Are particular theft categories concentrated in certain clusters?
- Are some theft patterns mixed with normal consumption?
- Does DBSCAN identify unusual observations as noise?

The labels will therefore be used **after clustering** to understand what the discovered clusters represent, rather than as inputs when fitting the clustering models.

---

# 11. Time-Series Classification

Since electricity consumption is recorded hourly, the consumption data will be treated as **sequential/time-series data rather than independent rows**.

The main classification task will initially be:

> **Classify electricity-consumption sequences as Normal or Theft.**

The project will investigate whether previous consumption patterns contain enough information to classify a consumption sequence.

For example, a sequence could use the previous **24 hours** of consumption to classify the following observation or period.

### Traditional Machine Learning Baselines

The following models will be used as baseline comparisons:

- Logistic Regression
- Random Forest

These models will use appropriately engineered time-series features such as:

- Lagged consumption
- Rolling mean
- Rolling standard deviation
- Peak consumption
- Hour of day
- Day of week
- Other relevant temporal features

### LSTM

The LSTM will be the main deep-learning/time-series model.

Unlike the traditional models, the LSTM will receive sequences of observations so that it can learn temporal dependencies directly.

For example:

**Previous 24 hours of consumption**

↓

**LSTM**

↓

**Normal / Theft**

The LSTM will investigate whether temporal behaviour provides useful information for distinguishing normal consumption from electricity theft.

If the initial Normal vs Theft classification is successful, the different theft categories can later be investigated.

---

# 12. Model Comparison

The project will compare the different approaches according to their purpose.

| Objective | Model/Technique | Purpose |
|---|---|---|
| Dimensionality Reduction | PCA | Visualize the structure of consumption patterns |
| Dimensionality Reduction | t-SNE | Additional visualization of consumption patterns |
| Clustering | K-Means | Identify consumption groups |
| Clustering | DBSCAN | Identify consumption groups and unusual observations |
| Classification Baseline | Logistic Regression | Provide a traditional classification baseline |
| Classification Baseline | Random Forest | Provide a traditional machine-learning comparison |
| Time-Series Classification | LSTM | Model temporal consumption sequences |

---

# 13. Model Evaluation

### Clustering Evaluation

The clustering models will be evaluated using:

- **Silhouette Score**

The Silhouette Score will help determine how well observations fit within their assigned clusters compared with other clusters.

After clustering, the known TDD2022 labels will be used to investigate:

- Cluster composition
- Whether clusters correspond to normal or theft-related patterns
- Which theft categories are concentrated in particular clusters
- Whether some theft patterns are mixed with normal consumption
- Whether DBSCAN identifies unusual observations as noise

The labels will therefore be used for **evaluation and interpretation rather than as inputs to the clustering algorithms**.

### Classification Evaluation

The classification models will be evaluated using:

- Precision
- Recall
- F1-score
- Confusion matrix

These metrics will be used to compare Logistic Regression, Random Forest and LSTM for the Normal vs Theft classification task.

---

# 14. Error Analysis

After model evaluation, classification errors and clustering results will be investigated to understand where the models struggle.

The analysis will examine:

- Which theft patterns are most difficult to detect
- Which theft cases are classified as normal
- Which normal consumption patterns are incorrectly classified as theft
- Whether there are particular times of day where errors are more common
- Whether some consumer types are more difficult to classify
- Which temporal patterns appear to contribute to incorrect predictions
- Which observations are identified as noise by DBSCAN

The purpose is to explain **why the models succeed or fail**, rather than simply reporting which model has the highest metric.

---

# 15. Explainability

Model interpretation will focus on understanding the consumption patterns identified through clustering and classification.

For clustering, cluster profiles can be examined based on:

- Average consumption
- Peak consumption
- Consumption variability
- Daytime versus nighttime consumption
- Weekday versus weekend consumption
- Daily consumption patterns
- Consumer type

For the classification models, the analysis will investigate the temporal and consumption patterns associated with correct and incorrect predictions.

The goal is to understand:

> **Which electricity-consumption patterns are associated with normal consumption or electricity theft, and which patterns contribute to incorrect classifications?**

---

# 16. Limitations

Several limitations should be considered.

1. **The dataset is not Kenyan** - therefore, the findings cannot be directly generalised to Kenyan electricity consumers without validation using Kenyan data.

2. **The theft scenarios are synthetic** - TDD2022 was created by applying theft-generation techniques to consumption profiles. The labels therefore represent controlled simulated theft rather than confirmed theft cases.

3. **Real-world theft can be more complex** - actual electricity theft may involve behaviours and environmental factors that are not represented in the dataset.

4. **Model performance may depend on the dataset** - high performance on a benchmark dataset does not necessarily mean equivalent performance in a real electricity distribution network.

5. **Temporal leakage must be avoided** - because the data contains hourly observations from the same consumption profiles, random row-level splitting could result in highly related observations appearing in both training and testing sets. The project will therefore use an appropriate time-aware and/or consumer-aware splitting strategy.

---

# 17. Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- TensorFlow / Keras
- Streamlit

---

# 18. Project Structure

```text
electricity-theft-detection/
│
├── data/
│   └── README.md
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_dimensionality_reduction.ipynb
│   ├── 04_clustering.ipynb
│   ├── 05_classification.ipynb
│   └── 06_evaluation.ipynb
│
├── models/
│   ├── preprocessing/
│   └── lstm/
│
├── app/
│   └── app.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 19. Expected Outcome

At the end of the project, the study will provide:

1. An analysis of electricity-consumption patterns.
2. An investigation of natural consumption groups using K-Means and DBSCAN.
3. A visualization of consumption patterns using PCA and optionally t-SNE.
4. An investigation of whether some discovered clusters correspond to normal or theft-related patterns.
5. A comparison of Logistic Regression, Random Forest and LSTM for Normal vs Theft classification.
6. An evaluation of the classification models using precision, recall, F1-score and confusion matrices.
7. Error analysis explaining common classification errors and unusual patterns.
8. An investigation of temporal patterns associated with correct and incorrect predictions.

---

# 20. Conclusion

This project investigates electricity-theft detection by combining **dimensionality reduction, clustering and time-series classification**.

PCA and optionally t-SNE will be used to visualize the structure of electricity-consumption data. K-Means and DBSCAN will be used to investigate whether consumption patterns naturally form different groups and whether some groups correspond to abnormal or theft-related patterns.

For classification, the project will initially focus on distinguishing **Normal consumption from Theft**. Logistic Regression and Random Forest will provide traditional machine-learning baselines, while an LSTM will be used as the main deep-learning/time-series model to learn temporal dependencies from consumption sequences.

The project will emphasize **depth of analysis and interpretation**, including clustering interpretation, classification evaluation, error analysis and investigation of the temporal patterns associated with model predictions.