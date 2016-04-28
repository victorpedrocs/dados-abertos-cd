import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Sequence, ForeignKey, DateTime
from sqlalchemy.orm import relationship


# creating engine
user = "dadosabertos"
password = "dadosabertos"
host = "localhost:5432"

engine = create_engine("postgresql://{0}:{1}@{2}".format( user, password, host ), echo=True)
Base = declarative_base()

class Partido(Base):
    """Modelo para a classe partido"""
    __tablename__ = 'partido'

    id = Column(Integer, Sequence( 'partido_sq' ), primary_key = True)
    sigla = Column( String(10) )
    nome = Column( String )

    parlamentares = relationship( "Legislatura", backref="partido" )

class Estado(Base):
    """Modelo para a classe estado"""

    __tablename__ = 'estado'

    id = Column( Integer, Sequence( 'estado_sq' ), primary_key=True )
    sigla = Column( String(2) )
    nome = Column( String )

    parlamentares = relationship( "Legislatura", backref="estado" )

class Parlamentar(Base):
    """Modelo para a classe parlamentar"""

    __tablename__ = 'parlamentar'

    id = Column( Integer, Sequence( 'parlamentar_sq' ), primary_key=True )
    identificador_unico = Column( Integer )
    nome = Column( String )

    legislaturas = relationship( "Legislatura", backref="parlamentar")

class Legislatura(Base):
    """Modelo para a classe legislatura, este modelo serve para diferenciar as legislaturas do parlamentar"""

    __tablename__ = 'legislatura'

    id = Column( Integer, Sequence( 'legislatura_sq'), primary_key=True )
    numero = Column( Integer )
    numero_carteira = Column( Integer )

    parlamentar_fk = Column( Integer, ForeignKey('parlamentar.id') )
    partido_fk = Column( Integer, ForeignKey('partido.id') )
    estado_fk = Column( Integer, ForeignKey('estado.id') )

    documentos = relationship( "Documento", backref="legislatura")


class Fornecedor(Base):
    """Modelo para a classe fornecedor"""

    __tablename__ = 'fornecedor'

    id = Column( Integer, Sequence( 'fornecedor_sq' ), primary_key=True )
    cnpj = Column( String )
    nome = Column( String )

    documentos = relationship( "Documento", backref="fornecedor")

class Documento(Base):
    """Modelo para a classe documento"""

    __tablename__ = 'documento'

    id = Column( Integer, Sequence( 'documento_sq' ), primary_key=True )
    numero_documento = Column( String )
    tipo_documento = Column( String )
    data_emissao = Column( DateTime )
    valor_documento = Column( Float )
    valor_glossa = Column( Float )
    valor_liquido = Column( Float )
    mes = Column( Integer )
    ano = Column( Integer )
    numero_parcela = Column( String )
    nome_passageiro = Column( String )
    trecho = Column( String )
    numero_lote = Column( String )
    numero_ressarcimento = Column( String )
    valor_restituicao = Column( Float )
    indentificador_solicitante = Column( String )
    numero_subcota = Column( String )
    descricao_subcota = Column( String )
    num_especificacao_subcota = Column( String )
    descricao_especificacao_subcota = Column( String )

    legislatura_fk = Column( Integer, ForeignKey('legislatura.id') )

    fornecedor_fk = Column( Integer, ForeignKey('fornecedor.id') )

def get_or_create(session, model, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        instance = model(**kwargs)
        session.add(instance)
        session.commit()
        return instance
