---
description: Quy trình tối ưu hóa nội dung video YouTube đa kênh (YouTube, LinkedIn, X.com, Beehiiv) chuẩn SEO & GEO sử dụng Perplexity.
---

# Workflow: Tối Ưu Video YouTube Đa Kênh (Perplexity)

// turbo-all
Quy trình này giúp biến một video YouTube (file phụ đề `.srt`) thành chuỗi nội dung chất lượng cao trên đa nền tảng, tối ưu cho SEO và AI Search (GEO), tận dụng sức mạnh tìm kiếm thời gian thực của Perplexity.

## 0. Khởi tạo Task & Plan (DỪNG LẠI ĐỂ HỎI Ý KIẾN NGƯỜI DÙNG)
- **Action**: 
  1. Tạo file `task.md` liệt kê toàn bộ 9 bước trong quy trình.
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
- **Tool**: Sử dụng MCP `perplexity-ask`.
- **Action**:
  1. Sử dụng công cụ `perplexity_ask` để thực hiện nghiên cứu chuyên sâu về chủ đề đã phân tích ở Bước 1.
  2. **Prompt Framework (Copy & Paste để sử dụng):**
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
- **QUAN TRỌNG: Dừng lại, trình bày kết quả Research và xin phê duyệt trước khi sang Bước 3.**
- **Post-Action**: Đánh dấu hoàn thành bước 2 trong `task.md`.


## 3. Đề xuất Tiêu đề YouTube (DỪNG LẠI ĐỂ HỎI Ý KIẾN NGƯỜI DÙNG)
- **Input**: Kết quả Research + Nội dung gốc.
- **Action**: 
  1. Đề xuất 5 tiêu đề (50-70 ký tự) tối ưu cho hiển thị mobile và click-through rate (CTR).
  2. Chọn 1 tiêu đề tốt nhất và giải thích lý do (dựa trên từ khóa và yếu tố tâm lý).
  3. **QUAN TRỌNG: Dừng lại và yêu cầu người dùng xác nhận hoặc chọn tiêu đề trước khi tiếp tục.**
- **Output**: 1 Tiêu đề chính thức.
- **Post-Action**: Đánh dấu hoàn thành bước 3 trong `task.md`.

## 4. Viết Mô tả & Tạo Prompt Thumbnail (DỪNG LẠI ĐỂ HỎI Ý KIẾN NGƯỜI DÙNG)
- **Skill**: Sử dụng skill `viet-mo-ta-youtube`.
- **Action**: 
  1. Viết mô tả chi tiết dựa trên Tiêu đề đã chọn và file `.srt`.
  2. Tạo Prompt chi tiết (Tiếng Việt) để vẽ ảnh Thumbnail bằng công cụ **Nano Banana Pro**. Prompt cần mô tả kỹ bố cục, màu sắc, text trên ảnh (ngắn gọn, gây tò mò), và cảm xúc nhân vật để tối ưu CTR.
- **Checklist**:
  - [ ] Hook 2 dòng đầu chứa từ khóa.
  - [ ] Timestamps chi tiết (trích xuất từ `.srt`).
  - [ ] Nội dung chính (Bullet points).
  - [ ] FAQ (tối ưu cho AI Search).
  - [ ] Links & Hashtags.
  - [ ] Prompt Thumbnail cho Nano Banana Pro (Mô tả hình ảnh + Text overlay).
- **QUAN TRỌNG: Dừng lại, trình bày mô tả & prompt và xin phê duyệt trước khi sang Bước 5.**
- **Post-Action**: Đánh dấu hoàn thành bước 4 trong `task.md`.

## 5. Viết Article LinkedIn (DỪNG LẠI ĐỂ HỎI Ý KIẾN NGƯỜI DÙNG)
- **Skill**: Sử dụng skill `Article-SEO-GEO`.
- **Action**: Viết bài dạng Long-form chuyên sâu.
- **Checklist**:
  - [ ] Tiêu đề H1 chứa từ khóa.
  - [ ] Ít nhất 5 thẻ H2.
  - [ ] Bảng so sánh (quan trọng cho GEO).
  - [ ] Case Study thực tế.
  - [ ] Câu ngắn gọn (<12 từ).
- **QUAN TRỌNG: Dừng lại, trình bày bài viết và xin phê duyệt trước khi sang Bước 6.**
- **Post-Action**: Đánh dấu hoàn thành bước 5 trong `task.md`.

## 6. Viết Article X.com (DỪNG LẠI ĐỂ HỎI Ý KIẾN NGƯỜI DÙNG)
- **Skill**: Sử dụng skill `Article-SEO-GEO`.
- **Format**: X.com Article Long-form (https://x.com/compose/articles).
- **Tone**: Punchy, trực diện, viral-friendly, storytelling.
- **X.com Article Format Framework:**
  > **1. Cover Image:** Ảnh bìa lớn ở đầu bài (giống Thumbnail YouTube, tạo ấn tượng đầu tiên).
  > **2. Tiêu đề H1:** Lớn, đậm, ngay dưới Cover Image. Ngắn gọn, gây tò mò.
  > **3. Heading đánh số:** Sử dụng format "1.", "2.", "3."... để chia section. In đậm.
  > **4. Single-column layout:** Gọn gàng, dễ đọc (giống Medium/LinkedIn Article).
  > **5. Bold keywords:** Nhấn mạnh từ khóa quan trọng bằng **in đậm**.
  > **6. Paragraph spacing:** Khoảng cách rõ ràng giữa các đoạn để dễ scan.
  > **7. Bảng so sánh:** Nếu có, giúp tăng tính thuyết phục và GEO.
  > **8. CTA cuối bài:** Link YouTube + Link cộng đồng.
- **Checklist**:
  - [ ] Cover Image placeholder.
  - [ ] Tiêu đề cực ngắn và thu hút.
  - [ ] Heading đánh số (1., 2., 3...).
  - [ ] Tập trung vào số liệu cụ thể.
  - [ ] Bold từ khóa quan trọng.
  - [ ] CTA trực tiếp cuối bài.
- **QUAN TRỌNG: Dừng lại, trình bày bài viết và xin phê duyệt trước khi sang Bước 7.**
- **Post-Action**: Đánh dấu hoàn thành bước 6 trong `task.md`.

## 7. Viết Article Beehiiv (DỪNG LẠI ĐỂ HỎI Ý KIẾN NGƯỜI DÙNG)
- **Skill**: Sử dụng skill `Article-SEO-GEO`.
- **Format**: Newsletter Article dạng Long-form (tối ưu cho email marketing).
- **Tone**: Thân thiện, chuyên nghiệp, dễ đọc trên email client.
- **Beehiiv Article Format Framework:**
  > **1. Hook mạnh:** 2-3 câu ngắn với số liệu/claim gây chú ý.
  > **2. Sapo tóm tắt:** 1 câu mô tả giá trị bài viết (GEO-friendly).
  > **3. Cấu trúc H2 đánh số:** ## 1., ## 2., ## 3.  rõ ràng.
  > **4. Bullet points:** Ưu tiên danh sách, tối thiểu 8 bullets.
  > **5. Bảng so sánh:** Ít nhất 1 bảng để AI dễ trích xuất.
  > **6. Case Study:** Ví dụ thực tế với số liệu cụ thể.
  > **7. FAQ:** Tối thiểu 5 câu hỏi (Featured Snippet ready).
  > **8. About Author:** Tăng E-E-A-T với thông tin tác giả.
  > **9. CTA cuối bài:** Link YouTube + Skool + Docs.
  > **10. Hashtags:** 8-10 hashtags phù hợp.
- **Checklist**:
  - [ ] Hook với số liệu ấn tượng.
  - [ ] Câu sapo tóm tắt giá trị bài viết.
  - [ ] Ít nhất 7 thẻ H2.
  - [ ] Câu ngắn gọn (≤12 từ).
  - [ ] Bảng so sánh (5+ cột).
  - [ ] Case Study thực tế.
  - [ ] FAQ (≥5 câu).
  - [ ] Mục About Author.
  - [ ] Internal links (YouTube, Skool, Docs).
  - [ ] 8-10 hashtags.
- **QUAN TRỌNG: Dừng lại, trình bày bài viết và xin phê duyệt trước khi sang Bước 8.**
- **Post-Action**: Đánh dấu hoàn thành bước 7 trong `task.md`.

## 8. Kiểm tra & Audit (DỪNG LẠI ĐỂ HỎI Ý KIẾN NGƯỜI DÙNG)
- **Skill**: Sử dụng skill `check-article`.
- **Action**: Kiểm tra lại bài viết LinkedIn, X.com và Beehiiv.
- **Checklist**:
  - [ ] Đánh giá điểm số (Scorecard).
  - [ ] Audit chi tiết (SEO & GEO).
  - [ ] Đề xuất cải thiện (Action Plan).
- **QUAN TRỌNG: Dừng lại, trình bày kết quả Audit và xin phê duyệt trước khi sang Bước 9.**
- **Post-Action**: Đánh dấu hoàn thành bước 8 trong `task.md`.

## 9. Tổng kết & Walkthrough (DỪNG LẠI ĐỂ HỎI Ý KIẾN NGƯỜI DÙNG)
- **Action**: 
  1. Tạo file `walkthrough.md` tổng hợp lại toàn bộ quá trình, kết quả đạt được, các số liệu (metrics) và bài học rút ra.
  2. Kiểm tra lần cuối file `task.md` đảm bảo tất cả các mục đã được đánh dấu hoàn thành.
- **Goal**: Cung cấp tài liệu tổng kết để người dùng dễ dàng xem lại hoặc chia sẻ quy trình.
- **QUAN TRỌNG: Dừng lại và trình bày Walkthrough để người dùng xem lại toàn bộ.**

---
*Lưu ý: Luôn đảm bảo các file output được lưu vào thư mục artifacts để dễ dàng truy xuất.*
