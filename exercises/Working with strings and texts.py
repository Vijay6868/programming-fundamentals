def students_info(*args,**kwargs):
    print(args)
    print(kwargs)

courses = ('math','art')
info = {'age':25,'name':'john'}
students_info(*courses,**info)


