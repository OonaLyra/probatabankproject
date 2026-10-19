import logging
from textual.app import App, ComposeResult
from textual.containers import  Center, Vertical
from textual.widgets import Buttom, Footer, Header, Static
from screens.register import RegisterScreen
from logs.logging_setup import setup_logging

setup_logging()
log_store = logging.getLogger(__name__)

# All predefined settings for the application layout
class ProbataBank(App):
	TITLE = "PróbataBank"
	SUBTITLE = "by Onix"
	ENABLE_COMMAND_PALETTE = False,
	CSS = """
	Screen {
	align: center-middle;
	}
	#menu {
	width: 44;
	height: auto;
	padding: 1 2;
	border: round $primary;
	}
	#intro {
	text-align: center;
	margin-bottom: 1;
	}
	Button {
	width: 100%;
	margin: 1 0;
	}
	#status {
	margin-top: 1;
	text-align: center;
	}
	"""

	def compose(self) -> ComposeResult:
		yield Header()
		with Center():
			with Vertical(id=menu):
				yield Static("PróbataBank by Onix", id=intro)
				yield Button("Acessar", id="login", variant="primary")
				yield Button("Criar conta", id="register")
				yield Button("Sair", id="exit", variant="error")
				yield Static("System ready",id="status")
		yield Footer()
	
	def on_button_pressed(self, event:Button.Pressed) -> None:
		if event.button.id == "register":
			self.push_screen(RegisterScreen())
		elif event.button.id == "exit":
			self.exit()

if __name__ == "__main__":
	logger.info("Iniciando Próbatabank")
	try:
		ProbataBank().run()
	except Exception:
		logger.exception("Erro fatal na execução da aplicação")
		raise
	finally:
		logger.info("Encerrando Próbatabank")