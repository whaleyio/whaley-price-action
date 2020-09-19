from ..candle import Candle

class DojiStar(Candle):

    def __init__(self, target=None):
        super().__init__(self.get_class_name(), 2, target=target)

    def get_price(self, candle):
        cl = candle[self.close_column]
        op = candle[self.open_column]
        hi = candle[self.high_column]
        lo = candle[self.low_column]

        return op, cl, hi, lo

    def logic(self, idx):
        candle = self.data.iloc[idx]
        prev_candle = self.data.iloc[idx + 1 * self.multi_coeff]

        op, cl, hi, lo = self.get_price(candle)
        prev_op, prev_cl, prev_hi, prev_lo = self.get_price(prev_candle)

        return prev_cl > prev_op and \
               abs(prev_cl - prev_op) / (prev_hi - prev_lo) >= 0.7 and \
               abs(cl - op) / (hi - lo) < 0.1 and \
               prev_cl < cl and \
               prev_cl < op and \
               (hi - max(cl, op)) > (3 * abs(cl - op)) and \
               (min(cl, op) - lo) > (3 * abs(cl - op))
