from enum import Enum
import datetime
from .entity import *

# Do not change the value of ISD_FACTOR var
ISD_FACTOR = 0.25


class TaxType(Enum):
    # Do not change this enum
    IVA = 1
    ISD = 2


class Tax:
    # Write the parameters in the next line
    def __init__(self, tax_id:str, tax_type: TaxType, percentage: float):
        # Write here your code
        self.tax_id = tax_id
        self.tax_type = tax_type
        self.percentage = percentage
        pass


class Product:
     # Write the parameters in the next line
    def __init__(self, product_id:str, name: str, expiration_date: datetime, bar_code: str, quantity: int, price: float, taxes: list[Tax]):
        # Write here your code
        self.product_id  = product_id
        self.name = name
        self.expiration_date = expiration_date
        self.bar_code = bar_code
        self.quantity = quantity
        self.price = price
        self.taxes = taxes
        pass        

    def calculate_tax(self, tax: Tax) -> float:
        # Write here your code
        base = self.quantity * self.price
        if tax.tax_type == TaxType.ISD:
            imp_isd = base * tax.percentage * ISD_FACTOR
            return imp_isd
        elif tax.tax_type == TaxType.IVA:
            imp_iva = base * tax.percentage
            return imp_iva

    def calculate_total_taxes(self) -> float:
        # Write here your code
        imp_total = 0
        for tax in self.taxes:
            imp_total += self.calculate_tax(tax)
        return imp_total

    def calculate_total(self) -> float:
        # Write here your code
        return sum(self.quantity * self.price for tax in self.taxes) + self.calculate_total_taxes()

    def __eq__(self, another):
        # Do not change this method
        return hasattr(another, 'product_id') and self.product_id == another.product_id

    def __hash__(self):
        # Do not change this method
        return hash(self.product_id)

    def print(self):
        # Do not change this method
        print(
            f"Product Id:{self.product_id} , name:{self.name}, quantity:{self.quantity}, price:{self.price}")
        for tax in self.taxes:
            print(f"Tax:{tax.tax_type} , percentage:{tax.percentage}")


class Bill:
    def __init__(self, bill_id: str, sale_date: datetime, seller: Seller, buyer: Buyer, products: list[Product]):
        # Write here your code
        self.bill_id = bill_id
        self.sale_date = sale_date
        self.seller = seller
        self.buyer = buyer
        self.products = products
        pass
       

    def calculate_total(self) -> float:
        # Write here your code
        sum = 0
        for producto in self.products:
            sum += producto.calculate_total()
        return sum

    def print(self):
        # Do not change this method
        self.buyer.print()
        self.seller.print()
        for product in self.products:
            product.print()