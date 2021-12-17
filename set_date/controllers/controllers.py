# -*- coding: utf-8 -*-
# from odoo import http


# class SetDate(http.Controller):
#     @http.route('/set_date/set_date/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/set_date/set_date/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('set_date.listing', {
#             'root': '/set_date/set_date',
#             'objects': http.request.env['set_date.set_date'].search([]),
#         })

#     @http.route('/set_date/set_date/objects/<model("set_date.set_date"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('set_date.object', {
#             'object': obj
#         })
