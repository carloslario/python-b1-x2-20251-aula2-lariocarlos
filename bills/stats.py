# Write your imports here
from bills.item import Bill, Product
from bills.entity import Seller, Buyer
from typing import List, Tuple


class OrderType:
    # Do not change this enum
    ASC = 0
    DES = 1


class Statistics:
    def __init__(self, bills: list[Bill]):
        # Do not change this method
        self.bills = bills

    def find_top_sell_product(self) -> Tuple[Product, int]:
        # Write here your code
        product_count = {}
        for bill in self.bills:
            for product in bill.products:
                if product in product_count:
                    product_count[product] += product.quantity
                else:
                    product_count[product] = product.quantity

        if not product_count:
            return None, 0
        
        top_product = max(product_count, key=product_count.get)
        return top_product, product_count[top_product]

    def find_top_two_sellers(self) -> list:
        seller_totals = {}
        for bill in self.bills:
            seller = bill.seller
            total = bill.calculate_total()
            if seller in seller_totals:
                seller_totals[seller] += total
            else:
                seller_totals[seller] = total

        sorted_sellers = sorted(seller_totals.items(), key=lambda x: x[1], reverse=True)
        return [s[0] for s in sorted_sellers[:2]]

    def find_buyer_lowest_total_purchases(self) -> {Buyer, float}:
        # Write here your code
        buyer_totals = {}
        for bill in self.bills:
            buyer = bill.buyer
            total = bill.calculate_total()
            if buyer in buyer_totals:
                buyer_totals[buyer] += total
            else:
                buyer_totals[buyer] = total

        if not buyer_totals:
            return None, 0

        lowest_buyer = min(buyer_totals, key=buyer_totals.get)
        return lowest_buyer, buyer_totals[lowest_buyer]

    def order_products_by_tax(self, order_type: OrderType) -> tuple:
        # Write here your code
        product_tax_totals = {}
        for bill in self.bills:
            for product in bill.products:
                tax_total = product.calculate_total_taxes()
                if product in product_tax_totals:
                    product_tax_totals[product] += tax_total
                else:
                    product_tax_totals[product] = tax_total

        reverse = order_type == OrderType.DES
        sorted_products = sorted(product_tax_totals.items(), key=lambda x: x[1], reverse=reverse)
        return sorted_products

    def show(self):
        # Do not change this method
        print("Bills")
        for bill in self.bills:
            bill.print()
