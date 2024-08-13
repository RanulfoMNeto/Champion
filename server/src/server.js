const cors = require('cors');
const express = require('express');
const path = require('path');
const nodemailer = require('nodemailer');

const app = express();
const port = 3000;

let champions = [];

// Middleware to parse JSON bodies
app.use(express.json());
app.use(cors());
// Serve static files from the 'front-end' directory
app.use(express.static(path.join(__dirname, 'front-end')));

// Route to handle incoming champion data
app.post('/api/champions', (req, res) => {
    champions = req.body;
    // console.log('Received champions data:', champions);
    res.status(200).json({
        message: 'Data received successfully.'
    });

    // Check if any champion has reached the chosen tier
    checkAlerts();
});

app.get('/api/champions', (req, res) => {
    res.json(champions);
});

// Route to get a specific champion by code
app.get('/api/champions/:code', (req, res) => {
    const code = req.params.code;
    const champion = champions.find(c => c.code === code);
    if (champion) {
        res.json(champion);
    } else {
        res.status(404).json({ message: 'Champion not found' });
    }
});

// Serve the champions.html file at the /champions route
app.get('/champions', (req, res) => {
    res.sendFile(path.join(__dirname, 'front-end', 'champions.html'));
});

app.get('/chart', (req, res) => {
    res.sendFile(path.join(__dirname, 'front-end', 'chart.html'));
});

// Route to process the form and send email alerts
// Configure Nodemailer transporter
const transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
        user: 'example@gmail.com',
        pass: 'password'
    }
});

alerts = []

app.post('/champions', (req, res) => {
    const { champion, email, tier } = req.body;
    
    console.log(`Champion: ${champion}, Email: ${email}, Tier: ${tier}`);

    // Store the alert preference
    alerts.push({ champion, email, tier });

    res.status(200).send('Data received successfully and alert configured!');
});

// Function to check if any champion has reached the chosen tier
function checkAlerts() {
    console.log("Checking Alerts:");
    console.log(alerts)
    alerts.forEach(alert => {
        console.log('Alert:', alert)
        const { champion, email, tier } = alert;
        const championData = champions.find(c => c.name.toLowerCase() === champion.toLowerCase());

        if (championData && championData.tier === tier) {
            // Configure email options
            const mailOptions = {
                from: 'example@gmail.com',
                to: email,
                subject: 'Champion Tier Alert',
                text: `The champion ${championData.name} has reached tier ${tier}.`
            };

            // Send the email
            transporter.sendMail(mailOptions, (error, info) => {
                if (error) {
                    console.error('Error sending email:', error);
                } else {
                    console.log('Email sent:', info.response);
                }
            });
            console.log("Reached");
            // Remove the alert after sending
            alerts = alerts.filter(a => a !== alert);
        } else {
            console.log("Not Reached");
        }
    });
}

// Catch-all route to serve static files
app.get('*', (req, res) => {
    res.status(404).send('Not Found');
});

// Start the server
app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
