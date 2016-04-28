create table partido (
  id serial primary key,
  sigla varchar,
  nome varchar
);

create table estado (
  id serial primary key,
  nome varchar,
  sigla varchar(2)
);

create table parlamentar (
  id serial primary key,
  identificador_unico integer,
  nome varchar,
  numero_carteira integer,
  partido_fk integer REFERENCES partido( id ),
  estado_fk integer REFERENCES estado( id )
);

create table fornecedor (
  id serial primary key,
  cnpj varchar(14),
  nome varchar(200)
);

create table documento (
  id serial primary key,
  parlamentar_fk integer REFERENCES parlamentar( id ),
  fornecedor_fk integer REFERENCES fornecedor( id ),
  numero_documento integer,
  tipo_documento integer,
  data_emissao date,
  valor_documento real,
  valor_glossa real,
  valor_liquido real,
  mes smallint,
  ano smallint,
  numero_parcela integer,
  nome_passageiro varchar,
  trecho varchar,
  numero_lote integer,
  numero_ressarcimento integer,
  valor_restituicao real,
  indentificador_solicitante integer,
  numero_subcota integer,
  descricao_subcota varchar,
  num_especificacao_subcota integer,
  descricao_especificacao_subcota varchar
);
