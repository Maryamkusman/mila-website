# Deploying Your Mila Website to Railway 🚀

Your website is now ready to be published! Follow these steps to go live in minutes.

## Step 1: Set Up Git

In your terminal:

```bash
cd /Users/maryamusman/mila-website
git init
git add .
git commit -m "Initial commit: Mila website ready for deployment"
```

## Step 2: Create a GitHub Repository

1. Go to https://github.com/new
2. Name it: `mila-website`
3. Click "Create repository"
4. Copy the commands from "…or push an existing repository from the command line"
5. Run those commands in your terminal

It will look something like:
```bash
git remote add origin https://github.com/YOUR-USERNAME/mila-website.git
git branch -M main
git push -u origin main
```

## Step 3: Set Up Railway

1. Go to https://railway.app
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your `mila-website` repository
5. Railway will auto-detect it's a Python/Flask app
6. Click "Deploy"

That's it! ✨

## Step 4: Get Your Live URL

Once deployed (takes ~2-3 minutes):
- Railway will give you a URL like `mila-website-prod.up.railway.app`
- Your site is now LIVE! 🎉
- Share this URL with anyone to showcase your services

## Step 5: Add a Custom Domain (Optional)

If you want a custom domain later:
1. In Railway dashboard → Settings → Domains
2. Add your custom domain
3. Update your DNS records (Railway provides instructions)

## Files Created for Deployment

- `Procfile` - Tells Railway how to run your Flask app
- `.gitignore` - Keeps sensitive files out of version control
- Updated `requirements.txt` - Added `gunicorn` for production
- Updated `app.py` - Now works with environment variables

## Troubleshooting

**Site won't load?** Check Railway logs:
- Railway Dashboard → Your Project → Logs tab
- Look for errors and resolve them

**Port issues?** Already handled! Your app now uses environment variables.

**Changes not updating?** 
- Push to GitHub: `git push`
- Railway auto-deploys (takes 1-2 mins)

## Next Steps

1. Get your domain name (Namecheap, Google Domains, etc.)
2. Point it to your Railway app
3. Start booking consultations! 💼

Need help? Railway docs: https://docs.railway.app
