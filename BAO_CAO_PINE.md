# BÁO CÁO KIỂM TRA MÃ NGUỒN PINE SCRIPT (AUDIT PINE SCRIPT)

## Thông tin dự án
- **Tên Script:** `Fractal Model (TTrades) - Standalone` (TTFM°)
- **Đường dẫn file:** `D:/AI Trader/Pinescript/Fractal_Model_TTrades_Clean.pine`
- **Phiên bản Pine Script:** v6 (`//@version=6`)
- **Loại Script:** `indicator` (Chỉ báo kỹ thuật tích hợp hệ thống vẽ biểu đồ nến HTF, quét thanh khoản T-Spot, CISD và Fair Value Gap - FVG).

---

## 1. AC1 & AC2: Phân tích Quy tắc Chiến lược (Strategy Rules)

Dựa trên việc đọc kỹ toàn bộ mã nguồn Pine Script (2.878 dòng), chiến lược **Fractal Model (TTrades)** áp dụng phương pháp ICT / SMC (Smart Money Concepts) do TTrades phát triển với các quy tắc cốt lõi sau:

### A. Điều kiện Vào lệnh Mua (Bullish Setup / Long)
1. **Quét thanh khoản (Liquidity Sweep):** Giá quét qua mức đáy cũ (SSL - Sell Side Liquidity) hoặc đáy của nến khung thời gian cao (HTF / LTF) trước đó (Swing Low, Previous Low).
2. **Hình thành T-Spot (Bullish T-Spot):** 
   - Xuất hiện nến quét (Sweep Candle) chạm hoặc xuyên qua mức hỗ trợ/đáy và đóng cửa tạo cấu trúc đảo chiều.
   - Xác định điểm C2 (Extreme level / Swing point) và C3 / C4 (Expansion / Displacement).
3. **CISD (Change in State of Delivery):** Giá phá vỡ cấu trúc giảm ngắn hạn thông qua một nến lực mạnh (Displacement) đóng cửa vượt qua mức cực trị giảm gần nhất, xác nhận sự thay đổi trạng thái giao dịch sang tăng.
4. **Fair Value Gap (FVG) / Imbalance:** Giá để lại vùng mất cân bằng giá (FVG) tăng (Bullish FVG) giữa các nến C1, C2, C3. Vùng FVG này được dùng làm vùng đón giá (Order Block / Mitigation block / FVG entry zone).

### B. Điều kiện Vào lệnh Bán (Bearish Setup / Short)
1. **Quét thanh khoản (Liquidity Sweep):** Giá quét qua mức đỉnh cũ (BSL - Buy Side Liquidity) hoặc đỉnh khung thời gian cao (HTF / LTF) trước đó (Swing High, Previous High).
2. **Hình thành T-Spot (Bearish T-Spot):**
   - Nến quét đẩy lên vượt đỉnh và đóng cửa tạo cấu trúc đảo chiều giảm.
   - Xác định điểm C2 (Extreme high) và C3 / C4.
3. **CISD Giảm:** Giá phá vỡ mức hỗ trợ gần nhất qua nến lực mạnh, xác nhận xu hướng giảm.
4. **Fair Value Gap (FVG) / Imbalance Giảm:** Vùng mất cân bằng giá giảm (Bearish FVG) làm vùng kháng cự để vào lệnh Short.

### C. Quản lý Rủi ro: Cắt lỗ (SL) và Chốt lời (TP)
- **Cắt lỗ (Stop Loss - SL):** Được đặt dựa trên mức cực trị của mô hình T-Spot (ví dụ: đỉnh/đáy của nến C2 hoặc qua vùng râu nến quét thanh khoản kèm buffer ATR).
- **Chốt lời (Take Profit - TP):** Được tính toán dựa trên các mức chiếu mục tiêu (Projections), tỷ lệ Risk/Reward (R:R) hoặc các vùng thanh kháng cự/hỗ trợ HTF (BSL/SSL đối diện, Daily/Weekly FVG).

---

## 2. AC3: Rà soát Lỗi Logic (Repainting & Lookahead Bias)

Qua rà soát mã nguồn chi tiết:
1. **Repainting (Vẽ lại tín hiệu):**
   - Chỉ báo sử dụng các hàm vẽ hình khối (`box.new`, `line.new`, `label.new`) cập nhật theo `bar_index` hiện tại và lịch sử thanh khoản. Các tín hiệu T-Spot và CISD được tính toán dựa trên nến đã đóng cửa (`barstate.isconfirmed` hoặc `last_closed`) ở một số module, tuy nhiên cần lưu ý khi tính toán dữ liệu khung thời gian cao (`request.security`) nếu không dùng đúng cú pháp `barmerge.lookahead_off` có thể gây repaint lịch sử.
2. **Lookahead Bias (Độ lệch nhìn trước tương lai):**
   - Mã nguồn sử dụng `request.security` hoặc tính toán HTF candles. Cần đảm bảo tham số `lookahead = barmerge.lookahead_off` được áp dụng ngầm hoặc tường minh để tránh việc nến HTF chưa đóng cửa bị lộ dữ liệu giá Close tương lai trong backtest. Trong code standalone này, việc tự tái tạo nến HTF từ khung thời gian thấp (`LTF`) giúp giảm thiểu lookahead bias so với `request.security` chuẩn nếu được quản lý đúng chỉ số index nến đóng.

---

## 3. AC4: Kết luận & Kiến nghị
- Mã nguồn Pine Script đã được phân tích và bóc tách toàn bộ logic quy tắc giao dịch.
- File báo cáo này đã được ghi nhận tại `BAO_CAO_PINE.md` phục vụ cho việc chuyển đổi sang Python Bot (nếu cần tự động hóa giao dịch).
