import React from 'react';
import { Link } from 'react-router-dom';
import '../styles/HomePage.css';

const HomePage: React.FC = () => {
  return (
    <div className="home-page">
      <div className="container">
        <div className="hero">
          <h1>Career Copilot AI</h1>
          <p>Master Your Career with AI-Powered Interview Preparation</p>
          <div className="cta-buttons">
            <Link to="/register" className="btn btn-primary">
              Get Started
            </Link>
            <Link to="/login" className="btn btn-secondary">
              Sign In
            </Link>
          </div>
        </div>

        <div className="features">
          <div className="feature-card">
            <h3>🎤 AI Interview Simulation</h3>
            <p>Practice with realistic AI-powered interviews in your field</p>
          </div>
          <div className="feature-card">
            <h3>📄 Resume Analysis</h3>
            <p>Get AI-powered feedback to improve your resume</p>
          </div>
          <div className="feature-card">
            <h3>💼 Job Matching</h3>
            <p>Find opportunities that match your profile</p>
          </div>
          <div className="feature-card">
            <h3>📊 Performance Tracking</h3>
            <p>Monitor your progress and improvement over time</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default HomePage;
