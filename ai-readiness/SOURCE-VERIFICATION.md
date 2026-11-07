# Source verification log · 7 พ.ย. 2026

การ review ด้านล่างทำโดย AI agent อ่านแหล่งที่ลิงก์ ณ วันที่ระบุ; `verified` ใน registry หมายถึง **claim ที่ระบุใน scope แคบ ๆ สอดคล้องกับหน้าแหล่ง ณ วันตรวจ** ไม่ใช่ legal opinion, independent expert review, current account permission หรือการรับประกันอนาคต. ไม่ copy เนื้อหาลิขสิทธิ์เป็น corpus สำหรับฝึก. URLs อาจเปลี่ยนได้; re-check ก่อนตัดสินใจ.

| Claim | แหล่งตรง / ส่วนที่ตรวจ | ผลและขอบเขต | สิ่งที่ยังไม่ทราบ |
|---|---|---|---|
| C-001 | [MSCI GICS methodology April 2026, §1.1](https://www.msci.com/indexes/documents/methodology/1_MSCI_Global_Industry_Classification_Standard_GICS_Methodology_20250220.pdf) | ระบุโครงสร้าง 11 sectors, 25 groups, 74 industries, 163 sub-industries ใน edition นั้น | edition ล่าสุดหลังวันที่ตรวจ, สิทธิแจกจ่าย taxonomy ทั้งชุด และ membership ของ index ไม่ยืนยันจาก source นี้ |
| C-009 | [YouTube monetization policies, introduction / reused content](https://support.google.com/youtube/answer/1311392?hl=en) | หน้ามีนโยบาย reused content และ applies to ช่องใน/สมัคร YPP | ผลอนุมัติของช่องเฉพาะ, สิทธิ copyright และ future policy |
| C-011 | [FTC Disclosures 101, When to Disclose](https://www.ftc.gov/business-guidance/resources/disclosures-101-social-media-influencers) | FTC แนะนำเปิดเผย material connection และระบุว่ากฎหมายประเทศอื่นอาจเกี่ยวข้อง | ไม่ใช่การยืนยันกฎหมายไทย; สถานการณ์ cross-border ให้ผู้เชี่ยวชาญตรวจ |
| C-012 | [Google Analytics manual tagging](https://support.google.com/analytics/answer/11242870) | บรรยายการใช้ UTM เก็บ traffic-source dimensions และข้อจำกัด field | ไม่มีการพิสูจน์ incremental sales หรือยืนยัน tracking ของบัญชี; คำเตือน causal เป็น methodology ไม่ใช่ข้ออ้างว่า Google รับรอง |
| C-007 | [TikTok Content Sharing Guidelines](https://developers.tiktok.com/docs/en/content-sharing-guidelines) | รอบนี้ fetch ตอบ HTTP 403 จึง **ยัง needs_review** | ข้อความ guideline ปัจจุบัน, app approval, permissions, consent และ intended use; ต้องตรวจผ่านบัญชี/หน้า official ที่เข้าถึงได้ |
| C-004 / C-005 | vendor report / Shopee landing page | **ยัง needs_review**: ไม่พบ/ตรวจ direct account-specific rate card จากข้อมูลที่มี | actual GP cut scope, timeline, category, statement และ rate ที่มีผล; ห้ามใช้เป็น verified rate |

`reviewed_calculation` ของ C-003 เป็นการตรวจ algebra ภายใต้ assumptions ด้วย unit tests ไม่ยืนยันต้นทุน/fee/เงื่อนไขของธุรกิจ. Claims อื่นคง `needs_review` แม้ source เป็น official เพราะยังไม่ได้ตรวจเนื้อหาและ scope รอบนี้.
