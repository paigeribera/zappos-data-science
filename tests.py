from flask import Flask, g, jsonify, json
import mysql.connector
import database
import final
import unittest
import requests
import queries
import json


class TestFlaskApiUsingRequests(unittest.TestCase):

    def __init__(self, test_id, *args, **kwargs):
        super(TestFlaskApiUsingRequests, self).__init__(test_id, *args, **kwargs)
        self.test_id = test_id

    def test_post_restaurant(self):
        data = {'name': 'Test', 'category': 'Test'}
        headers = {'content-type': 'application/json'}
        r = requests.post('http://localhost:3000/restaurant',
                          json=data)
        self.test_id = r.json()['id']
        self.assertEqual(response.json()['id']=self.test_id)
        return r

    def test_get_a_restaurant(self):
        response = requests.get('http://localhost:3000/restaurant/' + str(self.test_id))
        self.assertEqual(response.json()['id'], self.test_id)
        return response

    def test_get_a_menu(self):
        response = requests.get('http://localhost:3000/menu/' + str(self.test_id))
        self.assertEqual(response.json()['id'], self.test_id)
        return response

    def test_delete_menu(self):
        mydata = {}
        mydata['id'] = self.test_id
        r = requests.delete('http://localhost:3000/menu/', params=mydata)
        self.assertEqual(r.status_code, 200)
        return r

    def test_delete_menu_item(self):
        mydata = {}
        mydata['id'] = self.test_id
        r = requests.delete('http://localhost:3000/menu_item/', params=mydata)
        self.assertEqual(r.status_code, 200)
        return r

    def test_delete_menu_doesnt_exist(self):
        mydata = {}
        mydata['id'] = 1000
        r = requests.delete('http://localhost:3000/menu/', params=mydata)
        self.assertEqual(r.status_code, 200)
        return r


class TestFlaskApi(unittest.TestCase):

    def setUp(self, test_id):
        self.app = final.app.test_client()


if __name__ == '__main__':
    unittest.main()
