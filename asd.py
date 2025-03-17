import qrcode
data = '''BEGIN:VCARD
VERSION:3.0
N:Ivan
FN:Ivanov
ORG:ГК Дороги России
TITLE:Администратор
TEL;WORK;VOICE:+70000000000
TEL;CELL:+70000000000
EMAIL;WORK;INTERNET:foo@email.com
END:VCARD
'''

qrcod = qrcode.make(data)
qrcod.save('./test.png')