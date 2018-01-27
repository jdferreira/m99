
class Number:

    def __init__(self):
        self.value = [1]

    def get_value(self):
        return int(''.join(str(i) for i in self.value))

    def incr(self):
        idx = len(self.value) - 1
        while idx >= 0:
            if self.value[idx] == 1:
                self.value[idx] = 2
                break
            idx -= 1
        if idx == -1:
            self.value = [1] + [1] * len(self.value)

    def is_multiple_of_99(self):
        return self.is_multiple_of_9() and self.is_multiple_of_11()

    def is_multiple_of_9(self):
        return sum(self.value) % 9 == 0

    def is_multiple_of_11(self):
        sum = 0
        for idx, v in enumerate(self.value):
            if idx % 2 == 0:
                sum += v
            else:
                sum -= v
        return sum % 11 == 0

if __name__ == '__main__':
    n = Number()
    while not n.is_multiple_of_99():
        n.incr()
    n = n.get_value()

    print(f'answer = {n} = 99 * {n//99}')
