from typing import IO


class HtmlDoc:
    TAB: str = "   "  # HTML indentation tab (default: three spaces)

    def __init__(self, file_name: str, window_title: str) -> None:
        self.__fnam: str = file_name
        self.__wintitle: str = window_title
        self.fd: IO[str] = self.open_html_file()

    def generate_html_file(self) -> None:
        """write_html_file method"""
        self.write_html_head()
        self.write_html_tail()

    def open_html_file(self) -> None:
        return open(self.__fnam, "w")

    def close_html_file(self) -> None:
        self.fd.close()

    def __write_html_comment(self, t: int, com: str) -> None:
        """write_html_comment method"""
        ts: str = HtmlDoc.TAB * t
        self.fd.write(f"{ts}<!--{com}-->\n")

    def write_html_line(self, t: int, line: str) -> None:
        """write_thml_line method"""
        ts: str = HtmlDoc.TAB * t
        self.fd.write(f"{ts}{line}\n")

    def write_html_head(self) -> None:
        """write_html_header method"""
        self.write_html_line(0, "<html>")
        self.write_html_line(0, "<head>")
        self.write_html_line(1, f"<title>{self.__wintitle}</title>")
        self.write_html_line(0, "</head>")
        self.write_html_line(0, "<body>")
        self.__write_html_comment(1, "to be generated")

    def write_html_tail(self) -> None:
        self.write_html_line(0, "</body>")
        self.write_html_line(0, "</html>")