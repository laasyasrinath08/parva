# PARVA 🌱
### Age-Aware Learning for Safer, Clearer Education

> **Filter first. Teach clearly. Check understanding. Show progress.**

PARVA is an age-aware learning application designed to provide sensitive educational content through a safer and clearer learning journey.

The application routes learners into age-appropriate content based on their readiness, provides animated lessons, checks understanding through quizzes, and tracks learning progress.

---

## 🎯 Problem Statement

Children and teenagers need educational content that matches their age and readiness.

Sensitive topics can become difficult to understand when the language, examples, and level of responsibility are not appropriate for the learner.

PARVA addresses this problem by filtering educational content before teaching begins and creating a guided learning journey for each learner.

---

## 💡 Our Solution

PARVA follows a simple learning loop:

**Age → Learning Check → Age Band → Filtered Lesson → Quiz → Feedback → Next Lesson**

Instead of showing the same content to everyone, PARVA provides different learning experiences based on age groups.

---

## 👥 Age-Based Learning

| Age Group | Learning Focus |
|-----------|----------------|
| Up to 7 | Kindness |
| 8–11 | Puberty & Body Awareness |
| 12–15 | Menstruation, Consent & Harassment Awareness |
| 16–18 | Laws, Digital Safety & Relationships |
| 18+ | Adult Legal Awareness |

The goal is to make the language, examples, and responsibility level suitable for the learner.

---

## 📱 MVP – Seven Screen Experience

The initial PARVA prototype contains seven major screens:

1. **Welcome Screen**
   - Introduces the guided learning journey.

2. **Age Selection**
   - Selects the appropriate learning band.

3. **Math / Logic Check**
   - Used as an access or learning signal.
   - It is NOT true age verification.

4. **Learning Dashboard**
   - Shows the learner's next lesson and learning path.

5. **Animated Lesson**
   - Explains one sensitive concept in a simple way.

6. **Three-Question Quiz**
   - Checks recall and understanding.

7. **Score, Feedback & Badge**
   - Provides immediate feedback and motivates the learner to continue.

---

## 🎬 Animation Approach

PARVA uses simple and engaging animations to make difficult topics easier to understand.

Each animation focuses on:

- One concept
- One action
- One takeaway

The prototype can begin with **3–5 short animations**, with examples prioritized for different age bands.

---

## 🔄 Learning Flow

```text
        ┌───────────────┐
        │ Age Selection │
        └───────┬───────┘
                ↓
        ┌────────────────┐
        │ Learning Check │
        └───────┬────────┘
                ↓
        ┌───────────────┐
        │ Age Filtering │
        └───────┬───────┘
                ↓
        ┌────────────────┐
        │ Animated Lesson│
        └───────┬────────┘
                ↓
        ┌───────────────┐
        │     Quiz      │
        └───────┬───────┘
                ↓
        ┌──────────────────┐
        │ Feedback & Badge │
        └───────┬──────────┘
                ↓
          Next Lesson
