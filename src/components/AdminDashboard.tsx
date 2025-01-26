import React, { useEffect, useState } from 'react';
import { fetchAnalyticsData, fetchReportingData, fetchUserData } from '../api/adminApi';
import { AnalyticsData, ReportingData, UserData } from '../types';

const AdminDashboard: React.FC = () => {
  const [analyticsData, setAnalyticsData] = useState<AnalyticsData | null>(null);
  const [reportingData, setReportingData] = useState<ReportingData | null>(null);
  const [userData, setUserData] = useState<UserData[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [analytics, reporting, users] = await Promise.all([
          fetchAnalyticsData(),
          fetchReportingData(),
          fetchUserData(),
        ]);
        setAnalyticsData(analytics);
        setReportingData(reporting);
        setUserData(users);
      } catch (err) {
        setError('Failed to fetch admin dashboard data');
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>{error}</div>;
  }

  return (
    <div>
      <h1>Admin Dashboard</h1>
      <section>
        <h2>Analytics</h2>
        {analyticsData ? (
          <div>
            <p>Total Revenue: {analyticsData.totalRevenue}</p>
            <p>Total Bookings: {analyticsData.totalBookings}</p>
            <p>Total Customers: {analyticsData.totalCustomers}</p>
          </div>
        ) : (
          <p>No analytics data available</p>
        )}
      </section>
      <section>
        <h2>Reporting</h2>
        {reportingData ? (
          <div>
            <p>Monthly Revenue: {reportingData.monthlyRevenue}</p>
            <p>Monthly Bookings: {reportingData.monthlyBookings}</p>
            <p>Monthly Customers: {reportingData.monthlyCustomers}</p>
          </div>
        ) : (
          <p>No reporting data available</p>
        )}
      </section>
      <section>
        <h2>User Management</h2>
        {userData.length > 0 ? (
          <ul>
            {userData.map((user) => (
              <li key={user.id}>
                {user.name} - {user.email}
              </li>
            ))}
          </ul>
        ) : (
          <p>No users available</p>
        )}
      </section>
    </div>
  );
};

export default AdminDashboard;
