import React, { useState } from 'react';
import '../styles/InterviewPage.css';

const InterviewPage: React.FC = () => {
  const [started, setStarted] = useState(false);
  const [currentQuestion, setCurrentQuestion] = useState('');
  const [answer, setAnswer] = useState('');
  const [difficulty, setDifficulty] = useState('medium');

  const startInterview = () => {
    setStarted(true);
    // Load first question from API
    setCurrentQuestion(
      'Tell me about a challenging project you worked on and how you overcame it.'
    );
  };

  const submitAnswer = () => {
    // Send answer to backend for analysis
    console.log('Submitting answer:', answer);
    setAnswer('');
  };

  return (
    <div className="interview-page">
      <div className="container">
        {!started ? (
          <div className="interview-setup">
            <h2>AI Interview Preparation</h2>
            <div className="form-group">
              <label>Select Difficulty Level</label>
              <select
                value={difficulty}
                onChange={(e) => setDifficulty(e.target.value)}
              >
                <option value="easy">Easy</option>
                <option value="medium">Medium</option>
                <option value="hard">Hard</option>
              </select>
            </div>
            <button className="btn btn-primary" onClick={startInterview}>
              Start Interview
            </button>
          </div>
        ) : (
          <div className="interview-session">
            <div className="question-box">
              <h3>Question</h3>
              <p>{currentQuestion}</p>
            </div>
            <div className="answer-box">
              <h3>Your Answer</h3>
              <textarea
                value={answer}
                onChange={(e) => setAnswer(e.target.value)}
                placeholder="Type your answer here..."
              />
              <button className="btn btn-primary" onClick={submitAnswer}>
                Submit Answer
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default InterviewPage;
