import logging

from textual.app import ComposeResult
from textual.containers import Center, Vertical
from textual.screen import Screen
from textual.widgets import Button, Input, Label, Static
from utility import ReValidator

logger = logging.getLogger(__name__)


class RegisterScreen(Screen):
	CSS = """
	#register-form {
	width: 50;
	height: auto;
	padding: 1 2;
	border: round $primary;
	}

	#register-form Input {
	margin-top: 1;
	margin-bottom: 1;
	}

	#register-form Button {
	width: 100%;
	margin-top: 1;
	}
	"""

	def compose(self) -> ComposeResult:
		with Center():
			with Vertical(id="register-form"):
				yield Label("Digite seu cpf")
				yield Input(
					id="cpf",
					max_length=14,
					)
				yield Button(
					"Avançar",
					id="submit_cpf",
					variant="primary",
					)
				yield Button("Retornar", id="back")
				yield Static("", id="status")

	def on_button_pressed(self, event: Button.Pressed) -> None:
		if event.button.id == "back":
			self.app.pop_screen()
		elif event.button.id == "submit_cpf":
			cpf = self.query_one("#cpf", Input).value.strip()
			validator = ReValidator(cpf)
			if not validator.validate_cpf():
				logger.warning("Tentativa de cadastro com cpf inválido.")
				self.query_one("#status", Static).update(
					"Cpf inválido, tente novamente"
				)
				return
			logger.info("Validação de CPF concluída com sucesso.")
			self.query_one("#status", Static).update(
				"Boa! Avançando pra próxima etapa!"
			)