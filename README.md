# MSc Data Science and Analytics Scholarship Award Exam

## Project Overview:
The project aims to determine the demographic and socio-economic determinants of the well-being index of galaxies over a period of time and predict future well-being values using machine learning techniques.

## Dataset Description:
- The dataset contains 80 variables characterizing the demographic and socio-economic situation of 181 galaxies over a maximum period of 26 years.
- Each observation includes a composite index measuring the well-being of the galaxies.

## Files Included:
1. **Data**: 
   - `train.csv`: Contains training data with observed well-being index values.
   - `validation.csv`: Contains validation data for predicting future well-being index values.
2. **Instructions**: 
   - `MSc Data Science and Analytics  Research Scholar Test 2024`: Contains the instruction and expectations of the project.


3. **Analysis Notebook**:
   - `Analysis.ipynb`: Python/R notebook containing detailed analysis, including data exploration, feature selection, model building, and prediction.

4. **Slide Presentation**:
   - `presentation.pdf`: A slide presentation summarizing key findings, insights, and visualizations from the analysis.

5. **Predicted Values**:
   - `firstname_lastname_DSA.csv`: CSV file containing predicted future well-being index values for the validation dataset.

6. **README.md**: 
   - This file, providing an overview of the project, included files, and instructions.

## Project Workflow:
1. **Data Exploration**:
   - Load and explore the dataset to understand its structure and characteristics.
   - Perform descriptive statistics and visualizations to gain insights into the data.

2. **Feature Selection**:
   - Identify relevant features that explain the variance of the well-being index.
   - Utilize techniques like correlation analysis or feature importance to select significant features.

3. **Model Building**:
   - Choose appropriate regression models based on the problem requirements.
   - Split the data into training and validation sets.
   - Train the models using training data and evaluate their performance using metrics like RMSE.

4. **Prediction**:
   - Use the trained model to predict future well-being index values for the validation dataset.

5. **Documentation and Reporting**:
   - Prepare a slide presentation summarizing key findings, insights, and visualizations.
   - Document the analysis process, model selection, and prediction results in the analysis notebook.
   - Save predicted values in a CSV file for submission.

## Submission Instructions:
1. **Deadline**: Wednesday, 27th March 2024, 1:00 PM EAT.
2. **Submission Format**: 
   - Compress all files into a folder named `firstname_lastname.zip`.
   - Email the zipped folder to Laura Mideva, @iLabAfrica Course Administrator, at LMideva@strathmore.edu.

## Evaluation Criteria:
- Quality of presentation of findings in the slide presentation.
- Accuracy of future well-being index predictions using the RMSE metric.
- Reproducibility of the codebase and analysis process.

## Resources:
- [Python](https://www.python.org/) or [R](https://www.r-project.org/) programming language.
- Libraries: Pandas, NumPy, Matplotlib/Seaborn (for Python); dplyr, ggplot2 (for R).
- Machine Learning Libraries: Scikit-learn (for Python); caret, randomForest (for R).