# 💡 Ring Light

Web-based ring light for video calls with adjustable brightness, size, and color temperature.

## Deploy to Railway

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?code=ring-light)

### Manual Deployment Steps:

1. Install Railway CLI:
   ```bash
   npm install -g @railway/cli
   ```

2. Login to Railway:
   ```bash
   railway login
   ```

3. Initialize and deploy:
   ```bash
   railway init
   railway up
   ```

Or simply:
1. Push this repo to GitHub
2. Go to [railway.app](https://railway.app)
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your repository
5. Railway will auto-detect and deploy!

## Features

- 💡 Adjustable brightness (with progressive boost)
- 📏 Adjustable size
- 🌡️ Color temperature presets (Cold/Neutral/Warm)
- 🫁 Breathing animation
- 🖥️ Fullscreen mode
- ⚡ Instant web access

## Local Development

```bash
npm install
npm start
```

Visit `http://localhost:3000`
