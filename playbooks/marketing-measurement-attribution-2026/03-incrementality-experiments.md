# 03 · Incrementality และการตัดสินใจข้ามช่องทาง

## คำถามที่แต่ละวิธีตอบ
| วิธี | ตอบ | ข้อจำกัด |
|---|---|---|
| Platform attribution | ระบบให้เครดิตช่องทางตนอย่างไร | overlap, window และ modeled conversions; ไม่ใช่ causality |
| Blended MER | net revenue รวม / spend รวมใน window เดียวกัน | มี organic/repeat/seasonality; ไม่ใช่ causal ROAS |
| Randomized holdout | ผลของการเสนอ exposure เทียบ control | ต้องสุ่ม, ขนาดพอ, รักษา assignment และติดตามผล |
| Geo experiment | ความต่างเมื่อเปิด/ลด media ในพื้นที่ | พื้นที่ไม่เหมือนกันและ spillover; ต้อง pre-period และ design ที่เหมาะสม |
| MMM | ความสัมพันธ์ยอดขายกับ media และปัจจัยอื่นตามเวลา | data/assumption-sensitive; ไม่ใช่ ground truth; ใช้ test ช่วย calibrate |

## วิธีทำ randomized test แบบ practical
1. เขียน estimand: incremental **paid net orders ต่อ eligible user** หรือ incremental **qualified/won leads ต่อ eligible user** ภายใน horizon ที่ระบุ โดยวิเคราะห์ตามกลุ่มที่สุ่ม (intention-to-treat) ไม่ใช่คัดเฉพาะคนที่เห็น ad
2. เลือก unit ที่ไม่เกิด spillover: user, household, account หรือ geography; สุ่มและ log assignment. หากหลาย contact อยู่บริษัทเดียวต้องพิจารณาสุ่มระดับ account
3. กำหนด baseline, meaningful effect, power, confidence level, วิธีคำนวณ sample, data lag และ budget ก่อนเริ่ม; หากไม่ feasible ใช้ exploratory study ระบุชัดว่าไม่สรุป causal
4. กำหนดช่วง observation และ cooldown ตามรอบคืนสินค้า/วงจรขาย; บันทึก stockouts, policy changes, outside media, consent/measurement coverage และ control contamination
5. ประเมิน effect + confidence interval ตาม unit และ design; ติดลบหรือใกล้ศูนย์มีความไม่แน่นอน ห้ามหาร iCPA ด้วยผล incremental ≤0 หรือช่วงที่คร่อม 0 โดยไม่อธิบาย

## Worked example สินค้า (สมมติ ไม่ใช่ผลจริง)
กลุ่มสุ่มเท่ากัน 10,000 eligible users ต่อกลุ่ม; treatment มี 400 paid orders, control มี 300 → rate 4% vs 3%, **incremental 1 percentage point**, หรือ 100 orders ใน treatment population. Spend ฿20,000 → point estimate iCPA ฿200/ incremental order; หาก CM2/order ฿250 ที่มีนิยาม/return-window สอดคล้อง incremental contribution ก่อน fixed costs ≈ 100×250 − 20,000 = ฿5,000. ไม่มี interval จึงยังไม่เพียงพอตัดสินใจ scale

## Worked example บริการ (สมมติ)
สุ่มบริษัท A/B จำนวนเท่ากัน 1,000 บริษัท; qualified leads ต่อ account ที่เกิดภายใน 60 วัน 60 vs 40 → lift 20 qualified accounts ใน treatment population. ไม่เท่ากับลูกค้าใหม่ 20 ราย; ต้องติดตาม won และต้นทุนบริการใน cohort ที่ mature และตรวจว่า account-level tracking ใช้ได้ หากปิดการขายล่าช้าให้แสดงข้อมูล preliminary. Google ระบุ lift availability ไม่เท่ากันทุก account [S1,S2]

## Decision gate
ผ่าน tracking + privacy + sample และ budget: รายงาน point, interval, downside และ operational capacity; positive ไม่แปลว่า profitable เสมอ. Data ขาด/underpowered = inconclusive; ใช้ sensitivity scenario และกำหนด review date ไม่เลือก winner จากการแอบดูผลหลายรอบ
