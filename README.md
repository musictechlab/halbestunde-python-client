
# halbestunde-python-client

`halbestunde-python-client` is an unofficial and open source Python library for interacting with the Halbestunde API. It provides methods for authentication, managing OMR (Optical Music Recognition) uploads, and retrieving recognition results.

## Features

- **Authentication**: Sign in, refresh tokens, forgot password, and find user by email.
- **OMR**: Get presigned upload URLs, recognize uploaded files, retrieve recognition results, update recognition results, and get scans history.

## Installation

### Prerequisites

- Python 3.9.x
- [Poetry](https://python-poetry.org/)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/bravelab/halbestunde-python-client.git
   cd halbestunde-python-client
   ```

2. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

## Usage

### Initialize the Client

```python
from halbestunde_client.halbestunde_client import HalbestundeClient

client = HalbestundeClient(
    auth_base_url="https://omr.external.api.halbestunde.com/service-auth",
    omr_base_url="https://omr.external.api.halbestunde.com/service-omr",
    api_key="your_api_key_here"  # Use your actual API key
)
```

### Authentication

#### Sign In

```python
response = client.sign_in(email="your_email@example.com", password="your_password")
print(response)
```

#### Refresh Token

```python
response = client.refresh_token(refresh_token="your_refresh_token")
print(response)
```

#### Forgot Password

```python
response = client.forgot_password(email="your_email@example.com")
print(response)
```

#### Forgot Password Confirm

```python
response = client.forgot_password_confirm(email="your_email@example.com", password="new_password", code="confirmation_code")
print(response)
```

#### Find by Email

```python
response = client.find_by_email(email="your_email@example.com")
print(response)
```

### OMR (Optical Music Recognition)

#### Get Presigned Upload URL

```python
response = client.get_presigned_upload_url(filename="image.jpg")
print(response)
```

#### Recognize Presigned Uploaded File

```python
response = client.recognize_presigned_uploaded_file(filename="00281f59-66cc-4fb3-bd94-43bd83f9c3fa.jpg")
print(response)
```

#### Get Recognition Results

```python
response = client.get_recognition_results(inference_id="b4637410-65bc-44e8-9841-ea292c874615")
print(response)
```

#### Update Recognition Results

```python
response = client.update_recognition_results(filename="00281f59-66cc-4fb3-bd94-43bd83f9c3fa.pdf")
print(response)
```

#### Get Scans History List

```python
response = client.get_scans_history_list()
print(response)
```

## Running Tests

Tests are written using `pytest`. To run the tests, use the following command:

```bash
poetry run pytest
```

## More Examples

You can run some examples using `poetry`. To run scripts, use the following command:

```bash
poetry run python examples/example_usage.py
```

## Code quality
### Format the code using black
poetry run black .

### Auto-fix PEP 8 issues using autopep8
poetry run autopep8 --in-place --recursive .

### Check for any remaining issues with flake8
poetry run flake8

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some feature'`)
5. Push to the branch (`git push origin feature-branch`)
6. Create a new Pull Request

Please ensure your code adheres to the project's coding standards and passes all tests.

## License

This project is licensed under the MIT License.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

<div align="center">
  Bravelab. Digital Commerce Solution For The Music Industry<br>
  <a href="https://www.bravelab.io/">Website</a>
  <span> | </span>
  <a href="https://linkedin.com/company/bravelab.io">LinkdedIn</a><span> | </span>
  <a href="mailto:office@bravelab.io">Let's talk</a><br>
  Crafted by https://www.bravelab.io
</div>

