import requests


class HalbestundeClient:
    def __init__(self, auth_base_url, omr_base_url, api_key=None):
        self.auth_base_url = auth_base_url
        self.omr_base_url = omr_base_url
        self.api_key = api_key

    def _get_headers(self):
        headers = {}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        return headers

    def sign_in(self, email, password):
        url = f"{self.auth_base_url}/auth/signin"
        data = {"email": email, "password": password}
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()

    def refresh_token(self, refresh_token):
        url = f"{self.auth_base_url}/auth/refresh"
        data = {"refresh_token": refresh_token}
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()

    def forgot_password(self, email):
        url = f"{self.auth_base_url}/auth/password/forgot"
        data = {"email": email}
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()

    def forgot_password_confirm(self, email, password, code):
        url = f"{self.auth_base_url}/auth/password/forgot/confirm"
        data = {"email": email, "password": password, "code": code}
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()

    def find_by_email(self, email):
        url = f"{self.auth_base_url}/auth/find-by-email"
        params = {"email": email}
        response = requests.get(url, headers=self._get_headers(), params=params)
        response.raise_for_status()
        return response.json()

    def get_presigned_upload_url(self, filename):
        url = f"{self.omr_base_url}/recognize/presigned-upload"
        params = {"filename": filename}
        response = requests.get(url, headers=self._get_headers(), params=params)
        response.raise_for_status()
        return response.json()

    def recognize_presigned_uploaded_file(self, filename, pdf_image=False):
        url = f"{self.omr_base_url}/recognize/presigned-upload"
        data = {"filename": filename, "pdf_image": pdf_image}
        response = requests.post(url, headers=self._get_headers(), json=data)
        response.raise_for_status()
        return response.json()

    def get_recognition_results(self, inference_id, detailed=False):
        url = f"{self.omr_base_url}/recognize/{inference_id}"
        params = {"detailed": detailed}
        response = requests.get(url, headers=self._get_headers(), params=params)
        response.raise_for_status()
        return response.json()

    def update_recognition_results(self, filename):
        url = f"{self.omr_base_url}/callback/{filename}"
        response = requests.post(url)
        response.raise_for_status()
        return response.json()

    def get_scans_history_list(
        self,
        search_by=None,
        filter_by=None,
        sort_by=None,
        period_start=None,
        period_end=None,
        page_size=None,
        page_num=None,
    ):
        url = f"{self.omr_base_url}/scans-history"
        params = {
            "search_by": search_by,
            "filter_by": filter_by,
            "sort_by": sort_by,
            "period_start": period_start,
            "period_end": period_end,
            "page_size": page_size,
            "page_num": page_num,
        }
        response = requests.get(url, headers=self._get_headers(), params=params)
        response.raise_for_status()
        return response.json()
