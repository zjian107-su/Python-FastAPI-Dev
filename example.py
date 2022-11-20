posts
{
    "content": "first content",
    "created_at": "2022-11-19T18:13:21.772191-05:00",
    "published": true,
    "title": "first post",
    "id": 2,
    "owner_id": 6
},

SELECT posts.id AS posts_id, posts.title AS posts_title, posts.content AS posts_content,
posts.published AS posts_published, posts.created_at AS posts_created_at, posts.owner_id AS posts_owner_id
FROM posts
WHERE (posts.title LIKE '%%' || %(title_1)s || '%%')
LIMIT %(param_1)s OFFSET %(param_2)s

[<app.models.Post object at 0x1118e1eb0>, <app.models.Post object at 0x1118e1f40>, <app.models.Post object at 0x1118e1fa0>, <app.models.Post object at 0x1118e1fd0>, <app.models.Post object at 0x1118ea0a0>, <app.models.Post object at 0x1118ea100>, <app.models.Post object at 0x1118ea160>, <app.models.Post object at 0x1118ea1c0>]


result:
{
    "Post": {
        "content": "Updating for Robyn!",
        "created_at": "2022-11-19T22:40:27.467635-05:00",
        "published": true,
        "title": "my name is Daniel",
        "id": 13,
        "owner_id": 6
    }

SELECT posts.id AS posts_id, posts.title AS posts_title, posts.content AS posts_content,
posts.published AS posts_published, posts.created_at AS posts_created_at, posts.owner_id AS posts_owner_id,
count(votes.post_id) AS count_1
FROM posts LEFT OUTER JOIN votes ON votes.post_id = posts.id GROUP BY posts.id



[(<app.models.Post object at 0x106ce61c0>, 2), (<app.models.Post object at 0x106cddeb0>, 0), (<app.models.Post object at 0x106cddfd0>, 2), (<app.models.Post object at 0x106cddf40>, 1), (<app.models.Post object at 0x106ce60a0>, 2), (<app.models.Post object at 0x106ce6160>, 2), (<app.models.Post object at 0x106cddfa0>, 0), (<app.models.Post object at 0x106ce6100>, 2)]
