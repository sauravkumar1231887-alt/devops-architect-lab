
#import json
#from http.server import BaseHTTPRequestHandler, HTTPServer


#def health_payload():
 #   return {
  #      "status": "healthy",
   #     "service": "building-management-platform"
    #}


#class Handler(BaseHTTPRequestHandler):
 #   def do_GET(self):
  #      if self.path not in ("/", "/health"):
   #         self.send_error(404, "Not found")
    #        return

     #   body = json.dumps(health_payload()).encode("utf-8")

      #  self.send_response(200)
       # self.send_header("Content-Type", "application/json")
        #self.send_header("Content-Length", str(len(body)))
        #self.end_headers()
        #self.wfile.write(body)


#if __name__ == "__main__":
 #   server = HTTPServer(("0.0.0.0", 8080), Handler)
  #  print("Building Management API listening on port 8080")
   # server.serve_forever()

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


def health_payload():
    return {
        "status": "healthy",
        "service": "building-management-platform"
    }


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path not in ("/", "/health"):
            self.send_error(404, "Not found")
            return

        body = json.dumps(health_payload()).encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8080), Handler)
    print("Building Management API listening on port 8080")
    server.serve_forever()
