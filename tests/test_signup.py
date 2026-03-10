import pytest

class TestSignup:
    def test_signup_returns_200(self, client, valid_activity_names, sample_email):
        # Arrange
        activity = valid_activity_names[0]
        email = sample_email
        
        # Act
        response = client.post(
            f"/activities/{activity}/signup",
            params={"email": email}
        )
        
        # Assert
        assert response.status_code == 200

    def test_signup_returns_success_message(self, client, valid_activity_names, sample_email):
        # Arrange
        activity = valid_activity_names[0]
        email = sample_email
        
        # Act
        response = client.post(
            f"/activities/{activity}/signup",
            params={"email": email}
        )
        data = response.json()
        
        # Assert
        assert "message" in data
        assert sample_email in data["message"]
        assert activity in data["message"]

    def test_signup_for_nonexistent_activity_returns_404(self, client, sample_email):
        # Arrange
        nonexistent_activity = "Nonexistent Activity"
        email = sample_email
        
        # Act
        response = client.post(
            f"/activities/{nonexistent_activity}/signup",
            params={"email": email}
        )
        data = response.json()
        
        # Assert
        assert response.status_code == 404
        assert "Activity not found" in data["detail"]

    def test_signup_duplicate_returns_400(self, client, valid_activity_names):
        # Arrange
        activity = valid_activity_names[0]
        duplicate_email = "michael@mergington.edu"  # Already in Chess Club
        
        # Act
        response = client.post(
            f"/activities/{activity}/signup",
            params={"email": duplicate_email}
        )
        data = response.json()
        
        # Assert
        assert response.status_code == 400
        assert "already signed up" in data["detail"].lower()

    def test_signup_updates_participants_list(self, client, valid_activity_names):
        # Arrange
        activity = valid_activity_names[1]  # Programming Class
        new_email = "verify.participant@mergington.edu"
        
        # Act
        response = client.post(
            f"/activities/{activity}/signup",
            params={"email": new_email}
        )
        
        # Assert
        assert response.status_code == 200
        activities_response = client.get("/activities")
        activities = activities_response.json()
        assert new_email in activities[activity]["participants"]