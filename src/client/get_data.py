import os
import psutil
import requests
import socket
import json


def organizza_dati():
    # Return all data directly without nesting under 'info'
    data = {"username": get_logged_in_user(), "cpu_temperature": get_cpu_temperature(), "internet_connection": is_connected_to_internet(), "ram_usage": get_ram_usage()}
    return json.dumps({"hostname": get_hostname(), "data": data})


def get_hostname():
    return socket.gethostname()


def get_logged_in_user():
    return os.getlogin()


def get_cpu_temperature():
    return "TBD"


def is_connected_to_internet():
    try:
        requests.get("http://www.google.com", timeout=5)
        return True
    except (requests.ConnectionError, requests.Timeout):
        return False


def get_ram_usage():
    memory_info = psutil.virtual_memory()
    return memory_info.percent
