import os
from flask import Flask, request, jsonify, json, render_template
from flask_cors import CORS, cross_origin
import database as db
import queries

app = Flask(__name__)
CORS(app)
app.url_map.strict_slashes = False

try:
    @app.route("/",  methods=['GET', 'POST'])
    @cross_origin()
    def index():
        route_definitions = [
            {
                "route_name": "/restaurant, /restaurant/{restaurant_id}",
                "methods": {
                    "get": "Returns all restaurants / one given an id a restaurant",
                    "post": "Add a resturaunt, fields name and category required",
                    "delete": "remove resturaunt"
                }
            },
            {
                "route_name": "/menu, /menu/{menu_id}",
                "methods": {
                    "get": "Returns all menus / one given an id of a menu",
                    "post": "Add a menu, requires name and description",
                    "delete": "Remove a menu"
                }
            },
            {
                "route_name": "/menu_item/, /menu_item/{menu_item_id}",
                "methods": {
                    "get": "Returns all memu items / one given a menu item id",
                    "post": "Add a menu item, requires name and cost",
                    "delete": "Remove menu item"
                }
            },
            {
                "route_name": "/restaurant/{restaurant_id}/menu",
                "methods": {
                    "get": "Returns menu(s) of a specific restaurant",
                    "post": "Adds a menu to a specific restaurant",
                    "delete": "Deletes a menu from a restaurant"
                }
            },
            {
                "route_name": "/menu/{menu_id}/menu_items",
                "methods": {
                    "get": "Returns menu item(s) on a specific menu",
                    "post": "Adds a menu item to a specific menu",
                    "delete": "Deletes a menu item from a specific menu"
                }
            }
        ]

        return jsonify(route_definitions)

    @app.route("/restaurant", methods=['GET', 'POST'])
    @cross_origin()
    def restaurants():
        if (request.method == "POST"):
            body = request.get_json()
            result_id = queries.post_restaurant(body=body)
            body['id'] = result_id
            return jsonify(body)
        elif (request.method == "GET"):
            restaurants = queries.get_restaurants()
            return jsonify(restaurants)
        return "invalid method"

    @app.route("/restaurant/<int:restaurant_id>/", methods=['GET', 'POST', 'DELETE'])
    @cross_origin()
    def restaurant(restaurant_id):
        if (request.method == "POST"):
            body = request.get_json()
            result_id = queries.post_restaurant(body=body)
            body['id'] = result_id
            return jsonify(body)
        elif (request.method == "GET"):
            restaurant = queries.get_restaurant(restaurant_id)
            return jsonify(restaurant)
        try:
            if (request.method == "DELETE"):
                body = request.get_json()
                return jsonify(queries.delete_restaurant(restaurant_id))
        except Exception as e:
            print(e)
        return "invalid method"

    @app.route("/menu/", methods=['GET', 'POST', 'PUT', 'DELETE'])
    @cross_origin()
    def menus():
        if (request.method == "POST"):
            body = request.get_json()
            result_id = queries.post_menu(body=body)
            body['id'] = result_id
            return jsonify(body)
        elif (request.method == "GET"):
            menus = queries.get_menus()
            return jsonify(menus)
        return "error invalid method"

    @app.route("/menu/<int:menu_id>/", methods=['GET', 'POST', 'PUT', 'DELETE'])
    @cross_origin()
    def menu(menu_id):
        if (request.method == "POST"):
            body = request.get_json()
            result_id = queries.post_menu(body=body)
            body['id'] = result_id
            return jsonify(body)
        elif (request.method == "GET"):
            menu = queries.get_menu(menu_id)
            return jsonify(menu)
        elif (request.method == "PUT"):
            body = request.get_json()
            m_name = body['name']
            m_description = body['description']
            menu = queries.update_menu(menu_id, m_name, m_description)
            return jsonify(menu)
        try:
            if (request.method == "DELETE"):
                return jsonify(queries.delete_menu(menu_id))
        except Exception as e:
            print(e)
        return "error invalid method"

    @app.route("/menu_item/", methods=['GET', 'POST', 'PUT', 'DELETE'])
    @cross_origin()
    def menu_items():
        if (request.method == "POST"):
            body = request.get_json()
            result_id = queries.post_menu(body=body)
            body['id'] = result_id
            return jsonify(body)
        elif (request.method == "GET"):
            menu_items = queries.get_menu_items
            return jsonify(menu_items)
        return "error invalid method"

    @app.route("/menu_item/<int:menu_item_id>/", methods=['GET', 'POST', "DELETE", "PUT"])
    @cross_origin()
    def menu_item(menu_item_id):
        if (request.method == "POST"):
            body = request.get_json()
            result_id = queries.post_menu_item(body=body)
            body['id'] = result_id
            return jsonify(body)
        elif (request.method == "GET"):
            menu_item = queries.get_menu_item(menu_item_id)
            return jsonify(menu_item)
        elif (request.method == "DELETE"):
            return jsonify(queries.delete_menu_item(menu_item_id))
        elif (request.method == "PUT"):
            body = request.get_json()
            m_i_name = body['name']
            m_i_cost = body['cost']
            menu_item = queries.update_menu_item(menu_id, m_name, m_description)
            return jsonify(menu_item_id)
        return "error: invalid method"

    @app.route("/restaurant/<int:restaurant_id>/menu", methods=['GET', 'POST', 'PUT', 'DELETE'])
    @cross_origin()
    def menus_of_restaurant(menu_id, restaurant_id):
        if (request.method == "POST"):
            body = request.get_json()
            result_id = queries.post_menu_to_restaurant(body=body)
            body['id'] = result_id
            return jsonify(body)
        elif (request.method == "GET"):
            return jsonify(queries.get_menus_of_restaurant(restaurant_id))
        elif (request.method == "DELETE"):
            return jsonify(queries.delete_menu_from_restaurant(menu_id, restaurant_id))
        return "error invalid method"

    @app.route("/menu/<int:menu_id>/menu_items", methods=['GET', 'POST', 'DELETE'])
    @cross_origin()
    def items_on_menu(menu_id, menu_item_id):
        if (request.method == "POST"):
            body = request.get_json()
            result_id = queries.post_menu_item_to_menu(body=body)
            body['id'] = result_id
            return jsonify(body)
        elif (request.method == "GET"):
            return jsonify(queries.get_items_on_menu(menu_id))
        elif (request.method == "DELETE"):
            return jsonify(queries.delete_menu_item_from_menu(menu_item_id, menu_id))
        return "error invalid method"
except Exception as e:
    print(e)


if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 3000)))
    app.run()
