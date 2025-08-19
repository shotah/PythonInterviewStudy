interface FormData {
  name: string;
  email: string;
  age?: number;
}

function isValidEmail(email: string): boolean {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

export function validateForm(data: FormData): string[] {
  const errors: string[] = [];

  if (!data.name) errors.push("Name is required.");
  if (!data.email || !isValidEmail(data.email)) errors.push("Valid email is required.");
  if (data.age !== undefined && data.age < 18) errors.push("Age must be at least 18.");

  return errors;
}
