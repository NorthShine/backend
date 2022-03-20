from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank

from competitions.models import SkillToken


def search(search_query):
    vector = SearchVector('name', 'tags__name', 'competencies__name')
    query = SearchQuery(search_query)
    result = SkillToken.objects.annotate(rank=SearchRank(vector, query))\
        .order_by('-rank')
    return result
