from collection.ConfigArchive import import_config, export_config, get_current_time, get_user, get_posts, get_comments, get_likes, get_notifications, import_config_data, export_config_data

TOOL_MAPPING = {
    "import_config": (import_config, {
        "url": "/configArchive/import",
        "param": {"forceImport": True},
        "req_type": "POST",
        "data": {}
    }),
    "export_config": (export_config, {
        "url": "/configArchive/export",
        "req_type": "GET",
        "param": {},
        "data": {}
    }),
    "get_current_time": (get_current_time, {
        "url": "/time/current",
        "req_type": "GET",
        "param": {},
        "data": {}
    }),
    "get_user": (get_user, {
        "url": "/data/user",
        "req_type": "GET",
        "param": {},
        "data": {}
    }),
    "get_posts": (get_posts, {
        "url": "/data/posts",
        "req_type": "GET",
        "param": {},
        "data": {}
    }),
    "get_comments": (get_comments, {
        "url": "/data/comments",
        "req_type": "GET",
        "param": {},
        "data": {}
    }),
    "get_likes": (get_likes, {
        "url": "/data/likes",
        "req_type": "GET",
        "param": {},
        "data": {}
    }),
    "get_notifications": (get_notifications, {
        "url": "/data/notifications",
        "req_type": "GET",
        "param": {},
        "data": {}
    })
}
