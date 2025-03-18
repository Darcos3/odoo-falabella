# -*- coding: utf-8 -*-
{
    'name': "API Falabella",
    'summary': "API Falabella",
    'description': "Módulo para sincronizar productos desde la API de Falabella con Odoo",
    'author': "Alto Sentido",
    'website': "http://www.altosentido.net",
    'category': 'Electroventas',
    'version': '1.0',
    'company': 'Alto Sentido',
    'depends': ['base'],
    'data': [
        'views/product_sync_menu.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}