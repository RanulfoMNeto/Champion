const cors = require('cors');
const express = require('express');
const path = require('path');

const app = express();
const port = 3000;

let champions = [];

// Middleware to parse JSON bodies
app.use(express.json());
app.use(cors());
app.use(express.static(path.join(__dirname, 'src')));

// Route to handle incoming champion data
app.post('/api/champions', (req, res) => {
    champions = req.body;
    console.log('Received champions data:', champions);
    res.status(200).json({
        message: 'Data received successfully.'
    });
});

app.get('/api/champions', (req, res) => {
    res.json(champions);
});

// Serve the index.html file at the /champions route
app.get('/champions', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

// Start the server
app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
