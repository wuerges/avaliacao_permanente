<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 5.0//PT_BR">
<html>
<head>
<meta charset="UTF-8">
</head>
<body>

  <h1> Lista de ofertas</h1>

  %for codigo, oferta in ofertas.items():
    <fieldset>
      <p>Turma: <a href="/turma/{{codigo}}"> {{oferta.turma}} </a> </p>
      <p>disciplina: {{oferta.disciplina}}</p>
    </fieldset>
  %end

</body>
</html>
