import { configureStore } from '@reduxjs/toolkit';
import vehicleReducer from './vehicleSlice';
import bookingReducer from './bookingSlice';
import customerReducer from './customerSlice';

const store = configureStore({
  reducer: {
    vehicles: vehicleReducer,
    bookings: bookingReducer,
    customers: customerReducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({
      serializableCheck: false,
    }),
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;

export default store;
