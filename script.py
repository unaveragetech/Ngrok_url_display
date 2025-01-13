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

    # Create the new HTML content
    html_content = f"""
<!DOCTYPE html>
<html>
<head>
<base href="/" />
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Stylish Auto-Generated UI</title>
<style>
  @keyframes gradientBG {{
    0% {{background-position: 0% 50%;}}
    50% {{background-position: 100% 50%;}}
    100% {{background-position: 0% 50%;}}
  }}

  @keyframes float {{
    0% {{transform: translateY(0px);}}
    50% {{transform: translateY(-20px);}}
    100% {{transform: translateY(0px);}}
  }}

  @keyframes pulse {{
    0% {{transform: scale(1);}}
    50% {{transform: scale(1.05);}}
    100% {{transform: scale(1);}}
  }}

  body {{
    margin: 0;
    padding: 0;
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
  }}

  .container {{
    background: rgba(255, 255, 255, 0.95);
    padding: 40px;
    border-radius: 20px;
    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    backdrop-filter: blur(4px);
    border: 1px solid rgba(255, 255, 255, 0.18);
    width: 80%;
    max-width: 600px;
    text-align: center;
    animation: float 6s ease-in-out infinite;
  }}

  h1 {{
    color: #2c3e50;
    font-size: 2.5em;
    margin-bottom: 30px;
    text-transform: uppercase;
    letter-spacing: 2px;
    background: linear-gradient(45deg, #12c2e9, #c471ed, #f64f59);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }}

  .button-wrapper {{
    margin: 20px 0;
  }}

  button {{
    padding: 15px 30px;
    font-size: 18px;
    color: white;
    background: linear-gradient(45deg, #12c2e9, #c471ed, #f64f59);
    border: none;
    border-radius: 50px;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    animation: pulse 2s infinite;
  }}

  button:hover {{
    transform: translateY(-3px);
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
  }}

  .info {{
    margin-top: 30px;
    padding: 20px;
    border-top: 2px solid rgba(0, 0, 0, 0.1);
  }}

  .info p {{
    margin: 10px 0;
    color: #666;
    font-size: 16px;
  }}

  .info a {{
    color: #c471ed;
    text-decoration: none;
    transition: color 0.3s ease;
  }}

  .info a:hover {{
    color: #f64f59;
    text-decoration: underline;
  }}

  @media (max-width: 768px) {{
    .container {{
      width: 90%;
      padding: 20px;
    }}
    
    h1 {{
      font-size: 1.8em;
    }}
  }}
</style>
</head>
<body>
  <div class="container">
    <h1>Access the Latest Auto-Generated UI</h1>
    <div class="button-wrapper">
      <a href="{latest_url}" target="_blank" style="text-decoration: none;">
        <button>Visit Latest Link</button>
      </a>
    </div>
    <div class="info">
      <p><strong>Last Update:</strong> {last_update}</p>
      <p><strong>Last Link:</strong> <a href="{latest_url}" target="_blank">{latest_url}</a></p>
    </div>
  </div>

  <script>
    // Add some interactive elements
    document.querySelector('button').addEventListener('mouseover', function() {{
      this.style.transform = 'scale(1.1) translateY(-3px)';
    }});

    document.querySelector('button').addEventListener('mouseout', function() {{
      this.style.transform = 'scale(1) translateY(0)';
    }});
  </script>
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
