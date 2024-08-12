const cors = require('cors');
const express = require('express');
const path = require('path');

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
    console.log('Received champions data:', champions);
    res.status(200).json({
        message: 'Data received successfully.'
    });
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


// Serve the index.html file at the /champions route
app.get('/champions', (req, res) => {
    res.sendFile(path.join(__dirname, 'front-end', 'champions.html'));
});

app.get('/chart', (req, res) => {
    res.sendFile(path.join(__dirname, 'front-end', 'chart.html'));
});


// Catch-all route to serve static files
app.get('*', (req, res) => {
    res.status(404).send('Not Found');
});

// Start the server
app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
