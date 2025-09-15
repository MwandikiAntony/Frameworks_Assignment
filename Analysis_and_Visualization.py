import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns

# Assuming df_cleaned is your cleaned DataFrame

# Step 1: Count papers by publication year
year_counts = df_cleaned['year'].value_counts().sort_index()
print("Papers published per year:")
print(year_counts)

# Plot number of publications over time
plt.figure(figsize=(10,6))
sns.barplot(x=year_counts.index, y=year_counts.values, palette='viridis')
plt.title('Number of Publications by Year')
plt.xlabel('Year')
plt.ylabel('Number of Publications')
plt.xticks(rotation=45)
plt.show()

# Step 2: Identify top journals publishing COVID-19 research
top_journals = df_cleaned['journal'].value_counts().head(10)
print("\nTop 10 journals by publication count:")
print(top_journals)

# Bar chart of top publishing journals
plt.figure(figsize=(10,6))
sns.barplot(y=top_journals.index, x=top_journals.values, palette='magma')
plt.title('Top 10 Journals Publishing COVID-19 Research')
plt.xlabel('Number of Publications')
plt.ylabel('Journal')
plt.show()

# Step 3: Find most frequent words in titles
from collections import Counter
import re

# Combine all titles into a single string
all_titles = ' '.join(df_cleaned['title'].dropna().astype(str).tolist())

# Simple word frequency after cleaning text
words = re.findall(r'\b\w+\b', all_titles.lower())
common_words = Counter(words).most_common(20)

print("\n20 most common words in titles:")
for word, count in common_words:
    print(f"{word}: {count}")

# Step 4: Generate a word cloud of paper titles
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_titles)

plt.figure(figsize=(15,7.5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Paper Titles')
plt.show()

# Step 5: Plot distribution of paper counts by source
if 'source_x' in df_cleaned.columns:
    source_counts = df_cleaned['source_x'].value_counts().head(10)
    plt.figure(figsize=(10,6))
    sns.barplot(y=source_counts.index, x=source_counts.values, palette='coolwarm')
    plt.title('Top 10 Sources of Papers')
    plt.xlabel('Number of Publications')
    plt.ylabel('Source')
    plt.show()
else:
    print("\nColumn 'source_x' not found in DataFrame.")
