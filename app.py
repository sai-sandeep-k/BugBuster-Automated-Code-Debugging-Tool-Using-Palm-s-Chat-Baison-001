import streamlit as st
from debug_utils import initialize_palm, debug_code

model = initialize_palm()

def main():
    st.title("Automated Code Debugging Tool")

    project_description = """
    BugBuster: AI-Powered Code Debugger is an advanced tool designed to streamline the process of identifying and resolving errors in code. Leveraging the power of artificial intelligence, BugBuster analyzes code snippets provided by users, detects bugs, and offers detailed suggestions for fixes. Whether you're a novice coder or an experienced developer, BugBuster helps you quickly pinpoint and rectify errors, improving code quality and ensuring robust functionality. With its user-friendly interface and intelligent debugging capabilities, BugBuster enhances productivity, accelerates development, and promotes more efficient coding practices.
    """

    scenario_1 = """
    ## Scenario 1: Debugging Complex Algorithms 
    In scenarios where developers are working on complex algorithms or data structures, BugBuster can be invaluable. It helps identify logical errors, boundary condition issues, and performance bottlenecks, ensuring the algorithm functions as intended and delivers optimal results.
    """

    scenario_2 = """
    ## Scenario 2: Code Reviews and Quality Assurance 
    BugBuster can be integrated into code review processes and quality assurance workflows within corporate environments. It assists code reviewers in identifying potential bugs, improving code readability, and ensuring adherence to coding standards. Quality assurance teams can use BugBuster to conduct comprehensive testing and validate the functionality of software applications before deployment, reducing the risk of post-release issues.
    """

    scenario_3 = """
    ## Scenario 3: Cross-Platform Compatibility 
    BugBuster can play a vital role in ensuring consistent functionality and performance across platforms where a software product needs to be compatible across multiple platforms, such as Windows, macOS, and Linux by debugging and optimizing the codebase for each environment. Developers can use BugBuster to identify platform-specific bugs, optimize code for resource efficiency, and implement platform-specific features or optimizations. This ensures a seamless user experience across diverse platforms, enhancing the product's market reach and user satisfaction.
    """

    scenario_4 = """
    ## Scenario 4: Compliance and Security Audits 
    In regulated industries such as finance, healthcare, or government, corporations must adhere to strict compliance and security standards to protect sensitive data and ensure regulatory compliance. BugBuster can assist in this context by identifying security vulnerabilities, compliance violations, and potential data breaches within the codebase. Developers and security experts can leverage BugBuster to perform automated code audits, detect security flaws, and implement necessary fixes or mitigations to ensure compliance with industry regulations and safeguard corporate assets and sensitive information.
    """

    # Display all content in a single text area
    st.text_area("Project Description", 
                 project_description,
                 height=200)
    st.text_area("Scenario 1", 
                 scenario_1,
                 height=100)
    st.text_area("Scenario 2", 
                 scenario_2,
                 height=100)
    st.text_area("Scenario 3", 
                 scenario_3,
                 height=100)
    st.text_area("Scenario 4", 
                 scenario_4,
                 height=100)

    st.subheader("Code Debugging")
    code_snippet = st.text_area("Enter the code snippet you want to debug:")

    if st.button("Debug Code"):
        if code_snippet.strip():
            with st.spinner("Debugging code..."):
                try:
                    debug_result = debug_code(code_snippet)
                    st.success("Debugging complete!")
                    
                    st.text_area("Debugging result:", debug_result, height=300)
                except Exception as e:
                    st.error(f"Error debugging code: {e}")
        else:
            st.error("Please enter a code snippet.")
if __name__ == "__main__":
    main()

