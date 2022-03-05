from flask_wtf import FlaskForm
import wtforms


usernames = ["admin", "primero", "mauricio"]


class UserForm(FlaskForm):
    username = wtforms.StringField("Usuario", validators=[wtforms.validators.DataRequired()])
    email = wtforms.EmailField("Correo")

    def validate_username(self, field):
        if field.data in usernames:
            raise wtforms.ValidationError("El usuario ya existe")

    def save(self):
        username = self.data.get("username")
        email = self.data.get("email")
        usernames.append(username)
        print(f"He creado el usuario {username} con correo {email}")
