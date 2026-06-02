# ขึ้นเว็บ HAM SPU ออนไลน์ (Django)

เว็บชมรมรันด้วย **Django** ชื่อแสดงในเบราว์เซอร์: **HAM SPU | ชมรมวิทยุสมัครเล่น มหาวิทยาลัยศรีปทุม**

## รันในเครื่อง

```bash
cd /Users/kittapat.chi/spu-amateur-radio
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

เปิด http://127.0.0.1:8000

## Deploy บน Render (ฟรี, แนะนำ)

1. Push โปรเจกต์ขึ้น GitHub (repo สาธารณะหรือส่วนตัว)
2. สมัคร [render.com](https://render.com) → **New** → **Blueprint**
3. เชื่อม repo นี้ — Render อ่านไฟล์ `render.yaml` ให้อัตโนมัติ
4. หลัง deploy จะได้ URL เช่น `https://ham-spu-club.onrender.com`
5. ใน **Environment** ของ Render ตั้ง:
   - `CSRF_TRUSTED_ORIGINS` = `https://ชื่อ-service-ของคุณ.onrender.com`
   - `ALLOWED_HOSTS` = `.onrender.com,ชื่อโดเมนของคุณ` (ถ้ามีโดเมน)

### เปลี่ยนชื่อเว็บ / โดเมนของชมรม

- **ชื่อในแท็บเบราว์เซอร์:** แก้ `SITE_NAME`, `SITE_SHORT` ใน `config/settings.py`
- **โดเมนมหาวิทยาลัย (เช่น ham.spu.ac.th):** ตั้ง CNAME ชี้ไปที่ Render แล้วเพิ่ม Custom Domain ใน Render Dashboard

## ตัวแปรสภาพแวดล้อม (Production)

| ตัวแปร | ตัวอย่าง |
|--------|----------|
| `DEBUG` | `false` |
| `SECRET_KEY` | สุ่มยาวๆ (Render generate ให้ได้) |
| `ALLOWED_HOSTS` | `.onrender.com` |
| `CSRF_TRUSTED_ORIGINS` | `https://your-app.onrender.com` |

## โฟลเดอร์เดิม `HAM SPU/`

เป็นเวอร์ชัน HTML เก่า — ใช้ Django เป็นหลักแล้ว โฟลเดอร์เก่าเก็บไว้อ้างอิงได้
