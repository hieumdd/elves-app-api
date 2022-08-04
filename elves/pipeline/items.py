from elves.pipeline import interface

pipeline = interface.Pipeline(
    name="Items",
    url="https://hooks.elvesapp.com/webhook/analytics/items",
    transform=lambda rows: [
        {
            "request_id": row.get("request_id"),
            "status": row.get("status"),
            "created_at": row.get("created_at"),
            "completed_at": row.get("completed_at"),
            "merchant": row.get("merchant"),
            "vertical": row.get("vertical"),
            "user_id": row.get("user_id"),
            "elf_id": row.get("elf_id"),
            "headline": row.get("headline"),
            "title": row.get("title"),
            "quantity": row.get("quantity"),
            "price": row.get("price"),
            "price_original": row.get("price_original"),
            "cost": row.get("cost"),
        }
        for row in rows
    ],
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
