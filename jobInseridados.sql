insert into public."appPonto_frequencia"(data, pessoa_id,inconsistencia)
select current_date,p.user_ptr_id,TRUE from public."appPonto_pessoa" p
where p.situacao = 'Ativo' and not exists (select fr.pessoa_id from public."appPonto_frequencia" fr where fr.data = current_date)
and not exists (select d.data from public."appPonto_diassemexpediente" d where d.data = current_date);