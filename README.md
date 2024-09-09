## Inventory Management API

This is a **FastAPI** application for managing inventory items (name and price). The application is structured into separate layers: UI, Business Logic, and Data Access, following clean code principles.

### Project Structure

RestAPIAPPVersion1/
├── main.py  
├── requirements.txt  
├── .gitignore  
├── README.md  
├── app/  
├── business_logic/  
├── data_access/  
├── models/  
├── middleware/  
├── utils/

### Installation & Setup

1. **Clone the repository**:
   git clone https://github.com/Ofarukk/RestAPI_with_FastAPI_Application.git
   cd RestAPIAPPVersion1
2. **Install dependencies**:
   pip install -r requirements.txt

3. **Run the app**:
   uvicorn main:app --reload

The app will be available at `http://127.0.0.1:8000`.

### API Endpoints

- **GET** `/items`: Get all items.
- **GET** `/items/{item_name}`: Get an item by name.
- **POST** `/items`: Add a new item.
- **PUT** `/items/{item_name}`: Update an item.
- **DELETE** `/items/{item_name}`: Delete an item.

Access the API documentation at `http://127.0.0.1:8000/docs` for Swagger UI.

### Deployment on AWS EC2

1. **Set up EC2**: Create an EC2 instance, install Python and pip.
2. **Transfer files**: Use **WinSCP** or another tool to upload project files.
3. **Install dependencies**:
   pip install -r requirements.txt
4. **Run the app** using Gunicorn:
   gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
5. **Configure NGINX** as a reverse proxy to manage traffic.

### Future Improvements

- Database integration (PostgreSQL, MySQL)
- Add user authentication
- Dockerize the app

### License

MIT License
