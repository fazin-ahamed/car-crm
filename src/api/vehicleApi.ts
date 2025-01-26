import axios from 'axios';
import { Vehicle } from '../types';

const API_URL = '/api/vehicles';

export const fetchVehicles = async (): Promise<Vehicle[]> => {
  const response = await axios.get(API_URL);
  return response.data;
};

export const addVehicle = async (vehicle: Vehicle): Promise<Vehicle> => {
  const response = await axios.post(API_URL, vehicle);
  return response.data;
};

export const updateVehicle = async (vehicle: Vehicle): Promise<Vehicle> => {
  const response = await axios.put(`${API_URL}/${vehicle.id}`, vehicle);
  return response.data;
};

export const deleteVehicle = async (vehicleId: string): Promise<void> => {
  await axios.delete(`${API_URL}/${vehicleId}`);
};
