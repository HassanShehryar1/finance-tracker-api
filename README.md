# 💸 Finance Expense Tracker API

A complete REST API testing project built for **Software Quality Engineering (SQE) Lab**.

Built with **FastAPI (Python)** | Tested with **Postman + Newman** | CI/CD via **GitHub Actions**

---

## 📌 Tech Stack

| Layer | Tool |
|---|---|
| Backend | Python + FastAPI |
| Testing | Postman (manual) + Newman (automated) |
| CI/CD Pipeline | GitHub Actions |
| Data Storage | In-memory |

---

## 📌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | Health check |
| GET | `/expenses` | Fetch all expenses |
| POST | `/expenses` | Create new expense |
| GET | `/expenses/{id}` | Get expense by ID |
| PUT | `/expenses/{id}` | Full update of expense |
| PATCH | `/expenses/{id}` | Partial update of expense |
| DELETE | `/expenses/{id}` | Delete an expense |
| GET | `/expenses/summary` | Spending summary by category |

---

## 📌 Categories Supported

`food` | `transport` | `shopping` | `bills` | `entertainment` | `other`

---

## 📌 Test Case Summary (18 Test Cases)

| TC | Method | Description | Expected |
|---|---|---|---|
| TC01 | GET | Health check | 200 |
| TC02 | GET | Root endpoint | 200 |
| TC03 | GET | Get all expenses (empty) | 200, array |
| TC04 | POST | Create food expense | 201 |
| TC05 | POST | Create transport expense | 201 |
| TC06 | POST | Create bills expense | 201 |
| TC07 | POST | Negative amount validation | 422 |
| TC08 | POST | Missing required fields | 422 |
| TC09 | POST | Invalid category | 422 |
| TC10 | GET | Get expense by valid ID | 200 |
| TC11 | GET | Get non-existent expense | 404 |
| TC12 | PUT | Full update expense | 200 |
| TC13 | PUT | Update non-existent expense | 404 |
| TC14 | PATCH | Partial update (amount only) | 200 |
| TC15 | GET | Spending summary | 200 |
| TC16 | DELETE | Delete expense | 200 |
| TC17 | GET | Get deleted expense | 404 |
| TC18 | DELETE | Delete non-existent expense | 404 |

---

## 📌 How to Run Locally

### 1. Clone the Repo
```bash
git clone https://github.com/YOUR_USERNAME/finance-tracker-api.git
cd finance-tracker-api
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Start the API Server
```bash
uvicorn app.main:app --reload
```
API is live at: `http://localhost:8000`  
Auto docs at: `http://localhost:8000/docs`

### 4. Run Tests via Newman (CLI)
```bash
npm install -g newman
newman run tests/Finance_Tracker_API.postman_collection.json --env-var baseUrl=http://localhost:8000
```

### 5. Run via Postman (Manual)
1. Open Postman
2. Import `tests/Finance_Tracker_API.postman_collection.json`
3. Set collection variable `baseUrl` = `http://localhost:8000`
4. Run using Collection Runner

---

## 📌 CI/CD Pipeline

Every `git push` to `main` automatically:
1. Starts the FastAPI server
2. Installs Newman
3. Runs all 18 test cases
4. Generates an HTML test report (downloadable from GitHub Actions)

Check the **Actions** tab in GitHub to see live pipeline results.

---

🚀 **Built for SQE Lab — FastAPI + Postman + Newman + GitHub Actions**
