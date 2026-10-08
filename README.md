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



\- Python

\- Pandas

\- Scikit-learn

\- Matplotlib

\- PyPDF



\## How It Works



1\. The system extracts text from the resume PDF.

2\. The job description is loaded from job\_description.txt.

3\. TF-IDF and cosine similarity are used to calculate text similarity.

4\. The system checks for relevant technical and soft skills.

5\. Matching and missing skills are identified.

6\. Recommendations are generated.

7\. A skill-match visualization is created.



\## Project Structure



```text

AI-Resume-Job-Match-Analyzer/

│

├── resume\_analyzer.py

├── create\_resume.py

├── resume.pdf

├── job\_description.txt

├── requirements.txt

├── .gitignore

├── README.md

└── skill\_match\_chart.png

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

