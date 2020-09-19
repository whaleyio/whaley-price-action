# Price Action Pattern

Price action is the movement of a security's price plotted over time. Price action forms the basis for all technical analysis of a stock, commodity or other asset chart. Many short-term traders rely exclusively on price action and the formations and trends extrapolated from it to make trading decisions. Technical analysis as a practice is a derivative of price action since it uses past prices in calculations that can then be used to inform trading decisions. [Investopedia](https://www.investopedia.com/terms/p/price-action.asp)

## Feature
- Doji - [Ref](https://www.investopedia.com/terms/d/doji.asp)
- Doji Star

## Testing
Test framework using Pytest:
```python
(py38) ➜ whaley-price-action git:(master) ✗ pytest
========================== test session starts ==========================
platform darwin -- Python 3.8.3, pytest-5.4.3, py-1.9.0, pluggy-0.13.1
rootdir: /Users/mragungsetiaji/Documents/fork/whaley-price-action
collected 4 items                                                       

tests/test_doji.py .                                              [ 25%]
tests/test_doji_star.py ..                                        [ 75%]
tests/test_version.py .                                           [100%]

=========================== 4 passed in 0.28s ===========================

```

