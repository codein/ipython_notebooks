import facebook
import json
import pprint

ACCESS_TOKEN = 'CAACEdEose0cBADinm7CxuPaMb4uHytye1LE4PSKYZBjpYhpPZAHczNfgR8U7a3ZASsGazuI4sKCAEnVxpCDg5rhtJu2aP9gq2ZCwL0zU1z5H53R5Lk9qrVdGNcCb407G6xnznQlCgoOoTJTijXaQzRBGXVttzahKLZAdoIN91sOmCrphHjYfTOgQ0digmDygVSZBcVZBOD0WgZDZD'

fb = facebook.GraphAPI(ACCESS_TOKEN)

def get_company(company_name):
    result = fb.request('search',  {'q':company_name, 'type':'page', 'limit':10})

    company_id = result['data'][0]['id']
    company_obj = fb.get_object(company_id)
    location = company_obj.get('location', {})
    return {
        'Name': company_obj['name'],
        'Talked about count': company_obj['talking_about_count'],
        'Likes': company_obj['likes'],
        'Mission': company_obj.get('mission', ''),
        'Founded': company_obj.get('founded', ''),
        'Checkins': company_obj.get('checkins', ''),
        'thumbnail': company_obj['cover']['source'],
        'Location': '%s, %s' % (location.get('city', ''), location.get('state', ''))
    }

