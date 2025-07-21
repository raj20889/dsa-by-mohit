from datetime import date

# Input fields
platform = input("Platform (e.g., LeetCode, GFG): ").strip()
problem_name = input("Problem Name: ").strip()
problem_link = input("Problem Link: ").strip()
file_path = input("Solution File Path (relative): ").strip()
topic = input("Topic (e.g., Array, Stack): ").strip()

# Date
today = date.today().isoformat()

# New row for log table
new_entry = f"| {today} | {platform} | [{problem_name}]({problem_link}) | [{file_path}]({file_path}) | {topic} |\n"

# Read the README.md file
with open("README.md", "r", encoding="utf-8") as file:
    lines = file.readlines()

# Find the log table section and insert the new entry
for i, line in enumerate(lines):
    if line.startswith("| Date"):
        table_header_index = i + 2  # Skip header and separator
        break

lines.insert(table_header_index, new_entry)

# Write back the updated README.md
with open("README.md", "w", encoding="utf-8") as file:
    file.writelines(lines)

print("✅ README.md log updated successfully!")
