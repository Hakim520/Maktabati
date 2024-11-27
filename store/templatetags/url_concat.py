from django import template
from urllib.parse import urlencode, parse_qs, urlsplit, urlunsplit

register = template.Library()

@register.simple_tag(takes_context=True)
def modify_query(context, **params):
    request = context['request']
    get_request = request.META.get('QUERY_STRING', '')

    index = get_request.find('page')

    # If 'page' is not found, return the original string
    
    if index != -1:
        # Calculate start of the portion to be removed (which is 4 characters after 'page' starts)
        start_remove = index-1

        # Check if there are at least 6 characters after 'page'
        if start_remove + 7 <= len(get_request):
            # Remove the next 6 characters after 'page'
            get_request = get_request[:start_remove] + get_request[start_remove + 7:]
        else:
            # If less than 6 characters are available, remove all characters after 'page'
            get_request = get_request[:start_remove]
    
    
   
    
    page_string = next(iter(params)) + "=" + str(params["page"])
    

    query = get_request+"&"+page_string  # This keeps the multi-value property intact
    
    # Encode the updated QueryDict into a URL query string
    return query