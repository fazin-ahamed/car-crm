export interface Vehicle {
  id: string;
  type: string;
  registrationNumber: string;
  status: string;
  availability: boolean;
}

export interface Booking {
  id: string;
  vehicleId: string;
  userId: string;
  startDate: string;
  endDate: string;
  status: string;
}

export interface Customer {
  id: string;
  name: string;
  email: string;
  phone: string;
  address: string;
}
