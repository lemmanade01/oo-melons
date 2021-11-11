"""Classes for melon orders."""
class AbstractMelonOrder: 

    @classmethod
    def mark_shipped(cls):
        """Record the fact than an order has been shipped."""

        cls.shipped = True

class GovernmentMelonOrder(AbstractMelonOrder):
    tax = 0
    passed_inspection = False


    

class DomesticMelonOrder(GovernmentMelonOrder, AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, order, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = "domestic"
        self.tax = 0.08
        self.order = order


    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        if self.species == "Christmas Melons":
            base_price = base_price* 1.5
        total = (1 + self.tax) * self.qty * base_price

        return total

    def pass_inspection(self, passed):
        passed = True
        self.pass_inspection = True

        

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, order, species, qty, country_code):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.country_code = country_code
        self.shipped = False
        self.order_type = "international"
        self.tax = 0.17
        self.order = order_number

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        if self.qty > 9:
            total = (1 + self.tax) * self.qty * base_price
        else:
            total = ((1 + self.tax) * self.qty * base_price) + 3

        return total

    def get_country_code(self):
        """Return the country code."""

        return self.country_code



    
        






