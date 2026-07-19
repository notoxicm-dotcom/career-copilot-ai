import React, { useEffect, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { getCurrentUser, logoutUser } from '../services/api';
import '../styles/DashboardPage.css';

const DashboardPage: React.FC = () => {
  const [user, setUser] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchUser = async () => {
      try {
        const userData = await getCurrentUser();
        setUser(userData);
      } catch (error) {
        navigate('/login');
      } finally {
        setLoading(false);
      }
    };

    fetchUser();
  }, [navigate]);

  const handleLogout = async () => {
    await logoutUser();
    navigate('/');
  };

  if (loading) return <div className="dashboard-page">Loading...</div>;

  return (
    <div className="dashboard-page">
      <div className="container">
        <div className="dashboard-header">
          <h1>Welcome, {user?.full_name || user?.username}!</h1>
          <button className="btn btn-primary" onClick={handleLogout}>
            Logout
          </button>
        </div>

        <div className="dashboard-grid">
          <Link to="/interview" className="dashboard-card">
            <h3>🎤 Start Interview</h3>
            <p>Practice with AI-powered interviews</p>
          </Link>
          <Link to="/resume" className="dashboard-card">
            <h3>📄 Upload Resume</h3>
            <p>Get AI analysis and feedback</p>
          </Link>
          <div className="dashboard-card">
            <h3>💼 Browse Jobs</h3>
            <p>Find matching opportunities</p>
          </div>
          <div className="dashboard-card">
            <h3>📊 View Progress</h3>
            <p>Track your improvement</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default DashboardPage;
