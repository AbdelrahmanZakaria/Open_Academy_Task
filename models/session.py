from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Session(models.Model):
    _name = 'openacademy.session'
    _description = "OpenAcademy Sessions"

    name = fields.Char(required=True)
    start_date = fields.Date(default=fields.Date.today)
    end_date = fields.Date()
    duration = fields.Float(digits=(6, 2))
    seats = fields.Integer(string="Number of seats")
    instructor_id = fields.Many2one('res.partner', string="Instructor")
    course_id = fields.Many2one('openacademy.course', string="Course")
    attendee_ids = fields.Many2many('res.partner', string="Attendees")
    taken_seat = fields.Float(string="Taken seats", compute='taken_seats')
    active = fields.Boolean(default=True)

    @api.constrains('instructor_id', 'attendee_ids')
    def check_instructor_not_in_attendees(self):
        for record in self:
            if record.instructor_id and record.instructor_id in record.attendee_ids:
                raise ValidationError("A session's instructor can't be an attendee")

    @api.depends('seats', 'attendee_ids')
    def taken_seats(self):
        for record in self:
            if not record.seats:
                record.taken_seat = 0.0
            else:
                record.taken_seat = 100.0 * len(record.attendee_ids) / record.seats

    @api.onchange('seats', 'attendee_ids')
    def verify_valid_seats(self):
        if self.seats < 0:
            return {
                'warning': {
                    'title': "Incorrect 'seats' value",
                    'message': "The number of available seats may not be negative",
                },
            }
        if self.seats < len(self.attendee_ids):
            return {
                'warning': {
                    'title': "Too many attendees",
                    'message': "Increase seats or remove excess attendees",
                },
            }
