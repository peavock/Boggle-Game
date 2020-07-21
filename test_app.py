from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle

app.config['TESTING']=True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!

    def test_welcome(self):
        with app.test_client() as server:
            res = server.get('/')
            self.assertEqual(res.status_code,200)
            html = res.get_data(as_text=True)
            
            self.assertIn("<h1>Let's Play Boggle!</h1>",html)

    def test_begin(self):
        with app.test_client() as server:
            res = server.get('/begin')
            self.assertEqual(res.status_code,200)

    # def test_redirection(self):
    #     with app.test_client() as server:
    #         res = server.get('/redirect-me')
    #         self.assertEqual(res.status_code,302)
    #         self.assertEqual(res.location,'http://localhost/')

    # def test_redirection_folowed(self):
    #     with app.test_client() as server:
    #         res = server.get('/redirect-me',follow_redirects = True)
    #         self.assertEqual(res.status_code,200)
    #         html = res.get_data(as_text=True)
    #         self.assertIn('<h1>Color Form</h1>',html)

    # def test_session_count_set(self):
    #     with app.test_client() as server:
    #         # res = server.get('/')
    #         # server.get('/')
    #         # server.get('/')
    #         # server.get('/')
    #         with server.session_transaction() as change_session:
    #             change_session['count']=999

    #         res = server.get('/') 

    #         self.assertEqual(res.status_code,200)