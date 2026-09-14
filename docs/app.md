# `GET /app`

> `Display the JarbinLocalAPI application home page.`

---

## 🔹 Description

**Displays the main JarbinLocalAPI web application page with a welcome message and links to available application and API resources.**

---

## 🔹 Page

**Path:** `/app`

**Authentication:** `None`

**Content-Type:** `text/html`

---

## 🔹 Content

* JarbinLocalAPI name and version.
* Welcome message.
* Link to the System Overview page.
* Link to the API Swagger documentation.
* Link to the API ReDoc documentation.
* Application footer containing the API name and version.

---

## 🔹 Dependencies

* `index.html`
* `/static/css/main.css`
* `title` template variable
* `version` template variable

---

## 🔹 Notes

* The page does not perform API operations directly.
* New application pages can be added to the Links section.
