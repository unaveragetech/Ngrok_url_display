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
    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Latest Auto-Generated UI</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            color: #333;
        }}
        .container {{
            text-align: center;
            background: #ffffff;
            padding: 30px 40px;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
            width: 80%;
            max-width: 600px;
        }}
        h1 {{
            font-size: 1.8em;
            margin-bottom: 20px;
            color: #2c3e50;
        }}
        button {{
            padding: 12px 24px;
            font-size: 16px;
            color: #ffffff;
            background-color: #007bff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }}
        button:hover {{
            background-color: #0056b3;
        }}
        .info {{
            margin-top: 20px;
            font-size: 14px;
            color: #555;
        }}
        .info a {{
            color: #007bff;
            text-decoration: none;
        }}
        .info a:hover {{
            text-decoration: underline;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Access the Latest Auto-Generated UI</h1>
        <a href="{latest_url}" target="_blank" style="text-decoration: none;">
            <button>Visit Latest Link</button>
        </a>
        <div class="info">
            <p><strong>Last Update:</strong> {last_update}</p>
            <p><strong>Last Link:</strong> <a href="{latest_url}" target="_blank">{latest_url}</a></p>
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
