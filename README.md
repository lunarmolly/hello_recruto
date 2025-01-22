# Hello Recruto Web Service

This is a simple web service built with Python and Flask. It returns a greeting message in the format:  
**"Hello {name}! {message}!"**  
where `name` and `message` are passed as query parameters in the URL.

---

## Features
- Returns a customizable greeting message.
- Accepts `name` and `message` as query parameters via a GET request.
- Easy to set up and run locally or deploy to a cloud service.

---

## Prerequisites
Before running the project, ensure you have the following installed:

- **Python 3.8 or higher**
- **pip** (Python package manager)

---

## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/lunarmolly/hello_recruto.git
   cd hello_recruto
    ```
2. **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/MacOS
    venv\Scripts\activate     # On Windows
    ```
3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
## Running the project
1. **Start the Flask development server:**
    ```bash
    python app.py
    ```
2. **Access the web service:**
Open your browser or use a tool like curl or Postman to visit:
    ```bash
    http://127.0.0.1:5000/?name=Recruto&message=Let's%20be%20friends
    ```
3. **Expected output:**
    ```
    Hello Recruto! Let's be friends!
    ```
   
## Project structure
```
hello_recruto/
│
├── app/                         # Main application directory
│   ├── __init__.py              # Initializes the Flask app
│   ├── routes.py                # Defines the routes and logic
│   └── templates/               # Directory for HTML templates (optional)
│       └── index.html           # Example HTML template (not used in this project)
│
├── requirements.txt             # Lists project dependencies
├── config.py                    # Configuration file (optional)
├── run.py                       # Entry point to run the application
└── README.md                    # Project documentation (this file)
```

## Customizing the greeting message
You can customize the greeting by passing different values for name and message in the URL. For example:
- **Default behavior** (no parameters):
    ```bash
    http://127.0.0.1:5000/
    ```
    Output:
    ```
   Hello Recruto! Let's be friends!
    ```
- **Custom name and message**:
    ```bash
    http://127.0.0.1:5000/?name=John&message=Welcome%20to%20the%20team
    ```
    Output:
    ```
    Hello John! Welcome to the team!
    ```

## Deployment
To make the service accessible externally, you can deploy it to a cloud platform like Heroku, PythonAnywhere, or AWS. Alternatively, use ngrok for temporary external access:
1. **Install ngrok:**
    Download and install ngrok from [https://ngrok.com/download](https://ngrok.com/download).
2. **Run ngrok:**
    ```bash
    ngrok http 5000
    ```
3. **Access the service:**
   Use the URL provided by ngrok (e.g., `https://your-subdomain.ngrok.io`).

## Dependencies
The project uses the following Python packages:
- **Flask**: A lightweight web framework for Python.
All dependencies are listed in the `requirements.txt` file.