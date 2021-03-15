from src.app import app

tester = app.test_client()

def test_index():
    response = tester.get("/", content_type="html/text")
    assert response.status_code == 200

def test_filter():
    response = tester.get('/filter/test_swear')
    assert response.data == b'----------'

def test_wordlist():
    response = tester.get('/wordlist')
    assert response.status_code == 200