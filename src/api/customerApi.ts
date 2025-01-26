import axios from 'axios';
import { Customer } from '../types';

const API_URL = '/api/customers';

export const fetchCustomers = async (): Promise<Customer[]> => {
  const response = await axios.get(API_URL);
  return response.data;
};

export const addCustomer = async (customer: Customer): Promise<Customer> => {
  const response = await axios.post(API_URL, customer);
  return response.data;
};

export const updateCustomer = async (customer: Customer): Promise<Customer> => {
  const response = await axios.put(`${API_URL}/${customer.id}`, customer);
  return response.data;
};

export const deleteCustomer = async (customerId: string): Promise<void> => {
  await axios.delete(`${API_URL}/${customerId}`);
};
