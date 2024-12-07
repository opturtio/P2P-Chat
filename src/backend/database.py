from db import db
from logger import logger
from sqlalchemy import text
from datetime import datetime

def insert_message(msg):
    created_at = datetime.fromtimestamp(msg["timestamp"])
    sql = text("INSERT INTO messages (msg, sender, created_at) VALUES (:msg, :sender, :created_at)")
    db.session.execute(sql, {"msg": msg["message"], "sender": msg["sender"], "created_at": created_at})
    db.session.commit()
    logger.info(f"database/insert_message: Message inserted into DB: {msg}")


def insert_peer(user_id, name, ip, priority):
    sql = "INSERT INTO peers (user_id, name, ip, priority) VALUES (:user_id, :name, :ip, :priority) VALUES ()"
    db.session.execute(sql, {"user_id":user_id, "name":name, "ip":ip, "priority":priority})
    db.session.commit()
    logger.info(f"database/insert_peer: Peer inserted into DB: Name: {name}, IP: {ip}")

def fetch_peers():
    sql = "SELECT * FROM peers"
    result = db.session.execute(sql)
    logger.info("database_fetch_peers: Fetched all peers from DB!")
    return result.fetchall()