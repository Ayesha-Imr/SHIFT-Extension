# SHIFT - Eco-Friendly Product Analyzer

Make your shift towards a more sustainable lifestyle today.
SHIFT is a Chrome extension that helps you analyze the sustainability and eco-friendliness of products and discover eco-friendly alternatives. With SHIFT, you can make informed, greener choices effortlessly.

## Features

- **Instant Text Extraction**: Extract product descriptions from any webpage with a single click.
- **Comprehensive Analysis**: Get a detailed sustainability score and eco-friendliness rating for products.
- **Eco-Friendly Alternatives**: Discover environmentally friendly alternatives to your current products, complete with purchase options and links.
- **User-Friendly Interface**: Enjoy a clean, intuitive interface that makes it easy to access all features and information.

## Demo

[![YouTube Video Title](https://img.youtube.com/vi/Gt9M2XeEqzE/0.jpg)](https://www.youtube.com/watch?v=Gt9M2XeEqzE)

## Installation

### From the Chrome Web Store

1. **Visit the Chrome Web Store**:
   - Go to the [SHIFT Extension page on the Chrome Web Store](https://chrome.google.com/webstore/detail/shift/bpplgnhmfcoohmeppibphjoahlfaebhj).

2. **Add to Chrome**:
   - Click on the "Add to Chrome" button.
   - Confirm the installation by clicking "Add extension" in the pop-up dialog.

3. **Start Using SHIFT**:
   - Click on the SHIFT icon in the Chrome toolbar.
   - Follow the on-screen instructions to analyze products and discover eco-friendly alternatives.

### Local Setup Instructions

If you want to set up the SHIFT extension locally for development or testing, follow these steps:

1. **Clone the Repository**:
   - Clone the repository to your local machine using the following command:
     ```sh
     git clone https://github.com/Ayesha-Imr/SHIFT-Extension.git
     ```
     
2.  **Navigate to the Extension Directory**:
   - Change to the extension directory:
     ```sh
     cd SHIFT/extension
     ```

3. **Load the Extension in Chrome**:
   - Open Chrome and go to [chrome://extensions/](http://_vscodecontentref_/0).
   - Enable "Developer mode" by toggling the switch in the top right corner.
   - Click on the "Load unpacked" button.
   - Select the `SHIFT/extension` directory.

4. **Start Using SHIFT**:
   - Click on the SHIFT icon in the Chrome toolbar.
   - Follow the on-screen instructions to analyze products and discover eco-friendly alternatives.

## Backend Setup

The SHIFT extension relies on a backend server for processing product descriptions and providing analysis results. Follow these steps to set up the backend server:

1. **Navigate to the Backend Directory**:
   - Change to the backend directory:
     ```sh
     cd SHIFT/backend
     ```

2. **Create a Virtual Environment**:
   - Create a virtual environment using the following command:
     ```sh
     python -m venv venv
     ```

3. **Activate the Virtual Environment**:
   - Activate the virtual environment:
     - On Windows:
       ```sh
       venv\Scripts\activate
       ```
     - On macOS/Linux:
       ```sh
       source venv/bin/activate
       ```

4. **Install Dependencies**:
   - Install the required dependencies using the following command:
     ```sh
     pip install -r requirements.txt
     ```

5. **Set Up Environment Variables**:
   - Create a `.env` file in the `SHIFT/backend` directory and add the following environment variables:
     ```env
     GITHUB_TOKEN=your-github-token
     ```
    - This is required to access Github models.

6. **Run the Backend Server**:
   - Start the backend server using the following command:
     ```sh
     python app.py
     ```

---

**Download SHIFT now and take the first step towards a more sustainable lifestyle!**
