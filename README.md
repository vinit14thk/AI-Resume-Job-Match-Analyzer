\# AI Resume \& Job Match Analyzer



A Python-based resume analysis and job matching system that compares a resume with a job description using NLP and machine learning techniques.



\## Features



\- Extracts text from resume PDF files

\- Reads job descriptions from text files

\- Calculates Resume–Job similarity using TF-IDF

\- Calculates skill match percentage

\- Identifies matching skills

\- Identifies missing skills

\- Generates skill improvement recommendations

\- Creates a visual skill-match chart



\## Technologies Used



- Python
- Pandas
- Scikit-learn
- Matplotlib
- PyPDF
- ReportLab
- Regular Expressions (Regex)
- TF-IDF
- Cosine Similarity


\## How It Works


1. The system scans the project folder for available resume PDF files.
2. The user selects a resume PDF for analysis.
3. The system scans available job-description text files.
4. The selected job description is loaded and processed.
5. Resume text is extracted from the PDF using PyPDF.
6. Skills are loaded dynamically from skills.txt.
7. TF-IDF and cosine similarity are used to calculate text similarity.
8. The system identifies required and preferred skills mentioned in the job description.
9. Resume skills are matched using regular-expression-based phrase matching.
10. A weighted skill-match score is calculated.
11. An overall Resume–Job Match Score is generated.
12. Matching and missing skills are identified.
13. Skill improvement recommendations are generated.
14. A visual skill-match chart is created using Matplotlib.
15. A professional PDF analysis report is generated using ReportLab.



\## Project Structure



```text

AI-Resume-Job-Match-Analyzer/
│
├── resume_analyzer.py
├── report_generator.py
├── create_resume.py
├── resume.pdf
├── job_description.txt
├── skills.txt
├── requirements.txt
├── .gitignore
├── README.md
└── skill_match_chart.png

## Example Results

- TF-IDF Resume–Job Similarity: 34.59%
- Weighted Skill Match Score: 77.50%
- Overall Resume–Job Match Score: 64.63%
- Required Skills Matched: 7/7
- Preferred Skills Matched: 2/8
- Matching Skills: 9
- Missing Skills: 6

## Future Improvements

- Generate detailed PDF analysis reports
- Add interactive dashboard
- Build a web-based interface
- Improve skill extraction using advanced NLP models
- Support multiple resume formats
- Uses a configurable skill database through skills.txt
- Generates automated PDF analysis reports

## Generated Report

After analysis, the system automatically generates:

```text
resume_analysis_report.pdf
