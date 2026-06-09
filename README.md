# Gender Detection From Names

This project uses a simple machine-learning classification model to predict gender from Andhra Pradesh names.

## Files

- `generate_dataset.py` creates `data/names_gender.csv` with Andhra Pradesh `name,gender` rows.
- `train_model.py` trains a character n-gram classifier and saves it to `models/name_gender_model.joblib`.
- `predict_gender.py` predicts gender for a single name.

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Generate the dataset:

```bash
python generate_dataset.py
```

Train the model:

```bash
python train_model.py
```

Predict gender:

```bash
python predict_gender.py Dhille
```
## output images
<img width="1920" height="1346" alt="image" src="https://github.com/user-attachments/assets/f2974385-86cf-4e2a-a908-a83c5b586a3d" />
<img width="1920" height="2662" alt="image" src="https://github.com/user-attachments/assets/9e6a983a-c487-4803-97c5-8bf2bb23428c" />
<img width="1920" height="1326" alt="image" src="https://github.com/user-attachments/assets/f35d5d2a-04fb-44f0-8b41-6baa7fdf88cb" />




## Notes

- The classifier is a baseline model trained only on names.
- Predictions are approximate and should not be treated as ground truth.
