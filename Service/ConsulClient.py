import json
from flask import Flask
import consul

app = Flask(__name__)
consul = Consul(host='localhost', port=8500)


class ConsulClient:
    @staticmethod
    def save_to_consul(data):
        try:
            json_data = json.dumps(data, ensure_ascii=False)
            consul.kv.put('vacancy_data', json_data)
            return True
        except Exception as e:
            print(f"Error saving to Consul: {e}")
            return False