![Image description](https://github.com/adityakumar1309/learning/blob/master/images/django_middleware.png)


Things to remember when using middleware

## Order of middlewares is important.

## A middleware only need to extend from class object.

## A middleware is free to implement some of the methods and not implement other methods.

## A middleware may implement process_request but may not implement process_response and process_view. Infact it is very common and lot of Django provided middlewares do it.

## A middleware may implement process_response but not implement process_request.

### NOTE 
So if a Middleware’s process_request() returns a HttpResponse object then process_request of any subsequent middlewares is bypassed. Also view execution is bypassed.

So process_response() follows the reverse of what happens with process_request. process_response() is executed for last middleware then second last middleware and so on till the first middleware.
### return response does NOT skip process_response() of other middleares . 

Signatures of Middleware:

class BookMiddleware(object):
	
  def process_request(self, request):
		
    print "Middleware executed"
		
    print request.user

https://www.agiliq.com/blog/2015/07/understanding-django-middlewares/

