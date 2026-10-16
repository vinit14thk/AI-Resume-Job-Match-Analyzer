from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image,
    KeepTogether,
)


NAVY = colors.HexColor("#16324F")
BLUE = colors.HexColor("#2563EB")
LIGHT_BLUE = colors.HexColor("#EAF2FF")
GREEN = colors.HexColor("#15803D")
LIGHT_GREEN = colors.HexColor("#EAF7EE")
AMBER = colors.HexColor("#B45309")
LIGHT_GREY = colors.HexColor("#F3F6FA")
DARK_GREY = colors.HexColor("#475569")
WHITE = colors.white


def generate_report(
    resume_file,
    job_file,
    tfidf_score,
    weighted_skill_score,
    overall_match_score,
    skill_component,
    similarity_component,
    match_level,
    job_recommendation,
    required_job_skills,
    required_matches,
    preferred_job_skills,
    preferred_matches,
    matching_skills,
    missing_skills,
    skill_gap_priority
):
    output_file = "resume_analysis_report.pdf"

    document = SimpleDocTemplate(
        output_file,
        pagesize=A4,
        rightMargin=18 * mm,
        leftMargin=18 * mm,
        topMargin=18 * mm,
        bottomMargin=18 * mm,
        title="AI Resume and Job Match Analysis",
        author="AI Resume & Job Match Analyzer",
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "ReportTitle",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=21,
        leading=26,
        textColor=NAVY,
        alignment=TA_CENTER,
        spaceAfter=6,
    )

    subtitle_style = ParagraphStyle(
        "Subtitle",
        parent=styles["Normal"],
        fontSize=9,
        leading=13,
        textColor=DARK_GREY,
        alignment=TA_CENTER,
        spaceAfter=18,
    )

    heading_style = ParagraphStyle(
        "SectionHeading",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=13,
        leading=17,
        textColor=NAVY,
        spaceBefore=13,
        spaceAfter=7,
        keepWithNext=True,
    )

    body_style = ParagraphStyle(
        "ReportBody",
        parent=styles["BodyText"],
        fontSize=9,
        leading=13,
        textColor=DARK_GREY,
        spaceAfter=4,
        wordWrap="CJK",
    )

    small_style = ParagraphStyle(
        "SmallNote",
        parent=body_style,
        fontSize=8,
        leading=11,
        textColor=DARK_GREY,
    )

    score_style = ParagraphStyle(
        "MainScore",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=29,
        leading=34,
        alignment=TA_CENTER,
        textColor=BLUE,
    )

    score_label_style = ParagraphStyle(
        "ScoreLabel",
        parent=body_style,
        fontName="Helvetica-Bold",
        fontSize=10,
        leading=14,
        alignment=TA_CENTER,
        textColor=NAVY,
    )

    story = []

    story.append(Paragraph(
        "AI RESUME &amp; JOB MATCH ANALYZER",
        title_style,
    ))

    story.append(Paragraph(
        "RESUME ANALYSIS REPORT",
        subtitle_style,
    ))

    details = [
        [
            Paragraph("<b>Resume</b>", body_style),
            Paragraph(escape(str(resume_file)), body_style),
        ],
        [
            Paragraph("<b>Job description</b>", body_style),
            Paragraph(escape(str(job_file)), body_style),
        ],
    ]

    details_table = Table(
        details,
        colWidths=[37 * mm, 133 * mm],
    )

    details_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), LIGHT_GREY),
        ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#D8E0EA")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 9),
        ("RIGHTPADDING", (0, 0), (-1, -1), 9),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))

    story.append(details_table)
    story.append(Spacer(1, 13))

    story.append(Paragraph("Overall Match", heading_style))

    score_card = Table(
        [
            [Paragraph(
                f"{overall_match_score:.2f}%",
                score_style,
            )],
            [Paragraph(
                f"{escape(str(match_level))} "
                f"— {escape(str(job_recommendation))}",
                score_label_style,
            )],
        ],
        colWidths=[170 * mm],
    )

    score_card.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), LIGHT_BLUE),
        ("BOX", (0, 0), (-1, -1), 0.8, BLUE),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, 0), 12),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 3),
        ("TOPPADDING", (0, 1), (-1, 1), 3),
        ("BOTTOMPADDING", (0, 1), (-1, 1), 12),
    ]))

    story.append(score_card)

    story.append(Paragraph("Score Breakdown", heading_style))

    score_data = [
        ["Metric", "Score"],
        ["Weighted Skill Match", f"{weighted_skill_score:.2f}%"],
        ["Skill Match Contribution (70%)", f"{skill_component:.2f}%"],
        ["Text Overlap Similarity", f"{tfidf_score:.2f}%"],
        ["Text Overlap Contribution (30%)", f"{similarity_component:.2f}%"],
    ]

    score_table = Table(
        score_data,
        colWidths=[125 * mm, 45 * mm],
        repeatRows=1,
    )

    score_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("BACKGROUND", (0, 1), (-1, -1), WHITE),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#D8E0EA")),
        ("ALIGN", (1, 1), (1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))

    story.append(score_table)

    story.append(Paragraph("Skills Overview", heading_style))

    skills_data = [
        ["Skill category", "Identified", "Matched", "Missing"],
        [
            "Required skills",
            str(len(required_job_skills)),
            str(len(required_matches)),
            str(len(required_job_skills) - len(required_matches)),
        ],
        [
            "Preferred skills",
            str(len(preferred_job_skills)),
            str(len(preferred_matches)),
            str(len(preferred_job_skills) - len(preferred_matches)),
        ],
    ]

    skills_table = Table(
        skills_data,
        colWidths=[66 * mm, 34 * mm, 34 * mm, 36 * mm],
        repeatRows=1,
    )

    skills_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("BACKGROUND", (0, 1), (-1, 1), LIGHT_GREEN),
        ("BACKGROUND", (0, 2), (-1, 2), LIGHT_GREY),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#D8E0EA")),
        ("ALIGN", (1, 1), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("FONTSIZE", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))

    story.append(skills_table)

    story.append(Paragraph("Matching Skills", heading_style))

    if matching_skills:
        matching_text = "<br/>".join(
            f"&#8226; {escape(str(skill))}"
            for skill in matching_skills
        )
    else:
        matching_text = "No matching skills identified."

    story.append(Paragraph(matching_text, body_style))

    story.append(Paragraph("Missing Skills", heading_style))

    if missing_skills:
        missing_text = "<br/>".join(
            f"&#8226; {escape(str(skill))}"
            for skill in missing_skills
        )
    else:
        missing_text = "No missing skills identified."

    story.append(Paragraph(missing_text, body_style))

    story.append(Paragraph("Skill Gap Priority", heading_style))

    if skill_gap_priority:
        priority_rows = [["Skill", "Priority"]]

        for skill, priority in skill_gap_priority:
            priority_rows.append([
                Paragraph(escape(str(skill)), body_style),
                Paragraph(f"<b>{escape(str(priority))}</b>", body_style),
            ])

        priority_table = Table(
            priority_rows,
            colWidths=[125 * mm, 45 * mm],
            repeatRows=1,
        )

        priority_table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), NAVY),
            ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#D8E0EA")),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 8),
            ("TOPPADDING", (0, 0), (-1, -1), 6),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ]))

        story.append(priority_table)
    else:
        story.append(Paragraph(
            "No skill gaps identified.",
            body_style,
        ))

    story.append(Paragraph("Recommendations", heading_style))

    if missing_skills:
        recommendation_text = (
            "Consider developing the following skills where relevant "
            "to your target role:<br/>"
            + "<br/>".join(
                f"&#8226; {escape(str(skill))}"
                for skill in missing_skills
            )
        )
    else:
        recommendation_text = (
            "Your resume covers all skills identified by the current "
            "skill-matching configuration."
        )

    story.append(Paragraph(recommendation_text, body_style))

    chart_file = "skill_match_chart.png"

    try:
        chart = Image(chart_file, width=155 * mm, height=86 * mm)
        chart.hAlign = "CENTER"

        story.append(Paragraph("Skill Match Visualization", heading_style))
        story.append(KeepTogether([
            chart,
            Spacer(1, 8),
        ]))
    except Exception:
        story.append(Paragraph(
            "The skill chart was unavailable when this report was created.",
            small_style,
        ))

    story.append(Spacer(1, 12))

    story.append(Paragraph(
        "<b>Important note:</b> The match score is an estimate based on "
        "text overlap and configured skill-matching rules. It is not a "
        "validated hiring prediction, and a missing skill does not "
        "necessarily mean a candidate lacks that ability.",
        small_style,
    ))

    def add_page_number(canvas, doc):
        canvas.saveState()
        canvas.setStrokeColor(colors.HexColor("#D8E0EA"))
        canvas.line(
            18 * mm,
            14 * mm,
            A4[0] - 18 * mm,
            14 * mm,
        )
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(DARK_GREY)
        canvas.drawString(
            18 * mm,
            9 * mm,
            "AI Resume & Job Match Analyzer",
        )
        canvas.drawRightString(
            A4[0] - 18 * mm,
            9 * mm,
            f"Page {doc.page}",
        )
        canvas.restoreState()

    document.build(
        story,
        onFirstPage=add_page_number,
        onLaterPages=add_page_number,
    )

    print(f"\nPDF report generated successfully: {output_file}")