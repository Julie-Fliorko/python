class BottleOfMilk:
    is_vegitarian = True

    def __init__(self, producer="none", milkFatInPercents=0, volumeInMl=0, caloriesInHundredGr=0, shugarsInHundredGr=0,
                 madeOf="none", flavor="none"):
        self.producer = producer
        self.milkFatInPercents = milkFatInPercents
        self.volumeInMl = volumeInMl
        self.caloriesInHundredGr = caloriesInHundredGr
        self.shugarsInHundredGr = shugarsInHundredGr
        self.madeOf = madeOf
        self.flavor = flavor

    def __del__(self):
        print("Milk" + self.producer + "was successfully deleted!")

    def __str__(self):
        return 'producer=' + str(self.producer) + ', milk fat in percents =' + str(
            self.milkFatInPercents) + ', volume in ml =' + str(
            self.volumeInMl) + ', calories in hundred gr =' + str(
            self.caloriesInHundredGr) + ", shugars in hundred gr =" + str(self.shugarsInHundredGr) + ', made of=' + str(
            self.madeOf) + ', flavor=' + str(self.flavor)

    @staticmethod
    def get_is_vegitarian():
        return BottleOfMilk.is_vegitarian


if __name__ == '__main__':
    nature = BottleOfMilk("Nature")
    print("/////////////////")
    print(nature)
    alpro = BottleOfMilk("Alpro", 15, 200, 150)
    print("/////////////////")
    print(alpro)
    not_your_milk = BottleOfMilk("Not your milk", 10, 200, 170, 30, "Almond", "Vanilla")
    print("/////////////////")
    print(not_your_milk)
