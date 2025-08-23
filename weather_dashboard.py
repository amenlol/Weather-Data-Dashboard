import os
from pathlib import Path

import pandas as pd
import matplotlib
matplotlib.use("Agg")  # For headless environments; ensures figures can be saved without a display
import matplotlib.pyplot as plt


def load_dataset(csv_path: Path) -> pd.DataFrame:
    if not csv_path.exists():
        raise FileNotFoundError(f"Dataset not found at: {csv_path}")

    df = pd.read_csv(csv_path)

    # Convert Date
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    # Basic cleaning: coerce numerics
    for col in ["Temperature", "Rainfall", "Humidity"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Drop rows with missing critical fields
    df = df.dropna(subset=["Date", "Temperature", "Rainfall", "Humidity"]).copy()

    # Sort by date for consistent plotting
    df = df.sort_values("Date").reset_index(drop=True)
    return df


def ensure_output_dir(output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)


def plot_temperature(df: pd.DataFrame, output_dir: Path) -> Path:
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(df["Date"], df["Temperature"], marker="o", color="red")
    ax.set_title("Temperature Trend Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Temperature (°C)")
    fig.autofmt_xdate()
    out_path = output_dir / "temperature_trend.png"
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    return out_path


def plot_rainfall(df: pd.DataFrame, output_dir: Path) -> Path:
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(df["Date"], df["Rainfall"], color="blue")
    ax.set_title("Daily Rainfall")
    ax.set_xlabel("Date")
    ax.set_ylabel("Rainfall (mm)")
    fig.autofmt_xdate()
    out_path = output_dir / "daily_rainfall.png"
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    return out_path


def plot_humidity(df: pd.DataFrame, output_dir: Path) -> Path:
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(df["Date"], df["Humidity"], marker="s", color="green")
    ax.set_title("Humidity Levels Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Humidity (%)")
    fig.autofmt_xdate()
    out_path = output_dir / "humidity_levels.png"
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    return out_path


def plot_dashboard(df: pd.DataFrame, output_dir: Path) -> Path:
    fig, axs = plt.subplots(3, 1, figsize=(8, 10))

    # Temperature
    axs[0].plot(df["Date"], df["Temperature"], color="red")
    axs[0].set_title("Temperature (°C)")

    # Rainfall
    axs[1].bar(df["Date"], df["Rainfall"], color="blue")
    axs[1].set_title("Rainfall (mm)")

    # Humidity
    axs[2].plot(df["Date"], df["Humidity"], color="green")
    axs[2].set_title("Humidity (%)")

    fig.autofmt_xdate()
    plt.tight_layout()
    out_path = output_dir / "dashboard.png"
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    return out_path


def main() -> None:
    repo_root = Path(__file__).resolve().parent
    csv_path = repo_root / "weather.csv"
    output_dir = repo_root / "plots"

    ensure_output_dir(output_dir)
    df = load_dataset(csv_path)

    # Show a preview in the console
    print(df.head())

    # Generate plots
    temp_path = plot_temperature(df, output_dir)
    rain_path = plot_rainfall(df, output_dir)
    humid_path = plot_humidity(df, output_dir)
    dash_path = plot_dashboard(df, output_dir)

    print("Saved plots:")
    for p in [temp_path, rain_path, humid_path, dash_path]:
        print(f" - {p}")


if __name__ == "__main__":
    main()



