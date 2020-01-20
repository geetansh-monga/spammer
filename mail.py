import yagmail

# yagmail.register('localhost@vipsace.org', 'VWOeVxd0')
yag = yagmail.SMTP('localhost@vipsace.org', 'VWOeVxd0')
contents = [
    "This is the body, and here is just text http://somedomain/image.png",
    "You can find an audio file attached.", '/local/path/to/song.mp3'
]
yag.send('mukuljain0402@gmail.com', 'Test', contents)