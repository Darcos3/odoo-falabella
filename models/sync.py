from odoo import models, fields, api

class SyncModel(models.Model):
    _name = 'sync.model'
    _description = 'Sincronizar productos de falabella'

    name = fields.Char(string="Nombre")
    
    def action_importar(self):
        """Acción que se ejecuta al presionar el botón 'Importar'"""
        # Aquí puedes añadir la lógica de importación
        # Ejemplo: Importar datos desde un CSV, API externa, etc.
        for record in self:
            record.name = "Importado correctamente"
