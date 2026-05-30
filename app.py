from __future__ import annotations

from pathlib import Path

import joblib
from flask import Flask, render_template_string, request

MODEL_PATH = Path("models/name_gender_model.joblib")

app = Flask(__name__)

PAGE = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Gender Detection</title>
    <style>
      :root{
        --bg-1:#0b1220;
        --bg-2:#091226;
        --card:#0f1724;
        --muted:#94a3b8;
        --accent-start:#38bdf8;
        --accent-end:#2563eb;
        --glass:rgba(255,255,255,0.03);
      }
      html,body{height:100%;}
      body{
        margin:0;
        font-family:Inter, system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial;
        background: radial-gradient(1200px 600px at 10% 10%, #0b1228 0%, #0f172a 30%, #071026 100%);
        display:flex;align-items:center;justify-content:center;color:#e6eef8;
      }
      .card{
        width:min(780px,92vw);
        background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(0,0,0,0.18));
        border-radius:20px;padding:36px;border:1px solid rgba(255,255,255,0.03);
        box-shadow: 0 10px 40px rgba(2,6,23,0.7);
      }
      h1{font-size:34px;margin:0 0 8px 0}
      p{color:var(--muted);margin:0 0 18px 0}
      form{display:grid;gap:14px}
      input[name="name"]{height:54px;padding:14px 18px;border-radius:12px;background:transparent;border:1px solid rgba(255,255,255,0.08);color:inherit;font-size:16px}
      input::placeholder{color:rgba(230,238,248,0.35)}
      button{height:52px;border-radius:12px;border:none;color:white;font-weight:700;font-size:16px;cursor:pointer;background:linear-gradient(90deg,var(--accent-start),var(--accent-end));box-shadow:0 8px 24px rgba(37,99,235,0.22)}
      .result{margin-top:18px;padding:14px 18px;border-radius:12px;background:rgba(10,38,56,0.6);border:1px solid rgba(255,255,255,0.03);font-weight:600}
      .result.error{background:linear-gradient(90deg, rgba(255,90,90,0.12), rgba(255,60,60,0.08));border-color:rgba(255,90,90,0.12)}
      .pill{display:inline-block;padding:10px 14px;border-radius:10px;background:linear-gradient(90deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));border:1px solid rgba(255,255,255,0.03);}
      .meta{margin-top:12px;color:var(--muted);font-size:13px}
      @media (max-width:420px){h1{font-size:24px}}
    </style>
  </head>
  <body>
    <main class="card">
      <h1>Gender Detection</h1>
      <p>Enter a name and the model will predict <strong>male</strong> or <strong>female</strong>.</p>
      <form method="post">
        <input name="name" placeholder="Type a name like Durga or Ramesh" value="{{ name or '' }}" autofocus />
        <button type="submit">Predict</button>
      </form>
      {% if result %}
        <div class="result {{ 'error' if error else '' }}">
          <span class="pill">{{ result }}</span>
        </div>
      {% endif %}
    </main>
  </body>
</html>
"""


def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Model not found at {MODEL_PATH}. Train it first with train_model.py."
        )
    return joblib.load(MODEL_PATH)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = False
    name = ""

    if request.method == "POST":
        name = (request.form.get("name") or "").strip()
        if not name:
            result = "Please enter a name."
            error = True
        else:
            model = load_model()
            prediction = model.predict([name])[0]
            result = f"{name} -> {prediction}"

    return render_template_string(
      PAGE,
      result=result,
      error=error,
      name=name,
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
