
# Final Quality Checklist

Checklist ini menggabungkan CI, CT, dan CD agar mudah dimasukkan ke laporan akhir atau slide presentasi.

## Table 1 - CI Checklist

| Check Name | Rule | Status | Notes |
|---|---|---|---|
| Required columns exist | Kolom wajib tersedia | PASS | `price`, `distance`, `cab_type`, `source`, `destination`, `name`, dan `time_stamp` tersedia. |
| Target price is not missing | `price` tidak boleh missing pada data training | PASS | Missing target sudah dibuang saat cleaning. |
| distance > 0 | `distance` harus lebih besar dari 0 | PASS | Tidak ada jarak tidak valid pada cleaned data. |
| price > 0 | `price` harus lebih besar dari 0 | PASS | Tidak ada harga tidak valid pada cleaned data. |
| source is not missing | `source` tidak boleh missing | PASS | Kolom lengkap. |
| destination is not missing | `destination` tidak boleh missing | PASS | Kolom lengkap. |
| cab_type is not missing | `cab_type` tidak boleh missing | PASS | Kolom lengkap. |
| name is not missing | `name` tidak boleh missing | PASS | Kolom lengkap. |
| time_stamp can be converted to datetime | `time_stamp` harus bisa dikonversi | PASS | Timestamp valid untuk feature engineering waktu. |
| No exact duplicate rows | Tidak ada duplicate row persis | PASS | Duplicate sudah dicek. |

## Table 2 - CT Checklist

| Check Name | Metric / Rule | Current Value | Threshold | Status | Notes |
|---|---|---:|---:|---|---|
| MAE threshold check | MAE harus rendah | 1.4254 | <= 2.00 | PASS | Error rata-rata masih dalam batas baseline. |
| RMSE threshold check | RMSE harus rendah | 2.6181 | <= 3.50 | PASS | Error besar masih cukup terkendali. |
| R2 score threshold check | R2 harus cukup tinggi | 0.9214 | >= 0.85 | PASS | Model menjelaskan variasi target dengan baik untuk baseline. |
| Error by distance group | Group MAE tidak terlalu tinggi | Long trip MAE 1.8285 | Monitor | PASS | Long trip memiliki error tertinggi di distance group, tetapi masih wajar. |
| Error by cab_type | Group MAE tidak terlalu tinggi | Lyft MAE 1.6723 | Monitor | PASS | Perbedaan cab type perlu tetap dipantau. |
| Error by service name | Service MAE tidak terlalu tinggi | Lux Black XL MAE 2.9136 | Monitor | WARNING | Lux Black XL adalah service dengan error tertinggi. |
| Prediction error distribution review | Distribusi error perlu dicek | Reviewed | Review each run | PASS | Sudah dibuat plot error pada notebook evaluasi. |
| Robustness review for short and long trips | Short dan long trip perlu dicek | Reviewed | Review each run | PASS | Review distance group masuk ke checklist CT. |

## Table 3 - CD Checklist

| CD Component | Design Choice | Status | Notes |
|---|---|---|---|
| Model format | `.joblib` | READY | Model disimpan di `models/baseline_price_model.joblib`. |
| Model registry | `models/model_registry.json` | READY | Registry menyimpan versi, metrik, status, dan warning notes. |
| API framework | FastAPI | READY | API skeleton lokal ada di `api/app.py`. |
| Prediction endpoint | `/predict` | READY | Endpoint menerima input trip dan mengembalikan estimasi tarif. |
| Deployment strategy | Shadow Deployment | DESIGNED | Model diuji di background terlebih dahulu. |
| Rollback strategy | Previous approved model version | DESIGNED | Jika tidak stabil, kembali ke model approved sebelumnya. |
| Monitoring metrics | MAE, RMSE, R2, group-level MAE | DESIGNED | Metrik ini dipakai untuk memantau model setelah release simulation. |
| Logging plan | Input, output, timestamp, model version | PLANNED | Logging belum dibuat sebagai service, hanya dirancang. |
| Safety note | Learning simulation only | DOCUMENTED | Bukan sistem pricing produksi nyata. |
