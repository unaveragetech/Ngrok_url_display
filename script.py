import os

# Define paths
input_file = "Sent_urls.txt"
output_file = "docs/index.html"

def update_index():
    # Ensure the input file exists
    if not os.path.exists(input_file):
        print(f"{input_file} not found.")
        return

    # Read the newest URL from the input file
    with open(input_file, "r") as f:
        urls = f.readlines()

    # Ensure there are URLs in the file
    if not urls:
        print(f"No URLs found in {input_file}.")
        return

    # Get the last URL
    latest_url = urls[-1].strip()

    # Create the HTML content
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Latest Link</title>
</head>
<body>
    <h1>Click the button below to visit the latest link:</h1>
    <a href="{latest_url}" target="_blank" style="text-decoration: none;">
        <button style="padding: 10px 20px; font-size: 16px;">Go to Latest Link</button>
    </a>
</body>
</html>
"""

    # Save the HTML file
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w") as f:
        f.write(html_content)

    print(f"Updated {output_file} with the latest URL.")

if __name__ == "__main__":
    update_index()
