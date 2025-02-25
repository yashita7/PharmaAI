import os
import asyncio
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, LLM
from ocr_agent import OCRAgent
from nlp_agent import NLPAgent
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("Error: GEMINI_API_KEY is not set in the environment variables.")


# Initialize the LLM with the Gemini model
llm = LLM(
    model="gemini/gemini-1.5-pro",
    api_key=GEMINI_API_KEY,
    verbose=True
)

# Initialize OCR and NLP Agents
ocr_agent = OCRAgent()
nlp_agent = NLPAgent()

# Define AI Agent for NLP processing
nlp_ai_agent = Agent(
    name="Pharmacist Assistant",
    role="Medical AI",
    goal="Extract and analyze medical prescriptions using OCR and NLP.",
    backstory="An AI-powered assistant designed to help pharmacists extract and interpret medical information from prescriptions.",
    llm=llm,
    memory=True,
    verbose=True
)

async def process_prescription(image_path):
    """Process a prescription image and analyze the text using NLP."""
    print("🔍 Extracting text from image...")
    extracted_text = ocr_agent.extract_text(image_path)
    print(f"📜 Extracted Text: {extracted_text}\n")

    if not extracted_text:
        return "❌ No text found in the image."

    # Analyze extracted text using NLPAgent
    analysis_result = nlp_agent.analyze_text(" ".join(extracted_text))
    print(f"💊 Medicines Identified: {analysis_result['medicines_identified']}\n")

    # Define a task for the AI agent
    task = Task(
        description=f"Analyze this medical prescription: {extracted_text}",
        agent=nlp_ai_agent,
        expected_output="A structured interpretation of the prescription."
    )

    # Create and execute Crew task
    crew = Crew(
        agents=[nlp_ai_agent],
        tasks=[task]
    )
    result = await crew.kickoff_async()
    print("✅ Analysis Complete.")
    return result.raw

if __name__ == "__main__":
    image_path = input("🖼️ Enter the prescription image path: ")
    result = asyncio.run(process_prescription(image_path))
    print(f"\n🤖 Pharmacist Assistant: {result}")

