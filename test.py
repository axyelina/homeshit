import random
from os import path

def urlsh(long_url): # возвращает короткую ссылку вида http://surin.ru/sh/eGbWp
    domain_name='http://surin.ru/'
    phph_file_folder='./sh/'
    if not path.exists('.htaccess'):
        ht_f=open('.htaccess','w')# если нет создаем файл .htaccess
        ht_f.write('RewriteEngine On\nRewriteBase %s\n' % phph_file_folder[1:-1])# записываем в него первые две строчки для переадресации
    else:
        ht_f=open('.htaccess','a')
    link=''.join(random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',5)) # генерируем случайную последовательность из 5 символов для нашей короткой ссылки
    data=phph_file_folder + link + '.php'
    php_file=open(data,'w')
    php_file.write('<?php header(\'Location: %s\') ?>\n' % long_url)
    php_file.close()
    ht_f.write('RewriteRule ^%s %s%s' % (link,phph_file_folder[2:],link+'.php\n'))
    ht_f.close()
    return domain_name + phph_file_folder[2:] + link
a=urlsh('http://yandex.ru')
print(a)