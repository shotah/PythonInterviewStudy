import Big from "big.js";

interface LineItem {
  name: string;
  qty: number;
  price: string; // decimal string
}

export function generateInvoice(items: LineItem[], taxRate: number, discount: number): void {
  const subtotal = items.reduce((sum, item) => {
    return sum.plus(new Big(item.price).times(item.qty));
  }, new Big(0));

  const tax = subtotal.times(taxRate);
  const total = subtotal.plus(tax).minus(discount);

  console.log("Subtotal: $" + subtotal.toFixed(2));
  console.log("Tax: $" + tax.toFixed(2));
  console.log("Discount: -$" + discount.toFixed(2));
  console.log("Total: $" + total.toFixed(2));
}
