import sales_module

tax_for_thos_order = sales_module.calc_tax(sales_total=101.37, tax_rates=0.05)
print(f'Tax For Current order is: {tax_for_thos_order}')