# Project Report: Image Recommendation System

## 1. Introduction

## 1. Introduction

### Project Goal

The primary objective of this project is to develop an image recommendation system that suggests images based on user preferences. By leveraging data collection, annotation, analysis, and visualization techniques, we aim to create a personalized user experience that accurately reflects individual tastes and interests.

### Scope

The project encompasses several key tasks:

- **Data Collection**: Gathering a diverse set of open-licensed images and their associated metadata.
- **Labeling and Annotation**: Enhancing the dataset with meaningful labels and annotations to facilitate analysis and recommendation.
- **Data Analysis**: Understanding user preferences by examining selected images and their metadata.
- **Data Visualization**: Creating visual representations of the dataset and user preferences to gain insights and identify trends.
- **Recommendation System Development**: Building and evaluating a recommendation system using machine learning models.
- **Testing**: Conducting functional and user tests to ensure the system's performance and reliability.
- **Reporting**: Documenting the project's findings, challenges, and future improvements in a comprehensive report.

## 2. Data Collection

### Overview

The data collection phase of this project focused on gathering a set of open-licensed images and their associated metadata. The primary source for this data was Wikidata, a collaborative knowledge base that provides structured data about various topics. The goal was to collect images of railway stations in France, along with relevant metadata, to facilitate further analysis and recommendation tasks.

### Data Source

- **Wikidata**: We utilized Wikidata to query for railway stations in France that have associated images. The query was designed to retrieve essential metadata such as station names, opening dates, coordinates, and image URLs. Wikidata was chosen for its reliability and the availability of open-licensed images.

### Automation Process

1. **Query Execution**:
   - A SPARQL query was executed on Wikidata to select railway stations in France with available images. The query included filters to ensure that only stations with images and specific metadata (e.g., opening dates, coordinates) were retrieved.

2. **Image Download**:
   - The retrieved image URLs were used to download the images programmatically. A Python script was developed to handle the download process, ensuring that each image was saved locally with a meaningful filename derived from the station name.

3. **Metadata Extraction**:
   - Alongside the images, metadata such as image size, format, and orientation were extracted using the EXIF data embedded in the image files. This information was stored in a JSON file for easy access and analysis.

### Implementation Details

- **Libraries Used**:
  - `urllib`: For sending HTTP requests to download images.
  - `PIL` (Python Imaging Library): For opening images and extracting EXIF metadata.
  - `json`: For handling JSON data, which was used to store the metadata.

- **Storage**:
  - Images were stored in a local directory named `images`.
  - Metadata was saved in a JSON file for easy access and further processing.

### Challenges and Solutions

- **Handling Missing Data**:
  - The query and script were designed to handle optional metadata fields gracefully. If certain metadata (e.g., closing date, city names) were missing, the script continued processing without interruption.

- **Ensuring Uniqueness**:
  - The use of coordinates in the query helped ensure the uniqueness of the stations, preventing duplicate entries.

### Future Improvements

- **Expanding the Dataset**:
  - Future iterations could include a more diverse set of images, such as those from different countries or categories, to enhance the recommendation system's robustness.

- **Enhancing Metadata Extraction**:
  - Additional metadata, such as color profiles or more detailed EXIF data, could be extracted to provide richer information for analysis.

### Conclusion

The data collection phase was successfully automated, resulting in a dataset of over 100 images with associated metadata. This dataset forms the foundation for subsequent tasks, including labeling, analysis, visualization, and the development of the recommendation system. The use of Wikidata ensured that the images were open-licensed.

## 3. Labeling and Annotation

### Overview

The labeling and annotation phase of this project focused on enhancing the dataset by adding meaningful labels and annotations to each image. This process involved extracting additional metadata, identifying predominant colors, and using machine learning models to detect objects within the images. The goal was to enrich the dataset with information that could be used for further analysis and recommendation tasks.

### Process

1. **EXIF Data Extraction**:
   - The EXIF data, which includes technical details such as image size, format, and orientation, was extracted from each image. This data is crucial for understanding the basic characteristics of the images.

2. **Color Analysis**:
   - The predominant colors in each image were identified using a clustering algorithm (K-Means). This information helps in understanding the visual aesthetics of the images and can be used to recommend images based on color preferences.

3. **Object Detection**:
   - A pre-trained ResNet50 model was used to detect objects within the images. The model provided the top three object predictions for each image, which were then used as tags. This step automated the process of tagging images with relevant keywords, such as `#train`, `#station`, etc.

### Implementation Details

- **Libraries Used**:
  - `cv2` (OpenCV): For image processing tasks, such as reading and resizing images.
  - `numpy`: For numerical operations, especially in handling image data.
  - `json`: For managing JSON data, which was used to store metadata.
  - `sklearn.cluster.KMeans`: For clustering pixels to identify predominant colors.
  - `PIL` (Python Imaging Library): For opening and converting image formats.
  - `exifread`: For extracting EXIF metadata from images.
  - `tensorflow` and `keras`: For implementing the object detection model.

- **Storage**:
  - The extracted metadata, color information, and object tags were stored in JSON files. Each image had a corresponding JSON file that contained all the extracted information.

### Automation

- The process was automated using a Python script that iterated over all the images in the dataset. For each image, the script extracted EXIF data, identified predominant colors, and detected objects. The results were then saved to a JSON file.

### Challenges and Solutions

- **Handling Missing Data**:
  - Some images did not contain EXIF data or had incomplete metadata. The script was designed to handle such cases gracefully by continuing the process even if certain data was missing.

- **Ensuring Uniqueness**:
  - The script checked for the existence of a JSON file before processing each image to avoid duplicate entries and ensure that each image was processed only once.

### Future Improvements

- **Enhancing Object Detection**:
  - The object detection model could be fine-tuned or replaced with a more specialized model to improve the accuracy of the tags.

- **Expanding Color Analysis**:
  - Additional color analysis techniques could be employed to provide more detailed information about the color profiles of the images.

- **User Involvement**:
  - Incorporating user feedback in the tagging process could enhance the accuracy and relevance of the tags. Users could verify or modify the automatically generated tags.

## 4. Data Analyses

### Overview

The data analysis phase focused on understanding user preferences based on their interactions with the images. By analyzing the selected images and associated metadata, we aimed to build comprehensive user profiles that could inform the recommendation system. This process involved examining favorite colors, image orientations, sizes, and tags.

### Process

1. **User Preference Analysis**:
   - For each user, we analyzed their selected images to determine their favorite colors, orientations, sizes, and tags. This information was aggregated to create a user profile that reflected their preferences.

2. **Image Orientation and Size Categorization**:
   - Images were categorized based on their orientation (landscape, portrait, square) and size (thumbnail, medium, large). This categorization helped in understanding the types of images users prefer.

3. **Color and Tag Analysis**:
   - The predominant colors in each image were identified, and user-provided tags were collected. This data was used to determine the most frequent colors and tags preferred by each user.

### Implementation Details

- **Libraries Used**:
  - `json`: For handling JSON data, which was used to store user profiles and metadata.
  - `PIL` (Python Imaging Library): For opening and analyzing image files to determine orientation and size.
  - `collections.Counter`: For counting the frequency of colors, orientations, sizes, and tags.

- **Storage**:
  - User profiles were stored in JSON files, with each user having a separate profile file. These profiles contained aggregated data on favorite colors, orientations, sizes, and tags.

### Automation

- The analysis process was automated using a Python script. The script processed each user's selected images, extracted relevant metadata, and built a user profile. The results were then saved to JSON files for further use.

### Challenges and Solutions

- **Handling Missing Data**:
  - Some images might not have had complete metadata or user-provided tags. The script was designed to handle such cases by continuing the analysis even if certain data was missing.

- **Ensuring Uniqueness**:
  - The script checked for the existence of a user profile before processing each user's data to avoid duplicate entries and ensure that each user was processed only once.

### Future Improvements

- **Enhancing User Profiles**:
  - Additional user interactions, such as ratings or feedback, could be incorporated to enhance the accuracy of the user profiles.

- **Expanding Analysis**:
  - More sophisticated analysis techniques, such as clustering or classification algorithms, could be employed to identify patterns and trends in user preferences.

- **User Involvement**:
  - Incorporating user feedback in the analysis process could enhance the accuracy and relevance of the user profiles. Users could verify or modify the automatically generated profiles.

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