# Reads and writes data to the database
import sqlite3
from sqlite3 import Error

path = "./test.db"


# Create the connection to the database
def create_connection(the_path):
    c_connection = None
    try:
        c_connection = sqlite3.connect(the_path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return c_connection


connection = create_connection(path)


# Function to work with the data
def execute_query(q_connection, query):
    cursor = q_connection.cursor()
    try:
        cursor.execute(query)
        q_connection.commit()
    except Error as e:
        print(f"The error '{e}' occurred")


# Create tables if they don't exist, connect to them if they do
create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    gender TEXT,
    nationality TEXT
);
"""

execute_query(connection, create_users_table)

create_posts_table = """
    CREATE TABLE IF NOT EXISTS posts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id)
);
"""

execute_query(connection, create_posts_table)

create_comments_table = """
CREATE TABLE IF NOT EXISTS comments (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  text TEXT NOT NULL,
  user_id INTEGER NOT NULL,
  post_id INTEGER NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users (id) FOREIGN KEY (post_id) REFERENCES posts (id)
);
"""

create_likes_table = """
CREATE TABLE IF NOT EXISTS likes (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  post_id integer NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users (id) FOREIGN KEY (post_id) REFERENCES posts (id)
);
"""

execute_query(connection, create_comments_table)
execute_query(connection, create_likes_table)

print()


# Function to work with the data
def execute_read_query(r_connection, query):
    cursor = r_connection.cursor()
    #    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


# In this example, prints a list of all the users
select_users = "SELECT * from users"
users = execute_read_query(connection, select_users)

for user in users:
    print(user)

print()

# In this example, prints a list of all the posts
select_posts = "SELECT * FROM posts"
posts = execute_read_query(connection, select_posts)

for post in posts:
    print(post)

print()

# In this example, prints all the posts by a selected user
select_users_posts = """
SELECT
  users.id,
  users.name,
  posts.description
FROM
  posts
  INNER JOIN users ON users.id = posts.user_id
"""

users_posts = execute_read_query(connection, select_users_posts)

for users_post in users_posts:
    print(users_post)

print()

# In this example, prints all the comments
select_posts_comments_users = """
SELECT
  posts.description as post,
  text as comment,
  name
FROM
  posts
  INNER JOIN comments ON posts.id = comments.post_id
  INNER JOIN users ON users.id = comments.user_id
"""

posts_comments_users = execute_read_query(connection, select_posts_comments_users)

for posts_comments_user in posts_comments_users:
    print(posts_comments_user)

print()

# In this example, prints all the likes
select_post_likes = """
SELECT
  description as Post,
  COUNT(likes.id) as Likes
FROM
  likes,
  posts
WHERE
  posts.id = likes.post_id
GROUP BY
  likes.post_id
"""

post_likes = execute_read_query(connection, select_post_likes)

for post_like in post_likes:
    print(post_like)

print()

user = input("What user are you looking for?: ")

# In this example, prints parts of the user's information
select_post_description = (
    "SELECT name, age, nationality FROM users WHERE name = '%s'" % user
)

post_description = execute_read_query(connection, select_post_description)

for description in post_description:
    print(description)  # This was original output
    (name, age, lives) = description  # This unpacks it to a regular tuple
    print(f"{name} is {age} years old, and lives in {lives}.")

print()

# In this example, changes a post by the post text
update_post_description = """
UPDATE
  posts
SET
  description = "The weather has become pleasant now"
WHERE
  id = 2
"""

execute_query(connection, update_post_description)

select_post_description = "SELECT description FROM posts WHERE id = 2"

post_description = execute_read_query(connection, select_post_description)

for description in post_description:
    print(description)
