# `GET /app/system/system`

> `Display system boot information and logged-in users.`

---

## 🔹 Description

**Displays general system information, including the system boot time and currently logged-in users.**

---

## 🔹 Page

**Path:** `/app/system/system`

**Authentication:** `None`

**Content-Type:** `text/html`

---

## 🔹 Content

* System boot time as a Unix timestamp.
* List of currently logged-in users.
* User information grouped by user.
* Back button for returning to the previous page.
* Displays a fallback message when no users are logged in.

---

## 🔹 Dependencies

* `system.html`
* `/static/js/system/system.js`
* `/static/css/main.css`
* `/api/system/system`

---

## 🔹 Notes

* System data is initially rendered server-side from `system`.
* User fields are generated dynamically from the returned user objects.
* The JavaScript client updates the displayed system information using the system API.
