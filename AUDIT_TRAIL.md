# MDS 7: Audit Trail
 
## Week 1: Environment Setup
* **Milestone:** Repository created and structured.
* **Notes:** Environment initialized and Professor invited.

## Week 2: Distributed Data & SQL
* **Date:** 2026-04-08
* **Milestone:** Uploaded sample_2page.pdf to the week-02-sql directory.
* **Notes:** Pushed local work to the repository using Colab interactive upload.

## Week 3-4: Data Engineering & PowerBI Prep

* **Date:** 2026-04-22

* **Milestone:** Uploaded `titanic_clean.csv` to the `week-03-04-powerbi` directory.

* **Notes:** Built an ETL pipeline fetching raw Titanic data from AWS S3, engineered it in Colab (handling nulls and dummy variables), pushed the processed data back to S3, and synced it to GitHub for visualization in PowerBI.


## Week 3-4: Data Engineering & PowerBI Prep

* **Date:** 2026-04-29

* **Milestone:** Uploaded `best_model.pkl` to the `week-03-04-powerbi/machine_learning` directory.

* **Notes:** Week 4 ML_Assgn



## Week 5-6: Advanced Power BI & BigQuery Prep

* **Date:** 2026-05-06

* **Milestone:** Uploaded `spain_sales_clean.csv` and `mds_Lecture_5_first_task - Power BI_Anshul.pdf` to the `week-05-06-bigquery/PowerBI` directory.

* **Notes:** Transformed raw Spanish Beverage Excel data into CSV using Pandas, adding a 'Total Revenue' feature. Established a live web-connector pipeline between GitHub and Power BI. Demonstrated live data refresh by injecting extreme data points via Python and updating the repository. Exported final visualizations to PDF and backed up to AWS S3.



## Week 5-6: Advanced Power BI & BigQuery Prep

* **Date:** 2026-05-06

* **Milestone:** Uploaded `Germany-Power-Bi-Dataset.csv` and `mds_Lecture_5_self_task - Power BI.pdf` to the `week-05-06-bigquery/PowerBI` directory.

* **Notes:** Transformed raw German Beverage Excel data into CSV using Pandas, adding a 'Total Revenue' feature. Established a live web-connector pipeline between GitHub and Power BI. Demonstrated live data refresh by injecting extreme data points via Python and updating the repository. Exported final visualizations to PDF and backed up to AWS S3.



## Week 5-6: Deep Learning Classification & ETLS Deployment

* **Date:** 2026-05-13

* **Milestone:** Trained and deployed two Keras neural network models for Titanic survival classification.

* **Artifacts:** Uploaded `model_3_layers.h5`, `model_5_layers.h5`, `README.md`, and `titanic_dl_pipeline.ipynb` to the `week-05-06-bigquery/deeplearning/` directory.

* **AWS S3 Backup:** Saved the same deep learning artifacts to the `deeplearning/` folder in the `awsstoragecloud` S3 bucket.

* **Model A:** Shallow neural network with 1 hidden ReLU layer and 1 Sigmoid output layer.

* **Model B:** Deep neural network with 3 hidden ReLU layers and 1 Sigmoid output layer.

* **Notes:** Extended the Titanic ETLS pipeline from classical machine learning to deep learning. Applied feature scaling for neural network convergence, trained both models with Adam optimizer and binary crossentropy loss, generated automated README documentation with model metrics, and completed dual-cloud deployment to AWS S3 and GitHub.


* **2026-05-20 - Computer Vision:** Trained CIFAR-10 CNN (`cifar_custom_cnn.h5`) and deployed to S3/GitHub.



## Week 10-12: Green AI Experiment

Date: 2026-06-17

* **Milestone:** Completed NLP model training with carbon footprint tracking.

* **Artifacts:**
Uploaded green_ai_experiment.ipynb, emissions.csv, and README.md
to the week-10-12-ai directory.

* **Dataset:**
Used Scikit-learn 20 Newsgroups dataset for text classification.

* **Model:**
Built a machine learning pipeline using:
- TF-IDF Vectorizer
- Random Forest Classifier

* **Notes:**
Implemented an AI experiment to measure environmental impact.
Used CodeCarbon EmissionsTracker during model training to record CO2 emissions.
Evaluated model accuracy and compared performance with computational cost.

