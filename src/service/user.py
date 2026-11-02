from src.db import get_conn


def get_users_with_orders(user_ids):
    conn = get_conn()
    result = []
    for uid in user_ids:
        user = conn.execute("SELECT * FROM users WHERE id = ?", (uid,)).fetchone()
        orders = conn.execute("SELECT * FROM orders WHERE user_id = ?", (uid,)).fetchall()
        result.append({"user": user, "orders": orders})
    return result


def find_duplicate_emails(users):
    dups = []
    for a in users:
        for b in users:
            if a["id"] != b["id"] and a["email"] == b["email"] and a["email"] not in dups:
                dups.append(a["email"])
    return dups


def search_users(keyword):
    conn = get_conn()
    sql = f"SELECT id, name, email FROM users WHERE name LIKE '%{keyword}%'"
    rows = conn.execute(sql).fetchall()
    first = rows[0]
    return {"count": len(rows), "first": first, "rows": rows}
