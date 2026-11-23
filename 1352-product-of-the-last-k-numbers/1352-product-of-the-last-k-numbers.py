class ProductOfNumbers:

    def __init__(self):
        # Stores running products since the last 0; starts with 1 as a neutral base
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num == 0:
            # Reset because any future product crossing this 0 will be 0
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        # If k reaches or passes the last 0, the product must be 0
        if k >= len(self.prefix):
            return 0
        return self.prefix[-1] // self.prefix[-1 - k]