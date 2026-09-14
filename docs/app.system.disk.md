# `GET /app/system/disk`

> `Display disk usage, partitions, and I/O statistics.`

---

## 🔹 Description

**Displays disk usage, available partitions, and disk I/O statistics reported by the system.**

---

## 🔹 Page

**Path:** `/app/system/disk`

**Authentication:** `None`

**Content-Type:** `text/html`

---

## 🔹 Content

* Overall disk usage percentage.
* Disk usage statistics excluding the displayed percentage.
* List of available disk partitions and their properties.
* Disk I/O statistics grouped by device.
* Visual disk usage bar.
* Back button for returning to the previous page.
* Displays fallback messages when no partitions or disk I/O information are available.

---

## 🔹 Dependencies

* `disk.html`
* `/static/js/system/disk.js`
* `/static/css/main.css`
* `/api/system/disk`

---

## 🔹 Notes

* Disk data is initially rendered server-side from `disk`.
* The disk usage `percent` field is displayed separately from the other usage fields.
* Partition and I/O fields are generated dynamically from the returned API data.
