# Crop Recommendation API

This project provides a machine learning API for crop recommendation based on soil and weather features. It includes data exploration notebooks, model training, and a FastAPI-based prediction service.

## Link to the deployed API

The API is deployed in Render in the link: https://ml-backend-project.onrender.com/

The deployed project is the one on the following repository [AlejandroNovellino](https://github.com/AlejandroNovellino/alejandroNovellino-ml-backend-project/tree/main) this is because Render cannot have access to the projects in a Organization (or at least I couldn't connect it).

## Project Structure

- `app.py` — Streamlit app main file
- `models/` — Trained model and encoder files (`model.pkl`, `encoder.pkl`)
- `packages/` — DTOs and model wrapper classes
- `notebooks/` — Jupyter notebooks for EDA and model training
- `requirements.txt` — Python dependencies

## Setup

1. **Clone the repository:**
   ```bash
    git clone https://github.com/4GeeksAcademy/alejandroNovellino-streamlit-project.git
    cd alejandroNovellino-streamlit-project
    ```
   
2. **Install dependencies:**
    ```bash
    # for development
    pip install -r requirements-dev.txt
    # for deployment
    pip install -r requirements.txt
    ```

3. **Set up environment variables. Create a .env file in the root directory:**
    ```bash
    KAGGLEHUB_CACHE=../.
   ```

### Running the App

   ```bash
   streamlit run app.py
   ```

## Usage
Enter the required soil and weather parameters in the form. Click "Predict" to get the recommended crop.

## Notes
- The model and encoder files must be present in the **models/** directory as model.pkl and encoder.pkl.
- For development, you can use the provided Jupyter notebooks in **notebooks/** for EDA and model retraining.
