/**
 * Utility functions for common tasks
 */

/**
 * Formats a date to a readable string
 * @param date - The date to format
 * @returns The formatted date string
 */
export function formatDate(date: Date): string {
  const options: Intl.DateTimeFormatOptions = {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  };
  return date.toLocaleDateString(undefined, options);
}

/**
 * Validates an email address
 * @param email - The email address to validate
 * @returns True if the email is valid, false otherwise
 */
export function validateEmail(email: string): boolean {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

/**
 * Formats a currency value to a readable string
 * @param value - The currency value to format
 * @param currency - The currency code (e.g., 'USD')
 * @returns The formatted currency string
 */
export function formatCurrency(value: number, currency: string): string {
  return new Intl.NumberFormat(undefined, {
    style: 'currency',
    currency,
  }).format(value);
}

/**
 * Validates a phone number
 * @param phoneNumber - The phone number to validate
 * @returns True if the phone number is valid, false otherwise
 */
export function validatePhoneNumber(phoneNumber: string): boolean {
  const phoneRegex = /^\+?[1-9]\d{1,14}$/;
  return phoneRegex.test(phoneNumber);
}
