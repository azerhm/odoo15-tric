from odoo import api, fields, models


class KelompokBarang(models.Model):
    _name = 'tric.kelompokbarang'
    _description = 'New Description'

    name = fields.Selection([
        ('pendingin', 'Pendingin'), 
        ('pemanas', 'Pemanas'),     
    ], string='Nama Kelompok')

    kode_kelompok = fields.Char(string='Kode Kelompok')
    
        
    @api.onchange('name')
    def _onchange_kode_kelompok(self):
        if (self.name == 'pendingin'):
            self.kode_kelompok = 'D001'
        elif (self.name == 'pemanas'):
            self.kode_kelompok = 'P001'

    kode_rak = fields.Char(string='Kode Rak')
    barang_ids = fields.One2many(comodel_name='tric.barang', 
                                inverse_name='kelompokbarang_id', 
                                string='Daftar Barang')
    jml_item = fields.Char(compute='_compute_jml_item', string='Jumlah Item')
    
    @api.depends('barang_ids')
    def _compute_jml_item(self):
        for rec in self:
            a = self.env['tric.barang'].search([('kelompokbarang_id','=', rec.id)]).mapped('name')
            b = len(a)
            rec.jml_item = b
            rec.daftar = a

    daftar = fields.Char(string='Daftar Isi')
    
    
    
