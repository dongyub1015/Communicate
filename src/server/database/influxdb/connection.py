from influxdb import InfluxDBClient
from singleton_decorator import singleton
import os


@singleton
class InfluxDB():
    def __init__(self, config: dict):
        # InfluxDB 연결 정보 설정
        self.__host = config.get('INFLUXDB_HOST')  # InfluxDB 호스트 주소
        self.__port = config.get('INFLUXDB_PORT')  # InfluxDB 호스트 주소
        self.__username = config.get('INFLUXDB_USERNAME')  # InfluxDB 호스트 주소
        self.__password = config.get('INFLUXDB_PASSWORD')  # InfluxDB 호스트 주소
        self.__database = config.get('INFLUXDB_DATABASE')  # InfluxDB 호스트 주소
        # self.__host = 'localhost'  # InfluxDB 호스트 주소
        # self.__port = 8086         # InfluxDB 포트
        # self.__username = 'myuser' # InfluxDB 사용자명
        # self.__password = 'mypassword' # InfluxDB 비밀번호
        # self.__database = 'mydb'  # 사용할 데이터베이스 이름

        # InfluxDB 클라이언트 생성
        self.__client = InfluxDBClient(host=self.__host, port=self.__port, username=self.__username, password=self.__password, database=self.__database)
        return self.__client

    def get_client(self):
        return self.__client

    # def connect(self):
    #     self.__client.
    def ping(self):
        return self.__client.ping()

    def close(self):
        self.__client.close()
