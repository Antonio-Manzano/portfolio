import streamlit as st

st.set_page_config(
    page_title="Portfolio | Juan Antonio Manzano",
    layout="wide"
)

st.title("Juan Antonio Manzano Ceja")
st.subheader("Information Technology Engineering Student")

st.markdown("""
Information Technology Engineering student at Universidad Politécnica de Victoria with a strong interest in 
software development, data systems, and computational problem solving.

My work focuses on applying programming, database design, and algorithmic logic to build reliable 
software solutions and analytical tools. I have experience working with Python, C++, SQL, and modern 
development tools to design systems that manage and analyze information efficiently.
""")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Areas of Focus")

    st.markdown("""
- Software development and algorithm design  
- Data analysis and computational modeling  
- Database architecture and optimization  
- Backend systems and API development  
- Applied statistics and machine learning
""")

with col2:
    st.markdown("### Technical Stack")

    st.markdown("""
**Programming**

Python  
C++  
Java  
SQL  

**Data and Analytics**

Pandas  
NumPy  
Scikit-learn  
Statsmodels  
Plotly  

**Tools**

Git  
GitHub  
Linux  
Trello  
Jira
""")

st.divider()

st.markdown("### Experience")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
**Robotics Instructor and Project Coordinator**  
Centro Estatal de Tecnología Educativa  
2024 – 2025

- Delivered introductory robotics courses focused on computational logic and programming fundamentals.
- Mentored students through hands-on robotics projects and STEM activities.
- Coordinated curriculum development and task management using agile methodologies.
""")

with col2:
    st.markdown("""
**IT Support Technician**  
Escuela Secundaria General No. 7  
Feb 2021 – Aug 2021

- Maintained and supported more than 30 computer workstations.
- Diagnosed hardware and software issues within laboratory environments.
- Designed and deployed a CCTV surveillance system including cabling and configuration.
""")

st.divider()

st.markdown("### About This Portfolio")

st.markdown("""
This portfolio presents several projects where I apply programming, data analysis, and 
computational logic to real technical problems.

The applications shown here were primarily developed in Python and demonstrate work related to:

- Data analysis and visualization
- Algorithm implementation
- Database design
- Computational modeling
- Software system development

Use the navigation panel on the left to explore the projects and interact with the applications.
""")

st.divider()

st.markdown("""
**Contact**

Email: gracetimesant@gmail.com  
LinkedIn: linkedin.com/in/antonio-manzano-c
""")
