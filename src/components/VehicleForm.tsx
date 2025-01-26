import React, { useState } from 'react';
import { Vehicle } from '../types';
import { addVehicle, updateVehicle } from '../api/vehicleApi';

interface VehicleFormProps {
  vehicle?: Vehicle;
  onSuccess: () => void;
}

const VehicleForm: React.FC<VehicleFormProps> = ({ vehicle, onSuccess }) => {
  const [formData, setFormData] = useState<Vehicle>({
    id: vehicle?.id || '',
    make: vehicle?.make || '',
    model: vehicle?.model || '',
    year: vehicle?.year || '',
    status: vehicle?.status || '',
  });

  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      if (vehicle) {
        await updateVehicle(formData);
      } else {
        await addVehicle(formData);
      }
      onSuccess();
    } catch (err) {
      setError('Failed to save vehicle');
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="make">Make</label>
        <input
          type="text"
          id="make"
          name="make"
          value={formData.make}
          onChange={handleChange}
          required
        />
      </div>
      <div>
        <label htmlFor="model">Model</label>
        <input
          type="text"
          id="model"
          name="model"
          value={formData.model}
          onChange={handleChange}
          required
        />
      </div>
      <div>
        <label htmlFor="year">Year</label>
        <input
          type="number"
          id="year"
          name="year"
          value={formData.year}
          onChange={handleChange}
          required
        />
      </div>
      <div>
        <label htmlFor="status">Status</label>
        <input
          type="text"
          id="status"
          name="status"
          value={formData.status}
          onChange={handleChange}
          required
        />
      </div>
      {error && <div>{error}</div>}
      <button type="submit" disabled={loading}>
        {loading ? 'Saving...' : 'Save'}
      </button>
    </form>
  );
};

export default VehicleForm;
