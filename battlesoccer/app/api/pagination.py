from rest_framework.pagination import PageNumberPagination


class SmallSetPagination(PageNumberPagination):
    page_size = 3

class fourSetPagination(PageNumberPagination):
    page_size = 4

class fiveSetPagination(PageNumberPagination):
    page_size = 5