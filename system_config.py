def create_service_config(service_name, port=80, retries=3, ssl_enabled=False):
    service_config = {
        "service": service_name,
        "port": port,
        "retries": retries,
        "ssl": ssl_enabled
    }
    return service_config
service_config = create_service_config("httpd", 443, ssl_enabled=True)

print(service_config)