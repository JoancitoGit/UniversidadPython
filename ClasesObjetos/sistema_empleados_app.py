from empleado import Empleado
from empresa import Empresa

print('*** Sistema de Empleados ***')

# Crear nua instancia de una empresa
empresa1 = Empresa('Global Mentoring')

# Contratar algunos empleados
empresa1.contratar_empleado('Joan', 'Ingeniería')
empresa1.contratar_empleado('Katia','Administración')
empresa1.contratar_empleado('Daniel','Administración')
empresa1.contratar_empleado('Hervert','Recursos Humanos')

# Obtener el total de objetos de tipo empleado
print(f'Total de Empleados: {Empleado.obtener_total_empleados()}')

# Obtener el número de empleados en el departamento de Administración
print(f'Empleados en el departamento de Administración: {empresa1.obtener_numero_empleados_por_departamento("Administración")}')

# Mostrar todos los empleados de la empresa
empresa1.obtener_total_empleados()