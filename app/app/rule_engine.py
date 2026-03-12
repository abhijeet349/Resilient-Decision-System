import json

class RuleEngine:

    def __init__(self):

        with open("config/config.json") as f:
            config = json.load(f)

        self.rules = config["rules"]

    def check_rule(self, data, rule):

        field = rule["field"]
        op = rule["operator"]
        value = rule["value"]

        if field not in data:
            return False

        if op == "<":
            return data[field] < value

        if op == ">":
            return data[field] > value

        if op == "==":
            return data[field] == value

        return False

    def evaluate(self, data):

        triggered = []

        for rule in self.rules:

            if self.check_rule(data, rule):

                triggered.append(rule["name"])
                return rule["action"], triggered

        return "approved", triggered
