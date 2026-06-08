from .stats import (
    average_per_student,
    subjects_offered,
    top_scorer,
    passing_students,
)


def format_report(records: list[dict]) -> str:
    """
    Build a human-readable, multi-line report.

    The report MUST include:
      - Total number of records
      - Sorted list of subjects offered
      - Average score for each student (alphabetical order)
      - The top scorer (name + average)
      - The list of passing students (threshold 60.0)
    """
    total_records = len(records)

    subjects = sorted(subjects_offered(records))

    averages = average_per_student(records)

    top_name, top_avg = top_scorer(records)

    passing = sorted(passing_students(records, threshold=60.0))

    lines = [
        f"Total records: {total_records}",
        f"Subjects offered: {', '.join(subjects)}",
        "",
        "Average scores:",
    ]

    for student in sorted(averages):
        lines.append(f"  {student}: {averages[student]:.2f}")

    lines.extend([
        "",
        f"Top scorer: {top_name} ({top_avg:.2f})",
        f"Passing students: {', '.join(passing)}",
    ])

    return "\n".join(lines)