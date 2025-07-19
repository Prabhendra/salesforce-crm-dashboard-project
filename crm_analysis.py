import pandas as pd

# CSV File पढ़ना
df = pd.read_csv('crm_leads_data.csv')

# Data की पहली 5 rows देखो
print(df.head())

# कौन-कौन से Lead Sources हैं और कितनी बार आए हैं?
lead_source_counts = df['Lead Source'].value_counts()
print("\n📊 Lead Source Counts:")
print(lead_source_counts)

# कौन-कौन से Lead Sources हैं और कितनी बार आए हैं?
lead_source_counts = df['Lead Source'].value_counts()
print("\n📊 Lead Source Counts:")
print(lead_source_counts)


import pandas as pd

# CSV पढ़ना
df = pd.read_csv('crm_leads_data.csv')

print("🧾 Available Columns:")
print(df.columns)

# ✅ Lead Source Count
if 'Lead Source' in df.columns:
    print("\n📊 Lead Sources:")
    print(df['Lead Source'].value_counts())

# ✅ Lead Status Count
if 'Lead Status' in df.columns:
    print("\n🎯 Lead Status Distribution:")
    print(df['Lead Status'].value_counts())

# ✅ Rating Wise Analysis
if 'Rating' in df.columns:
    print("\n⭐ Rating Wise Leads:")
    print(df['Rating'].value_counts())

# ✅ Industry Wise Analysis
if 'Industry' in df.columns:
    print("\n🏭 Industry Wise Leads:")
    print(df['Industry'].value_counts())

# ✅ Monthly Trend (Created Date)
if 'Created Date' in df.columns:
    df['Created Date'] = pd.to_datetime(df['Created Date'], errors='coerce')
    df['Month'] = df['Created Date'].dt.to_period('M')
    print("\n📅 Leads per Month:")
    print(df['Month'].value_counts().sort_index())



