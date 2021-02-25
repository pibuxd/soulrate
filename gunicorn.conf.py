import multiprocessing

bind = "0.0.0.0:5000"
workers = multiprocessing.cpu_count() * 2 - 1
worker_connections = 1000
timeout = 30
keepalive = 2