insert into public."appPonto_frequencia"(data, pessoa_id)
select current_date,p.user_ptr_id from public."appPonto_pessoa" p
where p.situacao = 'ativo' and not exists (select fr.pessoa_id from public."appPonto_frequencia" fr where fr.data = current_date)
and not exists (select d.data from public."appPonto_dias_sem_expediente" d where d.data = current_date);
