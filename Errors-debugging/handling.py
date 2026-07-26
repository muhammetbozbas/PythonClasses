while True:
    try:
        x = int(input("x: "))
        y = int(input("y: "))
        print(x/y)
    except ZeroDivisionError as e:
        print('y sıfır olamaz!')
        print(e)
    except ValueError:
        print('x ve y sayısal bir değer olmalıdır!')
    except Exception as e:
        print("bilinmeyen bir haya oluştu")
        print(e)
    else:
        print('her şey yolunda')
        break
    finally:
        print("final bloğu çalıştı")
        # her halükarda çalışan blok
    




"""
try:
    x = int(input("x: "))
    y = int(input("y: "))
    print(x/y)
except (ZeroDivisionError,ValueError) as e: #iki hata türünün printini kısaca böyle alabiliriz.
    print("hata oluştu")
    print(e) #exception alırız.
except Exception as e:
    print("bilinmeyen bir haya oluştu")
    print(e)
"""