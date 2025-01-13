[Auto-Generated UI](https://unaveragetech.github.io/Ngrok_url_display/)
---

# Auto-Generated UI Deployment via GitHub Pages

This repository provides a public-facing link to access the latest auto-generated user interface (UI) using a dynamic URL system. The solution is designed to simplify deployment and make the UI accessible to users in a seamless and efficient manner.

## About the Project

The project utilizes a script to dynamically update a GitHub Pages-hosted `index.html` file with the latest URL required to access the auto-generated UI. This approach acts as a workaround to deploy and share the UI for public use without the need for a persistent server or manual updates.

## How It Works

1. **Dynamic URL Updates**:
   - The `Sent_urls.txt` file in the repository stores the generated URLs. The script automatically extracts the most recent URL (last entry in the file).

2. **Automatic HTML Generation**:
   - The script generates a simple `index.html` file containing a clickable button that redirects users to the latest URL.
   - This HTML file is stored in the `docs/` folder, which is used as the source for GitHub Pages.

3. **Continuous Integration**:
   - A GitHub Actions workflow is set up to monitor changes to the `Sent_urls.txt` file.
   - Whenever the file is updated, the workflow triggers the script, generates the new `index.html`, and pushes the changes back to the repository.

4. **GitHub Pages**:
   - The updated `index.html` is hosted on GitHub Pages and made publicly accessible at:
     [Auto-Generated UI](https://unaveragetech.github.io/Ngrok_url_display/).

## Access the UI

Visit the following link to access the updated auto-generated UI:
[Auto-Generated UI](https://unaveragetech.github.io/Ngrok_url_display/)

## Purpose

This project was designed to:
- Provide an automated solution for deploying and sharing the UI with public users.
- Eliminate the need for a persistent server or manual URL updates.
- Enable seamless integration with dynamic systems like Ngrok.

## How to Use the Repository

1. Update the `Sent_urls.txt` file with the latest URL (one URL per line).
2. Push the changes to the `main` branch.
3. The GitHub Actions workflow will automatically:
   - Run the script to update the `index.html` file.
   - Push the changes to the repository.
4. The updated link will be available at the GitHub Pages URL.

## Key Features

- **Automation**: Fully automated update process using GitHub Actions.
- **Ease of Use**: Simple, publicly accessible link to the latest UI.
- **Dynamic Deployment**: Supports dynamic and ephemeral URLs (e.g., from Ngrok).

---
