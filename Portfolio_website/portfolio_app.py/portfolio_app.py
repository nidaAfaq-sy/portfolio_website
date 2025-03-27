import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import io
import random

# Page Configuration
st.set_page_config(
    page_title="My Portfolio",
    page_icon="👨",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.big-font {
    font-size:50px !important;
    font-weight: bold;
}
.medium-font {
    font-size:30px !important;
}
.small-font {
    font-size:14px !important;
}
.highlight {
    background-color: #f0f2f6;
    padding: 20px;
    border-radius: 10px;
}
/* Add styles for profile picture */
.stImage {
    border-radius: 50% !important;
    overflow: hidden;
}
img {
    border-radius: 50%;
}
</style>
""", unsafe_allow_html=True)

# Navigation
def create_navigation():
    nav = st.sidebar.radio("Navigation", ["Home", "About", "Skills", "Projects", "Experience", "Contact"])
    return nav

# Add this function to create profile avatar
def create_profile_avatar(letter, size=(300, 300)):
    # Create a new image with a random background color
    def random_color():
        # Generate pastel colors for pleasant appearance
        return (
            random.randint(100, 200),
            random.randint(100, 200),
            random.randint(100, 200)
        )
    
    # Create image
    img = Image.new('RGB', size, color=random_color())
    draw = ImageDraw.Draw(img)
    
    try:
        # Try to load Arial font
        font = ImageFont.truetype("arial.ttf", size=120)
    except:
        # Fallback to default font
        font = ImageFont.load_default()
    
    # Get text size
    text_width = draw.textlength(letter, font=font)
    text_height = 120  # Approximate height for the font size
    
    # Calculate text position for center alignment
    x = (size[0] - text_width) // 2
    y = (size[1] - text_height) // 2
    
    # Draw the letter
    draw.text((x, y), letter, fill='white', font=font)
    
    return img

# Home Section
def home_section():
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<p class="big-font">Hello, I\'m [Nida Siddiqui]</p>', unsafe_allow_html=True)
        st.markdown('<p class="medium-font">Software Developer | Data Scientist</p>', unsafe_allow_html=True)
        st.write("Welcome to my portfolio! I'm passionate about creating innovative solutions and turning ideas into reality.")
        
        # Call to action buttons
        col3, col4, col5 = st.columns([1, 1, 2])
        with col3:
            st.button("📫 Hire Me")
        with col4:
            st.button("📄 Resume")
    
    with col2:
        # Create and display the profile avatar
        profile_img = create_profile_avatar("N")
        st.image(profile_img, width=300)

# About Section
def about_section():
    st.markdown('<p class="medium-font">About Me</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        I'm a passionate software developer with expertise in:
        - 🐍 Python Programming
        - 📊 Data Science
        - 🤖 Machine Learning
        - 🌐 Web Development
        
        With over [X] years of experience, I've worked on various projects ranging from web applications to data analysis solutions.
        I'm constantly learning and exploring new technologies to stay at the forefront of technological advancement.
        """)
    
    with col2:
        st.markdown("""
        ### Quick Facts
        - 🎓 Degree in Computer Science
        - 🌍 Based in [Location]
        - 💼 Open to opportunities
        - 🗣️ Languages: English, [Other languages]
        """)

# Skills Section
def skills_section():
    st.markdown('<p class="medium-font">Skills</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### Programming Languages")
        skills_data = {
            "Python": 90,
            "JavaScript": 80,
            "Java": 70,
            "SQL": 85
        }
        
        for skill, value in skills_data.items():
            st.write(f"{skill}")
            st.progress(value/100)
    
    with col2:
        st.markdown("### Frameworks/Libraries")
        frameworks = {
            "React": 85,
            "Django": 80,
            "Flask": 75,
            "Streamlit": 90
        }
        
        for framework, value in frameworks.items():
            st.write(f"{framework}")
            st.progress(value/100)
    
    with col3:
        st.markdown("### Tools & Technologies")
        tools = {
            "Git": 90,
            "Docker": 75,
            "AWS": 70,
            "MongoDB": 80
        }
        
        for tool, value in tools.items():
            st.write(f"{tool}")
            st.progress(value/100)

# Projects Section
def create_book_thumbnail(title, color_scheme="blue", size=(300, 200)):
    """Create a book-themed thumbnail"""
    # Color schemes
    colors = {
        "blue": {"bg": (100, 150, 200), "book": (50, 100, 150)},
        "purple": {"bg": (150, 100, 200), "book": (100, 50, 150)}
    }
    
    # Create base image
    img = Image.new('RGB', size, color=colors[color_scheme]["bg"])
    draw = ImageDraw.Draw(img)
    
    # Book dimensions
    book_width = 160
    book_height = 140
    x_start = (size[0] - book_width) // 2
    y_start = (size[1] - book_height) // 2
    
    # Draw book
    # Book spine
    draw.rectangle(
        [x_start, y_start, x_start + book_width, y_start + book_height],
        fill=colors[color_scheme]["book"],
        outline='white',
        width=2
    )
    
    # Book spine detail
    draw.line(
        [x_start + 20, y_start, x_start + 20, y_start + book_height],
        fill='white',
        width=2
    )
    
    try:
        # Try to load fonts
        title_font = ImageFont.truetype("arial.ttf", size=20)
        python_font = ImageFont.truetype("arial.ttf", size=24)
    except:
        title_font = ImageFont.load_default()
        python_font = ImageFont.load_default()
    
    # Add Python logo (simplified)
    draw.text(
        (x_start + 40, y_start + 20),
        "🐍",
        fill='white',
        font=python_font
    )
    
    # Add text
    draw.text(
        (x_start + 40, y_start + 60),
        "Python",
        fill='white',
        font=python_font
    )
    
    draw.text(
        (x_start + 40, y_start + 100),
        title,
        fill='white',
        font=title_font
    )
    
    return img

def projects_section():
    st.markdown('<p class="medium-font">Projects</p>', unsafe_allow_html=True)
    
    # Project 1
    with st.container():
        col1, col2 = st.columns([1, 2])
        with col1:
            # Create and display project 1 book thumbnail
            project1_img = create_book_thumbnail(
                "Data Analysis",
                color_scheme="blue"
            )
            st.image(project1_img, caption="Python Data Analysis")
            
        with col2:
            st.markdown("### Python Data Analysis Project")
            st.write("Description of project 1. Explain what you built and what technologies you used.")
            st.markdown("**Technologies used:** Python, Pandas, NumPy, Matplotlib")
            st.button("View Project 1", key="proj1")
    
    st.markdown("---")
    
    # Project 2
    with st.container():
        col1, col2 = st.columns([1, 2])
        with col1:
            # Create and display project 2 book thumbnail
            project2_img = create_book_thumbnail(
                 "Development",
                color_scheme="purple"
            )
            st.image(project2_img, caption="Python Development")
            
        with col2:
            st.markdown("### Python Development Project")
            st.write("Description of project 2. Explain what you built and what technologies you used.")
            st.markdown("**Technologies used:** Python, Django, PostgreSQL")
            st.button("View Project 2", key="proj2")

# Add this enhanced version of the book thumbnail creator for more detailed books
def create_detailed_book_thumbnail(title, color_scheme="blue", size=(300, 200)):
    """Create a more detailed book-themed thumbnail"""
    # Color schemes
    colors = {
        "blue": {
            "bg": (100, 150, 200),
            "book": (50, 100, 150),
            "accent": (200, 220, 255)
        },
        "purple": {
            "bg": (150, 100, 200),
            "book": (100, 50, 150),
            "accent": (220, 200, 255)
        }
    }
    
    # Create base image
    img = Image.new('RGB', size, color=colors[color_scheme]["bg"])
    draw = ImageDraw.Draw(img)
    
    # Book dimensions
    book_width = 160
    book_height = 140
    x_start = (size[0] - book_width) // 2
    y_start = (size[1] - book_height) // 2
    
    # Draw book shadow
    shadow_offset = 5
    draw.rectangle(
        [x_start + shadow_offset, y_start + shadow_offset, 
         x_start + book_width + shadow_offset, y_start + book_height + shadow_offset],
        fill=(30, 30, 30, 128)
    )
    
    # Draw book
    # Main cover
    draw.rectangle(
        [x_start, y_start, x_start + book_width, y_start + book_height],
        fill=colors[color_scheme]["book"],
        outline='white',
        width=2
    )
    
    # Spine detail
    draw.rectangle(
        [x_start, y_start, x_start + 25, y_start + book_height],
        fill=colors[color_scheme]["accent"],
        outline='white',
        width=1
    )
    
    try:
        title_font = ImageFont.truetype("arial.ttf", size=20)
        python_font = ImageFont.truetype("arial.ttf", size=24)
        detail_font = ImageFont.truetype("arial.ttf", size=16)
    except:
        title_font = ImageFont.load_default()
        python_font = ImageFont.load_default()
        detail_font = ImageFont.load_default()
    
    # Add Python logo
    draw.text(
        (x_start + 40, y_start + 20),
        "🐍",
        fill='white',
        font=python_font
    )
    
    # Add text
    draw.text(
        (x_start + 40, y_start + 60),
        "Python",
        fill='white',
        font=python_font
    )
    
    # Add title
    draw.text(
        (x_start + 40, y_start + 100),
        title,
        fill='white',
        font=title_font
    )
    
    # Add spine text (vertically)
    draw.text(
        (x_start + 5, y_start + 20),
        "PYTHON",
        fill='white',
        font=detail_font
    )
    
    return img

# Experience Section
def experience_section():
    st.markdown('<p class="medium-font">Experience</p>', unsafe_allow_html=True)
    
    # Experience Timeline
    experiences = [
        {
            "title": "Senior Software Developer",
            "company": "Tech Company A",
            "period": "2022 - Present",
            "description": "• Led development of key features\n• Managed team of 5 developers\n• Improved system performance by 40%"
        },
        {
            "title": "Software Developer",
            "company": "Tech Company B",
            "period": "2021 - 2022",
            "description": "• Developed full-stack applications\n• Implemented CI/CD pipeline\n• Reduced bug count by 50%"
        }
    ]
    
    for exp in experiences:
        with st.container():
            col1, col2 = st.columns([1, 3])
            with col1:
                st.markdown(f"**{exp['period']}**")
            with col2:
                st.markdown(f"### {exp['title']}")
                st.markdown(f"*{exp['company']}*")
                st.markdown(exp['description'])
        st.markdown("---")

# Contact Section
def contact_section():
    st.markdown('<p class="medium-font">Contact Me</p>', unsafe_allow_html=True)
    
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit_button = st.form_submit_button("Send Message")
        
        if submit_button:
            if name and email and message:
                st.success("Thanks for reaching out! I'll get back to you soon.")
            else:
                st.error("Please fill in all fields.")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("[LinkedIn](https://linkedin.com)")
    with col2:
        st.markdown("[GitHub](https://github.com)")
    with col3:
        st.markdown("[Twitter](https://twitter.com)")
    with col4:
        st.markdown("[Email](mailto:your.email@example.com)")

# Main App
def main():
    nav = create_navigation()
    
    if nav == "Home":
        home_section()
    elif nav == "About":
        about_section()
    elif nav == "Skills":
        skills_section()
    elif nav == "Projects":
        projects_section()
    elif nav == "Experience":
        experience_section()
    elif nav == "Contact":
        contact_section()

if __name__ == "__main__":
    main() 
