import pandas as pd
from price_action import main

df = pd.DataFrame({
    "time":["2020-09-01 00:00:00"],
    "open":[3500],
    "high":[4000],
    "low":[3000],
    "close":[3501]
}, columns=["time", "open", "high", "low", "close"])

def test_doji_pattern():
    df_ = main.doji(df, target="result")
    pattern = df_["result"][0]
    assert pattern == True