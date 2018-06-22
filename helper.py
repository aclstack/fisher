# -*- coding: utf-8 -*-


def is_isbn_or_key(world):
    # 判断用户输入类型
    isbn_or_key = 'key'
    if len(world) == 13 and world.isdigit():
        isbn_or_key = 'isbn'
    short_world = world.replace('-', '')
    if '-' in world and len(short_world) == 10 and short_world.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key
