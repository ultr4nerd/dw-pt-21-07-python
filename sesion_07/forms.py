from flask_wtf import FlaskForm
import wtforms


class UserForm(FlaskForm):
    usuario = wtforms.StringField("Usuario", validators=[wtforms.validators.DataRequired()])
    correo = wtforms.EmailField("Correo")
