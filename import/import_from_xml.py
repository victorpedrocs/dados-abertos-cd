import urllib
import xml.etree.ElementTree as ET
import zipfile
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import *
from datetime import datetime

print "Iniciando o script..."
url_ano_atual = "http://www.camara.gov.br/cotas/AnoAtual.zip"
url_ano_anterior = "http://www.camara.gov.br/cotas/AnoAnterior.zip"
print "Baixando o arquivo do site da camara..."
file_handler, _ = urllib.urlretrieve(url_ano_atual)
print "Colocando o arquivo em um objeto..."
zip_file_object = zipfile.ZipFile(file_handler, 'r')
print "Removendo o arquivo interno..."
first_file = zip_file_object.namelist()[0]
print "Colocando o arquivo xml em uma variavel..."
file = zip_file_object.open(first_file)
print "Abrindo o arquivo XML com o ElementTree..."
tree = ET.parse(file)
root = tree.getroot()

print "Criando a sessao..."
Session = sessionmaker(engine)
session = Session()

print "Criando os objetos a partir de cada objeto no arquivo xml..."
for despesa in root[0].findall('DESPESA'):
    nome_parlamentar = despesa.find('txNomeParlamentar')
    identificador_unico = despesa.find('ideCadastro')
    numero_carteira = despesa.find('nuCarteiraParlamentar')
    numero_legislatura = despesa.find('nuLegislatura')
    sigla_estado = despesa.find('sgUF')
    sigla_partido = despesa.find('sgPartido')
    codigo_legislatura = despesa.find('codLegislatura')
    numero_subcota = despesa.find('numSubCota')
    descricao_subcota = despesa.find('txtDescricao')
    num_especificacao_subcota = despesa.find('numEspecificacaoSubCota')
    descricao_especificacao_subcota = despesa.find('txtDescricaoEspecificacao')
    nome_fornecedor = despesa.find('txtFornecedor')
    cnpj = despesa.find('txtCNPJCPF')
    numero_documento = despesa.find('txtNumero')
    tipo_documento = despesa.find('indTipoDocumento')
    data_emissao_str = despesa.find('datEmissao')
    valor_documento = despesa.find('vlrDocumento')
    valor_glossa = despesa.find('vlrGlosa')
    valor_liquido = despesa.find('vlrLiquido')
    mes = despesa.find('numMes')
    ano = despesa.find('numAno')
    numero_parcela = despesa.find('numParcela')
    nome_passageiro = despesa.find('txtPassageiro')
    trecho = despesa.find('txtTrecho')
    numero_lote = despesa.find('numLote')
    numero_ressarcimento = despesa.find('numRessarcimento')
    valor_restituicao = despesa.find('vlrRestituicao')
    indentificador_solicitante = despesa.find('nuDeputadoId')

    # if sigla_partido is not None:
    partido_obj = get_or_create(session, Partido, sigla=sigla_partido.text )

    # if sigla_estado is not None:
    estado_obj = get_or_create(session, Estado, sigla=sigla_estado.text )

    # if nome_fornecedor is not None and cnpj is not None:
    fornecedor_obj = get_or_create(session, Fornecedor, nome=nome_fornecedor.text, cnpj=cnpj.text)

    #if nome_parlamentar is not None and identificador_unico is not None:
    parlamentar_obj = get_or_create(session, Parlamentar,
                                    nome=nome_parlamentar.text,
                                    identificador_unico=int(identificador_unico.text) )

    # if numero_legislatura is not None and numero_carteira is not None:
    legislatura_obj = get_or_create(session, Legislatura,
                                    numero=int(numero_legislatura.text),
                                    numero_carteira=int(numero_carteira.text),
                                    partido_fk=partido_obj.id,
                                    estado_fk=estado_obj.id )


    if legislatura_obj is not None:
        documento_obj = Documento()

        if numero_documento is not None:
            documento_obj.numero_documento=numero_documento.text
        if tipo_documento is not None:
            tipo_documento=int(tipo_documento.text)
        if data_emissao_str is not None:
            data_emissao=datetime.strptime(data_emissao_str.text, "%Y-%m-%dT%H:%M:%S")
        if valor_documento is not None:
            valor_documento=float(valor_documento.text)
        if valor_glossa is not None:
            valor_glossa=float(valor_glossa.text)
        if valor_liquido is not None:
            valor_liquido=float(valor_liquido.text)
        if mes is not None:
            mes=int(mes.text)
        if ano is not None:
            ano=int(ano.text)
        if numero_parcela is not None:
            numero_parcela=int(numero_parcela.text)
        if nome_passageiro is not None:
            nome_passageiro=nome_passageiro.text
        if trecho is not None:
            trecho=trecho.text
        if numero_lote is not None:
            numero_lote=int(numero_lote.text)
        if numero_ressarcimento is not None:
            numero_ressarcimento=int(numero_ressarcimento.text)
        if valor_restituicao is not None:
            valor_restituicao=float(valor_restituicao.text)
        if indentificador_solicitante is not None:
            indentificador_solicitante=int(indentificador_solicitante.text)
        if numero_subcota is not None:
            numero_subcota=int(numero_subcota.text)
        if descricao_subcota is not None:
            descricao_subcota=descricao_subcota.text
        if descricao_subcota is not None:
            num_especificacao_subcota=int(num_especificacao_subcota.text)
        if descricao_especificacao_subcota is not None:
            descricao_especificacao_subcota=descricao_especificacao_subcota.text
        if legislatura_obj is not None:
            legislatura_fk=legislatura_obj.id
        if fornecedor_obj is not None:
            fornecedor_fk=fornecedor_obj.id

        session.add(documento_obj)

    session.commit()
