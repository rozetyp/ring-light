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
  res.redirect('https://www.amazon.com/s?k=best+ring+light+for+content+creators&rh=p_n_condition-type%3A6503240011%2Cp_72%3A2491149011&dc=&ds=v1%3ARuejKD7SzH1bHDcOqABI8vz1decfyfM1z97aPrIOfKQ&crid=22172V9RTQDBQ&qid=1771007739&rnid=2491147011&sprefix=best+ring+light%2Caps%2C441&linkCode=ll2&tag=sandbarstudio-20&linkId=d8e88f0ba0b3f591287b0ae0af2c00ef&language=en_US&ref_=as_li_ss_tl');
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
