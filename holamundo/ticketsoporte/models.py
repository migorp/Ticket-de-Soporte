from django.db import models




CH_rol = [
    ('Cliente', 'Cliente'),
    ('Usuario', 'Usuario'),
]
#class Rol(models.Model):
#    nombre = models.CharField(max_length=20, choices=CH_rol)

class Usuario(models.Model):
    identificacion = models.CharField(max_length=13)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()
    clave = models.CharField(max_length=50)
    #rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    rol = models.CharField(max_length=20, choices=CH_rol)
    

CH_cliente_tipo = [
    ('Hogar', 'Hogar'),
    ('Empresa', 'Empresa'),
]

CH_cliente_registro = [
    ('Taller', 'Taller'),
    ('En Línea', 'En Línea'),
]

class Cliente(models.Model):
    identificacion = models.CharField(max_length=13)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    ciudad = models.CharField(max_length=100)
    correo = models.EmailField()
    clave = models.CharField(max_length=50)
    tipo_cliente = models.CharField(max_length=20, choices=CH_cliente_tipo)
    tipo_registro = models.CharField(max_length=20, choices=CH_cliente_registro)
    #rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    rol = models.CharField(max_length=20, choices=CH_rol)

    def __str__(self):
        return self.nombre


CH_dispositivo_tipo = [
    ('Portatil', 'Portatil'),
    ('Escritorio', 'Escritorio'),
    ('Impresora', 'Impresora'),
    ('Componente', 'Componente'),
]

class Dispositivo(models.Model):
    tipo = models.CharField(max_length=20, choices=CH_dispositivo_tipo)
    #nombre_corto_cliente = models.CharField(max_length=50, blank=True)
    marca = models.CharField(max_length=50, blank=True)
    modelo = models.CharField(max_length=50, blank=True)
    serie = models.CharField(max_length=50, blank=True)
    #observacion = models.CharField(max_length=80, blank=True)

    def __str__(self):
        return str(self.id)


CH_inci_tipo_serv = [
    ('Remoto', 'Remoto'),
    ('Taller', 'Taller'),
    ('Insitu', 'Insitu'),
]

CH_inci_estado = [
    ('No Iniciado', 'No Iniciado'),
    ('En Proceso', 'En Proceso'),
    ('Confirmación', 'Confirmación'),
    ('Confirmación', 'Confirmación'),
    ('Finalizado', 'Finalizado'), 
    ('Anulado', 'Anulado'),
]

class IncidenciaNoIniciado(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    fecha_hora_registro = models.DateTimeField()
    descripcion_corta = models.CharField(max_length=100)
    estado_fisico = models.CharField(max_length=250, blank=True)
    componente_adjunto = models.CharField(max_length=250, blank=True)
    incidencia_no_iniciado = models.TextField()
    observacion_no_iniciado = models.TextField(blank=True)
    costo_revision = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_servicio = models.CharField(max_length=20, choices=CH_inci_tipo_serv)
    estado = models.CharField(max_length=20, choices=CH_inci_estado)
    
    def __str__(self):
        return str(self.id)

class IncidenciaProceso(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    incidencia_no_iniciado = models.ForeignKey(IncidenciaNoIniciado, on_delete=models.CASCADE)
    resultado_proceso = models.TextField()
    observacion_proceso = models.TextField(blank=True)
    costo_adicional = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.id)


CH_inci_conf = [
    ('En espera', 'En espera'),
    ('Si', 'Si'),
    ('No', 'No'),
]

class IncidenciaConfirmacion(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    incidencia_no_iniciado = models.ForeignKey(IncidenciaNoIniciado, on_delete=models.CASCADE)
    confirmacion = models.CharField(max_length=20, choices=CH_inci_conf)

class IncidenciaFinal(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    incidencia_no_iniciado = models.ForeignKey(IncidenciaNoIniciado, on_delete=models.CASCADE)
    incidencia_proceso = models.ForeignKey(IncidenciaProceso, on_delete=models.CASCADE)
    resultado_finalizado = models.TextField(blank=True)
    observaciones_finalizado = models.TextField(blank=True)

class IncidenciaAnulado(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    incidencia_no_iniciado = models.ForeignKey(IncidenciaNoIniciado, on_delete=models.CASCADE)
    resultado_anulado = models.TextField()
    observaciones_anulado = models.TextField(blank=True)

    