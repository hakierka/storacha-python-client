import unittest
from unittest.mock import patch, MagicMock
from storacha_client import StorachaClient

class TestStorachaClient(unittest.TestCase):
    def setUp(self):
        # Set up a StorachaClient instance for each test
        self.client = StorachaClient()

    @patch('storacha_client.storacha_client.requests.post')
    def test_upload_file_success(self, mock_post):
        # Simulate a successful response from the API
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{
            'p': {'out': {'ok': {'url': 'https://someurl.com', 'status': 'upload'}}}
        }]
        mock_post.return_value = mock_response

        # Call upload_file and check the response
        cid = 'fake-cid'
        file_size = 1234
        did = 'did:key:fake-did'
        response = self.client.upload_file(cid, file_size, did)

        self.assertIn('url', response[0]['p']['out']['ok'])
        self.assertEqual(response[0]['p']['out']['ok']['status'], 'upload')

    @patch('storacha_client.storacha_client.requests.post')
    def test_upload_file_failure(self, mock_post):
        # Simulate a failure response from the API
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_post.return_value = mock_response

        cid = 'fake-cid'
        file_size = 1234
        did = 'did:key:fake-did'

        with self.assertRaises(Exception):
            self.client.upload_file(cid, file_size, did)

if __name__ == '__main__':
    unittest.main()
