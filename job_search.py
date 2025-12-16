# automated-job@automate-job-468807.iam.gserviceaccount.com
# from googlesearch import search
# import pandas as pd
# from datetime import datetime
# import os

# KEYWORDS = [
#     "myjobmag.com React Native Developer",
#     "myjobmag.com Frontend Developers",
#     "hotnigerianjobs.com React Native Developer",
#     "hotnigerianjobs.com Frontend Developers",
#     "workable.com Frontend Developer Remote",
#     "workable.com React Native Remote",
#     "my.greenhouse.io Frontend Developer remote",
#     "my.greenhouse.io React Native Developer remote", 
#     "jobs.eu.lever.co React Native Developer remote",
#     "jobs.lever.co Frontend Developer remote",  
#     "jobs.eu.lever.co Frontend Developer remote",
#     "jobs.lever.co Frontend Developer remote",  
# ]

# OUTPUT_FILE = "results/job_search_results.csv"

# def search_jobs():
#     os.makedirs("results", exist_ok=True)
#     all_results = []

#     for keyword in KEYWORDS:
#         print(f"Searching for: {keyword}")
#         try:
#             # FIX: Removed 'num' argument
#             urls = list(search(keyword, stop=10, pause=2))
#             for url in urls:
#                 all_results.append({
#                     "keyword": keyword,
#                     "url": url,
#                     "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#                 })
#         except Exception as e:
#             print(f"Error searching {keyword}: {e}")

#     df = pd.DataFrame(all_results)
#     try:
#         with open(OUTPUT_FILE, 'a') as f:
#             df.to_csv(f, header=f.tell() == 0, index=False)
#         print(f"Saved {len(all_results)} results to {OUTPUT_FILE}")
#     except Exception as e:
#         print(f"Error saving file: {e}")


# if __name__ == "__main__":
#     search_jobs()





from googlesearch import search
import pandas as pd
from datetime import datetime
import os

KEYWORDS = [
    "myjobmag.com React Native Developer",
    "myjobmag.com Frontend Developers",
    "hotnigerianjobs.com React Native Developer",
    "hotnigerianjobs.com Frontend Developers",
    "workable.com Frontend Developer Remote",
    "workable.com React Native Remote",
    "my.greenhouse.io Frontend Developer remote",
    "my.greenhouse.io React Native Developer remote", 
    "jobs.eu.lever.co React Native Developer remote",
    "jobs.lever.co Frontend Developer remote",  
    "jobs.eu.lever.co Frontend Developer remote",
    "jobs.lever.co Frontend Developer remote",  
    "jobs.lever.co Machine Learning Engineer remote", 
    "jobs.eu.lever.co Machine Learning Engineer remote",
    "my.greenhouse.io Machine Learning Engineer remote",
    "myjobmag.com Machine Learning Engineer", 
    "workable.com Machine Learning Remote",
    "jobs.lever.co Backend Engineer Django remote", 
    "jobs.eu.lever.co Backend Engineer Django remote",
    "my.greenhouse.io Backend Engineer Django remote",
    "myjobmag.com Backend Engineer Django", 
    "workable.com Backend Engineer Django Remote",
    "jobs.lever.co Django Developer remote", 
    "jobs.eu.lever.co Django Developer remote",
    "my.greenhouse.io Django Developer remote",
    "myjobmag.com Django Developer", 
    "workable.com Django Developer Remote",
]

OUTPUT_FILE = "results/job_search_results_new.csv"

def search_jobs():
    os.makedirs("results", exist_ok=True)
    all_results = []

    # Load existing URLs if file exists
    existing_urls = set()
    if os.path.exists(OUTPUT_FILE):
        try:
            existing_df = pd.read_csv(OUTPUT_FILE)
            existing_urls = set(existing_df['url'].dropna().unique())
        except Exception as e:
            print(f"Error reading existing file: {e}")

    for keyword in KEYWORDS:
        print(f"Searching for: {keyword}")
        try:
            # Search on Google
            urls = list(search(keyword, stop=10, pause=2))
            for url in urls:
                # Only add if URL is not already in the file
                if url not in existing_urls:
                    all_results.append({
                        "keyword": keyword,
                        "url": url,
                        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    })
                    existing_urls.add(url)  # Prevent duplicates within same run
        except Exception as e:
            print(f"Error searching {keyword}: {e}")

    # Save only new unique results
    if all_results:
        df = pd.DataFrame(all_results)
        try:
            with open(OUTPUT_FILE, 'a') as f:
                df.to_csv(f, header=f.tell() == 0, index=False)
            print(f"Added {len(all_results)} new results to {OUTPUT_FILE}")
        except Exception as e:
            print(f"Error saving file: {e}")
    else:
        print("No new unique URLs found.")

if __name__ == "__main__":
    search_jobs()
