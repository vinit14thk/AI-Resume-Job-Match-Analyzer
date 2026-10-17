AI Resume & Job Match Analyzer

A Python-based application that helps users evaluate how closely their resumes align with a job description. It uses rule-based skill matching and text-overlap analysis to calculate estimated match scores, identify missing skills, prioritize skill gaps, and generate improvement recommendations.

The application features an interactive Streamlit dashboard with visual score cards, skill analysis, and PDF report generation.

Live Demo: "Try the application" (https://ai-resume-job-match-analyzer-bykdp9a2vxmmkpnhu9ymnt.streamlit.app/)

GitHub Repository: "View the source code" (https://github.com/vinit14thk/AI-Resume-Job-Match-Analyzer)

«Note: Match scores are estimates based on rule-based analysis. They are not predictions of hiring outcomes.»

Features

- Interactive Web Dashboard: Analyze resumes through a Streamlit interface.
- Resume PDF Upload: Upload a resume PDF for analysis.
- Job Description Input: Enter or paste a job description for comparison.
- Skill Matching: Identify skills that match the job requirements using rule-based matching.
- Match Score: Calculate a weighted skill-match score and text-overlap similarity.
- Skill Gap Analysis: Identify missing skills and prioritize areas for improvement.
- Improvement Recommendations: Generate suggestions based on identified skill gaps.
- Visual Results: Display styled score cards and a skill-match chart.
- PDF Report Generation: Generate a downloadable report summarizing the analysis.
- Automated Testing: Include tests to help verify analyzer functionality.
- Sample Files: Test the application using sample resume and job-description files.
- Transparent Scoring: Explain that scores are estimates, not predictions of hiring outcomes.

Technologies Used

- Python — Core programming language
- Streamlit — Interactive web application and dashboard
- Matplotlib — Data visualization and charts
- Pandas — Data handling in the supporting analyzer scripts
- Regular Expressions — Skill matching and text processing
- Git and GitHub — Version control and project hosting
- Streamlit Community Cloud — Web app deployment

Installation & Setup

1. Clone the repository

git clone https://github.com/vinit14thk/AI-Resume-Job-Match-Analyzer.git
cd AI-Resume-Job-Match-Analyzer

2. Install dependencies

python -m pip install -r requirements.txt

3. Run the dashboard

python -m streamlit run app.py

Open the local URL displayed in your terminal to use the application.

System Architecture

User
  |
  v
Streamlit Dashboard (app.py)
  |
  v
Upload Resume + Enter Job Description
  |
  v
Resume Text Extraction and Preprocessing
  |
  v
Skill Matching (skill_matcher.py)
  |
  v
Score Calculation and Skill Gap Analysis
  |
  v
Interactive Results Dashboard
  |
  v
PDF Analysis Report and Visual Chart

How It Works

1. The user opens the Streamlit dashboard.
2. The user uploads a resume PDF.
3. The user enters or pastes a job description.
4. The application extracts and preprocesses the resume text.
5. The skill-matching module identifies matching and missing skills.
6. The application calculates a weighted skill-match score and text-overlap similarity.
7. The dashboard displays score cards, matching skills, missing skills, and skill-gap priorities.
8. The application provides recommendations to help improve the resume's alignment with the job description.
9. The user can generate a PDF analysis report and view the skill-match chart.

Scoring note: The scores are estimates based on rule-based skill matching and text overlap. They are not predictions of hiring outcomes.

Project Structure

AI-Resume-Job-Match-Analyzer/
├── app.py
├── skill_matcher.py
├── report_generator.py
├── resume_analyzer.py
├── resume_analyzer_backup.py
├── create_resume.py
├── test_resume_analyzer.py
├── skills.txt
├── job_description.txt
├── requirements.txt
├── sample_resume.pdf
├── sample_resume.txt
├── screenshots/
│   └── dashboard.jpeg
├── .gitignore
└── README.md

The ".venv" folder contains the local Python environment and should generally not be committed to GitHub.

The dashboard uses "app.py" as its entry point. Supporting modules handle skill matching, report generation, and other project functionality.

Analysis reports and charts may be generated when the application or analyzer runs.

Example Results

The application produces a resume–job description comparison with several evaluation metrics.

Metric| Example Result
Text-overlap similarity| 51.72%
Weighted skill-match score| 77.50%
Overall Resume–Job Match Score| 69.77%
Match level| Good Match
Required skills matched| 7/7
Preferred skills matched| 2/8
Matching skills identified| 9
Missing skills identified| 6

The application also provides a skill-match chart, skill-gap priorities, improvement recommendations, and a PDF analysis report.

Note: These example figures come from the sample data used in a previous successful run. Results vary depending on the resume and job description. Scores are estimates and do not predict hiring outcomes.

Scoring Method

Scoring Method

The application calculates the overall Resume–Job Match Score using two components.

1. Weighted Skill Match — 70%

The skill-match score combines required and preferred skills:

- Required skills contribute 70% of the skill score.
- Preferred skills contribute 30% of the skill score.

2. Text-overlap Similarity — 30%

The application compares relevant words in the resume and job description after removing selected common words.

Text-overlap formula:

Text Overlap Similarity = (Shared Relevant Words / Job Description Words) × 100

3. Final Score

Overall Match Score = (Weighted Skill Score × 0.70) + (Text-overlap Similarity × 0.30)

This is a rule-based scoring approach using skill matching and word overlap. It does not use TF-IDF or cosine similarity and has not been validated as a measure of hiring suitability.

The scores are intended to help users identify relevant skills and improve how their resumes align with a job description. They are estimates, not predictions of hiring outcomes

Generated Outputs

The application provides the following outputs after resume analysis:

- Interactive dashboard: Displays score cards, matching skills, missing skills, and skill-gap priorities.
- PDF analysis report ("resume_analysis_report.pdf"): Summarizes the analysis results, match level, and skill improvement recommendations.
- Skill-match chart ("skill_match_chart.png"): Visualizes skill-matching results.

The PDF report and chart are generated by the application when the relevant analysis or report-generation steps are completed. Actual output files depend on the application's implementation and successful execution.

Sample Files

The repository includes sample files to help users test the application.

- "sample_resume.pdf" — Sample resume for testing resume analysis.
- "sample_resume.txt" — Text-based sample resume.
- "job_description.txt" — Example job description used for comparison.

These files allow users to explore the application's features without uploading their own personal resume.

Privacy note: Use fictional or anonymized information in sample files. Avoid publishing personal information or resumes without permission.

Run the Analyzer

1. Install the dependencies listed in "requirements.txt".

2. Start the dashboard:
   
   python -m streamlit run app.py

3. Open the local URL displayed in the terminal.

4. Upload a resume PDF.

5. Enter or paste the job description.

6. Run the analysis and review the match scores, matching skills, missing skills, and recommendations.

7. Generate the PDF report and view the skill-match chart, if available.

Tip: Use "sample_resume.pdf" and "job_description.txt" to test the application without using personal documents.

Privacy note: Use fictional or anonymized resumes when sharing test data publicly. Do not upload personal resumes without permission.

Future Improvements

Potential improvements for future versions include:

- Advanced NLP: Improve skill extraction and contextual understanding of job descriptions.
- DOCX Support: Allow users to upload Word resumes as well as PDFs.
- Enhanced Similarity Analysis: Explore TF-IDF and cosine similarity as additional comparison methods.
- Expanded Skill Database: Add more technical skills, job roles, and industry-specific keywords.
- Automated Testing: Expand test coverage for different resume formats and edge cases.
- Input Validation: Improve error handling for invalid files and incomplete job descriptions.
- Report Customization: Add more flexible PDF report layouts and analysis options.

Author

GitHub: "vinit14thk" (https://github.com/vinit14thk)

## Dashboard Preview

![AI Resume & Job Match Analyzer Dashboard](screenshots/dashboard.jpeg)

