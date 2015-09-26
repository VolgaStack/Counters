from django.test import TestCase
from .kdm_tools import KdmToolSet


class KdmToolsTests(TestCase):

    def test_readfile(self):
        id = 'c9aff383ddfc4f7693637c984bfc064a'
        token = '7f56b1a9d80648c7b87ae588a905a9be'
        k = KdmToolSet()
        (a,b) = k.ReadFile('settings.txt')
        t_func = (a,b)
        t_should_be = (id, token)
        self.assertEqual(t_func, t_should_be)
		
#	def test_write_to_db_counters(self):
#        d = {"rows":1,"counters":[{"id":2215810,"code_status":"CS_ERR_EMPTY_DOMAIN_NAME","name":"Счётчик для тестового представителя","site":"","type":"simple",}]}
#		k = KdmToolSet()
#		k.WriteToDbCounters(d)