import streamlit as st

def calculate_risk_score(responses):
    # Sample weightings for questionnaire responses (adjust as needed)
    risk_score = 0
    
    # Sample questions and weightings
    question_weights = {
        "investment_horizon": 0.2,  # Weight for investment time horizon
        "willingness_to_accept_loss": 0.4,  # Weight for willingness to accept short-term losses
        "prior_investment_experience": 0.2,  # Weight for prior investment experience
        "investment_goals": 0.2,  # Weight for investment goals
    }
    
    # Calculate risk score based on questionnaire responses
    for question, weight in question_weights.items():
        if question in responses:
            response_value = responses[question]
            # Assign scores based on responses (adjust as needed)
            if question == "investment_horizon":
                if response_value == "long_term":
                    risk_score += weight * 1
                elif response_value == "medium_term":
                    risk_score += weight * 5
                elif response_value == "short_term":
                    risk_score += weight * 10
            elif question == "willingness_to_accept_loss":
                if response_value == "high":
                    risk_score += weight * 1
                elif response_value == "medium":
                    risk_score += weight * 5
                elif response_value == "low":
                    risk_score += weight * 10
            elif question == "prior_investment_experience":
                if response_value == "experienced":
                    risk_score += weight * 1
                elif response_value == "some_experience":
                    risk_score += weight * 5
                elif response_value == "no_experience":
                    risk_score += weight * 10
            elif question == "investment_goals":
                if response_value == "wealth_growth":
                    risk_score += weight * 1
                elif response_value == "education":
                    risk_score += weight * 5
                elif response_value == "retirement":
                    risk_score += weight * 10
    
    return risk_score

# Create a Streamlit app
st.title("Investor Risk Assessment")

# Collect questionnaire responses from the user
st.write("Please answer the following questions to calculate your risk score(1~10, The larger the score, the more risk-averse and more conservative the investment):")
investment_horizon = st.radio("Investment Time Horizon(short_term <2 years;medium_term 2~5 years;long_term>5 years)", ("short_term", "medium_term", "long_term"))
willingness_to_accept_loss = st.radio("Willingness to Accept Loss", ("low", "medium", "high"))
prior_investment_experience = st.radio("Prior Investment Experience(no_experience<1 year;some_experience 1~5 year;experienced >5 years)", ("no_experience", "some_experience", "experienced"))
investment_goals = st.radio("Investment Goals", ("retirement", "education","wealth_growth"))

responses = {
    "investment_horizon": investment_horizon,
    "willingness_to_accept_loss": willingness_to_accept_loss,
    "prior_investment_experience": prior_investment_experience,
    "investment_goals": investment_goals,
}

# Calculate the risk score based on responses
risk_score = calculate_risk_score(responses)

# Display the risk score to the user
st.write(f"Your Risk Score: {risk_score}")
