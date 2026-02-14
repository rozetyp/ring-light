const express = require('express');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

// Log all requests
app.use((req, res, next) => {
  const timestamp = new Date().toISOString();
  const userAgent = req.get('user-agent') || 'unknown';
  console.log(`[${timestamp}] ${req.method} ${req.url} - ${userAgent}`);
  next();
});

// Serve static files
app.use(express.static(__dirname));

// Serve index.html at root
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

app.listen(PORT, () => {
  console.log(`Ring Light server running on port ${PORT}`);
  console.log(`Local: http://localhost:${PORT}`);
});
