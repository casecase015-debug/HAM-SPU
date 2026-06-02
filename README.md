# ชมรมวิทยุสมัครเล่น ม.ศรีปทุม (HAM SPU)

เว็บไซต์ชมรม — **Django** · โทนสีกรมท่า + ฟ้า + ชมพูอ่อน (สี ม.ศรีปทุม)

## เริ่มใช้งาน

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

→ http://127.0.0.1:8000

## โครงสร้าง

- `club/` — หน้าเว็บ, ข้อมูล, templates
- `config/` — settings Django
- `render.yaml` — deploy บน Render
- `DEPLOY.md` — วิธีขึ้นอินเทอร์เน็ต + ตั้งโดเมน

## หน้าเว็บ

| URL | เนื้อหา |
|-----|---------|
| `/` | หน้าแรก |
| `/about/` | เกี่ยวกับชมรม |
| `/policy/` | นโยบายสื่อสาร |
| `/callsign/` | สัญญาณเรียกขาน |
| `/frequencies/` | ตารางความถี่ |
| `/project/` | โครงการศูนย์วิทยุฯ (วางแผน) |
| `/team/` | คณะกรรมการ |
| `/members/` | สมาชิก |
