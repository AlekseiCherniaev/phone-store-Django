class DataMixin:
    title_page = None
    extra_content = {}

    def __init__(self):
        if self.title_page is not None:
            self.extra_content['title'] = self.title_page

    def get_mixin_content(self, content, **kwargs):
        content.update(kwargs)
        return content
