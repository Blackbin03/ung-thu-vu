🩺 Dự đoán khối u vú bằng Random Forest
📌 Bài làm về gì

Xây dựng mô hình học máy (Random Forest) để dự đoán u vú là ác tính hay lành tính dựa trên dữ liệu xét nghiệm (Breast Cancer Dataset).

Triển khai mô hình dưới dạng ứng dụng web với giao diện nhập liệu và kết quả trực quan.

Cho phép người dùng nhập 5 đặc trưng quan trọng để dự đoán:

- concave points_mean

- concave points_worst

- area_worst

- concavity_mean

- radius_worst

⚙️ Sử dụng công nghệ, thuật toán, ngôn ngữ lập trình gì

- Ngôn ngữ lập trình: Python

- Framework backend: Flask

- Frontend: HTML + TailwindCSS + JavaScript (fetch API)

Thuật toán học máy: Random Forest Classifier (scikit-learn)

Thư viện chính:

- pandas, scikit-learn (xử lý dữ liệu & huấn luyện mô hình)

- joblib (lưu/trích xuất mô hình)

- Flask (triển khai API backend)

🖼️ Một số giao diện cơ bản
1. Trang nhập dữ liệu

Form gồm 5 trường số tương ứng với đặc trưng mô hình cần:

- concave points_mean

- concave points_worst

- area_worst

- concavity_mean

- radius_worst

<img width="598" height="746" alt="image" src="https://github.com/user-attachments/assets/655e862d-f5f7-4f0a-82d5-8b419e718537" />

2. Kết quả dự đoán

Hiển thị Ác tính (0) ❌ hoặc Lành tính (1) ✅.

Kèm theo xác suất dự đoán chi tiết.

<img width="598" height="547" alt="image" src="https://github.com/user-attachments/assets/da08b14a-026c-45c6-b459-33f48dd44bc8" />

Hiển thị dữ liệu đã gửi để người dùng kiểm tra lại.

<img width="556" height="215" alt="image" src="https://github.com/user-attachments/assets/46ad12bb-4b58-418c-9020-0b2cbe0b3795" />
