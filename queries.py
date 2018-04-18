import database as db


def get_restaurants():
    return db.query_db("SELECT id, name, category FROM restaurant")


def get_restaurant(id):
    return db.query_db(
        "SELECT id, name, category FROM restaurant WHERE id = %s",
        args=(id,)
    )


def post_restaurant(body):
    return db.query_db(
        "INSERT INTO restaurant VALUES (%s, %s, %s)",
        args=(None, body['name'], body['category']),
        post=True
    )


def delete_restaurant(id):
    return db.query_db("DELETE FROM restaurant WHERE id = %s", args=(id,))


def get_menu_items():
    return db.query_db("SELECT * FROM menu_item")


def get_menu_item(id):
    return db.query_db(
        "SELECT id, name, cost FROM menu_item WHERE id = %s",
        args=(id,)
    )


def post_menu_item(body):
    return db.query_db(
        "INSERT INTO menu_item VALUES (%s, %s, %s)",
        args=(None, body['name'], body['cost']), post=True)


def delete_menu_item(id):
    return db.query_db("DELETE FROM menu_item WHERE id = (%s)", args=(id,))


def update_menu_item(menu_item_id, n, c):
    return db.query_db(
        """
        UPDATE menu_item
        SET name = %s, cost = %s
        WHERE id = %s
        """,
        args=(n, c, menu_item_id)
    )


def get_menus():
    return db.query_db("SELECT name, description, id FROM menu")


def get_menu(id):
    return db.query_db(
        "SELECT id, name, description FROM menu WHERE id = %s",
        args=(id,)
    )


def post_menu(body):
    return db.query_db(
        "INSERT INTO lists VALUES (%s, %s, %s)",
        args=(None, body['name'], body['description']),
        post=True
    )


def update_menu(menu_id, n, d):
    return db.query_db(
        """
        UPDATE menu
        SET name = %s, description = %s
        WHERE id = %s
        """,
        args=(n, d, menu_id)
    )


def delete_menu(id):
    return db.query_db("DELETE FROM menu WHERE id = (%s)", args=(id))


def post_menu_to_restaurant(menu_id, restaurant_id):
    return db.query_db(
        """
        INSERT INTO restaurant_menus VALUES (%s, %s)
        """,
        args=(menu_id, restaurant_id),
        post=True
    )


def delete_menu_from_restaurant(menu_id, restauraunt_id):
    return db.query_db(
        """
        DELETE FROM restaurant_menus WHERE menu_id = restaurant_menus.menu_id
        AND restaurant_id = restaurant_menus.restaurant_id
        """,
        args=(menu_id, restaurant_id)
    )


def post_menu_item_to_menu(menu_item_id, menu_id):
    return db.query_db(
        """
        INSERT INTO restaurant_menus VALUES (%s, %s)
        """,
        args=(menu_id, restaurant_id),
        post=True
    )


def get_items_on_menu(menu_id):
    return db.query_db(
        """
        SELECT menu_items.name, menu_items.cost
        FROM items_on_menu
        INNER JOIN menu on menu.id = items_on_menu.menu_id
        INNER JOIN menu_item on menu_item.id = items_on_menu.menu_item_id
        """
    )


def delete_menu_item_from_menu(menu_item_id, menu_id):
    return db.query_db(
        """
        DELETE FROM items_on_menu WHERE menu_item_id = items_on_menu.menu_item_id
        AND menu_id = items_on_menu.menu_id
        """,
        args=(menu_item_id, menu_id)
    )


def get_menus_of_restaurant(restaurant_id):
    return db.query_db(
        """
    SELECT menu.name, menu.description
    FROM restaurant_menus
    INNER JOIN menu on menu.id = restaurant_menus.menu_id
    INNER JOIN restaurant on restauraunt.id = restaurant_menus.restaurant_id
    """
    )
