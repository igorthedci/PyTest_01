import requests
import pytest
import json


class TestBaseClass:

    @classmethod
    def setup_class(cls):
        cls.base_url = "http://pulse-rest-testing.herokuapp.com"

    def test_base_url(self):  # is the root is live
        response = requests.get(self.base_url)
        assert 200 == response.status_code
        return

    def test_404_url(self):  # is 404 page present
        url = self.base_url + '/reFR3ff'
        response = requests.get(url)
        assert 404 == response.status_code
        return

    def test_base_links(self):  # the root contains two links, they are live too
        response = requests.get(self.base_url)
        response_body = response.json()
        expected_body = {"Roles": self.base_url + "/roles", "Books": self.base_url + "/books"}
        assert expected_body == response_body
        url = self.base_url + "/roles"
        response = requests.get(url)
        assert 200 == response.status_code
        url = self.base_url + "/books"
        response = requests.get(url)
        assert 200 == response.status_code
        return


class TestBooksClass:
    @classmethod
    def setup_class(cls):
        cls.base_url = "http://pulse-rest-testing.herokuapp.com"
        cls.roles_url = "http://pulse-rest-testing.herokuapp.com/roles"


class TestRolesClass:

    @classmethod
    def setup_class(cls):
        cls.base_url = "http://pulse-rest-testing.herokuapp.com"
        cls.roles_url = "http://pulse-rest-testing.herokuapp.com/roles"

    def test_role_create(self, role):
        expected_role = dict(name="name1", type="typ1", level=1, book=1)
        response = requests.post(self.url, data=expected_role)  # create an item
        assert response.status_code == 201  # check code === 201
        body = response.json()

        self.role_ids.append(body["id"])  # save id for tearDown()
        #
        for key in role:
            self.assertEqual(str(role[key]).strip(), str(body[key]))
        return True