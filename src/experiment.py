from src.coin import Coin


class Experiment:

    # def p_2_heads(self, n):   

    #     c = Coin()
    #     l = []
    #     for i in range(n):
    #         for k in range(2):                
    #          l.append(c.flip())
    #     return l.count('H')/n

    # def __eq__(self, other):
    #     c = Coin()
    #     return self.coin == other.c


    def p_pattern(self, pat):

        l = len(pat)
        c = Coin()
        successes = []
        trials = 100_000_0
        for _ in range(trials):
            is_success = ''.join([c.flip() for _ in range(l)]) == pat
            successes.append(is_success)
        return sum(successes) / trials


        


# class Experiment:
#     def p_2_heads(self):
#         c = Coin()
#         successes = []
#         trials = 100_000
#         for _ in range(trials):
#             is_success = [c.flip() for _ in range(2)].count('H') == 2
#             successes.append(is_success)
#         return sum(successes) / trials