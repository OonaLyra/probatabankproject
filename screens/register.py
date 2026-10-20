import logging

from textual.app import ComposeResult
from textual.containers import Center, Vertical
from textual.screen import Screen
from textual.widgets import Button, Input, Label, Static
from utility import ReValidator

logger = logging.getLogger(__name__)


class RegisterScreen(Screen):
	STEP_IDS = (
		"step_cpf",
		"step_identity",
	)
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

	.hidden {
	display: none;
	}
	"""
	
	def __init__(self):
		super().__init__()
		self.current_step = 0	
	
	# Screen and steps for register with state management
	def compose(self) -> ComposeResult:
		with Center():
			with Vertical(id="register-form"):
				with Vertical(id="step_cpf"):
					yield Label("Digite seu CPF")
					yield Input(id="cpf", max_length=14)
				with Vertical(id="step_identity", classes="hidden"):
					yield Label("Nome civil")
					yield Input(id="legal_name", max_length=255)
				yield Static("", id="status")
				yield Static("", id="progress")
				yield Button("Voltar", id="back")
				yield Button("Avançar", id="next")
	# This is the lever for changing states
	def on_mount(self) -> None:
		self.show_step()
	# This is for show(in fact, this serves exact to show different steps)
	def show_step(self) -> None:
		for index, step_id in enumerate(self.STEP_IDS):
			self.query_one(f"#{step_id}").display = (
				index == self.current_step
			)
		total_steps = len(self.STEP_IDS)
		self.query_one("#progress", Static).update(
			f"Etapa {self.current_step + 1} de {total_steps}"
		)
		self.query_one("#back", Button).label = (
			"Retornar" if self.current_step == 0
			else "Voltar"
		)
		self.query_one("#next", Button).label = (
			"Confirmar cadastro"
			if self.current_step == total_steps - 1
			else "Avançar"
		)
		self.query_one("#status", Static).update("")
	def on_button_pressed(self, event: Button.Pressed) -> None:
		total_steps = len(self.STEP_IDS)
		if event.button.id == "back":
			if self.current_step > 0:
				self.current_step -= 1
				self.show_step()
			else:
				self.app.pop_screen()
		elif event.button.id == "next":
			if self.current_step < total_steps - 1:
				self.current_step += 1
			else:
				self.query_one("#status", Static).update(
					"Cadastro pronto para validação."
				)
				return
		self.show_step()