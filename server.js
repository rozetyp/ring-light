const express = require('express');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

// Parse JSON bodies
app.use(express.json());

// Log site visits
app.use((req, res, next) => {
  if (req.url === '/' && req.method === 'GET') {
    console.log(`✅ Site visit - ${req.get('referer') || 'direct'}`);
  }
  next();
});

// Referral redirects with tracking
app.get('/go/coffee', (req, res) => {
  const referrer = req.get('referer') || 'direct';
  console.log(`🔗 Coffee click (from: ${referrer})`);
  res.redirect('https://buymeacoffee.com/sandbar');
});

app.get('/go/amazon', (req, res) => {
  const referrer = req.get('referer') || 'direct';
  console.log(`🔗 Amazon click (from: ${referrer})`);
  res.redirect('https://amzn.to/4aAWAgA');
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
