import json
import httpagentparser

from django.forms.models import model_to_dict
from datetime import datetime, timezone
from django.core.cache import cache
from .models import UserProfile


class CachingService:
    def __init__(self, request, response):
        self.request = request
        self.response = response

    def add_to_cache(self):
        if "admin" in self.request.path or "login" in self.request.path:
            return

        if str(self.response.status_code).startswith("3") or str(
            self.response.status_code
        ).startswith("4"):
            return

        key = self.request.path + "_"
        data = UserProfile()

        if self.request.user.is_authenticated and not self.request.user.is_superuser:
            key += self.request.user.username + "_"
            data.user = self.request.user

        if self.request.method == "GET":
            data.request_data = self.request.GET

        if self.request.method == "POST":
            data.request_data = self.request.POST

        data.response_code = self.response.status_code
        data.date_time = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S%z")
        data.url = self.request.path
        data.os = httpagentparser.detect(self.request.headers["User-Agent"])["os"]
        data.http_agent = self.request.headers["User-Agent"]

        key += data.date_time
        return cache.set(key, json.dumps(model_to_dict(data)))


class DatabaseStoreService:
    def __init__(self):
        pass

    def store_cache_in_database(self):
        keys = cache.keys("*")
        if len(keys) == 0:
            return False

        for key in keys:
            value = json.loads(cache.get(key))
            print(value)
            profile = UserProfile(
                user=value["user"],
                date_time=value["date_time"],
                url=value["url"],
                os=value["os"],
                http_agent=value["http_agent"],
                request_data=value["request_data"],
                response_code=value["response_code"],
            )
            profile.save()

        return True
