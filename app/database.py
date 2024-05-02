from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import List, Optional


@dataclass
class RedisDataBase:
    key: bytes
    value: bytes
    expiry: datetime

    def is_expired(self) -> bool:
        if datetime.now() >= self.expiry:
            del self
            return True
        return False


class RedisDataBaseManager:
    def __init__(self):
        self.records: List[RedisDataBase] = []

    def add_record(self, key: bytes, value: bytes, expiry: bytes) -> None:
        expiry_str = expiry.decode()
        expiry_datetime = datetime.now() + timedelta(milliseconds=int(expiry_str))
        record = RedisDataBase(key, value, expiry_datetime)
        self.records.append(record)

    def fetch_record_by_key(self, key: bytes) -> Optional[RedisDataBase]:
        for record in self.records:
            if record.key == key and not record.is_expired():
                return record
