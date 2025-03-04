import streamlit as st




def get_interview_question(topic, previous_questions=[]):
    """Generates an interview question using Gemini API."""
    prompt = f"""
    Generate an interview question about {topic}.
    Avoid repeating previous questions: {previous_questions}

    Output only the question.
    """
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error: {e}"

def evaluate_answer(question, answer, topic):
    """Evaluates the user's answer using Gemini API."""
    prompt = f"""
    Evaluate the following answer to the interview question about {topic}.
    Provide feedback on the clarity, accuracy, and completeness of the answer.

    Question: {question}
    Answer: {answer}

    Provide feedback in a conversational style.
    """
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error: {e}"

# Streamlit App
def main():
    st.title("AI Interview Preparation Chatbot")

    topic = st.selectbox("Select Interview Topic:", ["Python", "Machine Learning", "Data Science", "Java", "Web Development"])
    if 'previous_questions' not in st.session_state:
        st.session_state.previous_questions = []

    if st.button("Get Question"):
        question = get_interview_question(topic, st.session_state.previous_questions)
        st.session_state.previous_questions.append(question)
        st.session_state.question = question
        st.write(f"**Question:** {question}")
        st.session_state.answer = st.text_area("Your Answer:")
        st.session_state.feedback = ""

    if 'question' in st.session_state and st.session_state.answer:
        if st.button("Submit Answer"):
            feedback = evaluate_answer(st.session_state.question, st.session_state.answer, topic)
            st.session_state.feedback = feedback
            st.write(f"**Feedback:** {feedback}")

    if 'feedback' in st.session_state and st.session_state.feedback:
        st.write(f"**Feedback:** {st.session_state.feedback}")

if __name__ == "__main__":
    main()
