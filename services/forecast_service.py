import pandas as pd
from typing import Dict
import openai

openai.api_key = "your-openai-api-key"  # Replace with environment variable

def analyze_forecast(df: pd.DataFrame) -> Dict:
    if "Actual" not in df.columns or "Forecast" not in df.columns:
        raise ValueError("Missing required columns")

    df["Variance"] = df["Forecast"] - df["Actual"]
    average_variance = df["Variance"].mean()

    commentary = generate_gpt_commentary(df)

    return {
        "average_variance": round(average_variance, 2),
        "rows": len(df),
        "commentary": commentary
    }

def generate_gpt_commentary(df: pd.DataFrame) -> str:
    prompt = f"Analyze this forecast vs actuals:\n{df.head().to_string()}"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a financial analyst assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating commentary: {str(e)}"
