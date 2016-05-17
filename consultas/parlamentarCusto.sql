SELECT parlamentar.nome,partido.sigla,count(*) as qtd_docs,sum(valor_documento) as valor_total
FROM legislatura
JOIN documento on documento.legislatura_fk = legislatura.id
JOIN partido on legislatura.partido_fk = partido.id
JOIN parlamentar on legislatura.parlamentar_fk = parlamentar.id
group by parlamentar.nome, partido.sigla
