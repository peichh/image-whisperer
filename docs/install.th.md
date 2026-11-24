# วิธีติดตั้ง Image Whisperer

ใช้ฟรีทั้งหมด ไม่ต้องมี API key

## 1. แอป Gemini (เว็บ มือถือ Mac) สำหรับบัญชีส่วนตัว

ตั้งแต่ 17 พ.ย. 2026 Google เปลี่ยน Gems เป็น "Skills"

1. ดาวน์โหลดไฟล์ `dist/image-whisperer.zip`
2. เปิด Gemini แล้วไปที่ **Skills** → **New skill** → **Upload** แล้วเลือกไฟล์ zip
3. บันทึก จากนั้นลองพิมพ์ "ขอรูปแมวนอนบนโซฟา ถ่ายมือถือ" หรือพิมพ์ `/image-whisperer` ตามด้วยสิ่งที่ต้องการ

## 2. Gems (บัญชีที่ทำงาน/โรงเรียน)

1. ไปที่ **Gems** → **New Gem** แล้วตั้งชื่อ `Image Whisperer`
2. ในช่อง Instructions ให้วางข้อความใต้เส้น `---` ของไฟล์ `integrations/standalone/image-whisperer-instructions.md`
3. ถ้าต้องการ ให้เพิ่มไฟล์ในส่วน Knowledge ตามรายการใน `integrations/gemini-gems/README.md`

## 3. Gemini CLI / Antigravity

```bash
gemini skills install https://github.com/peichh/image-whisperer.git
```
ถ้าใช้ Antigravity ให้คัดลอกโฟลเดอร์ไปไว้ที่ `.agents/skills/image-whisperer/`

## 4. ใช้กับแชทอื่น (ChatGPT, Claude และอื่นๆ)

คัดลอกเนื้อหาใน `integrations/standalone/image-whisperer-instructions.md` ไปวางเป็น custom instructions หรือวางไว้ตอนต้นแชท

## 5. Claude Code และ agent อื่นๆ

```bash
git clone https://github.com/peichh/image-whisperer.git ~/.claude/skills/image-whisperer
```
