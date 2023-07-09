import pytest
from main import app as tbdb_app
from unittest.mock import Mock
from tbdb_client import get_single_movie, get_poster_url, get_single_movie_cast, tbdb_image_url, API_TOKEN


@pytest.fixture
def app():
    return tbdb_app


def test_get_single_movie_cast(monkeypatch):
    mock_response = Mock()
    expected_result = [
        {"cast_id": 1, "character": "Character Name 1", "name": "Actor Name 1"},
        {"cast_id": 2, "character": "Character Name 2", "name": "Actor Name 2"}
    ]
    mock_response.json.return_value = {"cast": expected_result}

    mock_requests_get = Mock(return_value=mock_response)

    monkeypatch.setattr("requests.get", mock_requests_get)

    movie_id = 1
    result = get_single_movie_cast(movie_id)

    expected_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    mock_requests_get.assert_called_once_with(expected_url, headers={"Authorization": f"Bearer {API_TOKEN}"})

    assert result == expected_result



def test_get_single_movie(monkeypatch):
    mock_response = Mock()
    expected_result = {'movie_id': 1, 'title': 'Test Movie'}  
    mock_response.json.return_value = expected_result

    def mock_get(*args, **kwargs):
        return mock_response

    monkeypatch.setattr("requests.get", mock_get)

    result = get_single_movie(1)
    assert result == expected_result


def test_tbdb_image_url():
    profile_path = "test_path"
    size = "w500"
    result = tbdb_image_url(profile_path, size)
    
    expected_url = "https://image.tmdb.org/t/p/w500/test_path"
    
    assert result == expected_url


@pytest.mark.parametrize("list_type", ["now_playing", "top_rated", "upcoming", "popular"])
def test_homepage(monkeypatch, app, list_type):
    api_mock = Mock(return_value={'results': []})
    monkeypatch.setattr("tbdb_client.call_tbdb_api", api_mock)

    with app.test_client() as client:
        response = client.get(f'/?list_type={list_type}')
        assert response.status_code == 200
        api_mock.assert_called_once_with(f'movie/{list_type}')





if __name__ == '__main__':
    unittest.main()