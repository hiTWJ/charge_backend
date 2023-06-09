from http.server import HTTPServer, SimpleHTTPRequestHandler
import socketserver
import json


# 创建一个自定义的 HTTP 请求处理器
class CORSRequestHandler(SimpleHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type,Authorization")
        self.end_headers()

    # 重写 do_GET 方法以返回 JSON 格式的数据响应
    def do_GET(self):
        self.send_response(200)  # 设置响应状态码为 200
        self.send_header("Content-type", "application/json")  # 告诉浏览器返回的是 JSON 格式的数据
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        if self.path == "/query_queue":
            # 构造你需要返回的 JSON 数据
            data = {
                "code": 0,
                "message": "success?",
                "data": [
                    {
                        "pile_id": "P1",
                        "username": "12345678",
                        "battery_size": "60.00",
                        "require_amount": "12.34",
                        "waiting_time": 600,
                    },
                    {
                        "pile_id": "P2",
                        "username": "12345",
                        "battery_size": "60.00",
                        "require_amount": "56.78",
                        "waiting_time": 800,
                    },
                ],
            }
            # 将 Python 字典转换为 JSON 字符串，并返回到浏览器
            self.wfile.write(json.dumps(data).encode())
        if self.path == "/query_pile":
            # 构造你需要返回的 JSON 数据
            data = {
                "code": 0,
                "message": "success?",
                "data": [
                    {
                        "pile_id": "P1",
                        "status": "RUNNING",
                        "total_usage_times": 53,
                        "total_charging_time": 287218,
                        "total_charging_amount": "2191.32",
                    },
                    {
                        "pile_id": "P1",
                        "status": "RUNNING",
                        "total_usage_times": 53,
                        "total_charging_time": 287218,
                        "total_charging_amount": "2191.32",
                    },
                ],
            }
            # 将 Python 字典转换为 JSON 字符串，并返回到浏览器
            self.wfile.write(json.dumps(data).encode())
        if self.path == "/query_report":
            # 构造你需要返回的 JSON 数据
            data = {
                "code": 0,
                "message": "success?",
                "data": [
                    {
                        "day": 65,
                        "week": 9,
                        "month": 2,
                        "pile_id": "P1",
                        "total_usage_times": 173,
                        "total_charging_time": 1200000,
                        "total_charging_amount": "1873.25",
                        "total_charging_earning": "2312.12",
                        "total_service_earning": "121.08",
                        "total_earning": "2433.20",
                    },
                    {
                        "day": 65,
                        "week": 9,
                        "month": 2,
                        "pile_id": "P1",
                        "total_usage_times": 173,
                        "total_charging_time": 1200000,
                        "total_charging_amount": "1873.25",
                        "total_charging_earning": "2312.12",
                        "total_service_earning": "121.08",
                        "total_earning": "2433.20",
                    },
                ],
            }
            # 将 Python 字典转换为 JSON 字符串，并返回到浏览器
            self.wfile.write(json.dumps(data).encode())
        if self.path == "/query_order":
            # 构造你需要返回的 JSON 数据
            data = {
                "code": 0,
                "message": "success?",
                "data": [
                    {
                        "order_id": "20230501000001",
                        "create_time": "2023-05-01T12:11:11.000Z",
                        "charged_amount": "12.34",
                        "charged_time": 600,
                        "begin_time": "2023-05-01T11:11:11.000Z",
                        "end_time": "2023-05-01T12:11:11.000Z",
                        "charging_cost": "8.92",
                        "service_cost": "1.23",
                        "total_cost": "10.15",
                        "pile_id": "C01",
                    },
                    {
                        "order_id": "20230501000001",
                        "create_time": "2023-05-01T12:11:11.000Z",
                        "charged_amount": "12.34",
                        "charged_time": 600,
                        "begin_time": "2023-05-01T11:11:11.000Z",
                        "end_time": "2023-05-01T12:11:11.000Z",
                        "charging_cost": "8.92",
                        "service_cost": "1.23",
                        "total_cost": "10.15",
                        "pile_id": "C01",
                    },
                ],
            }
            # 将 Python 字典转换为 JSON 字符串，并返回到浏览器
            self.wfile.write(json.dumps(data).encode())
        if self.path == "/get_time":
            # 构造你需要返回的 JSON 数据
            data = {
                "code": 0,
                "message": "success?",
                "data": {
                    "datetime": "2023-05-01T11:11:11.000Z",
                    "timestamp": 1654087836,
                },
            }
            # 将 Python 字典转换为 JSON 字符串，并返回到浏览器
            self.wfile.write(json.dumps(data).encode())
        if self.path == "/preview_queue":
            # 构造你需要返回的 JSON 数据
            data = {
                "code": 0,
                "message": "success",
                "data": {
                    "charge_id": "F7",
                    "queue_len": 4,
                    "cur_state": "NOTCHARGING",
                    "place": "WAITINGPLACE",
                },
            }
            # 将 Python 字典转换为 JSON 字符串，并返回到浏览器
            self.wfile.write(json.dumps(data).encode())
        if self.path == "/end_request":
            data = {"code": 0, "message": "success"}
            self.wfile.write(json.dumps(data).encode())

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        if self.path == "/account_login":
            # 构造你需要返回的 JSON 数据
            data = {
                "code": 0,
                "data": {
                    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6ImppbnVvIiwiaWF0IjoxNTE2MjM5MDIyfQ.WhOxJUL0ZfPW6zrLNdkbQvoE8JObEB_5kr9DkgEVDeE",
                    "is_admin": True,
                },
                "message": "success?",
            }
            # 将 Python 字典转换为 JSON 字符串，并返回到浏览器
            self.wfile.write(json.dumps(data).encode())
        if (
            self.path == "/submit_request"
            or self.path == "/edit_request"
            or self.path == "/account_register"
            or self.path == "/update_pile"
        ):
            data = {"code": 0, "message": "success"}
            self.wfile.write(json.dumps(data).encode())
        content_length = int(self.headers["Content-Length"])
        data_body = self.rfile.read(content_length)
        print(data_body)


# 指定监听的端口
port = 8000

httpd = HTTPServer(("localhost", 8000), CORSRequestHandler)
httpd.serve_forever()
