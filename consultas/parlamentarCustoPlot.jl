using DBI
using PostgreSQL
using Plotly

conn = connect(Postgres, "localhost", "postgresUser", "postrgesSenha", "dadosabertos", 5433)

sql = "SELECT parlamentar.nome,partido.sigla,count(*) as qtd_docs,sum(valor_documento) as valor_total "
sql = string(sql,"FROM legislatura ")
sql = string(sql,"JOIN documento on documento.legislatura_fk = legislatura.id")
sql = string(sql," JOIN partido on legislatura.partido_fk = partido.id")
sql = string(sql," JOIN parlamentar on legislatura.parlamentar_fk = parlamentar.id")
sql = string(sql," group by parlamentar.nome, partido.sigla")

stmt = prepare(conn,sql)
result = execute(stmt)

parlamentarPartidoVet = []
valorTotalVet = []
for row in result
  parlamentarPartido = string(row[1],"/",row[2])
  parlamentarPartidoVet = vcat(parlamentarPartidoVet,parlamentarPartido)
  valorTotalVet = vcat(valorTotalVet,int(row[4]))
end


Plotly.set_credentials_file({"username"=>"userPlotLy","api_key"=>"apiKeyPlotly"})
data = [
  [
    "x" => parlamentarPartidoVet,
    "y" => valorTotalVet,
    "type" => "bar"
    ]
  ]
response = Plotly.plot(data, ["filename" => "dadosAbertos\valorTotal", "fileopt" => "overwrite"])
plot_url = response["url"]
