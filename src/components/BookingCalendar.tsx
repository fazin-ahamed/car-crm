import React, { useEffect, useState } from 'react';
import { fetchBookings } from '../api/bookingApi';
import { Booking } from '../types';

const BookingCalendar: React.FC = () => {
  const [bookings, setBookings] = useState<Booking[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const getBookings = async () => {
      try {
        const data = await fetchBookings();
        setBookings(data);
      } catch (err) {
        setError('Failed to fetch bookings');
      } finally {
        setLoading(false);
      }
    };

    getBookings();
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>{error}</div>;
  }

  return (
    <div>
      <h1>Booking Calendar</h1>
      <ul>
        {bookings.map((booking) => (
          <li key={booking.id}>
            {booking.vehicle.make} {booking.vehicle.model} - {booking.startDate} to {booking.endDate}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default BookingCalendar;
