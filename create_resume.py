from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


pdf = SimpleDocTemplate(
    "resume.pdf",
    pagesize=A4
)

styles = getSampleStyleSheet()

title_style = styles["Title"]
heading_style = styles["Heading2"]
body_style = styles["BodyText"]


content = []

content.append(
    Paragraph("Vinit Thakran", title_style)
)

content.append(
    Paragraph(
        "BCA Student | Python | Data Analytics | Machine Learning",
        body_style
    )
)

content.append(Spacer(1, 15))


content.append(
    Paragraph("Education", heading_style)
)

content.append(
    Paragraph(
        "Bachelor's in Computer Application Hons with Research — "
        "Maharshi Dayanand University | Expected Graduation: 2028",
        body_style
    )
)

content.append(Spacer(1, 10))


content.append(
    Paragraph("Technical Skills", heading_style)
)

content.append(
    Paragraph(
        "Python, C, C++, Java, HTML, SQL, Pandas, NumPy, "
        "Scikit-learn, Matplotlib, Git, GitHub, DBMS, OOPS, "
        "Data Structures and Algorithms",
        body_style
    )
)

content.append(Spacer(1, 10))


content.append(
    Paragraph("Projects", heading_style)
)

content.append(
    Paragraph(
        "Customer Churn Prediction & Business Analytics System — "
        "Built a Random Forest machine learning system for customer "
        "churn prediction, risk scoring and business analytics.",
        body_style
    )
)

content.append(Spacer(1, 6))

content.append(
    Paragraph(
        "Fraud & Anomaly Detection System — Developed a machine "
        "learning-based fraud detection system using Isolation Forest.",
        body_style
    )
)

content.append(Spacer(1, 6))

content.append(
    Paragraph(
        "Financial Transaction Analytics System — Built a Python, "
        "Pandas and SQLite-based financial analytics system.",
        body_style
    )
)

content.append(Spacer(1, 10))


content.append(
    Paragraph("Internship", heading_style)
)

content.append(
    Paragraph(
        "ESS Institute — Web & Graphic Designer Intern | June–July 2026. "
        "Worked with Canva, HTML, Photoshop and WordPress.",
        body_style
    )
)

content.append(Spacer(1, 10))


content.append(
    Paragraph("Languages", heading_style)
)

content.append(
    Paragraph(
        "English, German (Basic), Spanish (Basic)",
        body_style
    )
)


pdf.build(content)

print("Sample resume PDF created successfully!")
print("Output file: resume.pdf")