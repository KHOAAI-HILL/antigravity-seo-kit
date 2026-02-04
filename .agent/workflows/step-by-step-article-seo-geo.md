---
description: write article seo geo
---

# Workflow: Tối Ưu Bài Viết SEO GEO

// turbo-all
Quy trình này giúp biến một video YouTube (file phụ đề `.srt`) thành chuỗi nội dung chất lượng cao trên đa nền tảng, tối ưu cho SEO và AI Search (GEO), tận dụng sức mạnh Deep Research và phân tích nguồn tin của NotebookLM.

## 0. Khởi tạo Task & Plan (DỪNG LẠI ĐỂ HỎI Ý KIẾN NGƯỜI DÙNG)
- **Action**: 
  1. Tạo file `task.md` liệt kê toàn bộ 6 bước trong quy trình.
  2. Tạo file `implementation_plan.md` mô tả phương pháp thực hiện chi tiết cho từng bước.
- **Goal**: Giúp người dùng theo dõi tiến độ và kiểm soát chất lượng.
- **QUAN TRỌNG: Dừng lại và xin phê duyệt người dùng trước khi tiếp tục sang Bước 1.**

## 1. Phân tích nội dung gốc (DỪNG LẠI ĐỂ HỎI Ý KIẾN NGƯỜI DÙNG)
- **Input**: Đọc file phụ đề gốc (ví dụ: `phu-de.srt`).
- **Action**: Đọc toàn bộ file và tóm tắt nội dung chính, xác định vấn đề, giải pháp và giá trị cốt lõi.
- **Goal**: Hiểu rõ nội dung để định hướng từ khóa.
- **QUAN TRỌNG: Dừng lại, trình bày tóm tắt và xin phê duyệt trước khi sang Bước 2.**
- **Post-Action**: Đánh dấu hoàn thành bước 1 trong `task.md`.

## 2. Deep Research (Nghiên cứu từ khóa & Xu hướng) (DỪNG LẠI ĐỂ HỎI Ý KIẾN NGƯỜI DÙNG)
- **Tool**: Sử dụng MCP `notebooklm-mcp-server`.
- **Action**:
  1. **Research**: Dùng `research_start` (mode: deep) để tìm kiếm nguồn tin từ web về chủ đề. Dùng `research_status` để theo dõi và `research_import` để lưu vào Notebook.
  2. **Analyze**: Sử dụng `notebook_query` để tổng hợp thông tin theo Prompt Framework dưới đây.
  3. **Prompt Framework (Copy & Paste để sử dụng):**
     > **Role:** Đóng vai một Chuyên gia SEO & Content Strategist.
     > **Task:** Thực hiện nghiên cứu thị trường chuyên sâu về chủ đề: [CHỦ ĐỀ TỪ BƯỚC 1].
     > **Yêu cầu Output:**
     > 1.  **Top Ranking Analysis (SERP)**: Tìm 5-7 trang web/bài viết đang có thứ hạng cao nhất Google hiện nay về các từ khóa liên quan. Cung cấp URL và tiêu đề chính xác.
     > 2.  **Keyword Masterlist**:
     >     *   Primary Keywords: Các cụm từ khóa chính có lượng tìm kiếm cao nhất.
     >     *   Long-tail Keywords: Các từ khóa dài, cụ thể.
     >     *   LSI Keywords: Các từ khóa ngữ nghĩa liên quan.
     > 3.  **User Search Insight (PAS/PAA)**: Liệt kê danh sách "People Also Ask" và "Related Searches". Tập trung vào các câu hỏi về chi phí, độ khó, so sánh.
     > 4.  **Content Gap (Cơ hội)**: Các bài Top hiện tại đang thiếu điều gì mà chúng ta có thể giải quyết tốt hơn?
- **Fallback (Nếu lệnh research_import lỗi):** 
  - Yêu cầu người dùng nhấn nút "Import" thủ công trên giao diện NotebookLM.
  - Xác nhận "OK" với người dùng sau khi đã import nguồn xong.
- **QUAN TRỌNG: Dừng lại, trình bày kết quả Research và xin phê duyệt trước khi sang Bước 3.**
- **Post-Action**: Đánh dấu hoàn thành bước 2 trong `task.md`.


## 3. Viết Article (DỪNG LẠI ĐỂ HỎI Ý KIẾN NGƯỜI DÙNG)
- **Skill**: Sử dụng skill `Article-SEO-GEO`.
- **Action**: Viết bài dạng Long-form chuyên sâu.
- **Checklist**:
  - [ ] Tiêu đề H1 chứa từ khóa.
  - [ ] Ít nhất 5 thẻ H2.
  - [ ] Bảng so sánh (quan trọng cho GEO) - *Khuyến khích dùng Mermaid Chart*.
  - [ ] Case Study thực tế.
  - [ ] Câu ngắn gọn (<12 từ).
  - [ ] **Visual Strategy**:
    - [ ] Prompt tạo ảnh Thumbnail minh họa.
    - [ ] Biểu đồ minh họa (nếu có số liệu so sánh).
- **QUAN TRỌNG: Dừng lại, trình bày bài viết và xin phê duyệt trước khi sang Bước 4.**
- **Post-Action**: Đánh dấu hoàn thành bước 3 trong `task.md`.



## 4. Kiểm tra & Audit (DỪNG LẠI ĐỂ HỎI Ý KIẾN NGƯỜI DÙNG)
- **Skill**: Sử dụng skill `check-article`.
- **Action**: Kiểm tra lại bài viết LinkedIn.
- **Checklist**:
  - [ ] Đánh giá điểm số (Scorecard).
  - [ ] Audit chi tiết (SEO & GEO).
  - [ ] Đề xuất cải thiện (Action Plan).
- **QUAN TRỌNG: Dừng lại, trình bày kết quả Audit và xin phê duyệt trước khi sang Bước 5.**
- **Post-Action**: Đánh dấu hoàn thành bước 4 trong `task.md`.

## 5. Tổng kết & Walkthrough (DỪNG LẠI ĐỂ HỎI Ý KIẾN NGƯỜI DÙNG)
- **Action**: 
  1. Tạo file `walkthrough.md` tổng hợp lại toàn bộ quá trình, kết quả đạt được, các số liệu (metrics) và bài học rút ra.
  2. Kiểm tra lần cuối file `task.md` đảm bảo tất cả các mục đã được đánh dấu hoàn thành.
- **Goal**: Cung cấp tài liệu tổng kết để người dùng dễ dàng xem lại hoặc chia sẻ quy trình.
- **QUAN TRỌNG: Dừng lại và trình bày Walkthrough để người dùng xem lại toàn bộ.**

---
*Lưu ý: Luôn đảm bảo các file output được lưu vào thư mục artifacts để dễ dàng truy xuất.*