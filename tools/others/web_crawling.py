# coding=utf-8
from core import KryptonHub
from core import HackingToolsCollection


class GoSpider(KryptonHub):
    TITLE = "Gospider"
    DESCRIPTION = "Gospider - Fast web spider written in Go"
    INSTALL_COMMANDS = ["sudo go get -u github.com/jaeles-project/gospider"]
    PROJECT_URL = "https://github.com/jaeles-project/gospider"

    def __init__(self):
        super(GoSpider, self).__init__(runnable = False)


class WebCrawlingTools(HackingToolsCollection):
    TITLE = "Web crawling"
    TOOLS = [GoSpider()]
