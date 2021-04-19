from app.form import TaskForm
from app.models import Task
from flask import Blueprint, render_template, redirect, request, url_for, flash, abort
from flask_login import login_required, current_user


tasks_bp = Blueprint("tasks_bp", __name__,
                 template_folder="templates")

@tasks_bp.route("/tasks")
@login_required
def tasks():
    tasks = current_user.tasks
    print(tasks)
    return render_template("tasks/view.html",title_page="Tasks",tasks=tasks,current_user=current_user)

@tasks_bp.route("/tasks/new", methods=["GET","POST"])
@login_required
def task_new():
    task_form = TaskForm()


    if task_form.validate_on_submit():
        task = Task.create_task(title=task_form.title.data,description=task_form.description.data,user_id=current_user.id)

        if task:
            flash("Task created successful!","success")            
    
        return redirect(url_for("tasks_bp.tasks"))

    else:
        return render_template("tasks/new.html",title_page="New task",form=task_form)

@tasks_bp.route("/tasks/edit/<int:task_id>",methods=["GET","POST"])
@login_required
def task_edit(task_id):
    task = Task.query.get_or_404(task_id)

    if task.user_id != current_user.id:
        abort(404)

    task_form = TaskForm(obj=task)

    if task_form.validate_on_submit():
        task = Task.update_task(id=task.id,title=task_form.title.data,description=task_form.description.data)
        if task:
            flash("Task updated successfully","success")
            return redirect(url_for("tasks_bp.tasks"))

    return render_template("tasks/edit.html",title_page="Edit task",form=task_form,task_id=task_id)