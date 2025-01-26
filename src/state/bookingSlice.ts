import { createSlice, PayloadAction } from '@reduxjs/toolkit';
import { Booking } from '../types';

interface BookingState {
  bookings: Booking[];
  loading: boolean;
  error: string | null;
}

const initialState: BookingState = {
  bookings: [],
  loading: false,
  error: null,
};

const bookingSlice = createSlice({
  name: 'bookings',
  initialState,
  reducers: {
    fetchBookingsStart(state) {
      state.loading = true;
      state.error = null;
    },
    fetchBookingsSuccess(state, action: PayloadAction<Booking[]>) {
      state.bookings = action.payload;
      state.loading = false;
    },
    fetchBookingsFailure(state, action: PayloadAction<string>) {
      state.loading = false;
      state.error = action.payload;
    },
    addBookingStart(state) {
      state.loading = true;
      state.error = null;
    },
    addBookingSuccess(state, action: PayloadAction<Booking>) {
      state.bookings.push(action.payload);
      state.loading = false;
    },
    addBookingFailure(state, action: PayloadAction<string>) {
      state.loading = false;
      state.error = action.payload;
    },
    updateBookingStart(state) {
      state.loading = true;
      state.error = null;
    },
    updateBookingSuccess(state, action: PayloadAction<Booking>) {
      const index = state.bookings.findIndex(
        (booking) => booking.id === action.payload.id
      );
      if (index !== -1) {
        state.bookings[index] = action.payload;
      }
      state.loading = false;
    },
    updateBookingFailure(state, action: PayloadAction<string>) {
      state.loading = false;
      state.error = action.payload;
    },
    deleteBookingStart(state) {
      state.loading = true;
      state.error = null;
    },
    deleteBookingSuccess(state, action: PayloadAction<string>) {
      state.bookings = state.bookings.filter(
        (booking) => booking.id !== action.payload
      );
      state.loading = false;
    },
    deleteBookingFailure(state, action: PayloadAction<string>) {
      state.loading = false;
      state.error = action.payload;
    },
  },
});

export const {
  fetchBookingsStart,
  fetchBookingsSuccess,
  fetchBookingsFailure,
  addBookingStart,
  addBookingSuccess,
  addBookingFailure,
  updateBookingStart,
  updateBookingSuccess,
  updateBookingFailure,
  deleteBookingStart,
  deleteBookingSuccess,
  deleteBookingFailure,
} = bookingSlice.actions;

export default bookingSlice.reducer;
