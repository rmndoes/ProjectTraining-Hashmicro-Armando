# -*- coding: utf-8 -*-
# from odoo import http


# class Cateringmamah(http.Controller):
#     @http.route('/cateringmamah/cateringmamah', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cateringmamah/cateringmamah/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('cateringmamah.listing', {
#             'root': '/cateringmamah/cateringmamah',
#             'objects': http.request.env['cateringmamah.cateringmamah'].search([]),
#         })

#     @http.route('/cateringmamah/cateringmamah/objects/<model("cateringmamah.cateringmamah"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cateringmamah.object', {
#             'object': obj
#         })
