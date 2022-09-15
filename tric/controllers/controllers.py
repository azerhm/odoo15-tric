# -*- coding: utf-8 -*-
# from odoo import http


# class Tric(http.Controller):
#     @http.route('/tric/tric', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tric/tric/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tric.listing', {
#             'root': '/tric/tric',
#             'objects': http.request.env['tric.tric'].search([]),
#         })

#     @http.route('/tric/tric/objects/<model("tric.tric"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tric.object', {
#             'object': obj
#         })
