
# Final Project Summary

## 1. Project Title

Mini MLOps Pipeline Design for Online Transportation Fare Estimation Based on Trip and Weather Data

## 2. Short Description

Project ini adalah simulasi pembelajaran MLOps untuk memperkirakan tarif transportasi online berdasarkan data perjalanan. Fokus project adalah membuat alur kerja MLOps yang rapi mulai dari data audit, preprocessing, baseline model, evaluasi, quality checklist, sampai desain CD dan API lokal.

## 3. Dataset

- Raw trip data: `data/raw/cab_rides.csv`
- Raw weather data: `data/raw/weather.csv`
- Cleaned data: `data/processed/cleaned_cab_rides.csv`

Weather data belum digabungkan karena perlu alignment waktu dan lokasi yang hati-hati.

## 4. Target

Target prediksi adalah `price`.

## 5. Problem Type

Problem ini adalah **regression** karena model memprediksi nilai numerik berupa estimasi tarif.

## 6. Model Used

Model terbaik pada baseline adalah **Random Forest Regressor** dengan versi `v1.0-baseline-random-forest`.

## 7. Main Performance Metrics

| Metric | Value |
|---|---:|
| MAE | 1.4254 |
| RMSE | 2.6181 |
| R2 Score | 0.9214 |

## 8. Final Outputs Created

- Notebook Step 1 sampai Step 5.
- Final report dan final project summary.
- Final quality checklist gabungan CI, CT, dan CD.
- Member role distribution.
- Presentation script dan slide outline.
- MLOps pipeline diagram versi presentable dan vertical.
- Model registry JSON.
- Local FastAPI skeleton.
- Root README project.

## 9. Important Limitations

- Project ini adalah simulasi pembelajaran, bukan sistem pricing produksi nyata.
- Model tidak menentukan harga nyata untuk perusahaan transportasi apa pun.
- Weather data belum digabungkan.
- Model belum dideploy ke cloud.
- Shadow Deployment masih berupa desain simulasi lokal.
