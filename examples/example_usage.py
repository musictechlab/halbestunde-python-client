import sys
import os


from halbestunde_python_client.client import HalbestundeClient

# Initialize the client
client = HalbestundeClient(
    auth_base_url="https://omr.external.api.halbestunde.com/service-auth",
    omr_base_url="https://omr.external.api.halbestunde.com/service-omr",
    api_key="your_api_key_here",  # Replace with your actual API key
)

# Helper function to print detailed response


def print_response(response):
    if isinstance(response, dict):
        for key, value in response.items():
            print(f"  {key}: {value}")
    else:
        print(response)


# Example: Sign In
try:
    sign_in_response = client.sign_in(
        email="your_email@example.com", password="your_password"
    )
    print("Sign In Response:")
    print_response(sign_in_response)
except Exception as e:
    print("Error during sign in:", e)
    if hasattr(e, "response") and e.response is not None:
        print("Response content:", e.response.content)
