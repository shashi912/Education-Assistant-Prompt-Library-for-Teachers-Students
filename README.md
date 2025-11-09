# Education-Assistant-Prompt-Library-for-Teachers-Students
A system (and dataset) that stores teacher- and student-facing AI prompt templates and predicts how useful/engaging a prompt will be — helping schools and edtech teams create better prompts and automate content suggestions.
EdTech companies need scalable ways to recommend prompts and lesson templates to teachers & students. Predicting which prompts will be useful or engaging saves time and improves learning outcomes.

Automates A/B testing: deploy predicted-high-usefulness prompts first.

Integrates with LMS or content authoring pipelines to suggest prompt improvements and flag low-quality prompts automatically.

Helps product teams measure ROI of AI prompt investments.


# Education Assistant Prompt Library for Teachers & Students

**Project:** Predicting usefulness of educational prompts (text + metadata) to recommend best prompt templates to teachers and students.

## Overview
This project builds an end-to-end pipeline that:
- Creates/loads a prompt dataset.
- Cleans and explores the data.
- Extracts features from text and metadata.
- Trains a Random Forest model to predict a `usefulness_score`.
- Visualizes performance and exports a trained model.

## Why it matters
EdTech teams can use this system to surface high-value prompts, automate QA workflows, and improve teacher productivity.

## Structure






Real-world use cases:

Teacher assistant generation — suggest the best prompt templates for a lesson plan based on grade/subject.

Student practice generation — automatically supply practice questions for topics with high predicted usefulness.

Authoring analytics — score and rank teacher-contributed prompts so moderators review only low-scoring ones.

Adaptive learning — pick prompts that maximize engagement for specific student cohorts.

Content QA automation — automatically filter low-quality prompts before publishing to students.


Generate synthetic dataset

We create a fake dataset with n_samples = 2000.

Each row represents a prompt plus metadata: prompt_text, prompt_type (question/explanation/quiz/activity), subject, grade, audience (teacher/student), engagement_score (simulated), usefulness_score (target).

The usefulness_score is synthesized from logical rules (prompt type, subject, grade) plus noise to simulate real-world variability.

Save and load

We save the synthetic CSV and read it back to show a common real-world pattern (data created, saved, reloaded).

We remove duplicates and simulate a few missing values so the pipeline demonstrates imputation.

Exploratory Data Analysis (EDA)

We plot the distribution of usefulness_score — this shows whether scores cluster (e.g., many high or low).

We compute and save average usefulness by prompt_type to see which types generally perform better.

We save a sample CSV for manual inspection.

Split data

We split into train (80%) and test (20%) to evaluate generalization.

X contains all predictors; y is usefulness_score.

Feature engineering

Numerical features (grade, prompt_length, engagement_score) get imputed (missing filled) and scaled (standardization).

Categorical features (prompt_type, subject, audience) are imputed if missing and one-hot encoded to turn categories into numeric columns.

Text feature (prompt_text) is transformed by TfidfVectorizer (counts/weights of tokens) and reduced with TruncatedSVD (so vector becomes numeric features but not super high dimensional).

A ColumnTransformer applies these pipelines in parallel and returns a single combined numeric matrix.

Modeling

We use a RandomForestRegressor because it's robust, non-linear, and works well with mixed feature types.

The model is wrapped in a Pipeline together with the preprocessor so preprocessing and modeling are consistent and reproducible.

Model is trained on the training set.

Evaluation

Predictions are made on the test set.

We compute RMSE (Root Mean Squared Error): average absolute error-scale measure. Lower is better.

We compute R² (R-squared): fraction of variance explained. Higher (close to 1) is better.

We save results and plot Actual vs Predicted to visually judge performance.

Export & recommendations

We save the trained pipeline (joblib.dump) so it can be used in production without retraining.

We show how to use it to score new prompts and pick top recommendations.

