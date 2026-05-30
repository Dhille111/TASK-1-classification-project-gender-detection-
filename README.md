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
python predict_gender.py John
```

## Notes

- The classifier is a baseline model trained only on names.
- Predictions are approximate and should not be treated as ground truth.
