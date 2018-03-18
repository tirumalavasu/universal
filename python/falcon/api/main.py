import falcon

class ThingsResource(object):
    def on_get(self, req, resp):
        """Handles GET Requests"""
        resp.status = falcon.HTTP_200
        resp.body = ('\nTwo things awe me must\n')

app = falcon.API()

things = ThingsResource()

app.add_route('/things', things)
