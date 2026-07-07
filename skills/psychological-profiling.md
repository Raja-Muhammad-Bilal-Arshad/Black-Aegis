---
name: psychological-profiling
description: Target profiling, pretext development, social engineering psychology.
---

# Psychological Profiling for Social Engineering

## 1. Target Profiling Framework

### OSINT Collection
| Source | Information Gained |
|--------|--------------------|
| LinkedIn | Job role, skills, connections, company structure |
| Facebook/Instagram | Interests, family, travel, habits |
| Twitter/X | Opinions, complaints, location |
| Company website | Org chart, press releases, culture |
| Glassdoor | Employee sentiment, internal issues |
| WHOIS/DNS | Technical infrastructure, contacts |

### Personality Assessment
| Trait | Indicator | Exploit Vector |
|-------|-----------|----------------|
| Agreeableness | Helpful, trusting | Help desk impersonation |
| Conscientiousness | Rule-following | Authority impersonation |
| Extraversion | Talkative, social | Befriending, pretexting |
| Neuroticism | Anxious, stressed | Urgency/fear tactics |
| Openness | Curious, creative | Novelty/baiting |

## 2. Pretext Development

### Authority Pretext
```python
pretext = {
    "role": "IT Support",
    "urgency": "Critical security patch",
    "authority": "CISO directive",
    "deadline": "End of business today",
    "fallback": "Escalation to management"
}
```

### Urgency/Fear Pretext
```python
pretext = {
    "scenario": "Account compromise detected",
    "action_required": "Verify credentials immediately",
    "consequence": "Account will be locked",
    "trust_builder": "Reference real security team member"
}
```

### Befriending Pretext
```python
pretext = {
    "approach": "Common interest (hobby, team)",
    "duration": "Build over weeks",
    "goal": "Physical access or credential sharing",
    "channels": "Social media, in-person, email"
}
```

## 3. Phishing Psychology

### Emotional Triggers
| Trigger | Example | Effect |
|---------|---------|--------|
| Fear | "Your account is compromised" | Immediate action |
| Urgency | "Act within 24 hours" | Bypasses critical thinking |
| Curiosity | "See who viewed your profile" | Clicks link |
| Greed | "You've won a prize" | Provides info |
| Authority | "From: CEO" | Compliance |
| Social proof | "500 colleagues already updated" | Follows crowd |

### Anti-Phishing Indicators to Include in Reports
- Generic greetings ("Dear User")
- Mismatched URLs
- Urgency without verification
- Unexpected attachments
- Slight domain variations

## 4. Vishing Scripts

```
Script Template:
1. Introduction: Name + Company (borrowed authority)
2. Reason for call: Reference a real event/ticket
3. Verification: Ask them to verify NON-sensitive info first
4. Escalation: Request sensitive info as "required step"
5. Closing: Thank them + confirm process started
```

## 5. Physical Social Engineering

### Entry Techniques
- Follow authorized personnel through doors
- Carry packages (hands full = door held open)
- Wear branded clothing (fake vendor)
- Use phone call as distraction

### Elicitation
- Ask open-ended questions
- Show genuine interest
- Use silence effectively
- Mirror their language

## 6. Defense & Awareness

### Training Topics
- Recognizing authority impersonation
- Verifying requests through separate channels
- Understanding emotional manipulation
- Reporting suspicious contacts
- Clean desk/screen policies
