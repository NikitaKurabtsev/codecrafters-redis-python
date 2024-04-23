from dataclasses import dataclass
from typing import List

@dataclass
class RedisDataBase:
    key: bytes
    value: bytes


class RedisDataBaseManager:
    def __init__(self):
        self.records: List[RedisDataBase] = []

    def add_record(self, key: bytes, value: bytes) -> None:
        record = RedisDataBase(key, value)
        self.records.append(record)

    def fetch_record_by_key(self, key: bytes) -> RedisDataBase:
        for record in self.records:
            if record.key == key:
                return record
