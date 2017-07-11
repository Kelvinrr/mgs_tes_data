import unittest
from .. import io_db
import pytes

from shapely.geometry import box
from shapely.geometry import Point

class TestUtils(unittest.TestCase):
    # TODO: Make actual tests

    def test_init(self):

        df = pytes.query_postgres(engine, shape=Point(137.4, 20).buffer(10.0), ls=range(0,270))
        engine,meta = pytes.connect_postgres(host='dcos-node1', port=31180)
