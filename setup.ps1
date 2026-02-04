# Antigravity SEO Kit Installer for Windows
# Usage: powershell -ExecutionPolicy Bypass -File setup.ps1

$repoUrl = "https://github.com/KHOAAI-HILL/antigravity-seo-kit.git" # <--- THAY THẾ USERNAME CỦA BẠN Ở ĐÂY
$tempDir = Join-Path $env:TEMP "antigravity-seo-kit-$(Get-Random)"

Write-Host "`n🚀 Đang tải bộ Antigravity SEO Kit..." -ForegroundColor Cyan

# 1. Clone về thư mục tạm
New-Item -ItemType Directory -Force -Path $tempDir | Out-Null
git clone -q $repoUrl $tempDir

# 2. Kiểm tra và copy
if (Test-Path "$tempDir\.agent") {
    Write-Host "📦 Đang cài đặt Skills và Workflows..." -ForegroundColor Cyan
    
    # Tạo thư mục .agent nếu chưa có
    if (-not (Test-Path ".agent")) { New-Item -ItemType Directory -Force -Path ".agent" | Out-Null }
    
    # Copy đè
    Copy-Item -Path "$tempDir\.agent\*" -Destination ".agent" -Recurse -Force
    
    Write-Host "`n✅ CÀI ĐẶT THÀNH CÔNG!" -ForegroundColor Green
    Write-Host "👉 Hãy thử gõ lệnh: /step-by-step-article-seo-geo" -ForegroundColor White
} else {
    Write-Host "`n❌ LỖI: Không tìm thấy thư mục .agent trong repository." -ForegroundColor Red
}

# 3. Dọn dẹp
Remove-Item $tempDir -Recurse -Force -ErrorAction SilentlyContinue
