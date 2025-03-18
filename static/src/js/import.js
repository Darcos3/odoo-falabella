'use strict';

odoo.define('falabella.import', function( require ){
    require('web.dom_ready');
    var ajax = require('web.ajax');
    var button = $('#importar');

    var _onButton = function(e){
        ajax.jsonRpc('/get-products', 'json', {})
        .then(function(data){
            console.log(data);
        })
        .catch(function(err){
            console.error("Error al importar productos:", err);
        });
    }

    button.click( _onButton );

    

});