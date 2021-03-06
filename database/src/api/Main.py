#!python3
#encoding:utf-8
import sys
import subprocess
import shlex
import os.path
import getpass
import dataset
import database.src.TsvLoader
class Main:
    def __init__(self, db_path):
        self.db_path = db_path
        self.path_this_dir = os.path.abspath(os.path.dirname(__file__))

    def Run(self):
        self.__Create()
        self.__Insert()
#        self.__Check() # Check.shで正常に文字列結合できずパスを作成できない。

    def __Create(self):
        subprocess.call(shlex.split("bash \"{0}\" \"{1}\"".format(os.path.join(self.path_this_dir, "CreateTable.sh"), self.db_path)))

    def __Insert(self):
        tables = ['Apis']
        for table in tables:
            path_tsv = os.path.join(self.path_this_dir, "res/tsv/{0}.tsv".format(table))
            loader = database.src.TsvLoader.TsvLoader()
            loader.ToSqlite3(path_tsv, self.db_path, table)

    def __Check(self):
        # sqlite3: Error: too many options:
#        subprocess.call(shlex.split("bash \"{0}\" \"{1}\"".format(os.path.join(self.path_this_dir, "Check.sh"), self.db_path)))
#        cmd = "sqlite3 \"{0}\" < \"{1}\"".format(self.db_path, os.path.join(self.path_this_dir, "res/sql/check/check.sql"))
#        cmd = "sqlite3 {0} < {1}".format(self.db_path, os.path.join(self.path_this_dir, "res/sql/check/check.sql"))
#        cmd = 'sqlite3 "{0}" "{1}"'.format(self.db_path, os.path.join(self.path_this_dir, "res/sql/check/check.sql"))
#        cmd = 'sqlite3 {0} < {1}'.format(self.db_path, os.path.join(self.path_this_dir, "res/sql/check/check.sql"))
#        cmd = 'sqlite3 {0} < \"{1}\"'.format(self.db_path, os.path.join(self.path_this_dir, "res/sql/check/check.sql"))
#        print(cmd)
#        subprocess.call(shlex.split(cmd))
        pass
