# Inventory Management System

This project is a web-based inventory management application built with **Flask** (backend), a dynamic **frontend**, and **AWS integration** for storage and CI/CD.

## Features
- Add, update, delete, and view inventory items.
- Upload and download contracts using **AWS S3**.
- User-friendly interface with a responsive design.
- CRUD operations handled via RESTful APIs.

## Tech Stack
- **Backend**: Flask (Python)
- **Frontend**: HTML, JavaScript
- **Database**: JSON File (for simplicity)
- **Server Management**: Gunicorn (WSGI server)
- **Platform**: AWS EC2 Ubuntu instance

---

## **Current Status**

### **What We've Done So Far**
1. **Local Development**:
   - Flask app runs locally with CRUD operations and basic functionality.
   - Contracts can be uploaded to a local folder.

2. **AWS Deployment**:
   - Application deployed on an **AWS EC2 instance**.
   - **Gunicorn** configured as the production WSGI server.
   - Successfully accessed the application via `curl` on port 8000.

3. **AWS Configuration**:
   - EC2 security group set to allow inbound traffic on ports 22 (SSH), 80 (HTTP), and 443 (HTTPS).
   - Verified Flask app functionality on the server with Gunicorn.

---

## **TODO**

### **Immediate Next Steps**
- **Nginx Setup**:
   - [ ] Configure Nginx as a reverse proxy to forward requests from port 80 to Gunicorn.
   - [ ] Test accessibility via the public IP on port 80.

### **Future Enhancements**
- **CI/CD Pipeline**:
   - [ ] Set up an automated CI/CD pipeline using AWS CodePipeline, CodeBuild, and CodeDeploy.

---

## How to Run the Application

### Locally

- Clone the repository:

```bash
git clone https://github.com/SM-7603/simple_inventory_management_system_aws.git
cd simple_inventory_management_system_aws
```

- Set up the virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

- Run the application:

```bash
python3 app.py
```

- Access the application at:

```bash
http://127.0.0.1:8080
```

### On AWS EC2

- SSH into the EC2 instance and clone the repository:

```bash
git clone https://github.com/SM-7603/simple_inventory_management_system_aws.git
cd simple_inventory_management_system_aws
```

- Set up the virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install flask gunicorn
```

- Run Gunicorn:

```bash
gunicorn -b 0.0.0.0:8000 app:app
```

- Test the application:

```bash
curl http://127.0.0.1:8000
```
