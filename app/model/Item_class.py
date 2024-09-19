from typing import Optional
from model.enums import Item_field_type, Views

class Item_class :

    _id : Optional[int]
    view : Views
    name : str
    description : str
    _fields : list[dict[str,str]]

    def __init__(self, id: Optional[int], view: Views, name: str, description: str) -> None:
        self._id = id
        self.view = view
        self.name = name
        self.description = description
        self._fields = []

    def add_field(self,
                  name: str,
                  type: Item_field_type,
                  mandatory: bool,
                  description: str = '',
                  default: Optional[str|int|float] = None,
                  ) -> None:
        """
        add_field : Create a new field in the item class.

        Arguments:
            name -- Name of the field.
            type -- Type of the field.
            mandatory -- Is the field mandatory.
            description -- A description of the field.

        Keyword Arguments:
            default --  Default value of the field when an
                        item of this class is created.
                        Only for types String, Integer and Float.
                        (default: {None})
        """

    def add_ref(self,
                name: str
                ) :
        pass

