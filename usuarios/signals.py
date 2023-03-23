from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from usuarios.models import DatosUsuario


@receiver(post_save, sender=User)
def create_datosusuario(sender, instance, created, **kwargs):
    if created:
        DatosUsuario.objects.create(usuario=instance)
        print("Se han creado los datos ")


@receiver(post_save, sender=User)
def update_datosusuario(sender, instance, created, **kwargs):
    if created==False:
        instance.datosusuario.save()
        print("se han actualizado los datos")


"""
pre_save
post_save
@receiver()

"""