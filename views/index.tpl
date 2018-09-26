<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 5.0//PT_BR">
<html>
<head>
<meta charset="UTF-8">
</head>
<body>
<form action="/send" method=POST>

  <h1>Turma: {{oferta.turma}}</h1>
  <h2>disciplina: {{oferta.disciplina}}</h2>

  <input type="hidden" name="turma" value="{{oferta.codigo}}" />
  <input type="hidden" name="time" value="{{time}}" />

%for question in questions:
  <div><fieldset><h4> {{question.txt}} </h4>
  %for field in question.fields:
    <br />

      <div>
        %if field.t == "c.":
          <input type="checkbox" name="c.{{question.txt}}" value="{{field.txt}}" />
        %elif field.t == "r.":
          <input type="radio" name="r.{{question.txt}}" value="{{field.txt}}" />
        %elif field.t == "t.":
          <textarea cols="50" name="t.{{question.txt}}" ></textarea>
        %else:
          <!-- error -->
        %end

        %if field.txt:
            <label>{{field.txt}}</label>
        %end
      </div>
  %end
  </fieldset></div>
%end

<fieldset>
<input type="submit" value="Enviar" />
</fieldset>
</form>
</body>
</html>
