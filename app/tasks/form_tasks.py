from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, validators
from wtforms.validators import DataRequired, Length
from app.models import User


class TaskForm(FlaskForm):
    title = StringField("Title", validators=[
                        DataRequired(), Length(min=5, max=40)])
    description = TextAreaField(
        "Description",
        validators=[DataRequired(), Length(min=10, max=140)],
        render_kw={"rows": 6, "style": "resize:none;"},
    )

    submit = SubmitField("Submit")
