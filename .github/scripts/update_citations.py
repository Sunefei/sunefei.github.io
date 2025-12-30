import requests
from scholarly import scholarly
import json
import os

def get_citation_count(scholar_id):
    """
    获取Google Scholar的引用数
    """
    try:
        # 搜索作者
        author = scholarly.search_author_id(scholar_id)
        author = scholarly.fill(author)
        
        # 获取引用数
        citations = author['citedby']
        
        return citations
    except Exception as e:
        print(f"Error fetching citations: {e}")
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
    
    # 确保目录存在
    os.makedirs('google-scholar-stats', exist_ok=True)
    
    # 写入JSON文件
    with open('google-scholar-stats/gs_data_shieldsio.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"Updated citations to {citations}")

if __name__ == "__main__":
    # 替换为你的Google Scholar ID
    SCHOLAR_ID = os.environ.get('SCHOLAR_ID', 'FT8SBIkAAAAJ')  # 从环境变量获取
    
    citations = get_citation_count(SCHOLAR_ID)
    
    if citations is not None:
        update_json_file(citations)
        print("Citations updated successfully!")
    else:
        print("Failed to update citations")
        exit(1)