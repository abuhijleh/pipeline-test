from django.test import TestCase
#from .models import Item
# to test the edit of the existing item


# Create your tests here.
class TestViews(TestCase):
    def test_get_todo_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'todo/todo_list.html')
       
    # def test_get_add_item_page(self):
    #     response = self.client.get('/add')
    #     self.assertEqual(response.status_code,200)
    #     self.assertTemplateUsed(response, 'todo/add_item.html')
        
       
    # def test_can_add_item(self):
    #     response = self.client.get('/add',{'name':'Test Added'})
    #     self.assertRedirects(response ,'/')
    
    #def test_get_edit_item_page(self):
    #def test_get_edit_item_page(self):
    