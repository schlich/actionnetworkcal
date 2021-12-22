import requests
from django.conf import settings
from django.apps import apps


class Resource:
    def __init__(self, name, group="main", uuid=None, href=None, resource=None):
        self.name = name
        self.group = group
        self.uuid = uuid
        self.href = href
        self.resource = resource or name

    @property
    def json(self):
        return requests.get(
            self.href
            or "/".join(
                filter(
                    None,
                    ("https://actionnetwork.org/api/v2/", self.name, self.uuid),
                )
            ),
            headers={"OSDI-API-Token": settings.ACTIONNETWORK_API_KEYS[self.group]},
        ).json()

    @property
    def list(self):
        json = self.json
        return json["_embedded"].get(f"osdi:{self.resource}", [])


def get_events():
    return [
        Resource("events", group).list
        for group in settings.ACTIONNETWORK_API_KEYS.keys()
    ]


def save_events(events):
    for event in events:
        apps.get_model("events", "Event").objects.update_or_create(
            id=event["identifiers"][0].split(":")[1],
            defaults={
                "title": event["title"],
                "start": event["start_date"],
                "url": event["browser_url"],
                "description": event["description"],
            },
        )
