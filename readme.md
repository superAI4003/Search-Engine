## Prerequisites

- Node.js and npm (for the frontend)
- Python 3.7+ and pip (for the backend) 

## Frontend Setup

1. **Navigate to the frontend directory:**

   ```bash
   cd frontend
   ```

2. **Install dependencies:**

   ```bash
   npm install
   ```

3. **Create a `.env` file:**

   Create a `.env` file in the `frontend` directory with the following content:

   ```plaintext
   VITE_BACKEND_URL = http://127.0.0.1:8001
   ```

   Adjust the `VITE_BACKEND_URL` to point to your backend API.

4. **Run the frontend:**

   ```bash
   npm run dev
   ```

   The application will be available at `http://localhost:3000`.

## Backend Setup

1. **Navigate to the backend directory:**

   ```bash
   cd backend
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file:**

   Create a `.env` file in the `backend` directory with the following content:

   ```plaintext
    GOOGLE_API_KEY= 
    GOOGLE_CX=7 
    OPENROUTER_API_KEY=  

    DB_USER=postgres
    DB_PASSWORD=1005
    DB_HOST=localhost
    DB_NAME=mydb_search
   ```
 

5. **Run the backend:**

   ```bash
   uvicorn main:app --reload
   ```

   The API will be available at `http://localhost:8000`.

 