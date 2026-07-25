# Smart Study Buddy - AI Powered Study Material Generator

## Application Preview

**Home Page - Topic Input and Study Kit Overview**
![Home Page]<img width="1903" height="907" alt="SS1" src="https://github.com/user-attachments/assets/e45e7794-42d6-47f6-a9cc-c5bf9fdce62d" />


**Generated Explanation**
![Explanation]<img width="1900" height="907" alt="SS2" src="https://github.com/user-attachments/assets/5df7a777-7976-4f08-b2b9-260760b0ff89" />


**Real-Life Example and MCQs**
![MCQs]<img width="1902" height="900" alt="SS3" src="https://github.com/user-attachments/assets/bfbb0105-c30c-4617-b6f9-8667ecefda9c" />


**Interview Questions and Summary**
![Interview Questions and Summary]<img width="1892" height="907" alt="SS4" src="https://github.com/user-attachments/assets/6ccb9f12-c1b8-45b7-96bc-8258574d387a" />


## Project Overview

Smart Study Buddy is an AI-powered educational assistant that automatically generates complete study material using Google Gemini, LangChain, and Streamlit.

Instead of manually searching multiple websites or books, users simply enter a topic and select a difficulty level. The application instantly generates structured study notes including an explanation, examples, MCQs, interview questions, and a concise summary.

The project demonstrates practical implementation of Generative AI, Prompt Engineering, and Large Language Models (LLMs) to improve the learning experience.

## Business Problem

Students often spend significant time searching different websites, YouTube videos, blogs, and books to prepare study material for a single topic.

Common challenges include:

- Information scattered across multiple sources
- Time-consuming note preparation
- Lack of structured learning material
- Difficulty preparing interview questions
- Limited practice MCQs
- Inconsistent explanations

This project solves these problems by generating complete learning resources in one place using Generative AI.

## Objectives

The project aims to:

- Generate complete study notes using AI
- Support multiple difficulty levels
- Create beginner-friendly explanations
- Provide practical examples
- Generate interview preparation questions
- Generate multiple-choice questions automatically
- Summarize topics into quick revision notes
- Improve learning productivity

## Key Features

- AI-powered study material generation
- Google Gemini LLM integration
- Difficulty selection (Easy, Medium, Hard)
- Topic-based content generation
- Detailed explanations
- Simple examples
- Real-world examples
- Automatically generated MCQs
- Interview questions
- Topic summaries
- Clean and responsive Streamlit interface

## Application Workflow

**Step 1** - User enters a topic.
Example: `Gen AI`

**Step 2** - Select the difficulty level.
Options: Easy, Medium, Hard

**Step 3** - Click "Generate Study Material"

**Step 4** - LangChain builds a structured prompt.

**Step 5** - Prompt is sent to Google Gemini.

**Step 6** - Gemini generates:
- Explanation
- Simple Example
- Real-Life Example
- 5 MCQs
- 5 Interview Questions
- Summary

**Step 7** - Results are displayed in the Streamlit interface.

## AI Workflow

```
User
  |
  v
Streamlit UI
  |
  v
LangChain Prompt
  |
  v
Google Gemini API
  |
  v
AI Generated Study Material
  |
  v
Streamlit Output
```

## Prompt Engineering

The application uses a LangChain PromptTemplate to instruct Gemini to generate structured educational content.

The prompt asks the model to generate:

- Explanation
- Simple Example
- Real-Life Example
- 5 MCQs
- 5 Interview Questions
- Summary

This ensures consistent and well-organized responses.

## Technologies Used

| Category | Technology |
|---|---|
| Programming Language | Python |
| Framework | Streamlit |
| LLM | Google Gemini |
| AI Framework | LangChain |
| Environment Management | python-dotenv |

## Project Structure

```
Smart_Study_Buddy/
├── app.py
├── requirements.txt
├── .env.example
├── README.md
└── images/
    ├── ssb1.png
    ├── ssb2.png
    ├── ssb3.png
    └── ssb4.png
```

## Installation

1. Clone the repository
   ```bash
   git clone https://github.com/<your-username>/Smart-Study-Buddy.git
   ```

2. Move into the project directory
   ```bash
   cd Smart-Study-Buddy
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file
   ```
   GOOGLE_API_KEY=your_gemini_api_key_here
   ```

5. Run the application
   ```bash
   streamlit run app.py
   ```

## Example Output

The application generates:

- Detailed topic explanation
- Beginner-friendly examples
- Real-world examples
- Five MCQs with answers
- Five interview questions
- Topic summary

All content is generated dynamically using Google Gemini.

## Skills Demonstrated

This project demonstrates practical knowledge of:

- Generative AI
- Large Language Models (LLMs)
- Google Gemini API
- LangChain
- Prompt Engineering
- Streamlit Development
- Python Programming
- AI Application Development
- Environment Variable Management
- User Interface Design

## Business Applications

This project can be used for:

- AI Learning Platforms
- EdTech Applications
- Online Coaching
- Student Learning Assistants
- Corporate Training
- Interview Preparation
- AI Tutors
- Educational Chatbots
- Personalized Learning Systems

## Future Improvements

- PDF Notes Export
- Quiz Timer
- Voice-based Learning
- Multi-language Support
- Learning Progress Tracking
- User Authentication
- Chat History
- Dark and Light Themes
- Mobile Responsive Design

## License

This project is developed for educational and portfolio purposes.

## Author

**Dev Patel**
