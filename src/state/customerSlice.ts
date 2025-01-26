import { createSlice, PayloadAction } from '@reduxjs/toolkit';
import { Customer } from '../types';

interface CustomerState {
  customers: Customer[];
  loading: boolean;
  error: string | null;
}

const initialState: CustomerState = {
  customers: [],
  loading: false,
  error: null,
};

const customerSlice = createSlice({
  name: 'customers',
  initialState,
  reducers: {
    fetchCustomersStart(state) {
      state.loading = true;
      state.error = null;
    },
    fetchCustomersSuccess(state, action: PayloadAction<Customer[]>) {
      state.customers = action.payload;
      state.loading = false;
    },
    fetchCustomersFailure(state, action: PayloadAction<string>) {
      state.loading = false;
      state.error = action.payload;
    },
    addCustomerStart(state) {
      state.loading = true;
      state.error = null;
    },
    addCustomerSuccess(state, action: PayloadAction<Customer>) {
      state.customers.push(action.payload);
      state.loading = false;
    },
    addCustomerFailure(state, action: PayloadAction<string>) {
      state.loading = false;
      state.error = action.payload;
    },
    updateCustomerStart(state) {
      state.loading = true;
      state.error = null;
    },
    updateCustomerSuccess(state, action: PayloadAction<Customer>) {
      const index = state.customers.findIndex(
        (customer) => customer.id === action.payload.id
      );
      if (index !== -1) {
        state.customers[index] = action.payload;
      }
      state.loading = false;
    },
    updateCustomerFailure(state, action: PayloadAction<string>) {
      state.loading = false;
      state.error = action.payload;
    },
    deleteCustomerStart(state) {
      state.loading = true;
      state.error = null;
    },
    deleteCustomerSuccess(state, action: PayloadAction<string>) {
      state.customers = state.customers.filter(
        (customer) => customer.id !== action.payload
      );
      state.loading = false;
    },
    deleteCustomerFailure(state, action: PayloadAction<string>) {
      state.loading = false;
      state.error = action.payload;
    },
  },
});

export const {
  fetchCustomersStart,
  fetchCustomersSuccess,
  fetchCustomersFailure,
  addCustomerStart,
  addCustomerSuccess,
  addCustomerFailure,
  updateCustomerStart,
  updateCustomerSuccess,
  updateCustomerFailure,
  deleteCustomerStart,
  deleteCustomerSuccess,
  deleteCustomerFailure,
} = customerSlice.actions;

export default customerSlice.reducer;
