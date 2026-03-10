import pytest

class TestIntegration:
    def test_full_workflow_get_and_signup(self, client, valid_activity_names):
        # Arrange
        activity_name = valid_activity_names[2]  # Gym Class
        new_email = "integration.test@mergington.edu"
        
        # Act: Get initial state
        activities_response = client.get("/activities")
        activities = activities_response.json()
        initial_participants = len(activities[activity_name]["participants"])
        
        # Act: Sign up
        signup_response = client.post(
            f"/activities/{activity_name}/signup",
            params={"email": new_email}
        )
        
        # Assert: Signup successful
        assert signup_response.status_code == 200
        
        # Act: Get updated state
        updated_activities_response = client.get("/activities")
        updated_activities = updated_activities_response.json()
        
        # Assert: Participant added
        assert new_email in updated_activities[activity_name]["participants"]
        assert len(updated_activities[activity_name]["participants"]) == initial_participants + 1