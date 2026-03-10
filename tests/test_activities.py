import pytest

class TestGetActivities:
    def test_get_activities_returns_200(self, client):
        # Arrange
        # (TestClient fixture provides the client)
        
        # Act
        response = client.get("/activities")
        
        # Assert
        assert response.status_code == 200

    def test_get_activities_returns_dict(self, client):
        # Arrange
        # (TestClient fixture provides the client)
        
        # Act
        response = client.get("/activities")
        data = response.json()
        
        # Assert
        assert isinstance(data, dict)

    def test_get_activities_contains_expected_activities(self, client, valid_activity_names):
        # Arrange
        expected_activities = valid_activity_names
        
        # Act
        response = client.get("/activities")
        activities = response.json()
        
        # Assert
        for activity_name in expected_activities:
            assert activity_name in activities

    def test_get_activities_has_required_fields(self, client):
        # Arrange
        required_fields = {"description", "schedule", "max_participants", "participants"}
        
        # Act
        response = client.get("/activities")
        activities = response.json()
        
        # Assert
        for activity_name, activity_data in activities.items():
            assert isinstance(activity_data, dict)
            assert required_fields.issubset(activity_data.keys())

    def test_get_activities_participants_is_list(self, client):
        # Arrange
        # (TestClient fixture provides the client)
        
        # Act
        response = client.get("/activities")
        activities = response.json()
        
        # Assert
        for activity_name, activity_data in activities.items():
            assert isinstance(activity_data["participants"], list)

    def test_get_activities_max_participants_is_integer(self, client):
        # Arrange
        # (TestClient fixture provides the client)
        
        # Act
        response = client.get("/activities")
        activities = response.json()
        
        # Assert
        for activity_name, activity_data in activities.items():
            assert isinstance(activity_data["max_participants"], int)
            assert activity_data["max_participants"] > 0