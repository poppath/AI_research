# แผนที่วิจัยกว้าง → เลือกลงลึก

Research TH · 7 พ.ย. 2026 · นี่คือการจัดลำดับตามความเสี่ยงและ dependency สมมติสำหรับผู้เริ่มต้น ไม่ใช่ market sizing หรือข้อมูลบัญชีจริง. อ่านคู่กับ [7M](00-START-HERE.md) และ [แหล่งหลัก](SOURCES.md).

## ภูมิทัศน์ 12 ด้าน
| ด้าน | คำถามที่ต้องตอบ | หลักฐาน/ผลลัพธ์ | ลำดับ |
|---|---|---|---|
| ผู้ชมและ demand | ใครมีปัญหาอะไรและค้นหาคำตอบอย่างไร | interviews/คำถามที่ได้รับสิทธิ/แหล่งข้อมูลจริง | P1 |
| product/program | สินค้าและ traffic มีสิทธิรับคอมหรือไม่ | eligibility, return, payout; [บท 03](03-product-program-selection.md) | P1 |
| economics/cash | กำไรหลังต้นทุนและ reversal พอหรือไม่ | statement + labor, cap, cash | P1 |
| content/IP/trust | ทำเนื้อหาต้นฉบับและพิสูจน์ claim อย่างไร | asset rights, QA, [บท 07](07-content-audience-strategy.md) | P1 |
| compliance & category | เปิดเผย affiliate/AI อย่างไร, สินค้าใดต้องอนุญาต | ตรวจ platform และหน่วยงานไทย [บท 09](09-operations-business-model.md) | P1 |
| experiment & measurement | เรารู้อะไรจริงจากข้อมูลเล็ก/attribution | cohort, test design [บท 08](08-testing-and-learning.md) | P1 |
| agent & cyber security | ข้อมูลเว็บหลอก AI หรือ token รั่วได้อย่างไร | threat model, [บท 10](10-agent-security.md) | P1 ก่อนเชื่อม tools |
| audience/owned channels | ลดการพึ่ง algorithm โดยไม่เก็บข้อมูลเกินจำเป็น | traffic และ consent, [บท 07](07-content-audience-strategy.md) | P2 |
| distribution/platform | native vs API, การแปลง format | permissions, per-platform QA [บท 00](00-START-HERE.md) | P1 ก่อน publish |
| operations/resilience | 24h job, failure, backup และคนดูแล | runbook, RTO/RPO ที่ทีมกำหนด [บท 10](10-agent-security.md) | P1 ก่อน automation |
| business model | affiliate vs production service vs original IP | economics, contract, [บท 09](09-operations-business-model.md) | P2 |
| portfolio/scale | ควรเพิ่มหมวด เครื่อง ทีม หรือหยุดเมื่อไร | cohort mature, safety gate, documented thresholds | P3 หลัง pilot |

P1 = ทำก่อน launch หรือเชื่อม tool; P2 = ทดลองหลัง P1; P3 = หลังผลและความเสี่ยงผ่าน ไม่ใช่ระยะเวลาการันตี. P1 ไม่จำเป็นต้องรอวิจัย P2/P3 เสร็จ. รอบนี้ลงลึก 4 ด้านใหม่: audience/content, experiments, business models/กฎหมายไทย และ agent security. ด้านอื่นเชื่อมบทเดิม ไม่อ้างว่าศึกษาทุกด้านลึกเท่ากัน.

## Decision sequence
1. ระบุ audience, pain, ข้อเสนอและ platform → ตรวจสิทธิสินค้า/claims → กำหนดต้นทุนและ cap
2. เลือก concept ที่แก้ pain จริง + evidence + rights → คนตรวจและเผยแพร่ใน flow ที่อนุญาต
3. ตั้ง hypothesis/measurement ก่อนเผยแพร่; ถ้าไม่มี randomization หรือ data พอ ให้เรียก exploratory
4. กระทบยอดเมื่อ mature → ทบทวน safety, contribution, เวลาและความพึงพอใจ → stop/iterate/scale ตามเกณฑ์ที่กำหนดก่อนเริ่ม
5. เพิ่ม autonomy เฉพาะงานที่ security/approval ผ่าน ไม่ใช้ความสำเร็จของ content เป็นหลักฐานว่า API อนุญาต

## คำถามที่ต้องได้จากผู้ใช้ก่อนแผนเฉพาะ
สินค้าหรือบริการ, กลุ่มลูกค้า, สิทธิ/ช่องที่มี, เวลาเจ้าของต่อสัปดาห์, เงิน cap และโครงสร้างต้นทุน, ข้อมูล baseline, ความสามารถผลิต, ประเทศและ category. หากไม่มีข้อมูลให้ใส่ unknown ไม่คิดรายได้หรือ conversion แทน.
