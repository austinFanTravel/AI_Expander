"""
OpenAI API Key Tester

This script tests if an OpenAI API key is valid by making a simple API call.
"""

import os
import sys
from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path

def test_openai_key(api_key: str) -> tuple[bool, str]:
    """
    Test if an OpenAI API key is valid.
    
    Args:
        api_key: The OpenAI API key to test
        
    Returns:
        tuple: (is_valid, message)
    """
    try:
        client = OpenAI(api_key=api_key)
        
        # Make a simple API call to test the key
        models = client.models.list()
        
        # If we get here, the key is valid
        return True, "✅ API key is valid and working!"
        
    except Exception as e:
        error_msg = str(e)
        if "Incorrect API key" in error_msg:
            return False, "❌ Invalid API key. Please check your key and try again."
        elif "You didn't provide an API key" in error_msg:
            return False, "❌ No API key provided."
        elif "rate limit" in error_msg.lower():
            return False, f"⚠️  Rate limited: {error_msg}"
        else:
            return False, f"❌ Error: {error_msg}"

def main():
    # Try to load API key from environment variable first
    api_key = os.getenv("OPENAI_API_KEY")
    
    # If not in environment, try to load from .env file
    if not api_key:
        env_path = Path(__file__).parent / '.env'
        if env_path.exists():
            load_dotenv(dotenv_path=env_path)
            api_key = os.getenv("OPENAI_API_KEY")
    
    # If still no key, prompt the user
    if not api_key:
        print("No API key found in environment variables or .env file.")
        api_key = input("Please enter your OpenAI API key: ").strip()
        if not api_key:
            print("No API key provided. Exiting.")
            sys.exit(1)
    
    print("🔍 Testing OpenAI API key...")
    is_valid, message = test_openai_key(api_key)
    print(message)
    
    if is_valid:
        # Test a simple completion to verify full functionality
        try:
            print("\n🔍 Testing API functionality with a simple request...")
            client = OpenAI(api_key=api_key)
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": "Say this is a test"}],
                max_tokens=5
            )
            print(f"✅ API is fully functional! Response: {response.choices[0].message.content}")
        except Exception as e:
            print(f"⚠️  API key is valid but there was an error with the API: {str(e)}")

if __name__ == "__main__":
    main()
