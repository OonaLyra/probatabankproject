import sqlite3

engine = sqlite3.connect("probatauser.db")
cursor = engine.cursor()

cursor.execute("""
	CREATE TABLE IF NOT EXISTS account_history(
	history_id          INTEGER PRIMARY KEY,        -- identificador único do evento
	account_id          INTEGER NOT NULL,           -- ID da conta alterada
	event_type          TEXT NOT NULL,              -- Tipo de alteração
	old_value           TEXT,                       -- Json snapshot do valor anterior
	new_value           TEXT,                       -- Json snapshot do valor novo
	changed_at          TEXT NOT NULL,              -- De onde a alteração foi feita
	changed_by          INTEGER,                    -- ID do usuário ou operador que alterou este dado
	source              TEXT,                       -- Origem: API, system, admin, etc
	request_id          TEXT,                       -- Identificador da requisição que originou a alteração
	reason              TEXT                        -- Justificativa
	)
"""
)

cursor.execute("""
	CREATE TABLE IF NOT EXISTS transaction_history(
	history_id          INTEGER PRIMARY KEY,        -- identificador único do evento
	transaction_id      INTEGER NOT NULL,           -- ID de transação
	account_id          INTEGER NOT NULL,           -- ID da conta alterada
	changed_at          TEXT NOT NULL,              -- De onde a alteração foi feita
	source              TEXT,                       -- Origem: API, system, admin, etc
	request_id          TEXT,                       -- Identificador da requisição que originou a alteração
	reason              TEXT                        -- Justificativa
	)
"""
)

cursor.execute("""
	CREATE TABLE IF NOT EXISTS user_auth(
	uid                 INTEGER PRIMARY KEY,        -- ID interno
	uemail              TEXT NOT NULL UNIQUE,       -- identificador de login
	username            TEXT NOT NULL UNIQUE,       -- nome de usuário
	password_hash       BLOB NOT NULL,              -- hash da senha
	password_salt       BLOB NOT NULL,              -- salzinho da senha
	created_at          TEXT NOT NULL,              -- data de criação da conta
	email_verified_at   TEXT,                       -- null até o usuário confirmar o e-mail
	last_login_at       TEXT,                       -- null até o primeiro login
	acess_state         TEXT                        -- estado do acesso: pendente, ativo, bloqueado, encerrado.	
	)
"""
)

cursor.execute("""
	CREATE TABLE IF NOT EXISTS user_profile(
	uid                 INTEGER                     -- Chave de referencia ao users.uid
	cpf                 TEXT                        -- Único, validado pela API, identificador cadastral
	phone               TEXT                        -- Telefone de contato, validado pela API, incluindo código do país
	legal_name          TEXT                        -- Nome civil.
	social_name         TEXT                        -- Nome social, opcional, vai sobreescrever qualquer campo de nome dentro do app
	birth_date          TEXT                        -- Data no formato DD-MM-YYYY
	profession          TEXT                        -- Profissão declarada
	monthly_income      TEXT                        -- Lista de faixas de renda salarial de 1, 3, 6, 8 ou mais de 10 salários mínimos.
	dependents_count    TEXT                        -- Contagem de depedentes, podendo ser 0.
	postal_code         TEXT                        -- CEP, validado pela API aberta da via cep
	street              TEXT                        -- Logradouro(preenchido automaticamente pela API aberta da via cep, pode ser reescrito)
	address_number      TEXT                        -- Número do endereço
	address_complement  TEXT                        -- Complemento do endereço, opcional
	district            TEXT                        -- Bairro(validado pela API aberta da via cep, pode ser reescrito.)
	city                TEXT                        -- Cidade(validado pela API aberta da via cep, pode ser reescrito.)
	state               TEXT                        -- Estado(validado pela API aberta da via cep, pode ser reescrito.)
	country             TEXT                        -- País(validado pela API aberta da via cep)
	country_code        TEXT                        -- Código do país.
	)
""")

engine.commit()
engine.close()