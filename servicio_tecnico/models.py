from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.html import format_html
from product.models import Categoria


class Cliente(models.Model):

    nombre_completo = models.CharField(max_length=80)
    telefono = PhoneNumberField(unique = True, null = False, blank = False)
    documento = models.CharField(max_length=80, null = False, blank = False)
    
    def __str__(self):
        return self.nombre_completo


class Reparacion(models.Model):
    Motorola = 'Motorola',
    Samsung = 'Samsung',
    Lg = 'Lg',
    Xiaomi = 'Xiaomi',
    Alcatel = 'Alcatel',
    Huawey = 'Huawey',
    Chino = 'Chino',
    Iphone = 'Iphone',
    MARCA = (
        ('Motorola','Motorola'),
        ('Samsung','Samsung'),
        ('Lg','Lg'),
        ('Xiaomi','Xiaomi'),
        ('Sony','Sony'),
        ('Huawey','Huawey'),
        ('Chino','Chino'),
        ('Otro','Otro'),
    )

    Pendiente = 'Pendiente',
    Aceptado = 'Aceptado',
    Reparado = 'Reparado',
    Irreparable = 'Irreparable',
    Entregado = 'Entregado',
    Entregado_Irreparable = 'Entregado Irreparable',
    ESTADO = (
        ('Pendiente','Pendiente'),
        ('Aceptado','Aceptado'),
        ('Reparado','Reparado'),
        ('Irreparable','Irreparable'),
        ('Entregado','Entregado'),
        ('Entregado Irreparable','Entregado Irreparable'),
        
    )

    En_espera = 'En espera',
    Reparar = 'Reparar',
    No_reparar = 'No Reparar',
    ACCION = (
        ('En espera','En espera'),
        ('Reparar','Reparar'),
        ('No Reparar','No Reparar'),
        
    )

    fecha = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente,null=True, on_delete=models.CASCADE)
    whatsApp = PhoneNumberField(unique = False, null = False, blank = False)
    marca = models.CharField(max_length=40, choices=MARCA)
    modelo = models.CharField(max_length=40, blank=True)
    imei = models.CharField(max_length=40,blank=True )
    falla = models.CharField(max_length=100,blank=True )
    imagen = models.ImageField(upload_to="fallas//%Y/%m/%d", null=True, blank=True)   
    comentarios = models.TextField(null=True, blank=True)
    presupuesto = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    pago_seña = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    precio = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    estado = models.CharField(max_length=40, choices=ESTADO, default='Pendiente')
    tecnico = models.ForeignKey(User, on_delete=models.CASCADE,)
    accion = models.CharField(max_length=40, choices=ACCION, default='en espera')
    
    def tipo_de_reparacion(self):   #el metodo se agrega en el admin.py -- La misma logica se puede trabajar en cualquier atributo de instancia
        if self.estado == 'Pendiente':
            return format_html('<spam style="background-color: #5DF707; padding:7px;">{}</spam>', self.estado ) # le damos color a estado en el html
        elif self.estado == 'Aceptado':
            return format_html('<spam style="background-color: #f0f; padding:7px;">{}</spam>',  self.estado)
        elif self.estado == 'Reparado':
            return format_html('<spam style="background-color: #D9AD04; padding:7px;">{}</spam>',  self.estado)
        elif self.estado == 'Irreparable':
            return format_html('<spam style="background-color: #099; padding:7px">{}</spam>',  self.estado)
        elif self.estado == 'Entregado':
            return format_html('<spam style="background-color: #31B009; padding:7px">{}</spam>',  self.estado)
        elif self.estado == 'Entregado Irreparable':
            return format_html('<spam style="background-color: #f00; padding:7px">{}</spam>',  self.estado)


    def __str__(self):
            return ''


class Proveedores(models.Model):
    nombre = models.CharField(max_length=40)
    telefono = PhoneNumberField(unique = True, null = False, blank = False)
    tecnico = models.ForeignKey(User, on_delete=models.CASCADE,)
    direccion =  models.CharField(max_length=50)
   
    def __str__(self):
        return f'Proveedor {self.nombre}: {self.telefono}'

        
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)


class PedidoEspecial(models.Model):
    nombre = models.CharField(max_length=40)
    telefono =  models.CharField(max_length=40)
    solicitud = models.TextField(null=True, blank=True)
    imagen = models.ImageField(upload_to="pedido_especial//%Y/%m/%d", null=True, blank=True) 


class Transferencia(models.Model):
    nombre = models.CharField(max_length=40)
    telefono =  models.CharField(max_length=40)
    pedido_numero = models.CharField(max_length=40)
    foto = models.ImageField(upload_to="transferencia//%Y/%m/%d", null=True, blank=True)


class Pyme(models.Model):
    nombre = models.CharField(max_length=40)
    telefono =  models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    foto = models.ImageField(upload_to="empresa//%Y/%m/%d", null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    

class ActualizacionPrecios(models.Model):
    Motorola = 'Motorola',
    Samsung = 'Samsung',
    Lg = 'Lg',
    Xiaomi = 'Xiaomi',
    Alcatel = 'Alcatel',
    Huawey = 'Huawey',
    Chino = 'Chino',
    Iphone = 'Iphone',
    Nokia = 'Nokia',
    Alcatel = 'Alcatel',
    Tablet = 'Tablet',
    Asus = 'Asus',
    Otro = 'Otro',
    MARCA = (
        ('Motorola','Motorola'),
        ('Samsung','Samsung'),
        ('Lg','Lg'),
        ('Xiaomi','Xiaomi'),
        ('Sony','Sony'),
        ('Huawey','Huawey'),
        ('Chino','Chino'),
        ('Iphone','Iphone'),
        ('Nokia','Nokia'),
        ('Alcatel','Alcatel'),
        ('Tablet','Tablet'),
        ('Asus','Asus'),
        ('Otro','Otro'),
    )
    fecha = models.DateTimeField(auto_now_add=True)
    proveedor = models.ForeignKey(Proveedores, blank=True, null=True, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, blank=True, null=True, on_delete=models.CASCADE)
    marca =  models.CharField(max_length=40, choices=MARCA)
    modelo =  models.CharField(max_length=40)
    dato_extra =  models.CharField(max_length=40) 
    precio =  models.CharField(max_length=40)
    dolar_fecha = models.CharField(max_length=10)

