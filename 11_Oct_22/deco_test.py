from email import message
import http
import functools
from wsgiref.validate import validator

def login_required(route=None, **kwargs):
    def decorator(view_func):
        @functools.wrap(view_func)
        @http.route(route, **kwargs)
        def wrapper(self, **kw):
            http_method, body, headers, token=jwt_http.parse_request()
            result= validator.verify_token(token)
            if not result['status']:
                return jwt_http.errcode(code=result['code'], message=result['message'])
            kw.update(dict_body_data(**kw))
            if kw.get('message'):
                return jwt_http.errorcod(code=500, message=kw['message'])
            return view_func(self,**kw)
        return wrapper
    return decorator            
