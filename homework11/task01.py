class SimplifiedEnum(type):
    def __new__(mcs, future_class_name, future_class_parents,
                future_class_attr):
        attr_name = f'_{future_class_name}__keys'
        for key in future_class_attr[attr_name]:
            future_class_attr[key] = key
        future_class_attr.pop(attr_name)
        return super().__new__(mcs, future_class_name, future_class_parents,
                               future_class_attr)
