from rest_framework.permissions import BasePermission
from pprint import pp

class Custom_Permission(BasePermission):
    def has_permission(self, request, view):
         return request.user.is_superuser


# class User_custom_Permission(BasePermission):
#      def has_permission(self, request, view):
          
#         dynamic_value = getattr(request,'role' ,None)

#         if dynamic_value is not None:
#             return dynamic_value is True
        
#         else:
#             return False
        


class User_custom_Permission(BasePermission):
    

    def has_permission(self, request, view):

        # pp(view.__dict__)  
        print(getattr(view, 'roles', None))
        roles=(getattr(view, 'roles', None))

        # if roles == 'admin':
        #     print ('roles',None)
        if 'admin' in roles:
            print('admin present in roles list')

        else:
            print('admin is not present in roles')
        # if 12 in roles:
        #     print('12 present in roles list')

        # else:
        #     print('12 is not present in roles')
        
        dynamic_value = str(getattr(request, 'role', None)) 
        required_role = 'admin'  
        return dynamic_value == required_role
    

    # has permission ke view ke baare  me pata karna he 