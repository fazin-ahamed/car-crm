import React, { useState } from 'react';
import { Reservation } from '../types';
import { addReservation, updateReservation } from '../api/bookingApi';

interface ReservationFormProps {
  reservation?: Reservation;
  onSuccess: () => void;
}

const ReservationForm: React.FC<ReservationFormProps> = ({ reservation, onSuccess }) => {
  const [formData, setFormData] = useState<Reservation>({
    id: reservation?.id || '',
    vehicleId: reservation?.vehicleId || '',
    userId: reservation?.userId || '',
    startDate: reservation?.startDate || '',
    endDate: reservation?.endDate || '',
    status: reservation?.status || '',
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
      if (reservation) {
        await updateReservation(formData);
      } else {
        await addReservation(formData);
      }
      onSuccess();
    } catch (err) {
      setError('Failed to save reservation');
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="vehicleId">Vehicle ID</label>
        <input
          type="text"
          id="vehicleId"
          name="vehicleId"
          value={formData.vehicleId}
          onChange={handleChange}
          required
        />
      </div>
      <div>
        <label htmlFor="userId">User ID</label>
        <input
          type="text"
          id="userId"
          name="userId"
          value={formData.userId}
          onChange={handleChange}
          required
        />
      </div>
      <div>
        <label htmlFor="startDate">Start Date</label>
        <input
          type="datetime-local"
          id="startDate"
          name="startDate"
          value={formData.startDate}
          onChange={handleChange}
          required
        />
      </div>
      <div>
        <label htmlFor="endDate">End Date</label>
        <input
          type="datetime-local"
          id="endDate"
          name="endDate"
          value={formData.endDate}
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

export default ReservationForm;
