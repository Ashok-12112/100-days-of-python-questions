class Number:
    def number(self, total, i, n):
        if i > n:
            print(total)
            return

        self.number(total + i, i + 1, n)

obj = Number()
obj.number(0, 1, 10)