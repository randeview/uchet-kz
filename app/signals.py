# from django.db.models.signals import pre_save, post_save
# from django.dispatch import receiver
#
# from .models import Todo
# from .tasks import send_email_task
#
#
# @receiver(pre_save, sender=Todo)
# def partner_pre_save(sender, instance, *args, **kwargs):
#     if instance.id is not None:
#         prev_todo = Todo.objects.get(id=instance.id)
#         if instance.finished != prev_todo.finished:
#             send_email_task.delay()
