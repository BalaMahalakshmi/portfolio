
# import streamlit as st

# # ---------------- CONFIG ----------------
# st.set_page_config(page_title="Bala Bala Portfolio", page_icon="✨", layout="wide")

# # ---------------- CUSTOM CSS ----------------
# st.markdown(
#     """
#     <style>
#         /* Background gradient */
#         .main {
#             background: linear-gradient(135deg, #0f172a, #1e293b);
#             color: #e2e8f0;
#         }

#         h1, h2, h3, h4 {
#             color: #38bdf8;
#             text-shadow: 2px 2px 8px rgba(0,0,0,0.5);
#         }

#         /* Navbar styling */
#         .navbar {
#             display: flex;
#             justify-content: center;
#             gap: 30px;
#             padding: 15px;
#             background: linear-gradient(90deg, #06b6d4, #3b82f6);
#             border-radius: 15px;
#             margin-bottom: 30px;
#             box-shadow: 0px 5px 20px rgba(0,0,0,0.5);
#         }
#         .nav-item {
#             font-size: 18px;
#             font-weight: bold;
#             color: white;
#             cursor: pointer;
#             padding: 8px 20px;
#             border-radius: 12px;
#             transition: 0.3s;
#         }
#         .nav-item:hover {
#             background: rgba(255,255,255,0.2);
#             transform: translateY(-3px);
#         }
#         .active {
#             background: rgba(255,255,255,0.3);
#             transform: scale(1.1);
#         }

#         /* Card effect for sections */
#         .card {
#             background: rgba(255,255,255,0.05);
#             border-radius: 20px;
#             padding: 20px;
#             margin: 15px 0;
#             box-shadow: 0px 8px 30px rgba(0,0,0,0.5);
#             transition: transform 0.3s;
#         }
#         .card:hover {
#             transform: translateY(-8px) scale(1.02);
#         }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # ---------------- NAVBAR ----------------
# PAGES = ["Home", "About", "Services", "Projects", "Contact"]

# # Custom horizontal menu
# selected_page = st.session_state.get("selected_page", "Home")

# st.markdown('<div class="navbar">' + "".join(
#     [f'<span class="nav-item {"active" if page == selected_page else ""}" '
#      f'onclick="window.location.href=\'#{page.lower()}\'">{page}</span>'
#      for page in PAGES]
# ) + '</div>', unsafe_allow_html=True)

# # ---------------- CONTENT ----------------
# st.markdown(f"<div id='{selected_page.lower()}'></div>", unsafe_allow_html=True)

# if selected_page == "Home":
#     st.title("👋 Hi, I'm Bala Bala")
#     st.subheader("Machine Learning & Generative AI Enthusiast")
#     st.markdown(
#         """
#         <div class="card">
#         I'm passionate about building intelligent systems and deploying real-world AI applications.  
#         I specialize in **Machine Learning, Generative AI, and Data Engineering**, and I love turning ideas into reality.  
#         </div>
#         """, unsafe_allow_html=True)

# elif selected_page == "About":
#     st.title("👨‍💻 About Me")
#     st.markdown(
#         """
#         <div class="card">
#         I have hands-on experience with **scikit-learn, ML algorithms, AI techniques, and data visualization tools**.  
#         I've built strong foundations in **Pandas, NumPy, Matplotlib**, and applied them in real projects.  
#         My learning path has expanded to **Supervised & Unsupervised ML, Generative AI tools, and Streamlit apps**.  
#         </div>
#         """, unsafe_allow_html=True)

# elif selected_page == "Services":
#     st.title("🛠 Internship & Services")
#     st.markdown(
#         """
#         <div class="card">
#         During my internship at <b>Inlighnx Global Pvt. Ltd.</b>, I gained experience in:  
#         - ✅ Implementing ML algorithms (KNN, SVM, Decision Trees, Random Forest, etc.)  
#         - ✅ Practicing data preprocessing with Pandas & NumPy  
#         - ✅ Visualization using Matplotlib  
#         - ✅ Model evaluation (Accuracy, Precision, Recall, F1-score)  
#         - ✅ Building projects with real datasets  
#         </div>
#         """, unsafe_allow_html=True)

# elif selected_page == "Projects":
#     st.title("📂 My Projects")
#     projects = {
#         "Medical Image Classification": "Custom CNN pipelines with Grad-CAM explanations for disease detection.",
#         "Fake News Detection": "NLP-based classification system using TF-IDF + ensemble models.",
#         "AI-based Legacy Data Extraction Tool": "ETL toolkit for noisy legacy formats with ML validation.",
#         "MongoDB CRUD App": "Full-stack app demonstrating create, read, update, and delete operations.",
#     }
#     for name, desc in projects.items():
#         st.markdown(f"<div class='card'><b>{name}</b><br>{desc}</div>", unsafe_allow_html=True)

# elif selected_page == "Contact":
#     st.title("📞 Contact Me")
#     st.markdown(
#         """
#         <div class="card">
#         <b>📧 Email:</b> your.email@example.com  \n
#         <b>📱 Mobile:</b> +91-XXXXXXXXXX  \n
#         <b>🌐 LinkedIn:</b> [linkedin.com/in/yourprofile](https://linkedin.com/in/yourprofile)  \n
#         <b>💻 GitHub:</b> [github.com/your-username](https://github.com/your-username)  
#         </div>
#         """, unsafe_allow_html=True)

import streamlit as st

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Bala Bala Portfolio", page_icon="✨", layout="wide")

# ---------------- CSS ----------------
st.markdown(
    """
    <style>
        body {
            background-color: #0f172a;
            color: #e2e8f0;
            font-family: 'Segoe UI', sans-serif;
        }
        h1, h2, h3 {
            color: #38bdf8;
        }
        /* Navbar */
        .navbar {
            display: flex;
            justify-content: center;
            gap: 30px;
            padding: 15px;
            background: linear-gradient(90deg, #06b6d4, #3b82f6);
            border-radius: 15px;
            margin-bottom: 30px;
            box-shadow: 0px 5px 20px rgba(0,0,0,0.5);
        }
        .nav-item {
            font-size: 18px;
            font-weight: bold;
            color: white;
            cursor: pointer;
            padding: 8px 20px;
            border-radius: 12px;
            transition: 0.3s;
        }
        .nav-item:hover {
            background: rgba(255,255,255,0.2);
        }
        .active {
            background: rgba(255,255,255,0.3);
        }
        /* Card style */
        .card {
            background: rgba(255,255,255,0.05);
            border-radius: 16px;
            padding: 20px;
            margin: 15px 0;
            box-shadow: 0px 8px 30px rgba(0,0,0,0.4);
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- SESSION STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Navbar buttons
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("Home"):
        st.session_state.page = "Home"
with col2:
    if st.button("About"):
        st.session_state.page = "About"
with col3:
    if st.button("Services"):
        st.session_state.page = "Services"
with col4:
    if st.button("Projects"):
        st.session_state.page = "Projects"
with col5:
    if st.button("Contact"):
        st.session_state.page = "Contact"

# ---------------- CONTENT ----------------
if st.session_state.page == "Home":
    st.title("👋 Hi, I'm Bala Bala")
    st.subheader("Machine Learning & Generative AI Engineer")
    st.markdown(
        """
        <div class="card">
        I craft practical **Machine Learning** and **Generative AI** solutions that ship.  
        My expertise spans from **medical imaging pipelines** and **NLP systems** to **end-to-end ETL tools**.  
        With strong foundations in **ML algorithms, data processing, and visualization**, I enjoy turning messy data into reliable products.  
        </div>
        """, unsafe_allow_html=True)

elif st.session_state.page == "About":
    st.title("👨‍💻 About Me")
    st.markdown(
        """
        <div class="card">
        I’m an AI enthusiast with experience in:  
        - ML & AI algorithms (KNN, SVM, Decision Trees, Random Forest)  
        - Libraries: Scikit-learn, PyTorch, Streamlit, Pandas, NumPy  
        - Data visualization with Matplotlib  
        - Building projects in supervised & unsupervised ML  
        </div>
        """, unsafe_allow_html=True)

elif st.session_state.page == "Services":
    st.title("🛠 Internship & Services")
    st.markdown(
        """
        <div class="card">
        Internship at **Inlighnx Global Pvt. Ltd.** where I:  
        - ✅ Implemented and evaluated ML models  
        - ✅ Worked with Pandas, NumPy, and Matplotlib  
        - ✅ Strengthened AI fundamentals with hands-on projects  
        </div>
        """, unsafe_allow_html=True)

elif st.session_state.page == "Projects":
    st.title("📂 My Projects")
    projects = {
        "Medical Image Classification": "Custom CNN pipelines with Grad-CAM explanations for disease detection.",
        "Fake News Detection": "NLP-based system using TF-IDF + ensemble models.",
        "AI-based Legacy Data Extraction Tool": "ETL toolkit for messy legacy formats with ML validation.",
        "MongoDB CRUD App": "Full-stack app showcasing database CRUD with Streamlit.",
    }
    for name, desc in projects.items():
        st.markdown(f"<div class='card'><b>{name}</b><br>{desc}</div>", unsafe_allow_html=True)

elif st.session_state.page == "Contact":
    st.title("📞 Contact Me")
    st.markdown(
        """
        <div class="card">
        📧 **Email:** your.email@example.com  \n
        📱 **Mobile:** +91-XXXXXXXXXX  \n
        🌐 **LinkedIn:** [linkedin.com/in/yourprofile](https://linkedin.com/in/yourprofile)  \n
        💻 **GitHub:** [github.com/your-username](https://github.com/your-username)  
        </div>
        """, unsafe_allow_html=True)

