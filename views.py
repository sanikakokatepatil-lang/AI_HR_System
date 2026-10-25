from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Job, Candidate

def ai_score_calculator(resume_text, required_skills):
    resume_lower = resume_text.lower()
    skills = [s.strip().lower() for s in required_skills.split(',')]
    score = 0
    matched = []
    for skill in skills:
        if skill and skill in resume_lower:
            score += 25
            matched.append(skill)
    if score > 100: score = 95
    if score == 0: score = 10
    feedback = f"Matched Skills: {', '.join(matched) if matched else 'None'}"
    return score, feedback

def home(request):
    jobs = Job.objects.all()
    return render(request, 'hr/home.html', {'jobs': jobs})

def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        resume_text = request.POST['resume_text']
        score, feedback = ai_score_calculator(resume_text, job.required_skills)
        Candidate.objects.create(job=job, name=name, email=email, resume_text=resume_text, ai_score=score, ai_feedback=feedback)
        return render(request, 'hr/result.html', {'score': score, 'feedback': feedback, 'job': job, 'name': name})
    return render(request, 'hr/apply.html', {'job': job})