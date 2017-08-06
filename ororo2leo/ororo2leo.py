import csv
import os
import sys

import fire
import requests

LINGUALEO_API_URL = 'https://api.lingualeo.com/api/login'


class Ororo2leoUtil:
    """A command line tool for exporting ororo.tv dictionary to lingualeo"""

    def export(self, csv_dict, leo_login, leo_password):
        """Export CSV ororo.tv dictionary to lingualeo"""

        csv_dict = os.path.expanduser(csv_dict)
        auth = {'email': leo_login, 'password': leo_password}
        s = requests.Session()
        r = s.get(url=LINGUALEO_API_URL, params=auth)
        r.raise_for_status()
        if r.json()['error_msg']:
            raise Exception("Unable to auth in Lingualeo service as {}.".format(auth['email']))
        with open(csv_dict, 'r') as csvfile:
            words = filter(lambda x: x[2] == 'English => Russian', csv.reader(csvfile))
            dict_list = [{'word': w[0], 'tword': w[1].split(',')[0],
                          'context': w[3]} for w in words]
        print("Discovered {} word(s) for CSV file".format(len(dict_list)))
        for i, w in enumerate(dict_list):
            try:
                if not s.get(url='https://api.lingualeo.com/gettranslates?word={}'
                             .format(w['word'])).json()['translate'][0]['is_user']:
                    r = s.post(url='https://api.lingualeo.com/addword',
                               params=w)
                    if not r.json()['error_msg']:
                        print("[{}/{}] Word `{}` added".format(i, len(dict_list), w['word']))
                else:
                    print("[{}/{}] Word `{}` exists.".format(i, len(dict_list), w['word']))
            except Exception as e:
                print("[{}/{}] Word {} Error: {}".format(i, len(dict_list), w['word'], e))
        print("Job has been done. Now it's your turn at "
              "https://lingualeo.com/ru/glossary/learn/dictionary")


def main():
    try:
        fire.Fire(Ororo2leoUtil, name='ororo2leo')
    except Exception as e:
        print("Error: {}".format(e))
        sys.exit(1)


if __name__ == '__main__':
    main()
