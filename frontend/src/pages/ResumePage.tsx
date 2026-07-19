import React, { useState } from 'react';
import { uploadResume, analyzeResume } from '../services/api';
import '../styles/ResumePage.css';

const ResumePage: React.FC = () => {
  const [file, setFile] = useState<File | null>(null);
  const [loading, setLoading] = useState(false);
  const [analysis, setAnalysis] = useState<any>(null);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files) {
      setFile(e.target.files[0]);
    }
  };

  const handleUpload = async () => {
    if (!file) return;
    setLoading(true);

    try {
      const formData = new FormData();
      formData.append('file', file);
      const response = await uploadResume(formData);
      setAnalysis(response);
    } catch (error) {
      console.error('Upload failed:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="resume-page">
      <div className="container">
        <h2>Resume Analysis</h2>
        <div className="upload-section">
          <input
            type="file"
            accept=".pdf,.doc,.docx"
            onChange={handleFileChange}
          />
          <button
            className="btn btn-primary"
            onClick={handleUpload}
            disabled={!file || loading}
          >
            {loading ? 'Analyzing...' : 'Upload & Analyze'}
          </button>
        </div>

        {analysis && (
          <div className="analysis-result">
            <h3>Analysis Result</h3>
            <div className="score">
              <span>Score: {analysis.score}/100</span>
            </div>
            <div className="feedback">
              <h4>Feedback</h4>
              <p>{analysis.feedback}</p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default ResumePage;
