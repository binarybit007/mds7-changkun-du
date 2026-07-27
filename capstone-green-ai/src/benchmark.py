"""
Green AI Capstone Benchmark Script
----------------------------------
Measures accuracy, training time, inference latency, energy consumption (kWh),
and CO2 emissions (g CO2eq) across multiple ML model architectures.
"""

import time
import json
import os
import pandas as pd
import numpy as np
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

# Try importing CodeCarbon; use graceful fallback if offline/restricted
try:
    from codecarbon import OfflineEmissionsTracker
    CODECARBON_AVAILABLE = True
except ImportError:
    CODECARBON_AVAILABLE = False


def load_data():
    """Loads a subset of 20 newsgroups dataset for benchmarking."""
    categories = ['alt.atheism', 'comp.graphics', 'sci.med', 'talk.religion.misc']
    train_data = fetch_20newsgroups(subset='train', categories=categories, remove=('headers', 'footers', 'quotes'))
    test_data = fetch_20newsgroups(subset='test', categories=categories, remove=('headers', 'footers', 'quotes'))

    vectorizer = TfidfVectorizer(max_features=2500, stop_words='english')
    X_train = vectorizer.fit_transform(train_data.data)
    X_test = vectorizer.transform(test_data.data)
    
    y_train = train_data.target
    y_test = test_data.target

    return X_train, X_test, y_train, y_test


def get_models():
    """Defines 5 distinct model architectures representing different complexity levels."""
    return {
        "1_TFIDF_LogisticRegression": {
            "name": "TF-IDF + Logistic Regression",
            "type": "Linear Baseline",
            "model": LogisticRegression(max_iter=200, C=1.0)
        },
        "2_TFIDF_RandomForest": {
            "name": "TF-IDF + Random Forest",
            "type": "Ensemble",
            "model": RandomForestClassifier(n_estimators=100, max_depth=15, random_state=42)
        },
        "3_Lightweight_MLP": {
            "name": "Lightweight MLP (1x64)",
            "type": "Neural Network",
            "model": MLPClassifier(hidden_layer_sizes=(64,), max_iter=100, random_state=42)
        },
        "4_Deep_MLP": {
            "name": "Deep MLP (3x256)",
            "type": "Deep Neural Network",
            "model": MLPClassifier(hidden_layer_sizes=(256, 128, 64), max_iter=250, random_state=42)
        },
        "5_Green_Optimized_MLP": {
            "name": "Green-Optimized MLP (1x32, Early Stopping)",
            "type": "Green AI Efficient",
            "model": MLPClassifier(hidden_layer_sizes=(32,), early_stopping=True, n_iter_no_change=5, max_iter=100, random_state=42)
        }
    }


def run_benchmark():
    """Runs training, evaluation, and carbon benchmarking for all models."""
    print("==========================================================")
    print("    GREEN AI BENCHMARKING: ENERGY & CARBON FOOTPRINT      ")
    print("==========================================================")
    
    output_dir = os.path.join(os.path.dirname(__file__), "..", "outputs")
    os.makedirs(output_dir, exist_ok=True)
    
    print("\n[1/4] Loading and vectorizing benchmark dataset...")
    X_train, X_test, y_train, y_test = load_data()
    print(f"      Train samples: {X_train.shape[0]}, Test samples: {X_test.shape[0]}, Features: {X_train.shape[1]}")

    models = get_models()
    results = []

    print("\n[2/4] Executing Model Training & Carbon Tracking...")

    for key, config in models.items():
        model_name = config["name"]
        model_type = config["type"]
        clf = config["model"]

        print(f"\n---> Benchmarking: {model_name} [{model_type}]")

        # Initialize CodeCarbon emissions tracker if available
        tracker = None
        if CODECARBON_AVAILABLE:
            try:
                tracker = OfflineEmissionsTracker(
                    country_iso_code="DEU",
                    output_dir=output_dir,
                    output_file="codecarbon_emissions.csv",
                    log_level="error"
                )
                tracker.start()
            except Exception:
                tracker = None

        start_time = time.time()
        clf.fit(X_train, y_train)
        training_time = time.time() - start_time

        emissions_kg = 0.0
        energy_kwh = 0.0

        if tracker:
            try:
                emissions_kg = tracker.stop()
                if tracker.final_emissions_data:
                    energy_kwh = tracker.final_emissions_data.energy_consumed
            except Exception:
                pass
        
        # Fallback estimation if hardware tracking is unavailable in restricted containers
        if energy_kwh == 0.0 or energy_kwh is None:
            # Baseline power estimate for CPU execution (~45W TDP * time in hours)
            estimated_power_kw = 0.045
            energy_kwh = (training_time / 3600.0) * estimated_power_kw
            # Germany grid carbon intensity ~0.385 kg CO2eq / kWh
            emissions_kg = energy_kwh * 0.385

        emissions_g = emissions_kg * 1000.0  # Convert kg to grams

        # Measure Inference Latency
        infer_start = time.time()
        y_pred = clf.predict(X_test)
        infer_time = time.time() - infer_start
        latency_ms_per_1000 = (infer_time / len(y_test)) * 1000.0 * 1000.0

        # Calculate metrics
        acc = accuracy_score(y_test, y_pred) * 100.0
        f1 = f1_score(y_test, y_pred, average='weighted') * 100.0
        prec = precision_score(y_test, y_pred, average='weighted') * 100.0
        rec = recall_score(y_test, y_pred, average='weighted') * 100.0

        # Green AI Efficiency Score: Accuracy per gram of CO2 emitted
        efficiency_score = acc / (emissions_g + 1e-6)

        res = {
            "model_key": key,
            "model_name": model_name,
            "model_type": model_type,
            "accuracy_pct": round(acc, 2),
            "f1_score_pct": round(f1, 2),
            "precision_pct": round(prec, 2),
            "recall_pct": round(rec, 2),
            "training_time_sec": round(training_time, 4),
            "inference_latency_ms_per_1k": round(latency_ms_per_1000, 3),
            "energy_kwh": round(energy_kwh, 8),
            "emissions_g_co2": round(emissions_g, 5),
            "green_efficiency_score": round(efficiency_score, 2)
        }
        results.append(res)

        print(f"      Accuracy: {acc:.2f}% | F1: {f1:.2f}%")
        print(f"      Train Time: {training_time:.3f}s | Latency (1k samples): {latency_ms_per_1000:.2f}ms")
        print(f"      Energy Consumed: {energy_kwh*1e3:.4f} Wh | CO2 Emissions: {emissions_g:.4f} g CO2eq")
        print(f"      Green AI Efficiency Score: {efficiency_score:.2f}")

    # Save results to CSV and JSON
    print("\n[3/4] Saving results to outputs...")
    df = pd.DataFrame(results)
    csv_path = os.path.join(output_dir, "benchmark_results.csv")
    json_path = os.path.join(output_dir, "benchmark_results.json")
    
    df.to_csv(csv_path, index=False)
    with open(json_path, "w") as f:
        json.dump(results, f, indent=4)

    print(f"      CSV saved:  {csv_path}")
    print(f"      JSON saved: {json_path}")
    
    print("\n[4/4] Summary Table:")
    print(df[["model_name", "accuracy_pct", "training_time_sec", "emissions_g_co2", "green_efficiency_score"]].to_string(index=False))
    print("\nBenchmark completed successfully!")


if __name__ == "__main__":
    run_benchmark()
