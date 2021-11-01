# import  django
# django.setup()
from django.test import TestCase
from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase, APIClient, APIRequestFactory
from appapi.models import UserModel, StaffModel, QualificationModel
from appapi.views import *
from appapi.urls import *


# USING APICLIENT

# # class StaffTests(APITestCase, URLPatternsTestCase):
# client = APIClient()
#
# user_post_payload = {
#     "name": "Testnam",
#     "email": "Testmail@gmail.com",
#     "phone_no": "Testno09877655"
# }
# user_put_payload = {
#     "id": 21,
#     "name": "Testname4",
#     "email": "Testmail@gmail.com",
#     "phone_no": "Testno09877655"
# }
# user_delete_payload = {
#     "id": 21,
#     "name": "Testname",
#     "email": "Testmail@gmail.com",
#     "phone_no": "Testno09877655"
# }
# post = client.post('', user_post_payload, format='json')
# put = client.put('', user_put_payload, format='json')
# delete = client.delete('', user_delete_payload, format='json')


# Create your tests here.
class StaffTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        # path('', include('appapi.urls')),
        path('', StaffAPIView.as_view(), name='api')
    ]

    # id = 0

    # def setUp(self):
    #     self.urlpatterns = [
    #         # path('', include('appapi.urls')),
    #         path('', StaffAPIView.as_view(), name='api')
    #     ]

    # self.client = APIClient()

    # Post test case
    def test_all(self):
        url = reverse('api')

        print('######################### POST START ########################')
        user_post_payload = {
            "name": "Testname",
            "email": "Testmail@gmail.com",
            "phone_no": "Testno09877655"
        }
        user_post_response = self.client.post(url, user_post_payload, format='json')

        staff_post_payload = {
            "staff_id": "Test id",
            "joined_date": "2021-10-28",
            "position": "None",
            "user_name": 1
        }
        staff_post_response = self.client.post(url, staff_post_payload, format='json')

        qualification_post_payload = {
            "qualification": "PHD",
            "university": "Lahore garrison university",
            "staff_member": 1
        }
        qualification_post_response = self.client.post(url, qualification_post_payload, format='json')

        print(user_post_response)
        print(staff_post_response)
        print(qualification_post_response)

        self.assertEqual(user_post_response.status_code, user_post_response.status_code, 200)
        self.assertEqual(staff_post_response.status_code, staff_post_response.status_code, 200)
        self.assertEqual(qualification_post_response.status_code, qualification_post_response.status_code, 200)

        person = UserModel.objects.get(name='Testname')
        # global id
        id = person.id
        # print(id)

        print('######################### POST END ########################')

        print('######################### PUT START ########################')

        user_put_payload = {
            "id": id,
            "name": "Testname",
            "email": "Testmail@gmail.com",
            "phone_no": "Testno09877655"
        }
        user_put_response = self.client.put(url, user_put_payload, format='json')

        staff_put_payload = {
            "id": id,
            "staff_id": "Test id put",
            "joined_date": "2021-10-28",
            "position": "None",
            "user_name": id
        }
        staff_put_response = self.client.put(url, staff_put_payload, format='json')

        qualification_put_payload = {
            "id": id,
            "qualification": "MPhil",
            "university": "Lahore garrison university",
            "staff_member": id
        }
        qualification_put_response = self.client.put(url, qualification_put_payload, format='json')

        print(user_put_response)
        print(staff_put_response)
        print(qualification_put_response)

        self.assertEqual(user_put_response.status_code, user_put_response.status_code, 405)
        self.assertEqual(staff_put_response.status_code, staff_put_response.status_code, 405)
        self.assertEqual(qualification_put_response.status_code, qualification_put_response.status_code, 405)

        print('######################### PUT END ########################')

        print('######################### DELETE START ########################')

        qualification_delete_payload = {
            "id": id,
            "qualification": "PHD",
            "university": "Lahore garrison university",
            "staff_member": id
        }
        # client = APIClient()
        # self.client.delete(url, qualification_payload, format='json')
        qualification_delete_response = self.client.delete(url, qualification_delete_payload, format='json')
        print(qualification_delete_response)

        staff_delete_payload = {
            "id": id,
            "staff_id": "Test id",
            "joined_date": "2021-10-28",
            "position": "None",
            "user_name": id
        }
        staff_delete_response = self.client.delete(url, staff_delete_payload, format='json')
        print(staff_delete_response)

        user_delete_payload = {
            "id": id,
            "name": "Test name",
            "email": "Testmail@gmail.com",
            "phone_no": "Testno09877655"
        }

        user_delete_response = self.client.delete(url, user_delete_payload, format='json')
        print(user_delete_response)

        self.assertEqual(user_delete_response.status_code, user_delete_response.status_code, 202)
        self.assertEqual(staff_delete_response.status_code, staff_delete_response.status_code, 202)
        self.assertEqual(qualification_delete_response.status_code, qualification_delete_response.status_code, 202)

        print('######################### DELETE END ########################')

    def test_get(self):
        url = reverse('api')

        user_response = self.client.get(url)
        # print(user_response)
        self.assertEqual(user_response.status_code, user_response.status_code, 200)

    # def test_delete(self):
    #
    #     url = reverse('api')
    #     #
    #     print('######################### DELETE START ########################')
    #
    #     qualification_delete_payload = {
    #         "id": id,
    #         "qualification": "PHD",
    #         "university": "Lahore garrison university",
    #         "staff_member": id
    #     }
    #     # client = APIClient()
    #     # self.client.delete(url, qualification_payload, format='json')
    #     qualification_delete_response = self.client.delete(url, qualification_delete_payload, format='json')
    #     print(qualification_delete_response)
    #
    #     staff_delete_payload = {
    #         "id": id,
    #         "staff_id": "Test id",
    #         "joined_date": "2021-10-28",
    #         "position": "None",
    #         "user_name": id
    #     }
    #     staff_delete_response = self.client.delete(url, staff_delete_payload, format='json')
    #     print(staff_delete_response)
    #
    #     user_delete_payload = {
    #         "id": id,
    #         "name": "Test name",
    #         "email": "Testmail@gmail.com",
    #         "phone_no": "Testno09877655"
    #     }
    #
    #     user_delete_response = self.client.delete(url, user_delete_payload, format='json')
    #     print(user_delete_response)
    #
    #     self.assertEqual(user_delete_response.status_code, user_delete_response.status_code, 202)
    #     self.assertEqual(staff_delete_response.status_code, staff_delete_response.status_code, 202)
    #     self.assertEqual(qualification_delete_response.status_code, qualification_delete_response.status_code, 202)
    #
    #     print('######################### DELETE END ########################')

    # def test_put(self):
    #     url = reverse('api')
    #     person = UserModel.objects.get(name='Testname')
    #     id = person.id
    #     print(id)

    # user_payload = {
    #     "id": id,
    #     "name": "Testname",
    #     "email": "Testmail@gmail.com",
    #     "phone_no": "Testno09877655"
    # }
    # user_response = self.client.put(url, user_payload, format='json')

    #     staff_payload = {
    #         "id": 1,
    #         "staff_id": "Test id put",
    #         "joined_date": "2021-10-28",
    #         "position": "None",
    #         "user_name": 1
    #     }
    #     staff_response = self.client.put(url, staff_payload, format='json')
    #
    #     qualification_payload = {
    #         "id": 1,
    #         "qualification": "MPhil",
    #         "university": "Lahore garrison university",
    #         "staff_member": 1
    #     }
    #     qualification_response = self.client.put(url, qualification_payload, format='json')
    #
    #     # print(user_response)
    #     # print(staff_response)
    #     # print(qualification_response)
    #
    # self.assertEqual(user_response.status_code, user_response.status_code, 405)
    #     self.assertEqual(staff_response.status_code, staff_response.status_code, 405)
    #     self.assertEqual(qualification_response.status_code, qualification_response.status_code, 405)
    #
    # # def test_gett(self):
    # #     url = reverse('api')
    # #
    # #     user_response = self.client.get(url)
    # #     # print(user_response)
    # #     self.assertEqual(user_response.status_code, user_response.status_code, 200)
    #
    # def test_delete(self):
    #     # url = reverse('api', kwargs={'pk': qualification.get('id')})
    #     url = reverse('api')
    #
    #     qualification_payload = {
    #         "id": 1,
    #         "qualification": "PHD",
    #         "university": "Lahore garrison university",
    #         "staff_member": 1
    #     }
    #     # client = APIClient()
    #     # self.client.delete(url, qualification_payload, format='json')
    #     qualification_delete_response = self.client.delete(url, qualification_payload, format='json')
    #     print(qualification_delete_response)
    #
    #     staff_payload = {
    #         "id": 1,
    #         "staff_id": "Test id",
    #         "joined_date": "2021-10-28",
    #         "position": "None",
    #         "user_name": 1
    #     }
    #     staff_delete_response = self.client.delete(url, staff_payload, format='json')
    #     print(staff_delete_response)
    #
    #     user_payload = {
    #         "id": 1,
    #         "name": "Test name",
    #         "email": "Testmail@gmail.com",
    #         "phone_no": "Testno09877655"
    #     }
    #
    #     user_delete_response = self.client.delete(url, user_payload, format='json')
    #     print(user_delete_response)
    #
    #     self.assertEqual(user_delete_response.status_code, user_delete_response.status_code, 202)
    #     self.assertEqual(staff_delete_response.status_code, staff_delete_response.status_code, 202)
    #     self.assertEqual(qualification_delete_response.status_code, qualification_delete_response.status_code, 202)
    #
