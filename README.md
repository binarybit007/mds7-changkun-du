# MDS 7: Data Science Innovations — Portfolio & Capstone

**Student Name**: Changkun Du  
**Student Email**: [c.du@student.xu-university.de](mailto:c.du@student.xu-university.de)  
**Degree Program**: Master of Data Science (MDS)  
**Module**: MDS 7 - Data Science Innovations  

---

## 📽️ Capstone 10-Minute Video Presentation

[![Watch Presentation Video](https://img.shields.io/badge/Watch_Presentation-10_Min_Video-red?style=for-the-badge&logo=youtube)](https://youtu.be/AQixjCvGnWc)

[![MDS 7 Capstone Video Presentation](https://img.youtube.com/vi/AQixjCvGnWc/maxresdefault.jpg)](https://youtu.be/AQixjCvGnWc)

> 📌 **Video Link**: [Click here to watch the 10-Minute Recorded Video Presentation (YouTube)](https://youtu.be/AQixjCvGnWc)  
> 🌿 **Capstone Project Folder**: [`capstone-green-ai/`](capstone-green-ai/)  

---

## 🌿 Featured Capstone Topic: Green AI & Carbon Footprint Benchmarking

### Executive Summary
As AI models scale in size, their energy consumption and environmental footprint have exploded. This capstone project benchmarks **5 model architectures** ranging from linear models to deep neural networks on text classification tasks, measuring **Accuracy**, **Training Speed**, **Inference Latency**, **Energy Consumed (kWh)**, and **$CO_2$ Emissions ($g CO_2eq$)** measured dynamically via `CodeCarbon`.

### Key Findings
- **Deep Neural Network (3x256)**: 74.39% Accuracy | 2.03s Train Time | **0.00540 g $CO_2eq$**
- **Green-Optimized MLP (1x32, Early Stopping)**: **75.13% Accuracy** | **0.217s Train Time** | **0.00040 g $CO_2eq$**
- **Takeaway**: Rightsizing the model architecture and leveraging early stopping achieved **13.5x lower carbon emissions (92.6% emission reduction)** while outperforming the deeper model in accuracy.

---

## 📊 Pareto Frontier: Accuracy vs. Carbon Emissions

![Pareto Frontier](capstone-green-ai/outputs/tradeoff_accuracy_vs_carbon.png)

---

## ⚡ Quickstart (`uv` Environment Setup)

This repository utilizes [`uv`](https://github.com/astral-sh/uv) for fast, deterministic Python package and environment management.

```bash
# 1. Navigate to the Capstone project directory
cd capstone-green-ai

# 2. Sync all dependencies via uv
uv sync

# 3. Run the Green AI benchmarking script
uv run python src/benchmark.py

# 4. Generate all charts
uv run python src/visualize.py

# 5. Launch the interactive Jupyter demonstration notebook
uv run jupyter lab notebooks/green_ai_capstone_demo.ipynb
```

---

## 📁 Repository Structure & Course Modules

| Module Directory | Topic / Focus | Description |
| :--- | :--- | :--- |
| 🌿 **[`capstone-green-ai/`](capstone-green-ai/)** | **Green AI Capstone** | **Final Capstone Project: `uv`-managed benchmarking framework, CodeCarbon energy tracking, Pareto visualizations, LaTeX slides & demo notebook.** |
| 📊 [`week-10-12-async-lab/`](week-10-12-async-lab/) | Green AI Trade-Off Lab | Async lab investigating neural network epoch vs dataset size energy trade-offs. |
| 🤖 [`week-10-12-ai/`](week-10-12-ai/) | Green AI Experiments | Initial notebook and emissions logs for Green AI models. |
| 🐳 [`week-08-09-docker/`](week-08-09-docker/) | Containerization | Docker containerization setups and docker-compose files. |
| ☁️ [`week-05-06-bigquery/`](week-05-06-bigquery/) | Cloud Data Warehousing | Google BigQuery SQL queries and cloud data pipeline notebooks. |
| 📈 [`week-03-04-powerbi/`](week-03-04-powerbi/) | Data Visualization | Business intelligence dashboards and PowerBI reporting. |
| 🗄️ [`week-02-sql/`](week-02-sql/) | SQL & Data Engineering | Relational database schema design and advanced SQL queries. |

---

## 📄 License & Contact

Developed by **Changkun Du** ([c.du@student.xu-university.de](mailto:c.du@student.xu-university.de)) for the Master of Data Science program at XU Exponential University.