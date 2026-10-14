import os
import re
import sys

class ReValidator:
	def __init__(self, received_value: str):
		self.received_value = received_value

	def validate_email(self):
		return bool(re.fullmatch(r"(?=.{1,254}\Z)(?=[^@]{2,30}@)[A-Za-z0-9_%+-]+(?:\.[A-Za-z0-9_%+-]+)*@(?:[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?\.)+[A-Za-z]{2,63}", self.received_value))

	def validate_phone(self):
		return bool(re.fullmatch(r"((?:\+?55)\s?)?(?:\([0-9]{2}\)|[0-9]{2})\s?[0-9]{5}-?[0-9]{4}", self.received_value))
	
	def validate_cpf(self):
		if not re.fullmatch(r"\d{11}|\d{3}\.\d{3}\.\d{3}-\d{2}", self.received_value):
			return False
		cpf = [int(digit) for digit in re.sub(r"[^\d]", "", self.received_value)]
		sum = 0
		if len(set(cpf)) == 1: return False
		for i in range(9): sum = sum + (cpf[i] * (10 - i))
		if (sum % 11) >= 2: fdig = 11 - (sum % 11)
		else: fdig = 0
		if cpf[9] != fdig: return False
		sum = 0
		for i in range(10): sum = sum + (cpf[i] * (11 - i))
		if (sum % 11) >= 2: sdig = 11 - (sum % 11)
		else: sdig = 0
		return sdig == cpf[10]