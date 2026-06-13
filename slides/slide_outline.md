
# Slide Outline

## Slide 1 - Title

**Key bullet points:**
- Mini MLOps Pipeline Design for Online Transportation Fare Estimation Based on Trip and Weather Data
- Data Mining MLOps Mini Project
- Learning simulation for fare estimation

**Speaker:** Member 1

**Speaking note:** Perkenalkan judul project dan tekankan bahwa ini adalah simulasi pembelajaran MLOps, bukan sistem pricing nyata.

## Slide 2 - Background

**Key bullet points:**
- Fare estimation is common in online transportation services.
- Prediction needs clean data and model monitoring.
- MLOps helps organize the workflow from data to release plan.

**Speaker:** Member 1

**Speaking note:** Jelaskan mengapa estimasi tarif relevan dan mengapa workflow MLOps penting.

## Slide 3 - Problem Statement and Objective

**Key bullet points:**
- Target: `price`
- Problem type: regression
- Objective: build a mini MLOps pipeline for fare estimation simulation

**Speaker:** Member 1

**Speaking note:** Sampaikan masalah utama dan tujuan project secara singkat.

## Slide 4 - Dataset Overview

**Key bullet points:**
- Raw data: `cab_rides.csv` and `weather.csv`
- Raw cab rides: 693,071 rows
- Cleaned cab rides: 637,976 rows
- Weather data reserved for future improvement

**Speaker:** Member 2

**Speaking note:** Jelaskan dataset yang digunakan dan alasan weather data belum digabungkan.

## Slide 5 - MLOps Pipeline Overview

**Key bullet points:**
- Data Layer
- CI Stage
- CT Stage
- CD Stage
- Monitoring Stage

**Speaker:** Member 5

**Speaking note:** Tampilkan diagram pipeline dan beri gambaran besar alur project.

## Slide 6 - CI Stage

**Key bullet points:**
- Data validation
- Cleaning missing target
- Validate distance, price, timestamp, and categorical columns
- CI checklist: PASS

**Speaker:** Member 4

**Speaking note:** Jelaskan bahwa CI memastikan data aman sebelum training.

## Slide 7 - CT Stage

**Key bullet points:**
- Train baseline models
- Evaluate with MAE, RMSE, and R2
- Review group-level error
- CT status: mostly PASS with one WARNING

**Speaker:** Member 4

**Speaking note:** Jelaskan bahwa CT memantau kualitas model setelah training.

## Slide 8 - Model Evaluation Results

**Key bullet points:**
- Best model: Random Forest Regressor
- MAE: 1.4254
- RMSE: 2.6181
- R2 Score: 0.9214
- Highest error service: Lux Black XL

**Speaker:** Member 3

**Speaking note:** Jelaskan arti metrik dan warning pada service dengan error tertinggi.

## Slide 9 - CD Scenario and API Plan

**Key bullet points:**
- Model format: `.joblib`
- Registry: `models/model_registry.json`
- API framework: FastAPI local simulation
- Endpoint: `/predict`

**Speaker:** Member 5

**Speaking note:** Jelaskan bahwa API hanya skeleton lokal untuk demonstrasi alur MLOps.

## Slide 10 - Shadow Deployment, Monitoring, and Rollback

**Key bullet points:**
- Shadow Deployment runs predictions in background
- Monitor MAE, RMSE, R2, and group-level MAE
- Rollback to previous approved model if unstable
- No real cloud deployment

**Speaker:** Member 5

**Speaking note:** Jelaskan mengapa Shadow Deployment lebih aman untuk model estimasi tarif.

## Slide 11 - Member Roles

**Key bullet points:**
- Member 1: overview and dataset
- Member 2: audit, cleaning, preprocessing
- Member 3: training and evaluation
- Member 4: CI and CT checklist
- Member 5: CD, API, deployment scenario, diagram

**Speaker:** Member 1

**Speaking note:** Jelaskan pembagian tugas agar kontribusi kelompok terlihat jelas.

## Slide 12 - Conclusion

**Key bullet points:**
- Mini MLOps pipeline completed
- Model performs well as baseline
- CI passed, CT mostly passed with monitoring note
- Weather merge and improved features are future work

**Speaker:** Member 3

**Speaking note:** Tutup presentasi dengan kesimpulan dan batasan project secara jujur.
