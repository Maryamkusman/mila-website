import os

from flask import Flask, flash, render_template, request

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-not-for-production")

GENERAL_SOLUTIONS = [
    {
        "icon": "💬",
        "title": "AI Customer Support & Chatbots",
        "stat": "51% of companies have already deployed",
        "short": "AI agents resolving the majority of service issues without human involvement. 24/7 responses — no overnight staff required.",
    },
    {
        "icon": "🔥",
        "title": "Lead Follow-Up & CRM Automation",
        "stat": "Respond to new leads in under 60 seconds",
        "short": "Auto-respond to new leads instantly, run nurturing sequences, and keep your CRM updated. Stop losing revenue every hour a lead goes unanswered.",
    },
    {
        "icon": "📧",
        "title": "Inbox & Email Management",
        "stat": "The #1 first thing businesses pay to automate",
        "short": "Sort, draft, and route emails automatically. Stop drowning in email, scheduling, and small tasks that eat your day.",
    },
    {
        "icon": "📱",
        "title": "Content Repurposing & Distribution",
        "stat": "More reach, same production time",
        "short": "Turn long-form content into platform-specific assets across video, social, and written channels — automatically.",
    },
    {
        "icon": "⚙️",
        "title": "Workflow & Systems Integration",
        "stat": "Most companies use dozens of tools that don't talk",
        "short": "Connect your tools, automate cross-platform workflows, and remove operational drag. This is the AI-as-infrastructure play — massive demand.",
    },
    {
        "icon": "📊",
        "title": "Reporting & Analytics Dashboards",
        "stat": "No more waiting on analysts",
        "short": "Auto-generate weekly reports, KPI summaries, and performance dashboards so leadership always has what they need.",
    },
]

HEALTHCARE_SOLUTIONS = [
    {
        "icon": "📞",
        "title": "AI Receptionist & Scheduling",
        "stat": "2–3 missed calls = 2 lost bookings, instantly",
        "short": "AI voice receptionists handle calls, scheduling, and intake 24/7. Never lose a patient appointment to an unanswered phone again.",
    },
    {
        "icon": "🏥",
        "title": "Medical Billing & Coding",
        "stat": "40%+ of hospital costs are administrative",
        "short": "Automate claim submissions, billing, and coding. Reduce errors and denials, and free staff to focus on patient care.",
    },
    {
        "icon": "💌",
        "title": "Patient Reactivation & Follow-Up",
        "stat": "High ROI, low effort once live",
        "short": "Automatically re-engage patients who haven't booked recently via text or email. Set it up once and let it run.",
    },
]

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
    return render_template("index.html")


@app.route("/services")
def services():
    return render_template("services.html", services=SERVICES)


@app.route("/contact")
def contact():
    if request.args.get("sent"):
        flash("Thanks! We'll be in touch within 24 hours. ✨", "success")
    return render_template("contact.html")


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug)
