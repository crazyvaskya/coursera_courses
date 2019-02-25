class SomeObject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""


class EventGet:
    def __init__(self, kind):
        self.kind = kind


class EventSet:
    def __init__(self, kind):
        self.kind = kind


class NullHandler:
    def __init__(self, successor=None):
        self.__successor = successor

    def handle(self, obj, event):
        if self.__successor is not None:
            return self.__successor.handle(obj, event)


class IntHandler(NullHandler):
    def handle(self, obj, event):
        if event.kind == int or type(event.kind) == int:
            if type(event) == EventGet:
                # print("int return")
                return obj.integer_field
            elif type(event) == EventSet:
                # print("int set", event.kind)
                obj.integer_field = event.kind
        else:
            # print("int send further")
            return super().handle(obj, event)


class FloatHandler(NullHandler):
    def handle(self, obj, event):
        if event.kind == float or type(event.kind) == float:
            if type(event) == EventGet:
                # print("float return")
                return obj.float_field
            elif type(event) == EventSet:
                # print("float set", event.kind)
                obj.float_field = event.kind
        else:
            # print("float send further")
            return super().handle(obj, event)


class StrHandler(NullHandler):
    def handle(self, obj, event):
        if event.kind == str or type(event.kind) == str:
            if type(event) == EventGet:
                # print("str return")
                return obj.string_field
            elif type(event) == EventSet:
                # print("str set", event.kind)
                obj.string_field = event.kind
        else:
            # print("str send further")
            return super().handle(obj, event)


if __name__ == "__main__":
    chain = IntHandler(FloatHandler(StrHandler(NullHandler)))
    obj = SomeObject()
    chain.handle(obj, EventSet(4))
    print("--------------- int is set ----------")
    chain.handle(obj, EventSet(2.4))
    print("--------------- float is set ----------")
    chain.handle(obj, EventSet("kek"))
    print("--------------- str is set ----------")
    print(chain.handle(obj, EventGet(int)), chain.handle(
        obj, EventGet(float)), chain.handle(obj, EventGet(str)))
