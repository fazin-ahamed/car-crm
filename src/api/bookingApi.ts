import axios from 'axios';
import { Booking } from '../types';

const API_URL = '/api/bookings';

export const fetchBookings = async (): Promise<Booking[]> => {
  const response = await axios.get(API_URL);
  return response.data;
};

export const addBooking = async (booking: Booking): Promise<Booking> => {
  const response = await axios.post(API_URL, booking);
  return response.data;
};

export const updateBooking = async (booking: Booking): Promise<Booking> => {
  const response = await axios.put(`${API_URL}/${booking.id}`, booking);
  return response.data;
};

export const deleteBooking = async (bookingId: string): Promise<void> => {
  await axios.delete(`${API_URL}/${bookingId}`);
};
