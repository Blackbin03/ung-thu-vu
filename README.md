# 🩺 Ứng dụng Chẩn đoán Khối U Vú bằng Random Forest

Ứng dụng web đơn giản giúp **dự đoán khối u vú là Ác tính (Malignant) hay Lành tính (Benign)** dựa trên 5 đặc trưng xét nghiệm, sử dụng mô hình **Random Forest** được huấn luyện sẵn.

## 📌 Tính năng
- Giao diện web trực quan (HTML + TailwindCSS).
- Nhập các đặc trưng xét nghiệm:
  - `concave points_mean`
  - `concave points_worst`
  - `area_worst`
  - `concavity_mean`
  - `radius_worst`
- Gửi dữ liệu đến API `/predict` (Flask/FastAPI).
- Trả về kết quả dự đoán:
  - `prediction`: 0 = Ác tính ❌, 1 = Lành tính ✅
  - `proba`: mảng xác suất `[p_ac_tinh, p_lanh_tinh]`
- Hiển thị kết quả với màu sắc trực quan, biểu đồ xác suất bằng **Chart.js**.
