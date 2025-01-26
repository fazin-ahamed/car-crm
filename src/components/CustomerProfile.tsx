import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { getCustomerById } from '../api/customerApi';
import { Customer } from '../types';

const CustomerProfile: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const [customer, setCustomer] = useState<Customer | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchCustomer = async () => {
      try {
        const data = await getCustomerById(id);
        setCustomer(data);
      } catch (err) {
        setError('Failed to fetch customer data');
      } finally {
        setLoading(false);
      }
    };

    fetchCustomer();
  }, [id]);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>{error}</div>;
  }

  if (!customer) {
    return <div>No customer data available</div>;
  }

  return (
    <div>
      <h1>Customer Profile</h1>
      <p>Name: {customer.name}</p>
      <p>Email: {customer.email}</p>
      <p>Phone: {customer.phone}</p>
      <p>Address: {customer.address}</p>
      {/* Add more customer details as needed */}
    </div>
  );
};

export default CustomerProfile;
