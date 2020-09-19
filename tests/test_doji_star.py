import pandas as pd
from price_action import main

bullish_df = pd.DataFrame({
    "time":["2020-09-01", "2020-09-02"],
    "open":[3500, 2800],
    "high":[4000, 3000],
    "low":[2500, 2600],
    "close":[3000, 2801]
}, columns=["time", "open", "high", "low", "close"])

bearish_df = pd.DataFrame({
    "time":["2020-09-01", "2020-09-02"],
    "open":[3500, 3600],
    "high":[4100, 3650],
    "low":[3400, 3550],
    "close":[4000, 3599]
}, columns=["time", "open", "high", "low", "close"])

def test_bullish_doji_star_pattern():
    df_ = main.doji(bullish_df, target="result")
    first_candle = df_["result"][0]
    second_candle = df_["result"][1]
    assert first_candle == False and second_candle == True

def test_bearish_doji_star_pattern():
    df_ = main.doji(bearish_df, target="result")
    first_candle = df_["result"][0]
    second_candle = df_["result"][1]
    assert first_candle == False and second_candle == True
