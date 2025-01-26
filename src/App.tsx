import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import VehicleList from './components/VehicleList';
import VehicleForm from './components/VehicleForm';
import BookingCalendar from './components/BookingCalendar';
import ReservationForm from './components/ReservationForm';
import CustomerProfile from './components/CustomerProfile';
import AdminDashboard from './components/AdminDashboard';

const App: React.FC = () => {
  return (
    <Router>
      <Switch>
        <Route path="/vehicles" component={VehicleList} />
        <Route path="/add-vehicle" component={VehicleForm} />
        <Route path="/edit-vehicle/:id" component={VehicleForm} />
        <Route path="/booking-calendar" component={BookingCalendar} />
        <Route path="/make-reservation" component={ReservationForm} />
        <Route path="/customer-profile/:id" component={CustomerProfile} />
        <Route path="/admin-dashboard" component={AdminDashboard} />
      </Switch>
    </Router>
  );
};

export default App;
