import os
from datetime import datetime

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

    # Get the last update time
    last_update = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create the HTML content
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Latest Link</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
        }}
        .container {{
            text-align: center;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }}
        button {{
            padding: 10px 20px;
            font-size: 16px;
            margin-top: 20px;
        }}
        .info {{
            margin-top: 20px;
            font-size: 14px;
            color: #555;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Click the button below to visit the latest link:</h1>
        <a href="{latest_url}" target="_blank" style="text-decoration: none;">
            <button>Go to Latest Link</button>
        </a>
        <div class="info">
            <p>Last update: {last_update}</p>
            <p>Last button link: <a href="{latest_url}" target="_blank">{latest_url}</a></p>
        </div>
    </div>
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
