# วัดผล Affiliate และกระทบยอด

ตลาด TH · research 7 พ.ย. 2026 · [แหล่ง](SOURCES.md)

## Data contract และข้อจำกัด
เก็บ aggregate ต่อ platform × campaign × content version × product × cohort/window: impression/view, qualified click, attributed orders, pending, approved, reversed และ paid (จำนวนและ ฿), ad spend, software, แรงงานและต้นทุนอื่น. Program ID/order ID เก็บเฉพาะที่ได้รับอนุญาต; ไม่ดึง PII ที่ไม่จำเป็น ไม่สร้าง cross-platform user profile หรือพยายามหลบข้อจำกัด. บางระบบให้ข้อมูลแค่ aggregate หรือลิงก์รวมหลายโพสต์: ห้ามอนุมานยอดรายโพสต์จากข้อมูลรวม.

ใช้ official sub-ID หรือ tracking ID **เมื่อโปรแกรมและช่องทางอนุญาตและรองรับ**; พิสูจน์ลิงก์/ปลายทางก่อนใช้งาน ไม่เติม UTM หรือตัว redirect ลง affiliate link โดยอัตโนมัติ. หากมีเว็บไซต์ของตนและ traffic เข้าเว็บไซต์ก่อน ให้ใช้ UTM ที่ตรวจ policy แล้ว; GA4 manual tags จำแนก traffic บน property ที่ตนวัดได้ ไม่ทำให้เห็นยอดซื้อ Shopee หรือพิสูจน์ว่า affiliate ได้คอม [S15]. Redirect อาจทำ parameters หาย จึงทดสอบ end-to-end [S16]. ห้ามใส่ PII ใน URL.

## สถานะและการกระทบยอด
1. **Capture:** เก็บ timestamp, timezone, source report, cohort, attribution window, report version และสกุลเงิน; original statement เก็บแบบ read-only ตามนโยบาย.
2. **Reconcile:** เทียบ eligible clicks/order กับ affiliate statement โดยใช้ ID ที่อนุญาตและ grain ที่มี; ห้ามบวกยอด report คนละเวลาเป็นยอดใหม่. Flag missing/duplicate/refund และ difference ที่ยังอธิบายไม่ได้.
3. **Mature:** pending ยังไม่ถือเป็น approved; เมื่อรายการ resolve ให้โยกสถานะ ไม่เพิ่มคำสั่งซื้อซ้ำ. คอม approved อาจถูก reverse ภายหลัง; ledger บันทึก delta adjustment และวันที่เกิด.
4. **Settle:** paid เทียบ payout statement และ bank receipt ที่ผู้มีสิทธิรับผิดชอบดู; แยก withholding, conversion และค่าธรรมเนียม. ถ้าไม่มี payout reference ให้สถานะ unmatched ไม่เดาว่าเป็นรายการเดียวกัน.
5. **Freeze/restate:** snapshot วันที่ปิดงวดและบันทึก revision เมื่อ platform ปรับยอดย้อนหลัง; ใช้ cohort เดียวกันและ cutoff เดียวกันเมื่อเปรียบเทียบ.

ตัวอย่างสมมติ: มี 10 pending orders, ต่อมา 7 approved, 2 rejected, 1 pending; รวมยังเป็น 10 ไม่ใช่ 20. Approved commission ฿210, paid ฿150, จ่ายค้าง ฿60 **เฉพาะเมื่อ statement แสดงว่า ฿150 มาจาก approved ฿210 ชุดเดียวกัน และยังไม่มี reversal/fees**. ข้อมูลไม่ครบให้ unmatched.

## Decision ไม่หลงตัวเลข
- Contribution = net approved commission หลัง reversal − ค่าแรง/เครื่องมือ/ไฟ/ads ที่จัดสรรตามวิธีเดียวกัน; แยก paid cash, ภาษีและค่าเสื่อม
- Approval rate = approved / resolved eligible orders โดยระบุช่วงเวลาและนิยาม; ไม่รวม pending ใน denominator และไม่เปรียบเทียบ cohort อายุไม่เท่ากัน
- Attributed order หรือรายงาน platform ≠ incremental order. ถ้าจะทดสอบ causal effect ใช้ holdout/randomization ที่เหมาะสมและได้รับอนุญาต ระวัง sample เล็ก, seasonality และ spillover; ยังไม่มีการทดลองให้ระบุ unknown
- ตั้ง kill criteria และ cap ก่อนเริ่ม; งดขยายเมื่อ tracking แตก, reconciled variance หาคำตอบไม่ได้, สิทธิไม่ชัด หรือ contribution ไม่ถึงเป้าที่ owner กำหนด
