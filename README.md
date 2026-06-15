# Rancangan Mini Pipeline MLOps untuk Estimasi Tarif Transportasi Online Berdasarkan Data Perjalanan

## Deskripsi Proyek

Project ini merancang Mini Pipeline MLOps sederhana untuk estimasi tarif transportasi online berdasarkan data perjalanan. Project ini dibuat sebagai simulasi pembelajaran untuk kebutuhan assignment, bukan sistem pricing production nyata. Tidak ada deployment cloud sungguhan, dan model hanya menggunakan data perjalanan.

## Dataset

Sumber dataset: https://www.kaggle.com/datasets/ravi72munde/uber-lyft-cab-prices

File dataset tidak disimpan di repository GitHub. File yang diperlukan:

```text
data/raw/cab_rides.csv
```

Folder `data/raw/`, `data/processed/`, dan file `.csv` diabaikan oleh `.gitignore`.

## Alur Notebook

1. `notebooks/01_data_understanding.ipynb`
2. `notebooks/02_preprocessing_baseline_model.ipynb`
3. `notebooks/03_model_evaluation_quality_checklist.ipynb`
4. `notebooks/04_cd_scenario_pipeline_design.ipynb`

## Hasil Model

- Best model: Random Forest Regressor
- MAE: 1.4254
- RMSE: 2.6181
- R2 Score: 0.9214

## API Simulasi Lokal

API menggunakan FastAPI sebagai simulasi lokal untuk endpoint prediksi. API ini bukan deployment production.

Endpoint:

```text
POST /predict
```

Input:

- `distance`
- `cab_type`
- `source`
- `destination`
- `name`
- `time_stamp`

Output:

- `estimated_price`
- `model_version`

Cara menjalankan API:

```bash
uvicorn api.app:app --reload
```

Contoh request tersedia di:

```text
api/request_example.json
```

## Output Akhir

- `reports/final_report.md`
- `diagrams/mlops_pipeline_vertical.png`

## Struktur Folder

```text
MLOPS-TARIF-TRANSPORTASI-ONLINE/
|-- api/
|-- data/
|-- diagrams/
|-- models/
|-- notebooks/
|-- reports/
|-- src/
|-- .gitignore
`-- README.md
```

## Batasan Proyek

- Project ini hanya simulasi pembelajaran.
- Bukan sistem pricing production nyata.
- Tidak ada deployment cloud sungguhan.
- Model hanya menggunakan data perjalanan.
- Dataset tidak bersifat real-time.
