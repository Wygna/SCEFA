insert into public."appPonto_frequencia"(data, pessoa_id)
	  select current_date,f.pessoa_ptr_id from public."appPonto_funcionario" f, public."appPonto_dias_sem_expediente" d
	  where f.pessoa_ptr_id not in (select fr.pessoa_id from public."appPonto_frequencia" fr where fr.data =  current_date)
	  and d.data != current_date;