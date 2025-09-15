import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from collections import Counter
import re

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('metadata.csv')
    
    # Clean data (same as before)
    threshold = len(df) * 0.5
    missing_counts = df.isnull().sum()
    cols_to_drop = missing_counts[missing_counts > threshold].index
    df = df.drop(columns=cols_to_drop)
    df['abstract'] = df['abstract'].fillna('')
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    df['abstract_word_count'] = df['abstract'].apply(lambda x: len(str(x).split()))
    return df

df = load_data()

st.title("CORD-19 Data Explorer")
st.write("Exploring COVID-19 research papers metadata")

# Interactive year slider
min_year = int(df['year'].min())
max_year = int(df['year'].max())
year_range = st.slider("Select year range", min_year, max_year, (min_year, max_year))

filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

st.subheader(f"Papers published from {year_range[0]} to {year_range[1]}")
year_counts = filtered_df['year'].value_counts().sort_index()

fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x=year_counts.index, y=year_counts.values, ax=ax, palette='viridis')
ax.set_xlabel("Year")
ax.set_ylabel("Number of Publications")
ax.set_title("Publications by Year")
st.pyplot(fig)

# Top journals
st.subheader("Top Journals")
top_journals = filtered_df['journal'].value_counts().head(10)

fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.barplot(y=top_journals.index, x=top_journals.values, ax=ax2, palette='magma')
ax2.set_xlabel("Number of Publications")
ax2.set_ylabel("Journal")
ax2.set_title("Top 10 Journals")
st.pyplot(fig2)

# Word cloud of titles
st.subheader("Word Cloud of Paper Titles")
all_titles = ' '.join(filtered_df['title'].dropna().astype(str).tolist())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_titles)

fig3, ax3 = plt.subplots(figsize=(15, 7.5))
ax3.imshow(wordcloud, interpolation='bilinear')
ax3.axis('off')
st.pyplot(fig3)

# Show sample data
st.subheader("Sample Data")
st.dataframe(filtered_df[['title', 'journal', 'year', 'abstract_word_count']].head(10))
