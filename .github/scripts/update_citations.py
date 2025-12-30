import requests
import json
import os
import time
from scholarly import scholarly
from fake_useragent import UserAgent

def get_citation_count(scholar_id, max_retries=3):
    """
    获取Google Scholar的引用数，带重试机制
    """
    for attempt in range(max_retries):
        try:
            # 设置随机User-Agent
            ua = UserAgent()
            scholarly.set_random_user_agent(ua.random)
            
            # 添加延迟避免被检测
            if attempt > 0:
                time.sleep(10)
            
            print(f"Attempt {attempt + 1}/{max_retries}...")
            author = scholarly.search_author_id(scholar_id)
            author = scholarly.fill(author)
            citations = author['citedby']
            
            print(f"Successfully fetched {citations} citations")
            return citations
            
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                wait_time = (attempt + 1) * 15  # 递增等待时间
                print(f"Waiting {wait_time} seconds before retry...")
                time.sleep(wait_time)
    
    return None

def update_json_file(citations):
    """
    更新JSON文件
    """
    data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": str(citations)
    }
    
    os.makedirs('google-scholar-stats', exist_ok=True)
    
    with open('google-scholar-stats/gs_data_shieldsio.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"Updated citations to {citations}")

if __name__ == "__main__":
    SCHOLAR_ID = os.environ.get('SCHOLAR_ID', 'FT8SBIkAAAAJ')
    
    citations = get_citation_count(SCHOLAR_ID)
    
    if citations is not None:
        update_json_file(citations)
        print("Citations updated successfully!")
    else:
        # 读取现有文件保持数据
        try:
            with open('google-scholar-stats/gs_data_shieldsio.json', 'r') as f:
                existing_data = json.load(f)
                print(f"Failed to update, keeping existing citations: {existing_data.get('message', 'unknown')}")
        except:
            print("Failed to update citations and no existing data found")
        exit(0)  # 不报错，避免workflow失败