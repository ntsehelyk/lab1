class TravelVoucher:
    my_str = "static field"

    def __init__(self, country=None, durationInDays=None, priceInEuro=None, persons=None, period=None, flightDate=None):
        self.country = country
        self.durationInDays = durationInDays
        self.priceInEuro = priceInEuro
        self.persons = persons
        self.period = period
        self.flightDate = flightDate

    def __del__(self):
        return

    def __str__(self):
        return " Country: {} \n durationInDays: {} \n priceInEuro: {} \n persons: {} \n period: {} \n flightDate: {}" \
            .format(self.country, self.durationInDays, self.priceInEuro, self.persons, self.period, self.flightDate,
                    TravelVoucher.my_str)

    @staticmethod
    def get_str():
        return TravelVoucher.my_str

    @classmethod
    def main(cls):
        first_travelvoucher = TravelVoucher("Italy", 6, 600, 4, "05.08-10.08", "05.08")
        second_travelvoucher = TravelVoucher("France", 5, 500, 3)
        third_travelvoucher = TravelVoucher()

        print("----------------------------")
        print(first_travelvoucher)
        print("----------------------------")
        print(second_travelvoucher)
        print("----------------------------")
        print(third_travelvoucher)
        print("----------------------------")