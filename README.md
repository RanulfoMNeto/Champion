# Champion

**League of Legends Tier Notifier** is a web application designed to keep track of League of Legends champions' tiers and notify users via email when a champion reaches their desired tier. The application leverages Docker and Docker Compose to facilitate easy deployment and management of services.

## Prerequisites

- [Docker](https://www.docker.com/get-started) and [Docker Compose](https://docs.docker.com/compose/install/) installed on your machine.

## How to Run

Follow the steps below to run the project using Docker Compose:

1. **Clone the repository**

```bash
git clone https://github.com/RanulfoMNeto/Champion.git
cd Champion
```

2. **Run Docker Compose**

In the root of the project, execute the following command to build and start the containers:

```bash
docker-compose up --build
```

This will download the necessary images, build the containers, and start the services defined in the `docker-compose.yml` file.

3. **Access the Application**

After starting Docker Compose, the application will be accessible in your browser at [localhost](http://localhost:3000).

## Routes

The application has the following routes that allow interaction with champion data and notification alert configuration:

### User Interface Routes

- **GET /champions**

  - **Description:** Serves the `champions.html` file, which is the interface for viewing champions.

- **GET /chart**

  - **Description:** Serves the `chart.html` file, used to display champion charts.

### Notify Route

- **POST /champions**

  - **Description:** Processes the alert configuration form and stores alert preferences.
  - **Request Body:** JSON containing the champion's name, email, and desired Tier for the alert.
  - **Success Response:**
    ```json
    {
      "message": "Data received successfully and alert configured!"
    }
    ```

### Email Configuration

The project uses Nodemailer to send notification emails. The email service and credentials need to be configured in the code.

```javascript
const transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
        user: 'example@gmail.com',
        pass: 'password'
    }
});
```