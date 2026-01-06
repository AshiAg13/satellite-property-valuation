# Satellite Imagery Based Property Valuation

This project explores a multimodal regression approach for residential property valuation by combining structured housing data with satellite imagery–based visual features. The objective is to study how neighborhood-level visual context can be incorporated into traditional tabular valuation models and to analyze its impact on predictive performance.

---

## Project Overview

Property prices are influenced by both intrinsic characteristics, such as size and construction quality, and extrinsic factors related to location and surrounding infrastructure. While traditional machine learning models rely primarily on structured tabular data, satellite imagery provides additional contextual information about neighborhoods that is not explicitly captured by numerical features.

In this project:
- Satellite images are programmatically acquired using latitude and longitude
- A pretrained convolutional neural network (CNN) is used to extract visual embeddings
- Tabular and image features are combined to form a multimodal regression model
- Performance is analyzed through comparison with a tabular-only baseline
- Explainability of visual features is demonstrated using Grad-CAM

---

## Dataset Description

The dataset contains residential property records with structured attributes including number of bedrooms, bathrooms, living area, lot size, construction grade, and geographical coordinates. The target variable is the market price of the property.

Satellite images corresponding to each property location are fetched using geographical coordinates to capture neighborhood-level context.

---

## Data Preprocessing and Feature Engineering

The preprocessing pipeline includes removal of duplicate records and non-informative columns, followed by feature engineering based on domain knowledge. Derived features such as property age, basement area ratio, and neighborhood-relative living area were created to enhance model interpretability and learning.

Exploratory data analysis and geospatial analysis were performed to study feature relationships and spatial patterns in the data.

---

## Satellite Image Acquisition

Satellite images are programmatically fetched using a static maps API based on latitude and longitude coordinates. Image downloading is automated using a Python script to ensure reproducibility.

Raw satellite images are not included in the repository and are generated as needed.

---

## Image Feature Extraction

A pretrained ResNet-18 convolutional neural network is used as a feature extractor. The final classification layer is removed, and each satellite image is converted into a 512-dimensional embedding vector representing neighborhood-level visual characteristics.

---

## Modeling Approach

A Random Forest Regressor is used for prediction.

First, a tabular-only baseline model is trained using structured features.  
Next, a multimodal model is trained by concatenating tabular features with satellite image embeddings. Model performance is evaluated using RMSE and R², and results from both approaches are analyzed.

---

## Explainability Using Grad-CAM

Grad-CAM is applied to the CNN feature extractor on a small set of satellite images to visualize salient regions influencing feature extraction. The resulting heatmaps indicate attention to road networks, built-up areas, and green spaces, providing qualitative interpretability of the learned visual features.

---

## Results and Observations

The tabular-only model achieved stronger quantitative performance on the validation set. This suggests that structured features already capture strong predictive signals for property valuation. The multimodal framework, while not outperforming the baseline in this setting, demonstrates how satellite imagery can be integrated into valuation pipelines and highlights challenges related to feature alignment and high-dimensional visual data.

---

## Deliverables

- Code: Jupyter notebooks and Python scripts in this repository  
- Prediction file: `outputs/24118012_final.csv`  
- Final report: `report/24118012_report.pdf`

---

## How to Run (High-Level)

1. Run the preprocessing notebook to clean data and perform EDA  
2. Use the image fetching script to download satellite images  
3. Extract image embeddings using a pretrained CNN  
4. Run the model training notebook to train models and generate predictions  

---

## Conclusion

This project provides a practical exploration of multimodal learning for real estate valuation. It demonstrates both the potential and the limitations of incorporating satellite imagery into structured prediction tasks, offering a balanced and realistic perspective on multimodal machine learning in applied settings.
