import os
from pprint import pprint

import pandas
from django.core.management.base import BaseCommand

from storages.models import Part



def get_available_nomenclature(data_base):
    available_parts = []
    parts = pandas.read_excel(
                    data_base,
                    sheet_name='TDSheet',
                    na_values=False,
                    keep_default_na=False
                    ).to_dict(orient='records')
    for part in parts:
        if part.get('Unnamed: 2') and part.get('Unnamed: 2') != 'Код' and part.get('Unnamed: 1') != 'Номенклатура':
            pprint(part)
            part = {
                'name': part.get('Unnamed: 1'),
                'code': part.get('Unnamed: 2'),
            }
            available_parts.append(part)
    pprint(available_parts)
    return
    return available_parts


def load_database(parts):
    for part in parts:
        new_part = Part(
            name=part['name'],
            code=part['code'],
        )
        new_part.save()


class Command(BaseCommand):
    help = 'Load parts'

    def handle(self, *args, **options):
        try:
            data_base = 'Остатки.xlsx'
            print(data_base)

            parts = get_available_nomenclature(data_base)
            load_database(parts)
        except Exception as err:
            print(err)
