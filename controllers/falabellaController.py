import hashlib
import hmac
import time
import calendar
import urllib.parse
import logging

from odoo import http
import requests

_logger = logging.getLogger(__name__)

class FalabellaController(http.Controller):

    @http.route('/get-products', type='json', auth='public')
    def get_products(self):
        # api_url = 'https://sellercenter-api.falabella.com'
        # user_id = 'ferreteriaelectroventas@gmail.com'
        # api_key = '8d5293f60a5537d841efb3dd36b695628aac5a42'
        
        # if not user_id or not api_key:
        #     _logger.error("Las credenciales de Falabella no están configuradas.")
        #     return

        # timestamp = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
        # headers = {"accept": "application/json"}
        # action = 'GetProducts'
        # format_type = 'JSON'
        # version = '1.0'

        # param_string = f"Action={action}&Format={format_type}&Timestamp={timestamp}&UserID={user_id}&Version={version}"
        # signature = hmac.new(api_key.encode(), param_string.encode(), hashlib.sha256).hexdigest()
        # params = {
        #     'Action': action,
        #     'Format': format_type,
        #     'Timestamp': timestamp,
        #     'UserID': user_id,
        #     'Version': version,
        #     'Signature': signature
        # }
        
        # try:
        #     response = requests.get(f"{api_url}?{urllib.parse.urlencode(params)}", headers=headers, timeout=10)
        #     response.raise_for_status()
        #     products = response.json()
        #     self.importar_productos_falabella(products)
        # except requests.exceptions.RequestException as e:
        #     _logger.error(f"Error en la solicitud a Falabella: {e}")
        _logger.info("primera funcion")
        

    def importar_productos_falabella(self, products):
        # ProductTemplate = self.env['product.template']
        # for product in products.get('items', []):
        #     existing_product = ProductTemplate.search([('name', '=', product.get('name', ''))], limit=1)
        #     vals = {
        #         'name': product.get('name', ''),
        #         'list_price': product.get('price', 0.0),
        #         'qty_available': product.get('stock', 0),
        #         'brand': product.get('brand', ''),
        #     }
        #     if existing_product:
        #         existing_product.write(vals)
        #     else:
        #         ProductTemplate.create(vals)
        _logger.info("Productos de Falabella importados correctamente")
