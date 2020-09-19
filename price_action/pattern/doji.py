from ..candle import Candle

class Doji(Candle):
    
    def __init__(self, target=None):
        super().__init__(self.get_class_name(), 1, target=target)
    
    def logic(self, idx):
        candle = self.data.iloc[idx]

        cl = candle[self.close_column]
        op = candle[self.open_column]
        hi = candle[self.high_column]
        lo = candle[self.low_column]

        return abs(cl - op) / (hi - lo) < 0.1 and \
               (hi - max(cl, op)) > (3 * abs(cl - op)) and \
               (min(cl, op) - lo) > (3 * abs(cl - op))

