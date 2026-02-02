import streamlit as st
import random

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Itumeleng Marule | Mathematics Profile",
    page_icon="📐",
    layout="wide"
)

# -------------------- CUSTOM CSS --------------------
st.markdown(
    """
    <style>
    body {
        background-color: #f5f7fb;
    }
    .main-title {
        font-size: 40px;
        font-weight: 700;
        color: #1f3c88;
    }
    .section-title {
        font-size: 26px;
        font-weight: 600;
        color: #1f3c88;
        margin-top: 30px;
    }
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.08);
        margin-bottom: 20px;
    }
    .highlight {
        color: #ee6c4d;
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------- SIDEBAR --------------------
st.sidebar.title("📌 Navigation")
section = st.sidebar.radio(
    "Go to",
    ["Profile", "Education", "Skills", "Projects & Leadership", "Maths Game 🎮"]
)

st.sidebar.markdown("---")
st.sidebar.write("📧 itumelengtechron90@gmail.com")
st.sidebar.write("📍 Pretoria, South Africa")

# -------------------- MAIN CONTENT --------------------

# PROFILE
if section == "Profile":
    st.markdown("<div class='main-title'>Itumeleng Techron Marule</div>", unsafe_allow_html=True)
    st.write("### Mathematics Honours Student | Science Educator | Community Leader")

    st.markdown(
        """
        <div class='card'>
        I am a <span class='highlight'>motivated and community-focused Mathematics Honours student</span> 
        with a Bachelor of Science in Physical Sciences. I have strong experience in leadership, 
        facilitation, administration, and student governance.
        <br><br>
        My passion lies in <b>science education, youth empowerment</b>, and showing learners that 
        <b>mathematics is logical, fun, and achievable</b>.
        </div>
        """,
        unsafe_allow_html=True
    )

# EDUCATION
elif section == "Education":
    st.markdown("<div class='section-title'>🎓 Education</div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class='card'>
        <b>Sefako Makgatho Health Sciences University (SMU)</b><br>
        • BSc in Physical Sciences – Completed (2024)<br>
        • Honours in Mathematics – In Progress (2025)<br>
        • Mathematics Problem-Solving Course for Facilitators – Completed (2025)
        </div>

        <div class='card'>
        <b>Mshadza Secondary School</b><br>
        • National Senior Certificate – Completed (2018)
        </div>
        """,
        unsafe_allow_html=True
    )

# SKILLS
elif section == "Skills":
    st.markdown("<div class='section-title'>🧠 Skills</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class='card'>
            <b>Technical & Academic</b><br>
            • Scientific & Mathematical Knowledge<br>
            • ICT & Administrative Skills<br>
            • Financial Management<br>
            • Presentation & Facilitation
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class='card'>
            <b>Leadership & Interpersonal</b><br>
            • Community Development<br>
            • Teamwork & Communication<br>
            • Time Management<br>
            • Professional Conduct
            </div>
            """,
            unsafe_allow_html=True
        )

# PROJECTS & LEADERSHIP
elif section == "Projects & Leadership":
    st.markdown("<div class='section-title'>🏆 Projects & Leadership</div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class='card'>
        <b>Mathematics Facilitator – Problem-Solving Course (2025)</b><br>
        • Guided students in mathematical thinking<br>
        • Assisted with planning and assessment
        </div>

        <div class='card'>
        <b>Academic Support Volunteer – SMU (2022–2023)</b><br>
        • Facilitated Physical Sciences & Mathematics study groups<br>
        • Mentored peers
        </div>

        <div class='card'>
        <b>Leadership Roles</b><br>
        • Chairperson – SMU Residence (2022–2023)<br>
        • Treasurer & Secretary – ANC Youth League (SMU)<br>
        • Chairperson – UNASA SMU Chapter
        </div>
        """,
        unsafe_allow_html=True
    )

# -------------------- MATHS GAME --------------------
elif section == "Maths Game 🎮":
    st.markdown("<div class='section-title'>🎮 Fun Maths Challenge</div>", unsafe_allow_html=True)

    st.write("### Let’s prove that **Maths is EASY and FUN!** 😄")
    st.write("Solve the question below:")

    if "a" not in st.session_state:
        st.session_state.a = random.randint(1, 12)
        st.session_state.b = random.randint(1, 12)

    a = st.session_state.a
    b = st.session_state.b

    st.markdown(
        f"<div class='card'><h2>{a} × {b} = ?</h2></div>",
        unsafe_allow_html=True
    )

    answer = st.number_input("Your answer", step=1)

    if st.button("Check Answer"):
        if answer == a * b:
            st.success("🎉 Correct! You ARE good at maths!")
            st.session_state.a = random.randint(1, 12)
            st.session_state.b = random.randint(1, 12)
        else:
            st.error("❌ Not quite. Try again — you’re learning!")

    st.markdown(
        """
        <div class='card'>
        <b>Why this matters:</b><br>
        Mathematics is about practice and confidence. 
        The more you try, the easier it becomes. 
        <br><br>
        <i>Everyone can do maths.</i>
        </div>
        """,
        unsafe_allow_html=True
    )
