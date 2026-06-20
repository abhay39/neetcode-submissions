class TimeMap:

    def __init__(self):
        self.info={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.info:
            self.info[key] = []

        self.info[key].append({
            "val": value,
            "timestamp": timestamp
        })

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.info:
            return ""

        result = ""

        for item in self.info[key]:
            if item["timestamp"] <= timestamp:
                result = item["val"]
            else:
                break

        return result