from helper import Field

COUNTRIES = ('US', 'CN', 'JP', 'DE', 'ES', 'FR', 'NL')


class CountryPricer:

    DISCOUNT = 0.8
    country = Field(type_="str", default=COUNTRIES[0])

    def get_discounted_price(self, price, country):
        if country == self.country.value:
            return price * self.DISCOUNT
        else:
            return price
