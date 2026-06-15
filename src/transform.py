
#Transform data by dropping columns and renaming them.
def transform_data(data):
    print("Transforming data...")
    # Drop unnecessary columns
    data = data.drop(columns=[['urlToImage', 'publishedAt','content', 'source.id', 'source.name']], errors='ignore')
    
    # Rename columns for clarity
    data = data.rename(columns={'title': 'headline', 'description': 'summary'})
    
    return data


