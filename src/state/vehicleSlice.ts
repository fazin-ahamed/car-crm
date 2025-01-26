import { createSlice, PayloadAction } from '@reduxjs/toolkit';
import { Vehicle } from '../types';

interface VehicleState {
  vehicles: Vehicle[];
  loading: boolean;
  error: string | null;
}

const initialState: VehicleState = {
  vehicles: [],
  loading: false,
  error: null,
};

const vehicleSlice = createSlice({
  name: 'vehicles',
  initialState,
  reducers: {
    fetchVehiclesStart(state) {
      state.loading = true;
      state.error = null;
    },
    fetchVehiclesSuccess(state, action: PayloadAction<Vehicle[]>) {
      state.loading = false;
      state.vehicles = action.payload;
    },
    fetchVehiclesFailure(state, action: PayloadAction<string>) {
      state.loading = false;
      state.error = action.payload;
    },
    addVehicleStart(state) {
      state.loading = true;
      state.error = null;
    },
    addVehicleSuccess(state, action: PayloadAction<Vehicle>) {
      state.loading = false;
      state.vehicles.push(action.payload);
    },
    addVehicleFailure(state, action: PayloadAction<string>) {
      state.loading = false;
      state.error = action.payload;
    },
    updateVehicleStart(state) {
      state.loading = true;
      state.error = null;
    },
    updateVehicleSuccess(state, action: PayloadAction<Vehicle>) {
      state.loading = false;
      const index = state.vehicles.findIndex(
        (vehicle) => vehicle.id === action.payload.id
      );
      if (index !== -1) {
        state.vehicles[index] = action.payload;
      }
    },
    updateVehicleFailure(state, action: PayloadAction<string>) {
      state.loading = false;
      state.error = action.payload;
    },
    deleteVehicleStart(state) {
      state.loading = true;
      state.error = null;
    },
    deleteVehicleSuccess(state, action: PayloadAction<string>) {
      state.loading = false;
      state.vehicles = state.vehicles.filter(
        (vehicle) => vehicle.id !== action.payload
      );
    },
    deleteVehicleFailure(state, action: PayloadAction<string>) {
      state.loading = false;
      state.error = action.payload;
    },
  },
});

export const {
  fetchVehiclesStart,
  fetchVehiclesSuccess,
  fetchVehiclesFailure,
  addVehicleStart,
  addVehicleSuccess,
  addVehicleFailure,
  updateVehicleStart,
  updateVehicleSuccess,
  updateVehicleFailure,
  deleteVehicleStart,
  deleteVehicleSuccess,
  deleteVehicleFailure,
} = vehicleSlice.actions;

export default vehicleSlice.reducer;
