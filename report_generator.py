from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image
)


def generate_report(
    resume_file,
    job_file,
    tfidf_score,
    weighted_skill_score,
    overall_match_score,
    match_level,
    required_job_skills,
    required_matches,
    preferred_job_skills,
    preferred_matches,
    matching_skills,
    missing_skills
):

    output_file = "resume_analysis_report.pdf"

    document = SimpleDocTemplate(
        output_file,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "TitleStyle",
        parent=styles["Title"],
        alignment=TA_CENTER,
        fontSize=22,
        spaceAfter=20
    )

    heading_style = ParagraphStyle(
        "HeadingStyle",
        parent=styles["Heading2"],
        fontSize=14,
        spaceBefore=15,
        spaceAfter=8
    )

    normal_style = ParagraphStyle(
        "NormalStyle",
        parent=styles["BodyText"],
        fontSize=10,
        leading=15
    )

    story = []

    story.append(
        Paragraph(
            "AI Resume & Job Match Analysis Report",
            title_style
        )
    )

    story.append(
        Paragraph(
            f"<b>Resume:</b> {resume_file}<br/>"
            f"<b>Job Description:</b> {job_file}",
            normal_style
        )
    )

    story.append(Spacer(1, 15))

    story.append(
        Paragraph(
            "Overall Analysis",
            heading_style
        )
    )

    score_data = [
        ["Metric", "Result"],
        ["TF-IDF Similarity", f"{tfidf_score:.2f}%"],
        ["Weighted Skill Score", f"{weighted_skill_score:.2f}%"],
        ["Overall Match Score", f"{overall_match_score:.2f}%"],
        ["Match Level", match_level]
    ]

    score_table = Table(
        score_data,
        colWidths=[250, 180]
    )

    score_table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1f4e78")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
            ("ALIGN", (1, 1), (1, -1), "CENTER"),
            ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ("TOPPADDING", (0, 0), (-1, -1), 8)
        ])
    )

    story.append(score_table)

    story.append(
        Paragraph(
            "Required Skills",
            heading_style
        )
    )

    required_data = [
        ["Metric", "Count"],
        ["Required Skills", str(len(required_job_skills))],
        ["Required Skills Matched", str(len(required_matches))],
        ["Required Skills Missing",
         str(len(required_job_skills) - len(required_matches))]
    ]

    required_table = Table(
        required_data,
        colWidths=[250, 180]
    )

    required_table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#548235")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
            ("ALIGN", (1, 1), (1, -1), "CENTER"),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ("TOPPADDING", (0, 0), (-1, -1), 8)
        ])
    )

    story.append(required_table)

    story.append(
        Paragraph(
            "Preferred Skills",
            heading_style
        )
    )

    preferred_data = [
        ["Metric", "Count"],
        ["Preferred Skills", str(len(preferred_job_skills))],
        ["Preferred Skills Matched", str(len(preferred_matches))],
        ["Preferred Skills Missing",
         str(len(preferred_job_skills) - len(preferred_matches))]
    ]

    preferred_table = Table(
        preferred_data,
        colWidths=[250, 180]
    )

    preferred_table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#bf9000")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
            ("ALIGN", (1, 1), (1, -1), "CENTER"),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ("TOPPADDING", (0, 0), (-1, -1), 8)
        ])
    )

    story.append(preferred_table)

    story.append(
        Paragraph(
            "Matching Skills",
            heading_style
        )
    )

    if matching_skills:
        matching_text = "<br/>".join(
            [f"✓ {skill}" for skill in matching_skills]
        )
    else:
        matching_text = "No matching skills identified."

    story.append(
        Paragraph(
            matching_text,
            normal_style
        )
    )

    story.append(
        Paragraph(
            "Missing Skills",
            heading_style
        )
    )

    if missing_skills:
        missing_text = "<br/>".join(
            [f"✗ {skill}" for skill in missing_skills]
        )
    else:
        missing_text = "No missing skills identified."

    story.append(
        Paragraph(
            missing_text,
            normal_style
        )
    )

    story.append(
        Paragraph(
            "Recommendations",
            heading_style
        )
    )

    if missing_skills:
        recommendation_text = (
            "Consider improving or adding the following skills:<br/>"
            + "<br/>".join(
                [f"• {skill}" for skill in missing_skills]
            )
        )
    else:
        recommendation_text = (
            "Your resume covers all identified job skills."
        )

    story.append(
        Paragraph(
            recommendation_text,
            normal_style
        )
    )

    chart_file = "skill_match_chart.png"

    try:
        chart = Image(chart_file)
        chart.drawHeight = 250
        chart.drawWidth = 450
        story.append(Spacer(1, 15))
        story.append(chart)
    except Exception:
        pass

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            "Note: The match score is an analytical estimate based on "
            "text similarity and the configured skill-matching rules. "
            "It should not be treated as an actual hiring decision.",
            normal_style
        )
    )

    document.build(story)

    print(
        f"\nPDF report generated successfully: {output_file}"
    )