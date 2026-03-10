import pytest

class TestRootEndpoint:
    def test_root_returns_redirect(self, client):
        # Arrange
        # (TestClient fixture provides the client)
        
        # Act
        response = client.get("/", follow_redirects=False)
        
        # Assert
        assert response.status_code == 307

    def test_root_redirects_to_static_index(self, client):
        # Arrange
        expected_location = "/static/index.html"
        
        # Act
        response = client.get("/", follow_redirects=False)
        
        # Assert
        assert "location" in response.headers
        assert response.headers["location"] == expected_location