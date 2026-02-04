#!/bin/bash

# Antigravity SEO Kit Installer for Mac/Linux
# Usage: curl -fsSL https://raw.githubusercontent.com/YOUR_USERNAME/antigravity-seo-kit/main/install.sh | bash

REPO_URL="https://github.com/KHOAAI-HILL/antigravity-seo-kit.git" # <--- THAY THẾ USERNAME CỦA BẠN Ở ĐÂY
TEMP_DIR=$(mktemp -d)

echo -e "\n🚀 Đang tải bộ Antigravity SEO Kit..."

# 1. Clone về thư mục tạm
git clone -q "$REPO_URL" "$TEMP_DIR"

# 2. Kiểm tra và copy
if [ -d "$TEMP_DIR/.agent" ]; then
    echo -e "📦 Đang cài đặt Skills và Workflows..."
    
    mkdir -p .agent
    cp -R "$TEMP_DIR/.agent/"* .agent/
    
    echo -e "\n✅ CÀI ĐẶT THÀNH CÔNG!"
    echo -e "👉 Hãy thử gõ lệnh: /step-by-step-article-seo-geo"
else
    echo -e "\n❌ LỖI: Không tìm thấy thư mục .agent trong repository."
fi

# 3. Dọn dẹp
rm -rf "$TEMP_DIR"
