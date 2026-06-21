
#Transform data by dropping columns and renaming them.
def run_transformation(data):
    print("Transforming data...")
    # Drop unnecessary columns
    columns_to_drop = ['urlToImage', 'publishedAt', 'content', 'source.id', 'source.name']
    data = data.drop(columns=columns_to_drop)
    
    # Rename columns for clarity
    data = data.rename(columns={'title': 'headline', 'description': 'summary'})
    
    return data


