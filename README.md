# FastAPI Stock App

This is a simple FastAPI application that provides stock analysis.

## Setup

1. Create a virtual environment and activate it:

   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

2. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

3. Run the FastAPI application:

   ```sh
   uvicorn app.main:app --reload
   ```

4. Access the API:

   - Root endpoint: `http://127.0.0.1:8000`
   - Single stock analysis: `http://127.0.0.1:8000/stocks/{stock_code}`
   - All stocks analysis: `http://127.0.0.1:8000/stocks`

