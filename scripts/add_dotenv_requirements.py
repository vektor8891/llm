#!/usr/bin/env python3
"""
Add python-dotenv to requirements.txt for projects that need environment variables
"""

from pathlib import Path

def add_dotenv_to_requirements():
    """Add python-dotenv to requirements.txt files that need it"""
    
    # Projects that need environment variables
    projects_needing_env = [
        "26_prompt_engineering",
        "27_langchain", 
        "28_langchain_rag",
        "29_langchain_doc_loader",
        "30_full_doc_retrieve",
        "32_watsonx_embedding",
        "33_langchain_vector_store", 
        "34_langchain_retriever",
        "35_gradio"
    ]
    
    base_dir = Path(__file__).parent.parent / "projects"
    
    for project_name in projects_needing_env:
        project_dir = base_dir / project_name
        req_file = project_dir / "requirements.txt"
        
        if req_file.exists():
            # Read current requirements
            content = req_file.read_text()
            
            # Check if python-dotenv is already in requirements
            if 'python-dotenv' not in content:
                # Add python-dotenv to the beginning
                if content.strip():
                    new_content = f"python-dotenv\n{content}"
                else:
                    new_content = "python-dotenv\n"
                
                req_file.write_text(new_content)
                print(f"✅ Added python-dotenv to: {project_name}/requirements.txt")
            else:
                print(f"⏭️  python-dotenv already in: {project_name}/requirements.txt")
        else:
            # Create requirements.txt with python-dotenv
            req_file.write_text("python-dotenv\n")
            print(f"📝 Created requirements.txt with python-dotenv: {project_name}/requirements.txt")

if __name__ == "__main__":
    print("Adding python-dotenv to projects that need environment variables...")
    print("=" * 70)
    add_dotenv_to_requirements()
    print("=" * 70)
    print("✅ Done!")
