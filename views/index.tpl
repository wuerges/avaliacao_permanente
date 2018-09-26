<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 5.0//PT_BR">
<html>
<head>
<meta charset="UTF-8">
</head>
<body>
<form action="/send" method=POST>

%for question in questions:
  <div><fieldset><h4> {{question.txt}} </h4>
  %for field in question.fields:
    <br />

      <div>
        %if field.t == "c.":
          <input type="checkbox" name="{{question.name()}}" value="{{field.value()}}" />
        %elif field.t == "r.":
          <input type="radio" name="{{question.name()}}" value="{{field.value()}}" />
        %elif field.t == "t.":
          <textarea cols="50" name="{{question.name()}}" ></textarea>
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
