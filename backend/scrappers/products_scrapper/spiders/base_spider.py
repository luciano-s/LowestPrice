from typing import TypedDict
from itertools import cycle, product
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from typing import Any, Iterable
import scrapy
from scrapy.http import Request, Response


class QuerySettingsType(TypedDict):
    query_str_prefix: str
    strings_to_query: list[str]
    query_str_postfix: list[str]


class BaseSpider(scrapy.Spider):
    def __init__(
        self,
        name: str | None = "Base Spider",
        query_settings: QuerySettingsType = {
            "query_str_prefix": "",
            "strings_to_query": [],
            "query_strs_postfix": [],
        },
        domains: list[str] = [],
        **kwargs: Any,
    ):
        super().__init__(name, **kwargs)
        self._query_str_prefix = query_settings["query_str_prefix"]
        self._query_strs = [
            self.__transform_to_query_string(string)
            for string in query_settings["strings_to_query"]
        ]
        self._query_strs_postfix = query_settings["query_strs_postfix"]
        self.allowed_domains = self.__format_domains(domains)
        self.__validate_initial_data()
        self.start_urls = self.__build_start_urls()

    def start_requests(self) -> Iterable[Request]:
        for url in self.__get_search_urls():
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response: Response, **kwargs: Any) -> Any:
        return super().parse(response, **kwargs)

    def __validate_initial_data(self):
        def validate_postfix(query_strs: list[str], query_strs_postfix: list[str]):
            if not len(query_strs_postfix):
                return
            if len(query_strs_postfix) != len(query_strs):
                raise ValidationError(
                    "A quantidade de pós-fixos das query strings devem ser zero ou igual à quantidade de query strings."
                )

        def validate_domains(domains: list[str]):
            validate = URLValidator()
            for domain in domains:
                try:
                    validate(domain)
                except:
                    raise ValidationError(domain)

        validate_postfix(
            query_strs=self._query_strs,
            query_strs_postfix=self._query_strs_postfix,
        )
        validate_domains(self.allowed_domains)

    def __get_search_urls(self) -> str:
        postfix_gen = (
            cycle([""]) if not self._query_strs_postfix else self._query_strs_postfix
        )
        urls = []
        for query_str, postfix in zip(self._query_strs, postfix_gen):
            urls.append(
                f"{start_url}{query_str}{postfix}" for start_url in self.start_urls
            )
        return urls

    def __transform_to_query_string(self, query_str):
        return " ".join(query_str.split()).replace(" ", "+")

    def __add_backslash(self, url: str) -> str:
        if not url.endswith("/"):
            return f"{url}/"
        return url

    def __add_https_prefix(self, url: str) -> str:
        if not url.startswith("https://"):
            return f"https://{url}"
        return url

    def __format_domains(self, domains: list[str]) -> list[str]:
        urls = []
        for domain in domains:
            url_with_backslah = self.__add_backslash(domain)
            urls.append(self.__add_https_prefix(url_with_backslah))
        return urls

    def __build_start_urls(self) -> list[str]:
        return list(
            map(
                lambda url: "".join(url),
                product(self.allowed_domains, [self._query_str_prefix]),
            )
        )
