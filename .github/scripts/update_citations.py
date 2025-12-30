import requests
from scholarly import scholarly
import json
import os
import signal

class TimeoutException(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutException()

def get_citation_count(scholar_id, timeout=60):
    """
    获取Google Scholar的引用数，带超时限制
    """
    # 设置超时
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timeout)
    
    try:
        author = scholarly.search_author_id(scholar_id)
        author = scholarly.fill(author)
        citations = author['citedby']
        signal.alarm(0)  # 取消超时
        return citations
    except TimeoutException:
        print(f"Request timed out after {timeout} seconds")
        return None
    except Exception as e:
        print(f"Error fetching citations: {e}")
        return None
    finally:
        signal.alarm(0)  # 确保取消超时

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
    
    citations = get_citation_count(SCHOLAR_ID, timeout=120)  # 120秒超时
    
    if citations is not None:
        update_json_file(citations)
        print("Citations updated successfully!")
    else:
        print("Failed to update citations, keeping existing data")
        # 不退出失败，避免workflow报错
        exit(0)