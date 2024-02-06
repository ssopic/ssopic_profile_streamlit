import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
from streamlit_timeline import timeline

st.set_page_config(
    page_title="Silvio's Portfolio",
    page_icon=":tada:",
    layout="wide",
    initial_sidebar_state="auto"
)

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })


    def run(self):
        with st.sidebar:
            # Add some text
            st.sidebar.markdown("**Welcome to my website!**")
            st.sidebar.markdown("Please select something from the menu or download my CV below.")

            selected_app = option_menu(
                menu_title="Agenda",  # Provide a non-empty menu_title
                options=[app["title"] for app in self.apps],
                orientation="vertical",
                styles={
                    "container": {"padding": "0!important", "background-color": "#fafafa"},
                    "icon": {"color": "black", "font-size": "25px"},
                    "nav-link": {"font-size": "20px", "text-align": "left", "margin": "0px", "color":"black",
                                 "--hover-color": "#eee"},
                    "nav-link-selected": {'background-color': "grey"},
                }
            )
        for app in self.apps:
            if app["title"] == selected_app:
                app["function"]()
        pdfFileObj = open('assets/Sopic_CV.pdf', 'rb')
        st.sidebar.download_button('download resume', pdfFileObj, file_name='Sopic_CV.pdf', mime='pdf')



import streamlit


def homepage():
    import streamlit as st
    import requests
    from PIL import Image

    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    # --------------- LOAD ASSETS---------------------
    Face = Image.open("assets/face.jpg")

    # Use local CSS
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style> {f.read()}</style> ", unsafe_allow_html=True)

    local_css("style/style.css")

    # ---------------- HEADER SECTION ----------
    with st.container():
        text_column, face_column = st.columns((2, 1))
        with face_column:
            # Create a circle
            circle_element = st.image(Face, width=250)
        with text_column:
            st.markdown("### I am")
            st.markdown('# **Silvio Sopić**')
            st.markdown("**Data Scientist | MBA + (MSc)^2**")
            st.markdown(
                "**Data scientist with a relentless curiosity for uncovering patterns and a  \\\n passion for turning raw data into meaningful stories.** ")
            st.write("---")

            # --------WHAT I DO -------------
    # Define your service details
    # Define your service details
    service_container = st.empty()

    services = [
        {
            "title": "Geo Data Analysis",
            "description": "### Stuck in Location Data Chaos? Unlock Insights & Visualizations Now!\n\nDrowning in Google Maps & Yelp data? Our service transforms it into:\n\n* **Predictive models:** Forecast behavior, optimize campaigns, find hidden opportunities.\n* **Stunning visualizations:** Tell location stories clearly & beautifully. ✨\n\nNo more manual work! We collect, clean, & prep your data for:\n\n* **Machine learning models:** Feed them accurate location data for powerful insights.\n* **Data visualization tools:** Create captivating maps, charts & graphs.\n\nBenefits:\n\n* Faster insights: Cut through the noise & find what matters quickly. ⚡\n* Actionable intelligence: Make data-driven decisions based on real-world patterns.\n* Effortless workflow: Focus on your expertise, we handle the data transformation.\n\nReady to break free from location data chaos? Contact us today!"
            ,
            "ser_image": "assets/geo data analysis.jpeg",  # Optional link for more information
        },
        {
            "title": "Data Analysis",
            "description": """ ### Unleash Data's Story: Visualize Insights & Solve Business Problems\n\nConfused by data dashboards? We craft clear & impactful visualizations using:\n\n* Tableau, PowerBI, Cognos & more!\n* Your valuable data - no external sources needed.\n\nWe help you:\n\n* See the big picture: Understand trends, patterns & relationships in your data.\n* Solve business problems: Predict outcomes, classify customers, & make data-driven decisions.\n* Engage your audience: Tell compelling data stories with stunning visuals. ✨\n\nBenefits:\n\n* Faster insights: Cut through the noise & find what matters quickly. ⚡\n* Clear communication: Make complex data understandable for everyone.\n* Data-driven decisions: Turn insights into actionable strategies.\n* Expertise included: We handle the visualization & problem-solving.\n\nReady to unlock the power of your data? Contact us for a free consultation!\n\nSee the story - solve the problem.""",
            "ser_image": "assets/Data analysis.jpeg",  # Optional link for more information
        },
        # Add more services as needed
    ]
    # Store current service index in session state
    if "service_index" not in st.session_state:
        st.session_state.service_index = 0

    # Create navigation buttons
    col3, col4 = st.columns(2)
    with col4:
        next_button = st.button("Next Service", key="next_button")
    with col3:
        prev_button = st.button("Previous Service", key="prev_button")

    # Display current service
    service = services[st.session_state.service_index]
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            ser_picture = Image.open(service["ser_image"])
            st.image(ser_picture, width=500)

        with col2:
            st.write(f"## {service['title']}")
            st.markdown(service["description"])

    # Update index based on button clicks
    if next_button:
        st.session_state.service_index = (st.session_state.service_index + 1) % len(services)
    if prev_button:
        st.session_state.service_index = (st.session_state.service_index - 1) % len(services)

    # ------------- CONTACT FORM -------------------
    with st.container():
        st.write("---")
        st.header("Contact me")
        st.write("##")
        contact_form = """
    <form action="https://formsubmit.co/01001bb4e55e665b727a313eb18d5438" method="POST" id="contactForm">
         <input type="text"
          name="name" placeholder="Your name, please" required>
         <input type="email" name="email" placeholder="Your contact, please"required>
         <input type="text" name ="message" placeholder="Your message, please" required>
         <button type="submit">Send</button>
    </form>


    """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()

def Portfolio():
    import streamlit as st
    from PIL import Image

    Viz1 = Image.open("assets/convenience.png")
    Viz2 = Image.open("assets/cat_par_ali.png")
    Viz3 = Image.open("assets/ratings.png")
    Viz4 = Image.open("assets/random forest results.png")
    Viz5 = Image.open("assets/price prediction features.png")

    # Main title
    st.title("Geo Data Analysis streamlined sample")

    # Expander 1: Common real-estate mass price prediction analysis
    expander1 = st.expander("Step 1. Analyze the given data")
    with expander1:
        with st.container():
            viz1_column , text_column  = st.columns((2, 1))
            with viz1_column:
                st.image(Viz1, width = 650)
            with text_column:
                st.markdown(
                    "### Unleash Real Estate Insights in Clicks. No Magic Required.\n\nOur interactive dashboard empowers you to explore key real estate data variables with ease. Select any X and Y, nominal or continuous, and uncover hidden patterns in seconds.\n\nVisualize & Analyze:\n* Interactive map: See trends by location with bubble sizes and color intensity based on your choices.\n* Scatterplot: Uncover relationships between variables.\n* Histogram: Understand data distribution and filter for deeper analysis.\n* Boxplot: Compare distributions across categories.\n\nEffortless & Powerful:\n* Filter & update: Instantly see changes as you select and filter variables.\n* No coding required: Get started in seconds, no data science expertise needed.\n* Actionable insights: Make data-driven decisions to optimize pricing, target neighborhoods, and find profitable opportunities.\n\n **Boost Your Real Estate IQ!**")

    # Expander 2: Common real-estate mass price prediction analysis
    expander2 = st.expander("Step 2. Obtain Geo Data using Yelp or Google maps")
    with expander2:
        st.markdown("""## Unlock Hidden Yelp Insights: Fusion Tags at Your Fingertips\n\nDitch the guesswork and uncover the secrets behind local businesses with our interactive Yelp Fusion API visualization.\n\nDive into a World of Tags:\n* Location, location, location: Find tags associated with any object near your desired coordinates.\n* Beyond the basics: Go deeper than just addresses, explore the tag structure that defines each business.\n* Tag trends at a glance: Bar chart lengths reveal the most prevalent tags, guiding your understanding of local offerings.\n* Informed analysis: Use these insights to refine your searches and make data-driven decisions in your next project.\n\n **Stop scratching the surface, start exploring the depths of Yelp data!** """)
        st.image(Viz2, width = 600)

    # Expander 3: Common real-estate mass price prediction analysis
    expander3 = st.expander("Step 3. Explore your location(s)")
    with expander3:
        with st.container():
                st.markdown(
                    """## Unveil City Secrets with Yelp: Explore & Analyze Points of Interest\n\nDrill down beyond just locations with our interactive visualization powered by Yelp Fusion and your "
                convenience
                visualization
                " data (any mesh works!).\n\nUnlock Deeper Insights:\n* Location, location, impact: Go beyond presence, understand the quality of parks, stores, and more!\n* Map your surroundings: Explore the vibe around any chosen location.\n* Tag drill-down: Filter by Yelp Fusion's main tags for granular exploration.\n* Brand spotlight: See prominent stores like convenience stores, their numbers, and ratings.\n* Deeper analysis: Dive further with additional filters for tailored insights.\n\nStop just mapping, start understanding! Contact us today to unlock the full potential of your city data.""")
                st.image(Viz3, width=500)

    # Expander 4: Common real-estate mass price prediction analysis
    expander4 = st.expander("Step 4. Find out what matters")
    with expander4:
        with st.container():
            viz4_column , text_column  = st.columns((2, 1))
            with viz4_column:
                st.image(Viz4, width = 500)
            with text_column:
                st.markdown(
                    """### Cracking the Price Prediction Code: Uncover Key Drivers with This Model\n\nDon't settle for guesswork - unlock the variables that truly impact your price predictions with our powerful random-forest model!\n\nDive Deep into the Data:\n* Accuracy: See how effectively the model predicts values compared to actual outcomes.\n* Error Analysis: Measure the average difference between predictions and real values with MAE, MSE, and RMSE.\n* R-squared: Gauge the model's explanation power, revealing how well it captures true price variations.\n* Variable Combinations: Witness how different combinations of factors influence prediction accuracy.\n\nThe Big Reveal:\n* Using all variables: This combination stands out, significantly improving all metrics!\n* Hidden Gems: Discover which variables contribute most, guiding your future data collection and analysis.\n\nStop flying blind! Leverage the power of modeling to identify crucial factors and boost your price prediction precision like never before.""")

    # Expander 5: Common real-estate mass price prediction analysis
    expander5 = st.expander("Step 5. Understand where it is!")
    with expander5:
        with st.container():
            viz5_column , text_column  = st.columns((2, 1))
            with viz5_column:
                st.image(Viz5, width = 500)
            with text_column:
                st.markdown(
                    """### Decode Real Estate Goldmines: Predict Prices with Key Features\n\nUnveil the secret sauce behind precise real estate price predictions! This chart highlights the most impactful features guiding our powerful model.\n\nDive into the Details:\n* Geography matters: Location plays a role, but how? Discover nearby bar quantity (continuous) and their average quality (ordinal).\n* Beyond location: See how specific city areas with larger properties and key intrinsic features contribute to value.\n* Interactive insights: Choose "
                price
                " on one selector and explore variations with the other to unlock hidden patterns.\n\nDon't just estimate, predict with confidence! Leverage this powerful tool for smarter real estate decisions.""")
import streamlit as st
import json

def Tech_stack():
    # Load the hard skills data
    with open('assets/hard_skills.json', "r") as f:
        hs = json.load(f)

    # Create two columns using st.columns
    col1, col2 = st.columns(2)

    # Function to display skills in a column, handling lists of dictionaries
    def display_skills_in_column(column, skills_list):
        for skill_dict in skills_list:
            skill_name = skill_dict.get("skill_name", "Unknown Skill")  # Access skill name
            expertise_level = skill_dict.get("expertise_level", "Unknown Level")  # Access expertise level
            column.markdown(f"- **{skill_name}:** {expertise_level}")

    # Distribute skills across columns directly
    category_count = 0
    for category, skills_list in hs.items():
        if category_count % 2 == 0:
            col1.header(category)
            display_skills_in_column(col1, skills_list)
        else:
            col2.header(category)
            display_skills_in_column(col2, skills_list)
        category_count += 1


def timeline_details():
    import streamlit as st
    import json
    from streamlit_timeline import timeline
    st.markdown("## Please select area of interest below:")
    st.write("---")

    # Load data and define keywords
    with open('assets/timeline.json', "r") as f:
        data = json.load(f)

    education_keywords = ["ZSEM General MBA", "MsC Business Economics at KU Leuven","MsC Information Management at KU Leuven"]
    work_experience_keywords = ["Functional Data integration analyst", "Functional Analyst"]  # Add your keywords here
    prof_keywords = ["SAS Certified Specialist: Base Programming Using SAS 9.4", "Azure Data Essentials","Azure Fundamentals",]
    course_keywords = ["Generative Pre-trained Transformers","Generative AI for data scientists","IBM AI Engineering","IBM Machine Learning", "People and Soft Skills for Professional and Personal Success", "IBM Data Science","IBM Data Warehouse Engineer","IBM Data Analyst", "Tabkeau Data Steward", "Tabkeau Designer", "Tableau Author", "Tableau Consumer", "SQL for Database Administrators", "Marketing Analytics with Python", "Statistician", "SQL for business analysts", ]

    # Filter events based on selected categories
    def filter_events(events, keywords):
        return [event for event in events if any(keyword in event["text"]["headline"] for keyword in keywords)]

    filtered_education_events = filter_events(data["events"], education_keywords)
    filtered_work_experience_events = filter_events(data["events"], work_experience_keywords)
    filtered_prof_events = filter_events(data["events"], prof_keywords)
    filtered_course_events = filter_events(data["events"], course_keywords)

    import streamlit as st

    # Create columns to arrange checkboxes horizontally
    cols = st.columns(4)  # Adjust the number of columns based on your needs

    # Place each checkbox within its respective column
    with cols[0]:
        work_exp_selected = st.checkbox("Work Experience", key="work_experience")
    with cols[1]:
        education_selected = st.checkbox("Education", key="education")
    with cols[2]:
        courses_selected = st.checkbox("Professional Development Courses", key="courses")
    with cols[3]:
        IndustryCertifications_selected = st.checkbox("Industry Certifications", key="ind_cer")

    # Combine and filter based on selected categories
    filtered_events = []
    if work_exp_selected:
        filtered_events += filtered_work_experience_events
    if education_selected:
        filtered_events += filtered_education_events
    if courses_selected:
        filtered_events += filtered_course_events
    if IndustryCertifications_selected:
        filtered_events += filtered_prof_events

    # Check for empty results
    if not filtered_events:
        st.write("No events match the selected criteria.")
        return

    # Restructure data for streamlit-timeline
    timeline_data = {"events": filtered_events}

    # Ensure necessary keys (example, modify based on your data)
    for event in timeline_data["events"]:
        if not "start_date" in event:
            event["start_date"] = {"year": 2000}  # Example placeholder
        if not "media" in event:
            event["media"] = {}  # Example placeholder
        if not "text" in event:
            event["text"] = {}  # Example placeholder
    # Display the timeline
    timeline(timeline_data, height=500)

# Call the function to display the timeline
#timeline_details()


app = MultiApp()
app.add_app("Services Offered", homepage)  # Add homepage
app.add_app("Experience Timeline", timeline_details)  # Add homepage
app.add_app("Tech Stack", Tech_stack)  # Add homepage
app.add_app("Portfolio", Portfolio)  # Add homepage
app.run()
