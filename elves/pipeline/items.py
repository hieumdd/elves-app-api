from elves.pipeline import interface

pipeline = interface.Pipeline(
    name="Items",
    url="https://hooks.elvesapp.com/webhook/analytics/items",
    schema=[
        {"name": "request_id", "type": "NUMERIC"},
        {"name": "status", "type": "STRING"},
        {"name": "created_at", "type": "TIMESTAMP"},
        {"name": "completed_at", "type": "TIMESTAMP"},
        {"name": "merchant", "type": "STRING"},
        {"name": "vertical", "type": "STRING"},
        {"name": "user_id", "type": "NUMERIC"},
        {"name": "elf_id", "type": "NUMERIC"},
        {"name": "headline", "type": "STRING"},
        {"name": "title", "type": "STRING"},
        {"name": "quantity", "type": "NUMERIC"},
        {"name": "price", "type": "NUMERIC"},
        {"name": "cost", "type": "NUMERIC"},
    ],
)
