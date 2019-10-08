# coding: UTF-8
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

ID_ALL = os.environ.get("ID_ALL")
ID_HOT = os.environ.get("ID_HOT")
ID_ANIME = os.environ.get("ID_ANIME")
ID_VOCALO = os.environ.get("ID_VOCALO")
ID_WESTERN = os.environ.get("ID_WESTERN")
DEVELOPER_KEY = os.environ.get("DEVELOPER_KEY")
