import pytest
from scrappers.products_scrapper.spiders import BaseSpider


class TestUnitAmazonSpider:
    @pytest.fixture
    def base_data(self):
        name = "Base Spider v2"
        query_settings = {
            "query_str_prefix": "search?query=",
            "strings_to_query": [
                "  Creme de barbear",
                "Tacitus Germania ",
                "Notebook  Gamer",
            ],
            "query_strs_postfix": ["&price=10", "&price=250", "&price=5500"],
        }
        domains = [
            "www.loja.com.br",
            "www.loja.com",
            "www.loja.web",
            "www.loja.net",
        ]
        return name, query_settings, domains

    def test_init(self, base_data):
        name, query_settings, domains = base_data

        spider = BaseSpider(
            name=name,
            query_settings=query_settings,
            domains=domains,
        )

        assert spider.name == "Base Spider v2"
        assert spider._query_str_prefix == "search?query="
        assert spider._query_strs == [
            "Creme+de+barbear",
            "Tacitus+Germania",
            "Notebook+Gamer",
        ]
        assert spider.allowed_domains == [
            "https://www.loja.com.br/",
            "https://www.loja.com/",
            "https://www.loja.web/",
            "https://www.loja.net/",
        ]
        assert set(spider.start_urls) == set(
            [
                "https://www.loja.com.br/search?query=",
                "https://www.loja.com/search?query=",
                "https://www.loja.web/search?query=",
                "https://www.loja.net/search?query=",
            ]
        )
