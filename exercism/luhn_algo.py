### Exercise - 20 - Luhn Algo! - Great!

class Luhn:
    def __init__(self, card_num):
        self.cardy = card_num

    def valid(self):
        card_split = self.cardy.split()
        card_no1 = ''.join(card_split)
        if len(card_no1) <= 1:
            return False
        for i in card_no1:
            if i.isdigit() == False:
                return False
        card_no2 = [int(card_no1[i]) for i in range(len(card_no1))]
        card_no2.reverse()
        card_no2 = [card_no2[i] * 2 if i % 2 != 0 else card_no2[i]
                    for i in range(len(card_no2))]
        card_no2.reverse()
        card_no2 = [card_no2[i] - 9 if card_no2[i] > 9 else card_no2[i]
                    for i in range(len(card_no2))]
        sum_digs = 0
        for i in card_no2:
            sum_digs += i
        if sum_digs % 10 == 0:
            return True
        else:
            return False