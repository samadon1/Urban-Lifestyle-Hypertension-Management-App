import streamlit as st
import pandas as pd
import altair as alt
import random

# Mock data
bp_data = pd.DataFrame({
    'date': pd.date_range(start='2023-10-01', periods=30, freq='D'),
    'systolic': [random.randint(120, 140) for _ in range(30)],
    'diastolic': [random.randint(70, 90) for _ in range(30)]
})

companion_messages = [
    "Great job on your walk yesterday! Your BP is showing improvement.",
    "I noticed you've been logging more stress lately. Would you like to try a quick breathing exercise?",
    "Your food diary shows increased salt intake. Let's look at some low-sodium alternatives for your favorite foods.",
    "You've been consistent with your medication. Keep up the good work!",
    "How about we set a goal to reduce your sodium intake this week?",
]

def main():
    st.title("Urban Lifestyle BP Manager")

    # Sidebar for user input
    st.sidebar.header("Your Daily Log")
    activity = st.sidebar.number_input("Minutes of activity today", 0, 300, 30)
    stress_level = st.sidebar.slider("Stress level today", 1, 10, 5)
    salt_intake = st.sidebar.selectbox("Salt intake today", ["Low", "Medium", "High"])

    # Main app layout
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Your BP Trend")
        chart = alt.Chart(bp_data).mark_line().encode(
            x='date:T',
            y='systolic:Q',
            color=alt.value("#8884d8")
        ).properties(width=500, height=300)
        
        chart += alt.Chart(bp_data).mark_line().encode(
            x='date:T',
            y='diastolic:Q',
            color=alt.value("#82ca9d")
        )
        
        st.altair_chart(chart)

    with col2:
        st.subheader("AI Companion")
        if st.button("Chat with AI Companion"):
            message = random.choice(companion_messages)
            st.info(message)

    # Features
    st.subheader("Features")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Set Reminders"):
            st.success("Reminder set for a 10-minute walk at 6 PM!")
    with col2:
        if st.button("Log Activity"):
            st.success(f"Logged {activity} minutes of activity.")
    with col3:
        if st.button("Food Diary"):
            st.success(f"Logged salt intake as {salt_intake}.")

    # Stress Journal
    st.subheader("Stress Journal")
    stress_note = st.text_area("How are you feeling today?")
    if st.button("Save Journal Entry"):
        st.success("Journal entry saved!")

    # About AI Companion
    st.subheader("About Your AI Companion")
    st.write("""
    Your AI companion uses advanced machine learning to analyze your data and provide personalized advice. 
    It adapts to your unique lifestyle challenges in urban Ghana, offering tailored support for managing hypertension.
    """)

if __name__ == "__main__":
    main()
