Class pollo:
#metodo constructores
def_init_(self, id_pollo, dato_edad):
   self.codigo_pollo = id_pollo
   self.edad_pollo = dato_edad
#llamados de otras clases
self.objBase_datos = base_datos() #el objeto de la clase

#metodos publicos de modificar atributos
def getCodigo_pollo(self):
return self.codigo_pollo

def setCodigo_pollo(self, codigo_pollo):
  self.codigo_pollo = codigo_pollo

#metodos para conectar base datos
def guardar_pollo(self):
  self.obj_Base_datos.guardar_pollo()
  
