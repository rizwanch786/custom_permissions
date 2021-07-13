from rest_framework.permissions import BasePermission
class MyPermissions(BasePermission):
    def has_permission(self, request, view):
        '''In this function user on get the data not chage or delete the  data'''
        if request.method == 'GET':
            return True
        return False