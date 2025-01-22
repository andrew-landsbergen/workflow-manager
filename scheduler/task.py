class Task:
    name = ""
    priority = 1

    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    def __repr__(self):
        return f"Task(name='{self.name}', priority='{self.priority}')"
    
    def to_dict(self):
        return {
            "name": self.name,
            "priority": self.priority
        }

    @staticmethod
    def from_dict(data):
        return Task(
            name = data.get("name"),
            priority = data.get("priority")
        )