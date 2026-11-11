from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from datetime import datetime

class WebhookHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)
        data = json.loads(body.decode('utf-8'))

        group_category = data.get('groupLabels', {}).get('category', 'unknown')
        print(f"\n[{datetime.now().strftime('%H:%M:%S')}] === ГРУППА: {group_category.upper()} ===")

        for alert in data.get('alerts', []):
            status = alert.get('status', '').upper()
            name = alert.get('labels', {}).get('alertname')
            desc = alert.get('annotations', {}).get('description')
            color = "\033[91m" if status == "FIRING" else "\033[92m"
            reset = "\033[0m"
            print(f"Статус: {color}{status}{reset} | Алерт: {name} | Инфо: {desc}")

        self.send_response(200)
        self.end_headers()

    def log_message(self, format, *args):
        return 

if __name__ == '__main__':
    print("Webhook-сервер запущен на порту 5001. Ожидание алертов...")
    HTTPServer(('0.0.0.0', 5001), WebhookHandler).serve_forever()