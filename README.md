# DBaaS-Project

A simple Database-as-a-Service (DBaaS) application developed using Flask, deployed on an Amazon EC2 server.
This project provides a web-based interface for users to create, manage, and interact with databases seamlessly.

## Features

* User-friendly web interface for database operations
* Support for creating and deleting databases
* Execution of SQL queries through the web interface
* Deployed on Amazon EC2 for scalability and reliability

## Technologies Used

* **Backend:** Python, Flask
* **Frontend:** HTML, CSS (with Flask templating)
* **Deployment:** Amazon EC2

## Getting Started

### Prerequisites

* Python 3.x
* pip (Python package installer)
* Amazon EC2 instance (for deployment)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Athoillah21/DBaaS-Project.git
   cd DBaaS-Project
   ```

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**

   ```bash
   python app_dbaas.py
   ```

   The application will be accessible at `http://localhost:5000/`.

## Deployment on Amazon EC2

1. **Launch an EC2 instance:**

   * Choose an Amazon Machine Image (AMI) (e.g., Ubuntu Server)
   * Select an instance type (e.g., t2.micro)
   * Configure security groups to allow HTTP (port 80) and SSH (port 22)

2. **SSH into your EC2 instance:**

   ```bash
   ssh -i your-key.pem ubuntu@your-ec2-public-ip
   ```

3. **Install necessary packages:**

   ```bash
   sudo apt update
   sudo apt install python3-pip python3-venv
   ```

4. **Clone the repository and set up the application:**

   ```bash
   git clone https://github.com/Athoillah21/DBaaS-Project.git
   cd DBaaS-Project
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

5. **Run the application:**

   ```bash
   python app_dbaas.py
   ```

   Ensure that your Flask app is configured to run on `0.0.0.0` to be accessible externally.

## Usage

* Navigate to `http://your-ec2-public-ip:5000/` in your web browser.
* Use the interface to create new databases, execute SQL queries, and manage existing databases.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

* [Flask](https://flask.palletsprojects.com/) - Micro web framework used for the application
* [Amazon EC2](https://aws.amazon.com/ec2/) - Cloud platform for deployment
