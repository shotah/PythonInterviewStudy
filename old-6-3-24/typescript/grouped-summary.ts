interface Invoice {
  customer: string;
  total: string;
}

export function summarizeInvoices(invoices: Invoice[]): void {
  const summary: Record<string, number> = {};

  invoices.forEach(({ customer, total }) => {
    const amount = parseFloat(total);
    summary[customer] = (summary[customer] || 0) + amount;
  });

  for (const customer in summary) {
    console.log(`${customer} owes $${summary[customer].toFixed(2)}`);
  }
}
