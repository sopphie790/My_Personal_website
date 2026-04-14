import streamlit as st


st.set_page_config(
    page_title="My Portfolio Dashboard",
    page_icon="💼",
    layout="wide"
)
st.markdown("""
<style>

/* =========================
   PREMIUM ANIMATED BACKGROUND
========================= */
.stApp {
    background: linear-gradient(-45deg, #ffe6f2, #f3e8ff, #e6f7ff, #fff7e6);
    background-size: 400% 400%;
    animation: gradientMove 15s ease infinite;
}

@keyframes gradientMove {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* =========================
   GLASSMORPHISM MAIN CONTAINER
========================= */
.block-container {
    padding: 2rem;
    border-radius: 20px;
    background: rgba(255, 255, 255, 0.65);
    backdrop-filter: blur(12px);
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
}

/* =========================
   SIDEBAR PREMIUM LOOK
========================= */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #ffd6e8, #e9d5ff);
    border-right: 2px solid rgba(255,255,255,0.3);
}

/* =========================
   TYPOGRAPHY (CLEAN + PROFESSIONAL)
========================= */
html, body, [class*="css"] {
    font-family: "Times New Roman", serif;
    color: #2f2f2f;
}

/* HEADINGS */
h1, h2, h3 {
    color: #4b1f4f;
    font-weight: bold;
    letter-spacing: 0.5px;
}

/* =========================
   PREMIUM CARDS STYLE
========================= */
div.stContainer {
    background: rgba(255,255,255,0.75);
    border-radius: 16px;
    padding: 18px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.06);
    border: 1px solid rgba(255,255,255,0.4);
    transition: 0.3s ease;
}

div.stContainer:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
}

/* =========================
   BUTTON PREMIUM STYLE
========================= */
button[kind="primary"] {
    background: linear-gradient(90deg, #ff7eb3, #a78bfa);
    border-radius: 12px;
    border: none;
    color: white;
    font-weight: bold;
    padding: 0.5rem 1rem;
}

button[kind="primary"]:hover {
    transform: scale(1.05);
    transition: 0.2s ease;
}

/* =========================
   🟣 3D IMAGE ANIMATION (NEW ADD)
========================= */

.img-3d {
    width: 100%;
    border-radius: 15px;
    transition: transform 0.5s ease, box-shadow 0.5s ease;
    transform-style: preserve-3d;
}

/* 3D HOVER EFFECT */
.img-3d:hover {
    transform: perspective(1000px) rotateY(10deg) rotateX(5deg) scale(1.05);
    box-shadow: 0 20px 40px rgba(0,0,0,0.25);
}

/* FLOAT ANIMATION */
@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
    100% { transform: translateY(0px); }
}

.float-card {
    animation: float 4s ease-in-out infinite;
}

/* =========================
   REMOVE STREAMLIT DEFAULT UI
========================= */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

</style>
""", unsafe_allow_html=True)
# =========================
# SIDEBAR NAVIGATION
# =========================
st.sidebar.title("📌 Navigation")

menu = st.sidebar.radio(
    "Go to:",
    ["🏠 Home", "🧑 About", "⚡ Skills", "📁 Projects", "📬 Contact"]
)

# =========================
# HOME
# =========================
if menu == "🏠 Home":
    st.title("🏠 Home")

    st.image("profile.png", width=300)
    st.title("👨‍💻 Hi! I'm Liza Jaime")
    st.write("Student Developer | Designer | Administrative Virtual Assistant | Photo Editor")
    

    st.write("""
Welcome to my portfolio dashboard.

I am a passionate and driven BS Computer Science student with strong interest in both technology and creative digital services. My experiences have helped me develop skills not only in programming, but also in client-based and creative work.

I am passionate about:

- 💻 Web Development and System Development (building functional and user-friendly systems)
- 🎨 UI/UX Design (creating clean, modern, and professional interfaces)
- ⚙️ Backend & Database Systems (developing structured and efficient applications)
- 🧑‍💼 Virtual Assistance & Client Support (handling real client tasks and communication)
- 🎨 Graphic Design & Logo Creation (branding and creative visual design)
- ✨ Photo Editing & Digital Enhancement (improving visual content quality)
- 🎤 Online Leadership & Community Management (StarMaker team leadership experience)

I continuously aim to improve my skills, gain real-world experience, and grow as a future full-stack developer and digital professional.
""")

    st.success("Explore my profile using the sidebar 👈")

# =========================
# ABOUT
# =========================
elif menu == "🧑 About":
    st.title("🧑 About Me")

    st.write("""
    I am a Bachelor of Science in Computer Science student passionate about building
    real-world systems and creative digital services.
    """)

    st.subheader("🎓 Education")
    st.write("**College**  \nDr. Emilio B. Espinosa Sr. Memorial State College of Agriculture and Technology (DEBESMSCAT)  \nCourse: Bachelor of Science in Computer Science")

    st.write("**Senior High School**  \nNabongsoran High School  \nSchool Year: 2022–2023")

    st.write("**Junior High School**  \nLuy-a Nationalized High School  \nSchool Year: 2008–2009")

    st.write("**Elementary**  \nNabongsoran Elementary School  \nSchool Year: 2003–2004")

    st.subheader("🎯 Goals")

    st.write("""
My primary goal is to grow as a highly skilled and versatile Computer Science professional by combining both technical development and creative design expertise.

Specifically, I aim to:

- Become a Full-Stack Developer capable of building complete, scalable, and functional web systems
- Develop and deploy real-world systems such as Barangay Management Systems, Web Applications, and Data Management Platforms
- Strengthen my UI/UX Design skills to create modern, user-friendly, and visually appealing interfaces
- Enhance my backend development and database management skills for efficient system performance
- Gain more real-world experience in freelancing, client-based projects, and digital services
- Continue improving my skills in digital creativity such as logo design, photo editing, and branding
- Build a strong professional portfolio that showcases my growth as a developer and designer

My long-term vision is to become a professional full-stack developer and digital solutions creator who builds impactful systems for communities and businesses.
""")
    st.subheader("💼 Experiences")

    st.write("""
- Virtual Assistant (US Client) – Handled administrative tasks, client communication, data entry, and task management under a real international contract experience.
- Photo Editing Services – Provided creative photo enhancement services for clients including family portraits, weddings, graduations, debuts, posters, and digital designs across different locations.
- Logo Design & Branding Services – Created custom logos for small businesses and personal brands, improving skills in visual identity, typography, and digital branding.
- Online Team Leadership (StarMaker) – Started as a team member and later became a Team Captain, managing a group, setting rules, organizing activities, and leading participation in online singing competitions.
- Freelance Digital Services – Gained experience working with clients in various digital tasks including editing, design, and online assistance.
- Client-Based Project Experience – Worked with real clients locally and internationally, improving communication, time management, and professional workflow handling.
- Administrative & Communication Experience – Developed strong organizational and communication skills through virtual assistant work and online coordination tasks.
- Digital Content Creation – Engaged in creating visual and digital content for personal and client use, enhancing creativity and technical design skills.
""")

    st.subheader("🏆 Certificates & Achievements")

    st.write("""
- Completed certifications in HTML Essentials, CSS Essentials, and Computer Hardware Basics through Cisco Networking Academy and JS Institute  
- Completed Online Training / Courses from various learning platforms focused on digital skills and web development  
- Earned certificates in Digital Skills and Freelancing fundamentals  
- Recognized Online Team Leader in the StarMaker Community  
- Achieved milestones in Photo Editing & Design Services  
- Successfully completed Web Development academic certifications and project-based learning requirements  
""")
# =========================
# SKILLS
# =========================
elif menu == "⚡ Skills":
    st.title("⚡ Skills")

    st.subheader("💻 Programming")
    st.write("Python")
    st.progress(85)

    st.write("HTML/CSS")
    st.progress(80)

    st.write("JavaScript")
    st.progress(70)

    st.subheader("🎨 Design")
    st.write("UI/UX Design")
    st.progress(80)

    st.write("Canva / Editing")
    st.progress(90)

    st.subheader("🛠 Tools")
    st.write("- Streamlit")
    st.write("- GitHub")
    st.write("- VS Code")

# =========================
# PROJECTS
# =========================
elif menu == "📁 Projects":
    st.title("📁 Projects & Experience")

    # ======================
    # PROJECT 1
    # ======================
    st.image("BIMS.png", use_container_width=True)
    st.subheader("🏢Barangay Information Management System")

    st.write("The Barangay Information Management System is a web-based project I developed during my first year in college under Sir Marlon Hermoso. It is designed to manage resident data and basic barangay services. I later enhanced the system by improving its UI/UX design, making it more modern, user-friendly, and visually appealing. This project reflects my growth and passion as a future web developer.")

    st.markdown("---")

    # ======================
    # PROJECT 2
    # ======================
    st.image("LOGO.png", use_container_width=True)
    st.subheader("🎨 Logo Design – Jasmine Boutique")

    st.write("When I first started designing logos, I found the process time-consuming and challenging, especially in achieving a clean and professional look. Created branding logo and improved my design and creativity skills through practice. ")


    st.markdown("---")

    # ======================
    # PROJECT 3
    # ======================
    st.image("PORTRAIT.jpg", use_container_width=True)
    st.subheader("🎨 Photo Editing Services")
    st.write("After completing my contract as an Administrative Virtual Assistant, I focused on photo editing, starting with clients in Barangay Nabongsoran. I handled various projects such as family portraits, weddings, graduations, debuts, and poster designs. What began as a small opportunity grew into serving clients from different barangays, municipalities, and even abroad.As a student, mother, and wife, I learned to manage my time effectively while balancing my responsibilities. Photo editing has become not just a source of income, but a true passion that allows me to support my family.")
    st.markdown("---")

    # ======================
    # PROJECT 4
    # ======================
    st.image("VA.png", use_container_width=True)
    st.subheader("💼 Administrative Virtual Assistant Experience")

    st.write("I began my journey as an Administrative Virtual Assistant on December 26 after persistently applying to multiple job opportunities. Despite facing many rejections, I remained determined and gained valuable experience through numerous interviews. Eventually, I secured my first client from Los Angeles, California, where I worked under a one-month contract. This experience allowed me to apply my administrative skills in a real-world setting and marked a significant milestone in my career, earning my first professional income of ₱29,000.")
    # ======================
    # PROJECT 5
    # ======================
    st.image("STARMAKER.png", use_container_width=True)
    st.subheader("🎤 StarMaker Agent Experience (2019)")
    st.write("""In 2019, I had my first opportunity to gain online exposure and earnings through the StarMaker platform. What I initially thought was simply an app for singing, chatting, and games turned out to offer various opportunities for growth and income. I started as a regular team member and eventually built and led my own group as a Team Captain, where I established guidelines, encouraged collaboration, and actively participated in singing competitions. Our team fostered a supportive environment, helping each member grow and stay engaged. Motivated by this experience, I applied to become an official StarMaker Agent, which required completing several tasks and passing a live interview conducted within the platform. After successfully meeting all requirements, I was formally accepted as an agent under the codename "Sopphie Lee."
    This experience enhanced my leadership, communication, and online management skills, marking an important step in my early digital career journey.""")

    st.markdown("---")
    # ======================
    # PROJECT 6
    # ======================
    st.image("CERTIFICATE.jpg", use_container_width=True)
    st.subheader("🏆 Best in Frontend Development – Web Development Hackathon 2025")

    st.write("""I was awarded Best in Frontend Development during the Web Development Hackathon 2025 (Season 3) in recognition of my outstanding performance, consistency, and dedication in web programming.
    This achievement reflects my ability to design and develop user-friendly, visually appealing, and functional interfaces while maintaining a high level of task completion and quality.
    This milestone highlights my growing expertise in frontend development and strengthens my commitment to continuously improving my skills as a future web developer.""")

    st.info("✨ Awarded for excellence in UI/UX design and frontend development.")

    st.markdown("---")
    # ======================
    # PROJECT 7
    # ======================
    st.image("CERTIFICATE1.png", use_container_width=True)
    st.subheader("🤖 ChatGPT 101 Certification – Simplilearn SkillUp")

    st.write("""On March 25, 2026, I achieved a new milestone by completing the ChatGPT 101 course through Simplilearn SkillUp. This experience introduced me to the world of generative AI, helping me understand how AI models work and how they can enhance productivity and creativity in real-world applications.
    Completing this program (Certificate Code: 10002111) reflects my commitment to continuous learning, adapting to emerging technologies, and staying aligned with the evolving digital landscape.""")

    st.info("✨ Strengthened my knowledge in AI tools and modern digital workflows.")

    st.markdown("---")
    # ======================
    # PROJECT 8
    # ======================
    st.image("CERTIFICATE2.png", use_container_width=True)
    st.subheader("🤖 AI Agents for Beginners Certification – Simplilearn SkillUp")

    st.write("""On March 25, 2026, I took another important step in my AI journey by completing the AI Agents for Beginners course through Simplilearn SkillUp. This experience allowed me to explore the concept of autonomous AI systems and understand how intelligent agents can be designed to perform tasks and solve problems independently.
    Earning this certification (Certificate Code: 10002060) strengthened my technical foundation and reflects my commitment to staying at the forefront of innovation. More than just a credential, this achievement represents my continuous growth and passion for mastering emerging technologies that shape the future.""")

    st.info("✨ Expanded my knowledge in AI systems and autonomous technologies.")

    st.markdown("---")
    # ======================
    # PROJECT 9
    # ======================
    st.image("CERTIFICATE3.png", use_container_width=True)
    st.subheader("🤖 Artificial Intelligence Beginners Guide Certification – Simplilearn SkillUp")

    st.write("""On March 25, 2026, I completed the Artificial Intelligence Beginners Guide through Simplilearn SkillUp, marking the final milestone in my foundational AI learning journey. This course provided a comprehensive understanding of how AI systems function, including their real-world applications and the ethical considerations behind them.
    Earning this third certification (Certificate Code: 10005143) strengthened my confidence in navigating modern technologies and deepened my overall perspective on artificial intelligence. This achievement reflects my persistence in mastering complex concepts and my commitment to continuously evolving alongside the rapidly advancing digital landscape.""")

    st.success("🚀 Completed a strong foundation in Artificial Intelligence and emerging technologies.")

    st.markdown("---")
    # ======================
    # PROJECT 10
    # ======================
    st.image("CERTIFICATE4.png", use_container_width=True)
    st.subheader("🤖 Prompt Engineering Applications Certification – Simplilearn SkillUp")

    st.write("""On March 25, 2026, I completed the Prompt Engineering Applications course through Simplilearn SkillUp, marking a significant turning point in my AI learning journey. This experience allowed me to go beyond simply using AI tools and develop the ability to effectively communicate with them. I learned how precise and well-structured prompts can unlock the full potential of generative AI systems.
    Earning this certification (Certificate Code: 10002610) reflects my transition from a beginner to a more skilled practitioner capable of applying AI in real-world scenarios. This achievement highlights my commitment to continuously enhancing my technical expertise and staying at the forefront of emerging technologies.""")

    st.success("🚀 Developed strong skills in prompt engineering and AI interaction.")

    st.markdown("---")
    # ======================
    # PROJECT 11
    # ======================
    st.image("CERTIFICATE5.png", use_container_width=True)
    st.subheader("🐍 Python for Beginners Certification – Simplilearn SkillUp")

    st.write("""On March 26, 2026, I earned my certification in Python for Beginners through Simplilearn SkillUp, marking an important step in my transition into programming. While my previous focus was on AI tools, this course allowed me to understand the core programming concepts behind modern technologies. I developed foundational skills in coding, problem-solving, and logical thinking using Python.
    Earning this certification (Certificate Code: 10006998) reflects my commitment to going beyond using technology and truly understanding how it is built. This milestone represents my growth as a future developer and my dedication to continuously learning the language that powers innovation in data science, automation, and software development.""")

    st.success("🚀 Built a strong foundation in Python programming and logical problem-solving.")

    st.markdown("---")
    # ======================
    # PROJECT 12
    # ======================
    st.image("CERTIFICATE6.png", use_container_width=True)
    st.subheader("🗣️ English for IT Certification – Cisco Networking Academy")

    st.write("""On March 25, 2026, I received a Statement of Achievement in English for IT: Describing and Comparing from the Cisco Networking Academy. This course enhanced my ability to communicate effectively within the IT field by focusing on the proper use of technical language, terminology, and structured explanations.
    It strengthened my skills in describing systems, comparing processes, and collaborating in professional digital environments. This achievement reflects my commitment to becoming a well-rounded IT professional—one who can not only build and develop systems but also clearly communicate ideas, solutions, and their real-world impact.""")

    st.success("🚀 Strengthened my communication skills for professional IT environments.")

    st.markdown("---")
    # ======================
    # PROJECT 13
    # ======================
    st.image("CERTIFICATE7.png", use_container_width=True)
    st.subheader("🤝 Engaging Stakeholders for Success – Cisco Networking Academy")

    st.write("""On March 25, 2026, I completed the Engaging Stakeholders for Success course through the Cisco Networking Academy, marking an important step in my professional development. This experience emphasized that successful projects are not only built on technical skills but also on strong relationships, communication, and understanding stakeholder needs.
    I developed skills in identifying priorities, actively listening, and collaborating effectively to ensure that project goals align with stakeholder expectations. This achievement reflects my growth beyond technical execution and highlights my ability to bridge the gap between technology and the people it serves—ensuring meaningful and successful outcomes.""")

    st.success("🚀 Enhanced my stakeholder communication and collaboration skills.")

    st.markdown("---")
    # ======================
    # PROJECT 14
    # ======================
    st.image("CERTIFICATE8.png", use_container_width=True)
    st.subheader("🖥️ Computer Hardware Basics – Cisco Networking Academy")

    st.write("""
    Earning this Certificate of Course Completion in Computer Hardware Basics from the Cisco Networking Academy on April 10, 2025, felt like I was finally getting my hands on the physical heart of technology. It’s one thing to use a computer, but it’s another entirely to understand the intricate components that make it breathe. This chapter of my journey was all about the fundamentals—learning how to build, repair, and upgrade the systems we often take for granted. From mastering preventive maintenance to understanding the specialized functions of laptops and mobile devices, this experience gave me the practical confidence to look at a machine and know exactly how it works. For me, this achievement represents a solid foundation in my story; it’s a proud reminder that I’m building my expertise from the ground up, ensuring I have the technical "know-how" to support any digital challenge.
    """)

    st.success("🚀 Strengthened my foundational knowledge in computer hardware systems.")

    st.markdown("---")
    # ======================
    # PROJECT 15
    # ======================
    st.image("CERTIFICATE9.png", use_container_width=True)
    st.subheader("🎨 CSS Essentials – Cisco Networking Academy")

    st.write("""
    Earning this CSS Essentials certification from the Cisco Networking Academy on April 11, 2025, validated my professional mastery of modern web styling and responsive design. It strengthened my ability to create visually appealing, responsive, and user-friendly web interfaces. Through this certification, I gained hands-on knowledge in advanced layout techniques such as Flexbox and CSS Grid, along with the implementation of interactive animations and adherence to accessibility standards. This experience enhanced my understanding of how design and functionality work together to build high-performance digital experiences. For me, this achievement represents not only technical growth but also a deeper appreciation for creating polished, scalable, and user-centric web solutions in today’s evolving technological landscape.
    """)

    st.success("🚀 Strengthened my skills in modern CSS, responsive design, and UI/UX styling.")

    st.markdown("---")
    # ======================
    # PROJECT 16
    # ======================
    st.image("CERTIFICATE10.png", use_container_width=True)
    st.subheader("🌐 HTML Essentials – Cisco Networking Academy (with JS Institute)")

    st.write("""
    This HTML Essentials certification, issued by the Cisco Networking Academy in collaboration with JS Institute on March 10, 2025, validates a fundamental mastery of web architecture and semantic content structure. It demonstrates proficiency in creating accessible, well-formed HTML documents and integrating multimedia elements, hyperlinks, and validated web forms. This achievement highlights a strong technical foundation essential for modern web development. It serves as a professional testament to the ability to build the structural core of user-centric digital environments while ensuring full compatibility with CSS and JavaScript standards.
    """)

    st.success("🚀 Strengthened my foundation in HTML structure, semantic web design, and web development basics.")

    st.markdown("---")
    # ======================
    # PROJECT 17
    # ======================
    st.image("EMPLOYEE_SYSTEM.png", use_container_width=True)
    st.subheader("💼 Employee Management System – Web-Dev 101")

    st.write("""
    Every line of code and every pixel in this Employee Management System was driven by a commitment to excellence. Developed as a core project for Web-Dev 101 under the guidance of our instructor, Ma’am Daisy Jean Castillo, this system represents a journey of technical growth and creative refinement.
    What started as a functional requirement became a personal mission to push the boundaries of what a student project could achieve. I focused heavily on elevating the UI & UX design, going beyond basic functionality to craft a professional, high-fidelity dashboard that balances clean aesthetics with intuitive navigation.         
    From seamless “At-a-Glance” analytics to a refined task management interface, every element was meticulously designed to ensure that managing a workforce feels modern, efficient, and user-friendly. This project is not just a submission—it is a testament to the professional standard of design and development I strive to bring to every challenge.
    """)

    st.success("🚀 Enhanced skills in UI/UX design, dashboard development, and full project system design.")

    st.markdown("---")
    # ======================
    # PROJECT 18
    # ======================
    st.image("DOCUFLOW.png", use_container_width=True)
    st.subheader("📄 DocuFlow – Document Management System (Web-Dev 101 Final Project)")

    st.write("""
    Building on the momentum of the Employee Management System, I developed DocuFlow as a comprehensive final project for Web-Dev 101 under the mentorship of Ma’am Daisy Jean Castillo. This platform was designed to bridge the gap between administrative complexity and operational efficiency. While the management system focused on people, DocuFlow focuses on the lifeblood of any organization: its documentation. I approached this project with a deep focus on creating a secure, high-performance environment where document submission, approval workflows, and real-time tracking converge into one seamless interface.
    By refining the UI/UX design, I ensured that even the most complex approval hierarchies remain visually clear and easy to navigate. Every feature—from the dynamic "Approval Dashboard" to the granular "Document Tracking" system—was built with a user-first philosophy, ensuring transparency and speed in the digital workplace. DocuFlow is more than just a document handler; it is a reflection of my growth as a developer and my passion for building professional-grade tools that solve real-world organizational challenges.
    """)

    st.success("🚀 Strengthened full-stack development, workflow system design, and advanced UI/UX structuring.")
    st.markdown("---")
# =========================
# CONTACT
# =========================
elif menu == "📬 Contact":
    st.title("📬 Contact Me")

    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")

    if st.button("Send"):
        if name and email and message:
            st.success("Message sent successfully! ✅")
        else:
            st.error("Please complete all fields.")

    st.markdown("---")
    st.subheader("🌐 Social Links")
    st.write("GitHub: https://github.com/")
    st.write("Facebook: https://www.facebook.com/?ref=homescreenpwa")
