from django.test import TestCase
from nypl_img.views import img_capture
import rstr

#The regex is a mess but I didn't want to get too far in the weeds

class ImgCaptureTest(TestCase):
    
    test_date = rstr.xeger(r'19[0-9][0-9]-0[1-9]-[0-2][1-9]')

    def test_view_exists(self,test_date=test_date):      
        response = self.client.get(f'/nypl_img/randomimg/{test_date}/')
        self.assertEqual(response.status_code, 200)

    def test_view_results(self,test_date=test_date):
        #check that input date matches output date -- this currently fails a lot
        response = self.client.get(f'/nypl_img/randomimg/{test_date}/')
        self.assertEqual(response.context['obj_date'], test_date)


