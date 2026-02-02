# Antigravity SEO & GEO Content Kit

Bộ công cụ (Starter Kit) dành cho Antigravity IDE, giúp tự động hóa quy trình sản xuất nội dung chuẩn SEO (Search Engine Optimization) và GEO (Generative Engine Optimization) từ nguồn bài viết.

## 📦 Bộ Kit bao gồm

### 1. Workflows

* **`step-by-step-article-seo-geo`**: Quy trình 6 bước biến nguồn bài viết thành Article.
  * Phân tích phụ đề video.
  * Deep Research (Nghiên cứu sâu) với NotebookLM.
  * Viết bài chuẩn SEO/GEO.
  * Audit & Kiểm tra chất lượng.

### 2. Skills

* **`Article-SEO-GEO`**: Kỹ năng viết bài Long-form tối ưu cho cả Google và AI (ChatGPT, Gemini).
* **`check-article`**: Chuyên gia Audit nội dung, chấm điểm và đề xuất cải thiện.

## 🚀 Cài đặt siêu tốc (1 dòng lệnh)

Chỉ cần mở Terminal trong dự án Antigravity của bạn và chạy lệnh sau (chọn theo hệ điều hành):

### 🪟 Windows (PowerShell)
```powershell
irm https://raw.githubusercontent.com/KHOAAI-HILL/antigravity-seo-kit/main/setup.ps1 | iex
```

### 🍎 macOS / 🐧 Linux
```bash
curl -fsSL https://raw.githubusercontent.com/KHOAAI-HILL/antigravity-seo-kit/main/install.sh | bash
```


## 📦 Cài đặt thủ công (Không khuyến khích)

1. Clone repository này về máy.
2. Copy thư mục `.agent` vào thư mục gốc của dự án Antigravity của bạn.
3. Cấu hình MCP Server:
   * Đảm bảo bạn đã cài đặt và chạy `notebooklm-mcp-server`.
   * Kiểm tra kết nối bằng lệnh `Check MCP Status` trong Antigravity.

## 📖 Cách sử dụng

1. Mở dự án trong Antigravity IDE.
2. Mở file phụ đề (`.srt`) hoặc Transcript của video bạn muốn chuyển đổi.
3. Gõ lệnh `/step-by-step-article-seo-geo` vào khung chat với Agent.
4. Làm theo hướng dẫn của Agent từng bước.

## 🛠 Yêu cầu hệ thống

* Antigravity IDE.
* Python 3.10+.
* MCP Servers: `notebooklm-mcp-server`.

## 🤝 Đóng góp

Mọi ý kiến đóng góp xin vui lòng tạo Pull Request hoặc Issue trên GitHub.

---

**Author:** KHOA AI
**License:** MIT
