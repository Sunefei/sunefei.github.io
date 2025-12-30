import requests
from scholarly import scholarly
import json
import os
import time

def get_citation_count(scholar_id, max_retries=3):
    """
    获取Google Scholar的引用数，带重试机制
    """
    for attempt in range(max_retries):
        try:
            print(f"Attempt {attempt + 1}: Fetching citation count for {scholar_id}")
            
            # 直接搜索作者，不使用已废弃的方法
            author = scholarly.search_author_id(scholar_id)
            author_filled = scholarly.fill(author)
            
            citations = author_filled.get('citedby', 0)
            print(f"Successfully fetched citations: {citations}")
            return citations
            
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                wait_time = (attempt + 1) * 15  # 15, 30, 45秒
                print(f"Waiting {wait_time} seconds before retry...")
                time.sleep(wait_time)
            else:
                print(f"All {max_retries} attempts failed")
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

def get_existing_citations():
    """
    获取现有的引用数
    """
    try:
        with open('google-scholar-stats/gs_data_shieldsio.json', 'r') as f:
            data = json.load(f)
            return data.get('message', '0')
    except:
        return '0'

if __name__ == "__main__":
    SCHOLAR_ID = os.environ.get('SCHOLAR_ID', 'FT8SBIkAAAAJ')
    
    print(f"Starting citation update for Scholar ID: {SCHOLAR_ID}")
    
    citations = get_citation_count(SCHOLAR_ID)
    
    if citations is not None:
        update_json_file(citations)
        print("Citations updated successfully!")
    else:
        existing = get_existing_citations()
        print(f"Failed to update, keeping existing citations: {existing}")
        update_json_file(existing)  # 保持现有数据
    
    # 不退出失败状态，避免workflow报错
    exit(0)