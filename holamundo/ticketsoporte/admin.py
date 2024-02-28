from django.contrib import admin



from .models import Usuario, Cliente, Dispositivo, IncidenciaNoIniciado, IncidenciaProceso, IncidenciaConfirmacion, IncidenciaFinal, IncidenciaAnulado

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'identificacion', 'nombre', 'telefono', 'correo', 'clave', 'rol',)


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'identificacion', 'nombre', 'telefono', 'ciudad', 'correo', 'clave', 'tipo_cliente', 'tipo_registro', 'rol',)


@admin.register(Dispositivo)
class DispositivoAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo', 'marca', 'modelo', 'serie',)
    #list_filter = ('marca', 'modelo',)

@admin.register(IncidenciaNoIniciado)
class IncidenciaNoIniciadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'dispositivo', 'fecha_hora_registro', 'descripcion_corta', 
    'estado_fisico', 'componente_adjunto', 'incidencia_no_iniciado',
    'observacion_no_iniciado', 'costo_revision', 'tipo_servicio', 'estado',)

@admin.register(IncidenciaProceso)
class IncidenciaProcesoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'dispositivo', 'incidencia_no_iniciado', 'resultado_proceso', 'observacion_proceso', 'costo_adicional',)

@admin.register(IncidenciaConfirmacion)
class IncidenciaConfirmacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'dispositivo', 'incidencia_no_iniciado', 'confirmacion',)

@admin.register(IncidenciaFinal)
class IncidenciaFinalAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'dispositivo', 'incidencia_no_iniciado', 'incidencia_proceso', 'resultado_finalizado', 'observaciones_finalizado',)

@admin.register(IncidenciaAnulado)
class IncidenciaAnuladoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'dispositivo', 'incidencia_no_iniciado', 'resultado_anulado', 'observaciones_anulado', )



