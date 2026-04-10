from google.adk.agents import LlmAgent, SequentialAgent
from . import prompt_for_resume

GEMINI_MODEL = "gemini-2.5-flash"


resume_extraction_agent = LlmAgent(
    name="Resume_Extraction_Agent",
    model=GEMINI_MODEL,
    instruction=prompt_for_resume.prompt,
    output_key="extracted_resume_data"
)

role_suggestion_agent = LlmAgent(
    name="Role_Suggestion_Agent",
    model=GEMINI_MODEL,
    instruction="You are a role suggestion assistant. Based on the extracted resume data refering to {extracted_resume_data}, suggest 2-4 job roles that best match the candidate's skills and experience. Provide a brief justification for each suggested role.",
    output_key="suggested_roles"
)

job_search_agent = LlmAgent(
    name="Job_Search_Agent",
    model=GEMINI_MODEL,
    instruction="You are a job search assistant. Based on the suggested roles refering to {suggested_roles}, search for available job openings that match the candidate's qualifications and experience. Provide a list of recommended jobs with descriptions and application instructions.",
    output_key="recommended_jobs"
)

interview_questions_agent = LlmAgent(
    name="Interview_Questions_Agent",
    model=GEMINI_MODEL,
    instruction="You are an interview preparation assistant. Based on the suggested roles refering to {suggested_roles} and skills from {extracted_resume_data}, generate a list of common interview questions that the candidate might encounter for each suggested role. Provide a mix of technical and behavioral questions.",
    output_key="interview_questions"
)

interview_tips_agent = LlmAgent(
    name="Interview_Tips_Agent",
    model=GEMINI_MODEL,
    instruction="You are an interview coaching assistant. Based on the suggested roles refering to {suggested_roles} and skills from {extracted_resume_data}, provide personalized interview tips and strategies for the candidate. Include advice on how to highlight their strengths, address potential weaknesses, and make a strong impression during interviews.",
    output_key="interview_tips"
)


job_finder_agent = SequentialAgent(
    name="Job_Finder_Agent",
    sub_agents=[resume_extraction_agent, role_suggestion_agent, job_search_agent, interview_questions_agent, interview_tips_agent]
)


root_agent = job_finder_agent