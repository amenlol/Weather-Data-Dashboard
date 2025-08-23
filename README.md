## Weather Data Dashboard

Simple weather dashboard that loads a CSV dataset, cleans it, and generates multiple visualizations (temperature trend, rainfall, humidity, and a combined dashboard).

### Dataset
The project includes a sample dataset at `weather.csv`:

```csv
Date,Temperature,Rainfall,Humidity
2023-01-01,22,0.0,65
2023-01-02,24,0.0,60
2023-01-03,19,5.2,72
2023-01-04,21,0.0,68
2023-01-05,23,1.5,70
2023-01-06,20,3.0,75
2023-01-07,18,10.2,80
```

You can replace this with any real dataset (e.g., Kaggle) as long as it has the same columns: `Date`, `Temperature`, `Rainfall`, `Humidity`.

### Setup
1. Create and activate a virtual environment (optional but recommended):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage
Run the dashboard script; it will read `weather.csv`, clean the data, and save plots under `plots/`.

```bash
python weather_dashboard.py
```

Generated files:
- `plots/temperature_trend.png`
- `plots/daily_rainfall.png`
- `plots/humidity_levels.png`
- `plots/dashboard.png`

### Notes
- The script uses a non-interactive Matplotlib backend, so it saves figures instead of opening GUI windows.
- Dates are parsed using `pandas.to_datetime`, and numeric columns are coerced to numeric.

### Connect with Me
- **GitHub:** [@amenlol](https://github.com/amenlol)
- **Portfolio:** [ameneb.netlify.app](https://ameneb.netlify.app)
- **Email:** ebisagetachew18@gmail.com

