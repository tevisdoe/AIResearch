from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from .models import Shop, Address, Service, ServicePart, SimpleInvitation
from accounts.models import ShopOwner, Employee, EmployeeData, Customer
from vehicles.models import Part

class AddressTests(TestCase):
    def test_addressCreation(self):
        address = Address.objects.create(postal_code="M4E2T2", street="102 Test Street", city="Toronto", country="Canada", province="ON")

        self.assertEqual(address.postal_code,"M4E2T2")
        self.assertEqual(address.street,"102 Test Street")
        self.assertEqual(address.city,"Toronto")
        self.assertEqual(address.country,"Canada")
        self.assertEqual(address.province,"ON")

class ShopTests(TestCase):
    @classmethod
    def setUpTestData(self):
        address = Address.objects.create(postal_code="M4E2T2", street="104 Test Street", city="Toronto", country="Canada", province="ON")
        shop_owner = ShopOwner.objects.create_user(type="shop_owner", username="testuser", password="qwerty123", email="testemail@test.com")
        
        self.shop = Shop.objects.create(shop_owner=shop_owner, shop_email="testemail@test.com", address=address)
        self.employee = Employee.objects.create_user(username="testemployee", password="whatever", email="testemployee@test.com")
        self.employeeData = EmployeeData.objects.create(user=self.employee, shop=self.shop)

    def test_Employees(self):
        employee = EmployeeData.objects.filter(shop__pk=self.shop.pk)
        self.assertEqual(self.shop.num_employees, 1)
        self.assertQuerysetEqual(self.shop.get_employees(), employee)

    def test_hasEmployee(self):
        
        id = self.employeeData.user.pk

        self.assertTrue(self.shop.has_employee(id))

class SimpleInvitationModelTestGPT(TestCase):
    @classmethod
    def setUpTestData(self):
        # Set up test data for Customer
        self.customer_data = {
            'type': 'customer',
            'username': 'test_user',
            'password': 'test_password',
            'email': 'test_customer@example.com'
        }
        self.customer = Customer.objects.create(**self.customer_data)

        # Set up test data for SimpleInvitation
        self.invitation_data = {
            'email': 'test@example.com',
            'customer': self.customer,
        }

        # Create SimpleInvitation instance
        self.simple_invitation = SimpleInvitation.objects.create(**self.invitation_data)

    def test_simple_invitation_model_GPT(self):
        # Retrieve the saved instance from the database using invitation_key
        saved_invitation = SimpleInvitation.objects.get(invitation_key=self.simple_invitation.invitation_key)

        # Validate fields
        self.assertEqual(saved_invitation.email, self.invitation_data['email'])

        # Validate the customer field
        self.assertEqual(saved_invitation.customer.type, self.customer_data['type'])
        self.assertEqual(saved_invitation.customer.username, self.customer_data['username'])
        self.assertEqual(saved_invitation.customer.password, self.customer_data['password'])
        self.assertEqual(saved_invitation.customer.email, self.customer_data['email'])

class SimpleInvitationTestsCoPilot(TestCase):
    @classmethod
    def setUpTestData(self):
        self.customer = Customer.objects.create_user(type="customer", username="testcustomer", password="whatever", email="test@example.com")
        self.invitation_data = {
            "email": "test2@example.com",
            "customer": self.customer,
        }
        self.simple_invitation = SimpleInvitation.objects.create(**self.invitation_data)
    
    def test_simple_invitaiton_model(self):
        saved_invitation = SimpleInvitation.objects.get(invitation_key=self.simple_invitation.invitation_key)

        self.assertEqual(saved_invitation.email, self.invitation_data["email"])
        self.assertEqual(saved_invitation.customer, self.invitation_data["customer"])

        self.assertEqual(saved_invitation.customer.type, self.customer.type)
        self.assertEqual(saved_invitation.customer.username, self.customer.username)
        self.assertEqual(saved_invitation.customer.password, self.customer.password)
        self.assertEqual(saved_invitation.customer.email, self.customer.email)
# class ServicesTests(APITestCase):
#     @classmethod
#     def setUpTestData(self):
#         address = Address.objects.create(postal_code="M4E2T2", street="104 Test Street", city="Toronto", country="Canada", province="ON")
#         self.shop_owner = ShopOwner.objects.create_user(type="shop_owner", username="testuser2", password="qwerty123", email="testemail@test.com")
#         self.shop = Shop.objects.create(shop_owner=self.shop_owner, shop_email="testemail2@test.com", address=address)

#         self.part1 = Part.objects.create(condition="new", type="oem", name="testpart1", price="2.00")
#         self.part2 = Part.objects.create(condition="used", type="aftermarket", name="testpart2", price="2.00")
    
#     def setUp(self):
#         self.client = APIClient()
#         self.client.force_authenticate(self.shop_owner)
    
#     def test_createService(self):
#         expectedPartList = [self.part1.pk]
#         expectedName = "testname"
#         expectedDescription = "test description"
#         expectedActive = True

#         response = self.client.post('/shops/services/', {'shop': self.shop.pk, 'name': expectedName, 'description': expectedDescription, 'price': 2.00, 'parts': [self.part1.pk], 'active': True})
#         id = response.data['id']
#         service = Service.objects.get(pk=id)

#         self.assertEqual(service.name, expectedName)
#         self.assertEqual(service.description, expectedDescription)
#         self.assertEqual(service.shop, self.shop)
#         self.assertEqual(service.price, 2.00)
#         self.assertEqual(response.data['parts'], expectedPartList)
#         self.assertEqual(service.active, expectedActive)

#         self.assertEqual(self.part1.pk, ServicePart.objects.get(part=self.part1).pk)
    
#     def test_updateServiceSwapPart(self):
#         expectedPartList = [self.part2.pk]
#         expectedName = "testname"
#         expectedDescription = "test description"
#         expectedActive = True

#         response = self.client.post('/shops/services/', {'shop': self.shop.pk, 'name': expectedName, 'description': expectedDescription, 'price': 2.00, 'parts': [self.part1.pk], 'active': True})
#         id = response.data['id']
#         response = self.client.patch(f'/shops/services/{id}/', {'shop': self.shop.pk, 'name': expectedName, 'description': expectedDescription, 'price': 2.00, 'parts': [self.part2.pk], 'active': True})
        

#         service = Service.objects.get(pk=id)

#         self.assertEqual(service.name, expectedName)
#         self.assertEqual(service.description, expectedDescription)
#         self.assertEqual(service.shop, self.shop)
#         self.assertEqual(service.price, 2.00)
#         self.assertEqual(response.data['parts'], expectedPartList)
#         self.assertEqual(service.active, expectedActive)

#         self.assertEqual(self.part2.pk, ServicePart.objects.get(part=self.part2).part.pk)


