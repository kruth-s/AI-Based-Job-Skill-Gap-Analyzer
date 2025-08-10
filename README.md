# AI-Based Job Skill Gap Analyzer

## Overview
An advanced AI-powered EdTech platform that evaluates a student’s technical and soft skills against current industry requirements, identifies gaps, and recommends targeted, personalized learning paths. Designed to bridge the gap between academic learning and real-world job market needs.

---

## Key Features

### 1. Automated Skill Extraction
- Leverages **spaCy** and **BERT** to accurately extract skills from LinkedIn, GitHub profiles, and uploaded resumes.

### 2. Industry Demand Analysis
- Aggregates and analyzes job postings (scraped from LinkedIn) to identify trending skills, technologies, and emerging industry requirements.

### 3. Skill Gap Detection
- Compares a user’s skill set with requirements for target roles and identifies missing competencies.

### 4. Personalized Learning Path
- Maps missing skills to relevant online courses and training materials from **Coursera**, **edX**, **Udemy**, and **O*NET** resources.

---

## Technology Stack

| Layer           | Technologies Used |
|-----------------|-------------------|
| **Backend**     | Python, FastAPI |
| **NLP**         | spaCy, BERT (HuggingFace Transformers) |
| **Data Processing** | Pandas, NumPy |
| **Web Scraping** | BeautifulSoup, Selenium (LinkedIn job postings) |
| **Database**    | PostgreSQL / MongoDB |
| **Frontend**    | React.js / Next.js |
| **Deployment**  | Docker, AWS EC2/S3 |

---

## Dataset Sources
- **O*NET** — Comprehensive skills and job role dataset
- **LinkedIn Job Postings** — Scraped using Selenium
- **Sample Student Profiles** — Sourced from LinkedIn, GitHub, and mock resumes

---

## MVP Workflow

1. **Profile Upload** — User provides LinkedIn, GitHub profile, or resume file.  
2. **Skill Extraction** — NLP model parses and detects skills.  
3. **Industry Demand Analysis** — Fetches and processes real-time job postings.  
4. **Gap Analysis** — Compares extracted skills with job requirements.  
5. **Recommendation Generation** — Produces a personalized learning roadmap.  

---

## Testing & Evaluation
- Conducted with diverse student and graduate profiles.  
- Achieved ~85% accuracy in skill detection and recommendation mapping.  
- Continuous improvement through real-world feedback from job application outcomes.  

---

## Future Enhancements
- Integration with **LinkedIn** and **Coursera** APIs for real-time updates.  
- Interactive user dashboards with skill progress tracking.  
- Multilingual NLP support for global reach.  

---

## System Architecture

```mermaid
flowchart TD
    A[Profile Upload (LinkedIn / GitHub / Resume)] --> B[Skill Extraction (spaCy / BERT)]
    B --> C[Industry Demand Analysis (LinkedIn Scraper)]
    C --> D[Gap Analysis Engine]
    D --> E[Recommendation Engine]
    E --> F[Personalized Learning Path Output]
```

---

## License
Licensed under the **MIT License** — free to use, modify, and distribute with attribution.
