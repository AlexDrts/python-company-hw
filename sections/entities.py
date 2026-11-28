from dataclasses import dataclass, field
from datetime import date


@dataclass
class Employee:
    first_name: str
    last_name: str
    position: str
    email: str | None = None
    since: date | None = None
    skills: list[str] = field(default_factory=list)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


EXECUTIVES = [
    Employee('John', 'Doe', 'Chief Executive Officer', 'ceo@example.com', date(2016, 3, 1), ['Strategy', 'Sales']),
    Employee('Jane', 'Smith', 'Chief Technology Officer', 'cto@example.com', date(2017, 6, 15), ['Python', 'Django', 'AWS']),
    Employee('Alex', 'Brown', 'Chief Financial Officer', None, date(2019, 1, 10), ['Finance', 'Reporting']),
]

PRINCIPLES = [
    {'icon': '🤝', 'title': 'Open doors', 'text': 'Any employee can talk to the management directly.'},
    {'icon': '📊', 'title': 'Decisions based on data', 'text': 'We measure results and plan using numbers.'},
    {'icon': '🌱', 'title': 'Team growth', 'text': 'Every manager is responsible for the growth of the team.'},
]
