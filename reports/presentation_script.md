
# Presentation Script

Script ini menggunakan bahasa Indonesia sederhana agar mudah dipakai saat presentasi kelas.

## Member 1 - Project Overview, Problem Statement, and Dataset

Selamat pagi/siang, kami akan mempresentasikan project berjudul **Mini MLOps Pipeline Design for Online Transportation Fare Estimation Based on Trip and Weather Data**.

Latar belakang project ini adalah kebutuhan untuk memahami bagaimana tarif transportasi online dapat diperkirakan dari data perjalanan. Dalam project ini, kami tidak membuat sistem harga nyata, tetapi membuat simulasi pembelajaran untuk memahami alur MLOps dari awal sampai akhir.

Dataset yang kami gunakan adalah `cab_rides.csv` dan `weather.csv`. Data utama yang dipakai untuk model adalah data perjalanan dari `cab_rides.csv`. Target prediksi kami adalah kolom `price`, sehingga tipe masalahnya adalah regression karena output yang diprediksi berupa angka.

## Member 2 - Data Audit, Cleaning, and Preprocessing

Pada tahap data audit, kami mengecek struktur dataset, missing value, duplicate row, dan validitas data. Raw cab ride data memiliki 693.071 baris. Setelah cleaning, data yang dipakai menjadi 637.976 baris.

Cleaning utama yang dilakukan adalah menghapus baris dengan `price` yang kosong, karena `price` adalah target dan tidak bisa digunakan jika nilainya missing. Kami juga mengecek bahwa `distance` dan `price` harus lebih besar dari nol.

Untuk feature engineering, kami mengubah `time_stamp` menjadi fitur waktu sederhana, yaitu `hour`, `day`, `month`, dan `day_of_week`. Kolom seperti `id`, `product_id`, dan `surge_multiplier` tidak digunakan pada baseline utama.

## Member 3 - Model Training and Evaluation

Pada tahap training, kami membandingkan Dummy Regressor, Ridge Regression, dan Random Forest Regressor. Model terbaik adalah Random Forest Regressor.

Hasil evaluasi model terbaik adalah MAE sebesar 1.4254, RMSE sebesar 2.6181, dan R2 Score sebesar 0.9214. MAE berarti rata-rata selisih absolut antara prediksi dan nilai aktual. RMSE memberi penalti lebih besar pada error yang besar. R2 menunjukkan seberapa baik model menjelaskan variasi target.

Kami juga melakukan error analysis berdasarkan group perjalanan. Hasilnya, service `Lux Black XL` memiliki error tertinggi, sehingga bagian ini menjadi catatan untuk monitoring dan pengembangan model berikutnya.

## Member 4 - CI and CT Quality Checklist

Dalam project ini, CI atau Continuous Integration digunakan untuk memastikan data dan preprocessing aman sebelum training. Contoh check CI adalah kolom wajib harus tersedia, `price` tidak missing, `distance` lebih besar dari nol, dan timestamp bisa dikonversi.

CT atau Continuous Training digunakan untuk memantau kualitas model setelah training. Metrik yang dipantau adalah MAE, RMSE, R2 Score, dan group-level MAE.

Secara umum, CI checklist semuanya PASS. Untuk CT, sebagian besar PASS, tetapi ada satu WARNING pada error by service name karena `Lux Black XL` memiliki error tertinggi. Warning ini bukan berarti model gagal, tetapi perlu dipantau jika model dikembangkan lagi.

## Member 5 - CD Scenario, API Plan, Shadow Deployment, and Pipeline Diagram

Pada tahap CD, kami membuat desain release model secara sederhana. Model disimpan dalam format `.joblib`, lalu metadata model dicatat di `models/model_registry.json`.

Kami juga membuat skeleton API lokal menggunakan FastAPI. Endpoint utama adalah `/predict`, yang menerima input perjalanan seperti `distance`, `cab_type`, `source`, `destination`, `name`, dan `time_stamp`. API ini tidak membutuhkan `price` karena `price` adalah target yang ingin diprediksi.

Deployment strategy yang kami pilih adalah Shadow Deployment. Artinya, model baru berjalan di background terlebih dahulu dan prediksinya dimonitor tanpa mempengaruhi user. Jika stabil, model bisa dipromosikan dalam simulasi. Jika tidak stabil, model bisa rollback ke versi approved sebelumnya.

Kesimpulannya, project ini menunjukkan alur MLOps lengkap mulai dari data audit, preprocessing, training, evaluasi, CI/CT checklist, model registry, API plan, sampai CD scenario. Project ini tetap merupakan simulasi pembelajaran, bukan sistem pricing produksi nyata.
