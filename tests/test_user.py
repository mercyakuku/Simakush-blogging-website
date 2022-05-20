import unittest
# Import class to be tested
from app.models import User

class UserModelTest(unittest.TestCase):
    '''
    Test class to test behaviours of the [Class] class

    Args:
        unittest.TestCase : Test case class that helps create test cases
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_user = User(password = 'beth')


    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)


    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password


    def test_password_verify(self):
        self.assertTrue(self.new_user.verify_password('KusH'))































# import unittest
# from app.models import *

# def setUp(self):
#         """
#         Will be called before every test
#         """
#         db.create_all()

#         # create test admin user
#         admin = User(author="admin", password="admin2022", is_admin=True)

#         # create test non-admin user
#         other = User(author="test_user", password="test2022")

#         # save users to database
#         db.session.add(admin)
#         db.session.add(other)
#         db.session.commit()

# def tearDown(self):
#         """
#         Will be called after every test
#         """
#         db.session.remove()
#         db.drop_all()

# class UserModelTest(unittest.TestCase):

#     def setUp(self):
#         self.new_user = User(password = 'cherry')

#     def test_password_setter(self):
#         self.assertTrue(self.new_user.password_hash is not None)

#     def test_no_access_password(self):
#         with self.assertRaises(AttributeError):
#             self.new_user.password

#     def test_password_verification(self):
#         self.assertTrue(self.new_user.verify_password('cherry'))

# class CommentsModelTest(unittest.TestCase):

#     def setUp(self):
#        self.new_comment = Comments(id=1, user_id = 2, comment = 'jaysafu',blogs_id = '5',date_posted='2022-05-10')

#     def test_comment_variables(self):

       
#        self.assertEquals(self.new_comment.comment,'jaysafu')
#        self.assertEquals(self.new_comment.date_posted,'2022-05-10')
#        self.assertEquals(self.new_comment.user_id, 2)
     

#     def test_save_comment(self):

#         self.assertTrue(len(Comments.query.all())>0)

# class BlogsModelTest(unittest.TestCase):

#     def test_save_blog(self):
#         self.assertTrue(len(Blogs.query.all())>0)


# class SubscriberModelTest(unittest.TestCase):

#     def setUp(self):
#         self.new_subscriber = Subscriber(id = 1 , name = 'Love', email = 'jay@msela.men')

#     def test_instance(self):
#         self.assertTrue(isinstance(self.new_subscriber,Subscriber))

#     def test_variables(self):
#         self.assertEquals(self.new_subscriber.id, 1)
#         self.assertEquals(self.new_subscriber.name, 'Love')
#         self.assertEquals(self.new_subscriber.email, 'jay@msela.men')