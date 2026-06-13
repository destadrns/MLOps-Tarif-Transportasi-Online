
# Final Report

## 1. Cover / Title

**Mini MLOps Pipeline Design for Online Transportation Fare Estimation Based on Trip and Weather Data**

Project ini dibuat sebagai mini project Data Mining dan MLOps. Fokusnya adalah membuat simulasi pipeline MLOps untuk estimasi tarif transportasi online berdasarkan data perjalanan.

## 2. Project Background

Estimasi tarif transportasi online adalah contoh kasus yang relevan karena melibatkan data perjalanan, fitur lokasi, jarak, waktu, dan jenis layanan. Dalam dunia nyata, sistem seperti ini harus memiliki data yang bersih, model yang terukur, dan proses monitoring.

Dalam project ini, kami tidak membangun sistem pricing nyata. Project ini hanya simulasi pembelajaran untuk memahami bagaimana alur MLOps dapat dirancang dari awal sampai release scenario.

## 3. Problem Statement

Masalah yang ingin diselesaikan adalah bagaimana membuat model baseline yang dapat memperkirakan `price` dari data perjalanan, serta bagaimana menyiapkan pipeline MLOps sederhana untuk memvalidasi data, mengevaluasi model, dan merancang deployment scenario.

## 4. Project Objective

- Memahami struktur dan kualitas dataset.
- Membersihkan data untuk supervised regression.
- Melatih beberapa baseline model sederhana.
- Mengevaluasi model dengan metrik regression.
- Membuat CI, CT, dan CD checklist.
- Menyiapkan model registry, API plan, Shadow Deployment scenario, dan pipeline diagram.

## 5. Dataset Description

- `data/raw/cab_rides.csv`: data perjalanan dan harga.
- `data/raw/weather.csv`: data cuaca.
- `data/processed/cleaned_cab_rides.csv`: data cab ride yang sudah dibersihkan.

Raw cab ride data memiliki 693.071 baris. Setelah cleaning, data yang digunakan menjadi 637.976 baris. Weather data belum digabungkan karena perlu alignment waktu dan lokasi.

## 6. Data Audit Summary

Target utama adalah `price`. Kolom `price` memiliki 55.095 missing values, sehingga baris tersebut tidak dipakai untuk supervised training.

Hasil audit penting: `distance <= 0` sebanyak 0 baris, `price <= 0` sebanyak 0 baris pada non-missing price, dan `source`, `destination`, `cab_type`, serta `name` tidak memiliki missing value.

## 7. Preprocessing Summary

Cleaning dilakukan dengan menghapus missing `price`, mengecek `distance > 0`, mengecek `price > 0`, mengecek duplicate row, dan membuat fitur waktu dari `time_stamp`.

Fitur baseline utama: `distance`, `cab_type`, `source`, `destination`, `name`, `hour`, `day`, `month`, dan `day_of_week`.

Fitur yang dikeluarkan: `id`, `product_id`, `price`, `surge_multiplier`, dan weather columns.

## 8. Model Training Summary

Model yang dibandingkan adalah Dummy Regressor, Ridge Regression, dan Random Forest Regressor. Model terbaik adalah **Random Forest Regressor** dan disimpan di `models/baseline_price_model.joblib`.

## 9. Model Evaluation Summary

| Metric | Value |
|---|---:|
| MAE | 1.4254 |
| RMSE | 2.6181 |
| R2 Score | 0.9214 |

Group error analysis menunjukkan bahwa service `Lux Black XL` memiliki error tertinggi.

## 10. CI Checklist Summary

Status CI: **PASS**. Check utama meliputi required columns, target tidak missing, `distance > 0`, `price > 0`, categorical columns tidak missing, timestamp valid, dan tidak ada exact duplicate rows.

## 11. CT Checklist Summary

Status CT: **mostly PASS with one WARNING**. Warning muncul pada service-level error karena `Lux Black XL` memiliki error tertinggi.

## 12. CD Scenario Summary

CD pada project ini berarti menyiapkan model agar dapat dirilis sebagai prediction service dalam simulasi lokal. Komponen CD meliputi model artifact `.joblib`, model registry JSON, FastAPI skeleton, Shadow Deployment strategy, monitoring, dan rollback plan.

## 13. MLOps Pipeline Diagram

Diagram final tersedia di `diagrams/mlops_pipeline_diagram.md`, `diagrams/mlops_pipeline_diagram_presentable.md`, dan `diagrams/mlops_pipeline_diagram_vertical.md`.

## 14. Model Registry

Model registry disimpan di `models/model_registry.json` dengan versi `v1.0-baseline-random-forest`, model type Random Forest Regressor, target `price`, dan approval status `Approved for shadow deployment simulation`.

## 15. API Plan

API skeleton tersedia di `api/app.py`. Endpoint utama adalah `POST /predict`. Input meliputi `distance`, `cab_type`, `source`, `destination`, `name`, dan `time_stamp`.

## 16. Shadow Deployment Strategy

Shadow Deployment dipilih karena model dapat menghasilkan prediksi di background terlebih dahulu tanpa mempengaruhi user. Jika stabil, model bisa dipromosikan dalam simulasi.

## 17. Monitoring and Rollback Plan

Monitoring yang direncanakan meliputi MAE, RMSE, R2 Score, group-level MAE, prediction input, prediction output, timestamp, dan model version. Jika tidak stabil, model dapat rollback ke previous approved model version.

## 18. Limitations

- Project ini hanya learning simulation.
- Model tidak menentukan harga nyata untuk perusahaan transportasi apa pun.
- Weather data belum digabungkan.
- Model belum dideploy ke cloud.
- API masih skeleton lokal.
- Error pada service `Lux Black XL` perlu dimonitor.

## 19. Conclusion

Project ini berhasil membuat mini MLOps pipeline dari data understanding sampai CD scenario. Model baseline memberikan hasil yang cukup baik untuk simulasi pembelajaran. CI sudah PASS, CT mostly PASS dengan satu warning, dan CD scenario sudah dirancang menggunakan registry, API plan, Shadow Deployment, monitoring, dan rollback.

## 20. Member Roles

| Member | Role |
|---|---|
| Member 1 | Project overview, problem statement, dan dataset explanation |
| Member 2 | Data audit, cleaning, dan preprocessing |
| Member 3 | Model training dan evaluation |
| Member 4 | CI dan CT quality checklist |
| Member 5 | CD scenario, API plan, shadow deployment, dan pipeline diagram |
