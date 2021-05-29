from src.app import app, wordlist_path, censor_symbols
import json
import os
import re
tester = app.test_client()

def test_index():
    response = tester.get("/", content_type="html/text")
    assert response.status_code == 200
    assert b"This is working" in response.data

def test_filter():
    response = tester.get('/filter/test_swear') #Test if swear words are getting censored as expected.
    assert response.status_code == 200
    assert re.match(f'[{censor_symbols}]*', str(response.data))

    response = tester.get('/filter/clean_text') #Test for clean strings.
    assert response.status_code == 200
    assert response.data == b'clean_text'

    response = tester.get('/filter/test_swe ar') #Test for secondry run where whitespaces are ignored.
    assert response.status_code == 200
    assert re.match(f'[{censor_symbols} ]*', str(response.data))

def test_wordlist():
    response = tester.get('/wordlist')
    filter_words = json.load(open(wordlist_path))
    assert response.status_code == 200
    assert all([i.encode() in response.data for i in filter_words])