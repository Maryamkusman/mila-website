from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "mila-change-this-in-production"

SERVICES = [
    {
        "icon": "🤖",
        "title": "Custom AI Assistants",
        "short": "Chatbots trained on your exact business — your tone, your knowledge, your brand.",
        "description": "We build AI chatbots and virtual assistants that know your products, policies, and customers. Deploy on your website, WhatsApp, Instagram DMs, or internal tools.",
        "examples": ["Customer service automation", "Sales qualification bots", "Internal HR/ops assistants"],
    },
    {
        "icon": "⚡",
        "title": "AI Workflow Automation",
        "short": "Eliminate the tasks that eat your time. Automate with intelligence.",
        "description": "We map your current workflows and identify where AI can take over — from email triage and document processing to scheduling and reporting.",
        "examples": ["Email & inbox automation", "Document summarization", "Report generation"],
    },
    {
        "icon": "📊",
        "title": "Data Intelligence",
        "short": "Your data is a goldmine. We help you actually use it.",
        "description": "We build AI-powered dashboards and analytics tools that surface insights from your business data — no data science team required.",
        "examples": ["Sales forecasting", "Customer behavior analysis", "Inventory & demand prediction"],
    },
    {
        "icon": "🧭",
        "title": "AI Strategy Consulting",
        "short": "Not sure where to start with AI? We map the path for you.",
        "description": "We audit your business, identify the highest-ROI AI opportunities, and give you a clear, actionable roadmap — so you invest in the right things first.",
        "examples": ["AI readiness assessment", "Technology roadmap", "Team training & onboarding"],
    },
]


@app.route("/")
def index():
    return render_template("index.html", services=SERVICES[:3])


@app.route("/services")
def services():
    return render_template("services.html", services=SERVICES)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        business = request.form.get("business", "").strip()
        message = request.form.get("message", "").strip()

        if not name or not email or not message:
            flash("Please fill in all required fields.", "error")
        else:
            # TODO: wire up email sending or a CRM here
            flash(f"Thanks {name}! We'll be in touch within 24 hours. ✨", "success")
            return redirect(url_for("contact"))

    return render_template("contact.html")


if __name__ == "__main__":
    import os
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug)
