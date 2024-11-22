# Employee Prediction Web App
![CI](https://github.com/marlonszm/patterns-project/actions/workflows/ci.yml/badge.svg?event=push)
![Coverage](https://codecov.io/gh/marlonszm/patterns-project/branch/main/graph/badge.svg)
![Deployment](https://img.shields.io/github/deployments/marlonszm/patterns-project/production)
![Pull Requests](https://img.shields.io/github/issues-pr/marlonszm/patterns-project)
![Last Commit](https://img.shields.io/github/last-commit/marlonszm/patterns-project)

![Commit Activity](https://img.shields.io/github/commit-activity/m/marlonszm/patterns-project)
![Languages](https://img.shields.io/github/languages/top/marlonszm/patterns-project)
![Contributors](https://img.shields.io/github/contributors/marlonszm/patterns-project)
![Release](https://img.shields.io/github/v/release/marlonszm/patterns-project)
![License](https://img.shields.io/github/license/marlonszm/patterns-project?style=flat-square)

## Description

This is a machine learning-powered web application built using Flask. It predicts the potential career outcome of employees based on their profile data, such as joining year, payment tier, age, experience, and education level. The app allows users to input their details via a form, and the model predicts the outcome based on trained data. The web app is deployed on Vercel for production use.

### Features:
- Input form for employee details: joining year, payment tier, age, ever benched status, experience, gender, and education level.
- Predicted career outcome displayed upon form submission.
- Simple and intuitive user interface for easy interaction.
- Secure model loading with file path handling.

## Production

The application is deployed and is available at the following link:
[Employee Prediction Web App](https://patterns-project-10ysz1h1c-marlon-souza-de-melos-projects.vercel.app)

## Installation

### Prerequisites:
1. Python 3.8+
2. Node.js (for testing scripts)
3. Flask (for running the app)
4. Required libraries for model handling and prediction

### Steps to set up:

1. Clone the repository:
    ```bash
    git clone https://github.com/your-repository-url.git
    cd your-repository
    ```

2. Install Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Install Node.js dependencies:
    ```bash
    npm install
    ```

4. Run the Flask app:
    ```bash
    python app.py
    ```

5. Open your browser and navigate to:
    ```bash
    http://127.0.0.1:5000/
    ```

## Testing

To run tests for the application:

1. Install pytest:
    ```bash
    pip install pytest
    ```

2. Run the tests:
    ```bash
    pytest
    ```

## Contributing

Feel free to fork the repository and submit pull requests. Contributions are welcome!

## Developers

This project is developed and maintained by:
- Marlon Melo
- Victor Melo
- Pedro Sérgio
- Tatiana Limongi

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
