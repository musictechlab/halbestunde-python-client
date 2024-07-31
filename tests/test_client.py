import pytest
import requests
from unittest.mock import patch
from halbestunde_python_client.client import HalbestundeClient

# Sample test data
test_email = "test@example.com"
test_password = "test_password"
test_refresh_token = "test_refresh_token"
test_code = "test_code"
test_filename = "test.jpg"
test_inference_id = "test_inference_id"
api_key = "test_api_key"

# Mock responses
sign_in_response = {
    "AccessToken": "access_token",
    "ExpiresIn": 3600,
    "TokenType": "Bearer",
    "IdToken": "id_token",
    "RefreshToken": "refresh_token",
}

refresh_token_response = {
    "AccessToken": "new_access_token",
    "ExpiresIn": 3600,
    "TokenType": "Bearer",
    "IdToken": "new_id_token",
}

find_by_email_response = {"userid": "1910ad91-c190-4000-8a5e-45d046f97301"}

presigned_upload_response = {
    "url": "https://example.com/upload",
    "filename": "54c1d600-a588-4ebf-a331-95de51cfc049_00281f59-66cc-4fb3-bd94-43bd83f9c3fa.jpg",
    "url_storage": "https://s3.example.com/input/test.jpg",
}

recognize_response = {"inference_id": "b4637410-65bc-44e8-9841-ea292c874615"}

recognition_results_response = {
    "job_status": "completed",
    "body": {
        "filename_musicxml": "https://s3.example.com/output/test.musicxml",
        "filename_midi": "https://s3.example.com/output/test.mid",
    },
}

scans_history_response = {
    "total": 1,
    "items": [
        {
            "id": "30141655-ea0c-48e7-9cdb-875d30e9a400",
            "inference_id": "b4637410-65bc-44e8-9841-ea292c874615",
            "created_at": "1970-01-01T00:00:00.000Z",
            "uid": "a8a88d2e-2eca-4fce-b06d-dd64bbf6ff3e",
            "device_hash": "string",
            "scan_result": True,
            "source_file": "https://s3.example.com/input/test.pdf",
            "source_preview_file": "https://s3.example.com/input/test.png",
            "result_xml": "https://s3.example.com/output/test.xml",
            "result_midi": "https://s3.example.com/output/test.mid",
            "result_pdf": "https://s3.example.com/output/test.pdf",
            "result_preview_pdf": "https://s3.example.com/output/test.png",
        }
    ],
}


@pytest.fixture
def client():
    return HalbestundeClient(
        auth_base_url="https://omr.external.api.halbestunde.com/service-auth",
        omr_base_url="https://omr.external.api.halbestunde.com/service-omr",
        api_key=api_key,
    )


def test_sign_in(client):
    with patch("requests.post") as mock_post:
        mock_post.return_value.json.return_value = sign_in_response
        response = client.sign_in(email=test_email, password=test_password)
        assert response == sign_in_response


def test_refresh_token(client):
    with patch("requests.post") as mock_post:
        mock_post.return_value.json.return_value = refresh_token_response
        response = client.refresh_token(refresh_token=test_refresh_token)
        assert response == refresh_token_response


def test_find_by_email(client):
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = find_by_email_response
        response = client.find_by_email(email=test_email)
        assert response == find_by_email_response


def test_get_presigned_upload_url(client):
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = presigned_upload_response
        response = client.get_presigned_upload_url(filename=test_filename)
        assert response == presigned_upload_response


def test_recognize_presigned_uploaded_file(client):
    with patch("requests.post") as mock_post:
        mock_post.return_value.json.return_value = recognize_response
        response = client.recognize_presigned_uploaded_file(filename=test_filename)
        assert response == recognize_response


def test_get_recognition_results(client):
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = recognition_results_response
        response = client.get_recognition_results(inference_id=test_inference_id)
        assert response == recognition_results_response


def test_get_scans_history_list(client):
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = scans_history_response
        response = client.get_scans_history_list()
        assert response == scans_history_response
