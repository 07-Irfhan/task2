import pandas as pd
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors


data = pd.read_csv('sample_data.csv')
summary = data.describe()


plt.figure(figsize=(6, 4))
data['Salary'].hist(color='skyblue', edgecolor='black')
plt.title('Salary Distribution')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('plot.png')
plt.close()


doc = SimpleDocTemplate("automated_report.pdf", pagesize=letter)
styles = getSampleStyleSheet()
story = []


story.append(Paragraph("Automated Report", styles['Title']))
story.append(Spacer(1, 12))

intro_text = "This report was generated automatically using Python's ReportLab library. It includes summary statistics and a histogram of the 'Salary' column."
story.append(Paragraph(intro_text, styles['BodyText']))
story.append(Spacer(1, 12))


story.append(Paragraph("Data Summary", styles['Heading2']))
summary_data = [summary.columns.insert(0, "Statistic").tolist()]  # Header
for index, row in summary.iterrows():
    summary_data.append([index] + [f"{val:.2f}" for val in row])

table = Table(summary_data)
table.setStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
])
story.append(table)
story.append(Spacer(1, 20))


story.append(Paragraph("Salary Histogram", styles['Heading2']))
img = Image("plot.png", width=400, height=300)
story.append(img)


doc.build(story)

print("✅ PDF report generated: automated_report.pdf")
