from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
import subprocess

class CurlCLI:
    def __init__(self):
        self.console = Console()

    def run_command(self, command):
        self.console.print(f"[bold cyan]Executing:[/bold cyan] {command}")
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        self.console.print(result.stdout)
        if result.stderr:
            self.console.print(f"[bold red]Error:[/bold red] {result.stderr}")

    def fetch_data(self):
        url = Prompt.ask("🌐 [bold yellow]Enter the URL to fetch data from[/bold yellow]")
        self.run_command(f"curl {url}")

    def download_file(self):
        url = Prompt.ask("💾 [bold yellow]Enter the file URL to download[/bold yellow]")
        self.run_command(f"curl -O {url}")

    def post_request(self):
        url = Prompt.ask("🔄 [bold yellow]Enter the URL to send POST request to[/bold yellow]")
        data = Prompt.ask("📑 [bold yellow]Enter the POST data (param1=value1&param2=value2)[/bold yellow]")
        self.run_command(f"curl -d \"{data}\" -X POST {url}")

    def fetch_headers(self):
        url = Prompt.ask("📬 [bold yellow]Enter the URL to fetch HTTP headers from[/bold yellow]")
        self.run_command(f"curl -I {url}")

    def use_proxy(self):
        proxy = Prompt.ask("🔌 [bold yellow]Enter the proxy (e.g., http://proxy.example.com:8080)[/bold yellow]")
        url = Prompt.ask("🌐 [bold yellow]Enter the URL[/bold yellow]")
        self.run_command(f"curl -x {proxy} {url}")

    def send_cookie(self):
        cookie = Prompt.ask("🍪 [bold yellow]Enter the cookie (e.g., name=value)[/bold yellow]")
        url = Prompt.ask("🌐 [bold yellow]Enter the URL[/bold yellow]")
        self.run_command(f"curl -b \"{cookie}\" {url}")

    def send_user_agent(self):
        user_agent = Prompt.ask("🕵️ [bold yellow]Enter the User-Agent string (e.g., Mozilla/5.0)[/bold yellow]")
        url = Prompt.ask("🌐 [bold yellow]Enter the URL[/bold yellow]")
        self.run_command(f"curl -A \"{user_agent}\" {url}")

    def follow_redirects(self):
        url = Prompt.ask("🔀 [bold yellow]Enter the URL to follow redirects[/bold yellow]")
        self.run_command(f"curl -L {url}")

    def save_output(self):
        url = Prompt.ask("💾 [bold yellow]Enter the URL to save output from[/bold yellow]")
        filename = Prompt.ask("📂 [bold yellow]Enter the output filename[/bold yellow]")
        self.run_command(f"curl -o {filename} {url}")

    def upload_file(self):
        file_path = Prompt.ask("📤 [bold yellow]Enter the file path to upload[/bold yellow]")
        ftp_url = Prompt.ask("🌐 [bold yellow]Enter the FTP URL[/bold yellow]")
        username = Prompt.ask("👤 [bold yellow]Enter the FTP username[/bold yellow]")
        password = Prompt.ask("🔑 [bold yellow]Enter the FTP password[/bold yellow]", password=True)
        self.run_command(f"curl -T {file_path} {ftp_url} --user {username}:{password}")

    def resume_download(self):
        url = Prompt.ask("🔄 [bold yellow]Enter the file URL to resume downloading[/bold yellow]")
        self.run_command(f"curl -C - -O {url}")

    def download_multiple_files(self):
        urls = Prompt.ask("💾 [bold yellow]Enter the URLs separated by space to download multiple files[/bold yellow]")
        for url in urls.split():
            self.run_command(f"curl -O {url}")

    def send_delete_request(self):
        url = Prompt.ask("🗑️ [bold yellow]Enter the URL to send a DELETE request to[/bold yellow]")
        self.run_command(f"curl -X DELETE {url}")

    def verbose_output(self):
        url = Prompt.ask("🔍 [bold yellow]Enter the URL for verbose output[/bold yellow]")
        self.run_command(f"curl -v {url}")

    def silent_mode(self):
        url = Prompt.ask("🤫 [bold yellow]Enter the URL to fetch in silent mode[/bold yellow]")
        self.run_command(f"curl -s {url}")

    def display_progress(self):
        url = Prompt.ask("📊 [bold yellow]Enter the file URL to download with progress display[/bold yellow]")
        self.run_command(f"curl -# -O {url}")

    def send_json_data(self):
        url = Prompt.ask("📮 [bold yellow]Enter the URL to send JSON data to[/bold yellow]")
        json_data = Prompt.ask("📄 [bold yellow]Enter the JSON data[/bold yellow]")
        self.run_command(f"curl -d '{json_data}' -H \"Content-Type: application/json\" -X POST {url}")

    def use_with_api(self):
        url = Prompt.ask("🔗 [bold yellow]Enter the API URL[/bold yellow]")
        token = Prompt.ask("🔑 [bold yellow]Enter the Authorization token[/bold yellow]")
        self.run_command(f"curl -H \"Authorization: Bearer {token}\" {url}")

    def download_in_background(self):
        url = Prompt.ask("⏳ [bold yellow]Enter the file URL to download in the background[/bold yellow]")
        self.run_command(f"curl -O {url} &")

    def send_data_from_file(self):
        url = Prompt.ask("📄 [bold yellow]Enter the URL to send data from file[/bold yellow]")
        file_path = Prompt.ask("📁 [bold yellow]Enter the file path[/bold yellow]")
        self.run_command(f"curl -d @{file_path} -X POST {url}")

    def fetch_from_ftp(self):
        ftp_url = Prompt.ask("🌐 [bold yellow]Enter the FTP URL[/bold yellow]")
        username = Prompt.ask("👤 [bold yellow]Enter the FTP username[/bold yellow]")
        password = Prompt.ask("🔑 [bold yellow]Enter the FTP password[/bold yellow]", password=True)
        self.run_command(f"curl {ftp_url} --user {username}:{password}")

    def fetch_with_authentication(self):
        url = Prompt.ask("🔐 [bold yellow]Enter the URL[/bold yellow]")
        username = Prompt.ask("👤 [bold yellow]Enter the username[/bold yellow]")
        password = Prompt.ask("🔑 [bold yellow]Enter the password[/bold yellow]", password=True)
        self.run_command(f"curl -u {username}:{password} {url}")

    def fetch_with_ssl(self):
        url = Prompt.ask("🔒 [bold yellow]Enter the URL to fetch with SSL warnings ignored[/bold yellow]")
        self.run_command(f"curl -k {url}")

    def send_put_request(self):
        url = Prompt.ask("🔄 [bold yellow]Enter the URL to send a PUT request to[/bold yellow]")
        data = Prompt.ask("📑 [bold yellow]Enter the data to send[/bold yellow]")
        self.run_command(f"curl -X PUT -d \"{data}\" {url}")

    def fetch_response_headers(self):
        url = Prompt.ask("📬 [bold yellow]Enter the URL to fetch only response headers from[/bold yellow]")
        self.run_command(f"curl -I {url}")

    def fetch_with_cookies(self):
        url = Prompt.ask("🍪 [bold yellow]Enter the URL to fetch content with cookies[/bold yellow]")
        cookie_file = Prompt.ask("📄 [bold yellow]Enter the path to the cookies file[/bold yellow]")
        self.run_command(f"curl -b {cookie_file} {url}")

    def fetch_with_custom_headers(self):
        url = Prompt.ask("🔧 [bold yellow]Enter the URL to fetch with custom headers[/bold yellow]")
        header = Prompt.ask("🔧 [bold yellow]Enter the custom header (e.g., Custom-Header: Value)[/bold yellow]")
        self.run_command(f"curl -H \"{header}\" {url}")

    def fetch_with_timeout(self):
        url = Prompt.ask("⏱️ [bold yellow]Enter the URL to fetch with a timeout[/bold yellow]")
        timeout = Prompt.ask("⏱️ [bold yellow]Enter the timeout in seconds[/bold yellow]", default="10")
        self.run_command(f"curl -m {timeout} {url}")

    def fetch_in_verbose_mode(self):
        url = Prompt.ask("🔍 [bold yellow]Enter the URL to fetch in verbose mode[/bold yellow]")
        self.run_command(f"curl -v {url}")

    def fetch_with_progress_meter(self):
        url = Prompt.ask("📊 [bold yellow]Enter the URL to fetch with progress meter[/bold yellow]")
        self.run_command(f"curl -# {url}")

    def show_menu(self):
        while True:
            table = Table(title="🔥 [bold cyan]cURL CLI - Commandes[/bold cyan] 🔥")
            table.add_column("Option", justify="center", style="bold green")
            table.add_column("Description", justify="left")

            table.add_row("1", "🌐 Fetch data from a URL")
            table.add_row("2", "💾 Download a file")
            table.add_row("3", "🔄 Send a POST request")
            table.add_row("4", "📬 Fetch HTTP headers")
            table.add_row("5", "🔌 Use a proxy")
            table.add_row("6", "🍪 Send a cookie with the request")
            table.add_row("7", "🕵️ Send a custom User-Agent")
            table.add_row("8", "🔀 Follow redirects")
            table.add_row("9", "💾 Save output to a file")
            table.add_row("10", "📤 Upload a file via FTP")
            table.add_row("11", "🔄 Resume a download")
            table.add_row("12", "💾 Download multiple files")
            table.add_row("13", "🗑️ Send a DELETE request")
            table.add_row("14", "🔍 Verbose output")
            table.add_row("15", "🤫 Silent mode")
            table.add_row("16", "📊 Display download progress")
            table.add_row("17", "📮 Send JSON data via POST")
            table.add_row("18", "🔗 Use cURL with an API")
            table.add_row("19", "⏳ Download a file in the background")
            table.add_row("20", "📄 Send data from a file in a POST request")
            table.add_row("21", "🌐 Fetch content from an FTP server")
            table.add_row("22", "🔐 Fetch content from a password-protected website")
            table.add_row("23", "🔒 Fetch content from a website with SSL")
            table.add_row("24", "🔄 Send a PUT request")
            table.add_row("25", "📬 Fetch only the response headers")
            table.add_row("26", "🍪 Fetch content from a website with cookies")
            table.add_row("27", "🔧 Fetch content with custom headers")
            table.add_row("28", "⏱️ Fetch content with a timeout")
            table.add_row("29", "🔍 Fetch content in verbose mode")
            table.add_row("30", "📊 Fetch content and display the progress meter")
            table.add_row("q", "[bold red]Quit[/bold red]")

            self.console.print(table)

            choice = Prompt.ask("🤖 [bold cyan]Select an option[/bold cyan]")

            command_methods = {
                "1": self.fetch_data,
                "2": self.download_file,
                "3": self.post_request,
                "4": self.fetch_headers,
                "5": self.use_proxy,
                "6": self.send_cookie,
                "7": self.send_user_agent,
                "8": self.follow_redirects,
                "9": self.save_output,
                "10": self.upload_file,
                "11": self.resume_download,
                "12": self.download_multiple_files,
                "13": self.send_delete_request,
                "14": self.verbose_output,
                "15": self.silent_mode,
                "16": self.display_progress,
                "17": self.send_json_data,
                "18": self.use_with_api,
                "19": self.download_in_background,
                "20": self.send_data_from_file,
                "21": self.fetch_from_ftp,
                "22": self.fetch_with_authentication,
                "23": self.fetch_with_ssl,
                "24": self.send_put_request,
                "25": self.fetch_response_headers,
                "26": self.fetch_with_cookies,
                "27": self.fetch_with_custom_headers,
                "28": self.fetch_with_timeout,
                "29": self.fetch_in_verbose_mode,
                "30": self.fetch_with_progress_meter
            }

            if choice in command_methods:
                command_methods[choice]()
            elif choice == "q":
                self.console.print("[bold red]Exiting the cURL CLI. Goodbye![/bold red] 👋")
                break
            else:
                self.console.print("[bold red]Invalid choice, please try again.[/bold red]")

if __name__ == "__main__":
    cli = CurlCLI()
    cli.show_menu()
