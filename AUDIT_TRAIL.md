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



## Week 5-6 Deep Learning ETLS Deployment - 2026-05-13 10:34:54

- Updated Titanic classification pipeline from classical machine learning to deep learning.
- Trained Model A: shallow neural network with 1 hidden ReLU layer and 1 sigmoid output layer.
- Trained Model B: deep neural network with 3 hidden ReLU layers and 1 sigmoid output layer.
- Model A test accuracy: 0.4190
- Model B test accuracy: 0.7263
- Saved artifacts as Keras HDF5 files:
  - model_3_layers.h5
  - model_5_layers.h5
- Generated README.md automatiically using Python File I/O.
- Deployed artifacts to AWS S3 bucket `anshulmds1` under `deeplearning/`.
- Deployed artifacts to GitHub directory `week-05-06-bigquery/deeplearning`.
