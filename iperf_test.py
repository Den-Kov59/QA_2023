import parser_1
from confest import client, server
import sys
import logging

class TestSuite():

    def test_iperf3_server_connection(self, server):
        stderr = server
        assert stderr
    
    def test_iperf3_client_connection(self, client):
        stdout, error= client
        print ("    >Received form fixture client is: {}".format(stdout))
        assert not error
        dict = parser_1.parser(stdout.decode())
        for value in dict:
            assert value['Transfer']> 10 and value["Bitrate"] > 80
        