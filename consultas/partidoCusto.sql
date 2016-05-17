SELECT partido.sigla,count(*) as qtd_docs,sum(valor_documento) as valor_total,count(distinct(legislatura_fk))
FROM legislatura
JOIN documento on documento.legislatura_fk = legislatura.id
JOIN partido on legislatura.partido_fk = partido.id
group by partido.sigla
