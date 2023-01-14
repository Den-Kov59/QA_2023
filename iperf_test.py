import parser_1
from confest import client, server
import sys
import logging

class TestSuite():

    def test_iperf3_server_connection(self, server):
        stdout, stderr = server
        logging.basicConfig(stream=stderr, level=logging.DEBUG)
        assert not stderr
    
    def test_iperf3_client_connection(self, client):
        stdout, error, error_serv= client
        print ("    >Received form fixture client is: {}".format(stdout))
        assert not error
        dict = parser_1.parser(stdout)
        for value in dict:
            assert value['Transfer']> 5.5 and value["Bitrate"] > 40.2
        