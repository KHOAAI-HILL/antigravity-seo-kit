#!/bin/bash

# Antigravity SEO Kit Installer for Mac/Linux
# Usage: curl -fsSL https://raw.githubusercontent.com/YOUR_USERNAME/antigravity-seo-kit/main/install.sh | bash

REPO_URL="https://github.com/KHOAAI-HILL/antigravity-seo-kit.git" # <--- THAY THẾ USERNAME CỦA BẠN Ở ĐÂY
TEMP_DIR=$(mktemp -d)

echo -e "\n> Dang tai bo Antigravity SEO Kit..."

# 1. Clone về thư mục tạm
git clone -q "$REPO_URL" "$TEMP_DIR"

# 2. Kiểm tra và copy
if [ -d "$TEMP_DIR/.agent" ]; then
    echo -e "📦 Dang cai dat Skills va Workflows..."
    
    mkdir -p .agent
    cp -R "$TEMP_DIR/.agent/"* .agent/
    
    echo -e "\nOK! CAI DAT THANH CONG!"
    echo -e "> Hay thu go lenh: /step-by-step-article-seo-geo"
else
    echo -e "\nX LOI: Khong tim thay thu muc .agent trong repository."
fi

# 3. Dọn dẹp
rm -rf "$TEMP_DIR"
