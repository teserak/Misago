import floppyforms as forms


class AutoStripInputMixin(object):
    dont_strip = None

    def full_clean(self):
        self.data = self.data.copy()
        for name, field in self.fields.iteritems():
            if (field.__class__ == forms.CharField and
                    not name in self.dont_strip):
                try:
                    self.data[name] = self.data[name].strip()
                except KeyError:
                    pass
        return super(AutoStripInputMixin, self).full_clean()


class Form(AutoStripInputMixin, forms.Form):
    pass


class ModelForm(AutoStripInputMixin, forms.ModelForm):
    pass