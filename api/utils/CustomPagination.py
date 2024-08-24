from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 10  # Limita o número de itens por página
    page_size_query_param = 'page_size'  # Permite ao usuário definir o tamanho da página via parâmetro de consulta
    max_page_size = 100  # Limita o tamanho máximo da páginagina