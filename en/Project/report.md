# Project Report: Image Recommendation System

## 1. Introduction

- **Project Goal**: Briefly describe the main objective of your project, which is to recommend images based on user preferences.
- **Scope**: Mention the key tasks involved, such as data collection, annotation, analysis, visualization, recommendation system development, testing, and reporting.

## 2. Data Collection

- **Sources**: Describe the sources of your open-licensed images and any specific criteria used for selection.
- **Automation**: Explain the automated approaches used for downloading images and collecting metadata.
- **Metadata**: List the types of metadata collected (e.g., image size, format, orientation, creation date, camera model).

## 3. Labeling and Annotation

- **Process**: Detail the process of labeling and annotating images, including any automated tools or algorithms used.
- **Additional Information**: Mention additional data collected, such as predominant colors and user tags.
- **User Involvement**: Describe how users were involved in the tagging process and any automation efforts in this area.

## 4. Data Analyses

- **User Preferences**: Explain how user preferences were analyzed to build user profiles.
- **Techniques**: Describe the types of analyses performed, including any data mining or machine learning models used.
- **Tools**: Mention the use of libraries like Pandas and Scikit-learn.

## 5. Data Visualization

In this section, we visualize and analyze the dataset to understand its key characteristics and how they relate to the recommendation system. The visualization is divided into two main parts.

### Dataset Evaluation and Representation

First, we evaluate and represent the dataset by focusing on key characteristics relevant to our recommendation system. Specifically, attributes such as "camera make," "orientation," and predominant colors are analyzed, as they will be used in the recommendation process.

To provide meaningful insights, we compare the dataset’s overall distribution (represented in blue) with the images selected by the user (represented in red). This allows us to visualize the distribution of user-selected images and identify trends in user preferences.

### User Data Representation

In the second part, we visualize the user preference data computed in Section 4 (Data Analysis). This graphical representation helps in understanding user choices more intuitively. To improve clarity, proportions below 10% are grouped under the "Other" category.

For all visualizations, we utilize **Matplotlib**, a powerful Python library for data visualization, ensuring clear and interpretable representations of our dataset and user preferences.

---

## 6. Recommendation System

The recommendation system was built using a structured approach, starting with data preparation, followed by model training and selection, and finally testing and feature importance analysis.

### Data Preparation

First, we extract data from different sources and consolidate them into **dataframes**, which are easier to manipulate and analyze. This step ensures consistency and allows seamless integration of various metadata attributes into the recommendation pipeline.

### Data Splitting

To build and evaluate the recommendation system effectively, we split the data into two parts:
- **Training set (75%)**: Used to train the models.
- **Test set (25%)**: Used to evaluate model performance.

Splitting the data in this way helps prevent overfitting and ensures the models generalize well to new data.

### Model Comparison

We compare multiple classification models to determine the best-performing approach:
- **Logistic Regression**
- **Support Vector Machine (SVM)**
- **DecisionTreeClassifier**
- **Random Forest**

For each method, we employ **GridSearchCV** to test different parameter combinations and find the best-performing configuration. This ensures optimal model performance.

The results indicate that **DecisionTreeClassifier** performs the worst (accuracy: 0.88), while the other models achieve an accuracy of **0.92**. Additionally, **Random Forest** takes longer to execute, likely due to the following parameter grid:
```python
param_grid = {
    'n_estimators': [50, 100, 200, 250],
    'max_depth': [None, 10, 20],
    'criterion': ['gini', 'entropy', 'log_loss']
}
```
The increased execution time is likely due to the **n_estimators** parameter, which defines the number of trees in the forest. More trees generally improve accuracy but increase computational cost.

### Model Selection

Since the models (excluding DecisionTreeClassifier) perform similarly, we choose **Random Forest** for our recommendation system. This decision is based on prior experience in coursework and its robust performance across various datasets.

### Feature Importance Analysis

To further understand the recommendation process, we analyze the feature importance when predicting user preferences. The results are as follows:

| Feature              | Importance |
|----------------------|------------|
| openingDate         | 0.267866    |
| object_tags         | 0.256373    |
| predominant_colors  | 0.209164    |
| make               | 0.133714    |
| state              | 0.112226    |
| orientation        | 0.020657    |

These results show that **openingDate** and **object_tags** are the most influential factors in determining user preferences, while **orientation** has the least impact.

This detailed analysis provides insights into the key components driving recommendations, ensuring a more transparent and interpretable system.


## 7. Tests

- **Functional Tests**: Describe the tests conducted to ensure the functionality of different components.
- **User Tests**: Explain how the recommendation system was tested with users.
- **Verification**: Mention the methods used to verify the system's performance.

## 8. Conclusion

While our recommendation system performs well, we acknowledge several limitations related to the dataset. The available dataset provides a limited amount of metadata, which constrains the model's ability to make highly accurate predictions. A richer dataset with more detailed attributes, such as user interactions, additional contextual metadata, or higher-quality image annotations, could significantly enhance the performance of the system.

One way to overcome dataset limitations is through data augmentation. In image-related machine learning tasks, data augmentation involves applying transformations such as:

Rotation

Cropping

Grayscale conversion

Brightness and contrast adjustments

By implementing these techniques, we could artificially expand our dataset and improve the model's ability to generalize, leading to better recommendations. Future work could explore the integration of these augmentation methods to further optimize the system.