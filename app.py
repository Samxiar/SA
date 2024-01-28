import streamlit as st
from nltk.sentiment.vader import SentimentIntensityAnalyzer
# Page Config 
st.set_page_config(page_title='Dash', page_icon='👽',layout="wide")
hide_st_style = """
            <style>
            
            footer {visibility: hidden;}
            
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Function to perform sentiment analysis
def analyze_sentiment(sentence):
    sid = SentimentIntensityAnalyzer()
    sentiment_score = sid.polarity_scores(sentence)
    
    # Determine the sentiment based on the compound score
    if sentiment_score['compound'] >= 0.05:
        return 'Positive'
    elif sentiment_score['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

# Streamlit application
def main():
    st.title('Sentiment Analysis with VADER')

    # Checkbox to toggle the visibility of the description
    view_description = st.checkbox('View Description')

    # Description section
    if view_description:
        st.write("""
        Welcome to the Sentiment Analysis with VADER app! This app provides a simple sentiment analysis tool powered by VADER (Valence Aware Dictionary and sEntiment Reasoner).
        
        To use the app, simply enter a sentence in the text box below and click the "Analyze Sentiment" button to view the sentiment analysis results.
        """)

    # Input text box for the user to enter a sentence
    sentence = st.text_input('Enter a sentence:')
    
    # Perform sentiment analysis when the user submits the sentence
    if st.button('Analyze Sentiment'):
        if sentence:
            result = analyze_sentiment(sentence)
            st.write(f'Overall Sentiment: {result}')
        else:
            st.warning('Please enter a sentence.')

    # Add credits
    st.sidebar.markdown('**Credits**')
    st.sidebar.markdown('- **Creator**: Sameer Kulkarni')
    st.sidebar.markdown('- **Affiliation**: TYBSCIT, Data Science enthusiast')

if __name__ == "__main__":
    main()
