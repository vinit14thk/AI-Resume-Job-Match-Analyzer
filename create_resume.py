from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet

pdf = SimpleDocTemplate(
    "sample_resume.pdf",
    pagesize=A4
)

styles = getSampleStyleSheet()
content = []

content.append(
    Paragraph("Alex Morgan", styles["Title"])
)
content.append(
    Paragraph(
        "Sample Data Analyst Resume | Fictional Example",
        styles["BodyText"]
    )
)
content.append(Spacer(1, 15))

content.append(Paragraph("Professional Summary", styles["Heading2"]))
content.append(
    Paragraph(
        "Entry-level data analyst with foundational knowledge "
        "of Python, SQL, statistics and business analytics.",
        styles["BodyText"]
    )
)
content.append(Spacer(1, 10))

content.append(Paragraph("Education", styles["Heading2"]))
content.append(
    Paragraph(
        "Bachelor's Degree in Computer Applications "
        " | Sample University | Expected Graduation: 2027",
        styles["BodyText"]
    )
)
content.append(Spacer(1, 10))

content.append(Paragraph("Technical Skills", styles["Heading2"]))
content.append(
    Paragraph(
        "Python, SQL, Pandas, NumPy, Data Analysis, Statistics, "
        "Data Visualization, Matplotlib, Machine Learning, "
        "Git, GitHub, Excel and Business Analytics.",
        styles["BodyText"]
    )
)
content.append(Spacer(1, 10))

content.append(Paragraph("Projects", styles["Heading2"]))
content.append(
    Paragraph(
        "Sales Data Analysis - Analyzed fictional sales data "
        "using Python and Pandas and created charts with Matplotlib.",
        styles["BodyText"]
    )
)
content.append(Spacer(1, 6))
content.append(
    Paragraph(
        "Customer Insights - Used SQL to query sample customer "
        "data and summarize business performance.",
        styles["BodyText"]
    )
)
content.append(Spacer(1, 10))

content.append(Paragraph("Core Competencies", styles["Heading2"]))
content.append(
    Paragraph(
        "Analytical Thinking, Problem-Solving, Communication, "
        "Teamwork and Attention to Detail.",
        styles["BodyText"]
    )
)

pdf.build(content)

print("Fictional sample resume PDF created successfully!")
print("Output file: sample_resume.pdf")