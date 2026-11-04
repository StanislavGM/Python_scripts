# Constructor polymorphizm and inheritance.
'''
# Пример полиморфизма. Использование одинаковых методов в разных классах
class Tomcat(object):
    def __init__(self, home, ver):
        self.home = home
        self.version = ver
        return None
    def display(self):
        print("This is from tomcat class")
        print(self.home)
        print(self.version)
        return None
class Apache(object):
    def __init__(self, home, ver):
        self.home = home
        self.version = ver
        return None
    def display(self):
        print("This is from apache class")
        print(self.home)
        print(self.version)
        return None
tom_ob = Tomcat("/home/tomcat9", "7.6")
ap_ob = Tomcat("/etc/httpd", "2.4")
tom_ob.display()
ap_ob.display()
'''
class Tomcat(object):
    def __init__(self, home, ver):
        self.home = home
        self.version = ver
        #print("This is from tomcat class")
        return None
    def display(self):
        print(self.home)
        print(self.version)
        return None
    
class Apache(Tomcat):
    '''
    def __init__(self, home, ver):
        self.home = home
        self.version = ver
        #print("This is from apache class") -- в режиме inheritance данная команда не работает, используется команда из род.класса
        return None
    '''
tom_ob = Tomcat("/home/tomcat9", "7.6")
ap_ob = Tomcat("/etc/httpd", "2.4")
tom_ob.display()
ap_ob.display()